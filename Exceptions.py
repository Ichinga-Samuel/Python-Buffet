import logging
#!
logging.basicConfig(filename='exceptionlogs.txt', level=logging.DEBUG, style='{', format=f'{asctime} - {levelname} - {message}')

logging.debug('Start script')

def getposnum():
	num = int(input('Enter your num\t'))
	if num < 0:
		my_error = ValueError('{0} is not a valid number'.format(num))
		raise my_error
	return num


def readposint():
	try:
		a = getposnum()
	except Exception as err:
		print('not a valid number:\t', str(err))
	else:
		print('{} is a valid number'.format(a))
	finally:
		print('Thanks')


# define your own error in a class
class NameTooShortError(ValueError):  # inherits from value error. it can inherit from any type of error
	pass

def validate(name):
	if len(name) < 10:
		raise NameTooShortError(name)
	else:
		print('correct')

validate('sammyo')
