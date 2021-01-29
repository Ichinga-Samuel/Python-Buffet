import json
import xml.etree.ElementTree as ET
import sys
import os


inputs = {'region': {'name': "Africa", 'avgAge': 19.7, 'avgDailyIncomeInUSD': 4,
          'avgDailyIncomePopulation': 0.73}, 'periodType': "days", 'timeToElapse': 38, 'reportedCases': 2747,
          'population': 92931687, 'totalHospitalBeds': 678874}


def estimator(data):
    data1 = data.copy()

    if data['periodType'] == 'weeks':
        data1['timeToElapse'] = data['timeToElapse'] * 7

    elif data['periodType'] == 'months':
        data1['timeToElapse'] = data['timeToElapse'] * 30

    impact = estimates(data1)
    severeImpact = estimates(data1, severe=True)
    estimate = {'impact': impact, 'severeImpact': severeImpact}
    result = {'data': data, 'estimate': estimate}
    return result


def estimates(data, severe=False):
    x = 10
    if severe:
        x = 50

    currentlyInfected = data['reportedCases'] * x
    infectionsByRequestedTime = currentlyInfected * 2 ** (data['timeToElapse'] // 3)
    severeCasesByRequestedTime = infectionsByRequestedTime * 0.15
    hospitalBedsByRequestedTime = data['totalHospitalBeds'] * 0.35 - severeCasesByRequestedTime
    casesForICUByRequestedTime = infectionsByRequestedTime * 0.05
    casesForVentilatorsByRequestedTime = infectionsByRequestedTime * 0.02
    dollarsInFlight = infectionsByRequestedTime * data['region']['avgDailyIncomePopulation'] * \
        data['region']['avgDailyIncomeInUSD'] * data['timeToElapse']

    output = {'currentlyInfected': currentlyInfected, 'infectionsByRequestedTime': infectionsByRequestedTime,
              'severeCasesByRequestedTime': severeCasesByRequestedTime,
              'hospitalBedsByRequestedTime': hospitalBedsByRequestedTime,
              'casesForICUByRequestedTime': casesForICUByRequestedTime,
              'casesForVentilatorsByRequestedTime': casesForVentilatorsByRequestedTime,
              'dollarsInFlight': dollarsInFlight}
    return output


def _json(data):
    with open('results.json', 'w') as res:
        json.dump(data, res, indent='\t')
    return res


def _xml(tree, data):
    for i in data:
        if isinstance(data[i], dict):
            element = ET.Element(i)
            tree.append(element)
            _xml(element, data[i])
        else:
            ET.SubElement(tree, i).text = str(data[i])
    return tree


def display(data):
    results = estimator(data)
    _json(results)
    os.startfile('results.json')


def display_xml(data):
    results = estimator(data)
    root = ET.Element('root')
    root = _xml(root, results)
    tree = ET.ElementTree(root)
    tree.write('results.xml')
    os.startfile('results.xml')


if sys.argv[1] == 'xml':
    display_xml(inputs)
elif sys.argv[1] == 'json':
    display(inputs)
else:
    print('invalid input')
