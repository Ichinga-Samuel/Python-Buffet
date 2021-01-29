import xml.etree.ElementTree as ET
import xml.dom.minidom as md


tree = ET.parse('Countries.xml')
root = tree.getroot()

# te = ET.ElementTree(c)
# te.write('result.xml')


def cxml(tre, data):
    for i in data:
        if isinstance(data[i], dict):
            t = ET.Element(i)
            tre.append(t)
            cxml(t, data[i])
        else:
            ET.SubElement(tre, i).text = str(data[i])
    return tre


inputs = {'data': {'region': {'name': 'Africa', 'avgAge': 19.7, 'avgDailyIncomeInUSD': 4, 'avgDailyIncomePopulation': 0.73}, 'periodType': 'days', 'timeToElapse': 38, 'reportedCases': 2747, 'population': 92931687, 'totalHospitalBeds': 678874}, 'estimate': {'impact': {'currentlyInfected': 27470, 'infectionsByRequestedTime': 112517120, 'severeCasesByRequestedTime': 16877568.0, 'hospitalBedsByRequestedTime': -16639962.1, 'casesForICUByRequestedTime': 5625856.0, 'casesForVentilatorsByRequestedTime': 2250342.4, 'dollarsInFlight': 12484899635.199999}, 'severeImpact': {'currentlyInfected': 137350, 'infectionsByRequestedTime': 562585600, 'severeCasesByRequestedTime': 84387840.0, 'hospitalBedsByRequestedTime': -84150234.1, 'casesForICUByRequestedTime': 28129280.0, 'casesForVentilatorsByRequestedTime': 11251712.0, 'dollarsInFlight': 62424498176.0}}}

ET.dump(tree)
print(md.parseString(ET.tostring(root)).toprettyxml())