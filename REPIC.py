'''
REPIC is a Python function that will let you print output to comments inside the current file.
It stands for Read Evaluate Print In Comments.#OUTPUT: [1, 2, 3]

Usage:
from REPIC import REPIC
test = [1,2,3] + [4,5,6]
REPIC(test)#OUTPUT [1,2,3,4,5,6]

Note that the #OUTPUT comment gets written automatically after you evaluate the REPIC function.

By David@Pinney.org in August 2016.
'''

import inspect
import fileinput
import sys

def REPIC(obToPrint):
	'''REPIC stands for Read, Evaluate, Print In Comment. Call this function with an object obToPrint and it will rewrite the current file with the output in the comment in a line after this was called.'''
	cf = inspect.currentframe()
	callingFile = inspect.getfile(cf.f_back)
	callingLine = cf.f_back.f_lineno
	# print 'Line I am calling REPIC from:', callingLine
	for line in fileinput.input(callingFile, inplace=1):
		if callingLine == fileinput.filelineno():
			# Make results, but get rid of newlines in output since that will break the comment:
			resultString = '#OUTPUT: ' + str(obToPrint).replace('\n','\\n') +'\n'
			writeIndex = line.rfind('\n')
			# Watch out for last line without newlines, there the end is just the line length.
			if '\n' not in line:
				writeIndex = len(line)
			# Replace old output and/or any comments:
			if '#' in line:
				writeIndex = line.rfind('#')
			output = line[0:writeIndex] + resultString
		else:
			output = line # If no REPIC, then don't change the line.
		sys.stdout.write(output)

def REATE(obToPrint):
	'''REATE stands for Read, Evaluate, Append To End. Call this function with an object obToPrint and it will append the output to the file it is in. This is in here for historical purposes. It was the much easier simpler version of REPIC.'''
	callingFile = inspect.getfile(cf.f_back)
	with open(callingFile,'a') as thisFile:
		thisFile.write('\n#OUTPUT: ' + str(content))