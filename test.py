import glob
import yaml
import datetime
import re

#TODO Write test log in markdown and CSV

files = glob.glob('./regex/*.yaml')
today = datetime.date.today()
startTime = datetime.datetime.now()
failCount = 0

for regexDoc in files:
	yamlFile = open(regexDoc, 'r')
	docData = yaml.load (yamlFile.read())

	regexString =  docData['regex']
	expectedResults = docData['testResults']
	expectedSubgroupResults = docData['testSubgroupResults']
	p = re.compile(regexString)
	iterator = p.finditer(docData['testString'])
	subgroupCount = regexString.count('(')
	actualResults = []
	actualSubgroupResults = []
	for match in iterator:
		if match:
			actualResults.append(match.group())
			for subgroup in range(1,subgroupCount + 1):
				actualSubgroupResults.append(match.group(subgroup))

	print 'Testing regex in:', regexDoc
	
	if expectedResults == actualResults and expectedSubgroupResults == actualSubgroupResults:
		print 'Test passed.'
	else:
		failCount += 1
		print 'FAIL'
		print 'Expected matches:'
		print expectedResults
		print 'Actual matches:'
		print actualResults
		print 'Expected subgroup matches:'
		print expectedSubgroupResults
		print 'Actual subgroup matches:'
		print actualSubgroupResults

testTime = datetime.datetime.now() - startTime
print 'Test complete.'
print 'Failed tests:', failCount
print 'Time elapsed:', testTime