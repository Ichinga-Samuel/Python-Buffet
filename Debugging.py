import traceback
import logging


logging.basicConfig(filename='logging.txt', style='{', level=logging.DEBUG, format='{asctime} - {levelname} - {message}')
logging.debug('Start of Program')

ef = open('errofile.txt', 'a+')

try:
    a = 5 / 0
except:
    ef.write(traceback.format_exc())
    ef.close()
