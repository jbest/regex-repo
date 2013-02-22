import glob
import yaml
import datetime
import re

files = glob.glob('./regex/*.yaml')
today = datetime.date.today()
startTime = datetime.datetime.now()
failCount = 0

for regexDoc in files:
	yamlFile = open(regexDoc, 'r')
	docData = yaml.load (yamlFile.read())

	regexString =  docData['regex']
	expectedResults = docData['testResults']
	p = re.compile(regexString)
	iterator = p.finditer(docData['testString'])
	actualResults = []
	for match in iterator:
		if match:
			actualResults.append(match.group())

	print 'Testing regex in:', regexDoc
	#print docData['testString']
	
	if expectedResults == actualResults:
		print 'Test passed.'
	else:
		failCount += 1
		print 'FAIL'
		print 'Expected:'
		print expectedResults
		print 'Actual:'
		print actualResults

testTime = datetime.datetime.now() - startTime
print 'Test complete.'
print 'Failed tests:', failCount
print 'Time elapsed:', testTime