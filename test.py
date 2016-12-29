''' Tests for the REPIC library. '''

from REPIC import REPIC

def _tests():
	# TODO: remove some comments before running the tests so that doesn't have to be manual.
	# A test:
	test = [1,2,3,999]
	test.append(4)
	test.append(8)
	REPIC(test)#OUTPUT: [1, 2, 3, 999, 4, 8]
	# Another test:
	REPIC(345 + 2 / 4)#OUTPUT: 345
	# Tricky test:
	REPIC('Uh oh here is\n a multiline output')#OUTPUT: Uh oh here is\n a multiline output

if __name__ == '__main__':
	# If just running the module, run the tests:
	_tests()