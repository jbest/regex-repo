import glob
import yaml
import datetime

files = glob.glob('./regex/*.yaml')
today = datetime.date.today()
startTime = datetime.datetime.now()

# Start creating a markdown document string
mdString = '# Regex Repository Contents' + '  \n\n'
mdString += 'Compiled: ' + str(today) + '  \n\n'
mdString += '---' + '  \n'

for regexDoc in files:
	#yaml.load
	yamlFile = open(regexDoc, 'r')
	docData = yaml.load (yamlFile.read())
	#print repoDoc
	#print yaml.dump(docData, default_flow_style=False)

	mdString += '## ' + docData['title'] + '  \n'
	mdString += '    ' + docData['regex'] + '  \n' # Print as code in markdown
	mdString += '### Description' + '  \n'
	mdString += docData['description'] + '  \n'
	mdString += 'Keywords: ' + str(docData['keywords']) + '  \n'
	mdString += 'Authors: ' + str(docData['authors']) + '  \n\n'
	mdString += '---' + '  \n'

print mdString
f = open('./docs/repo-contents.md', 'w+')
f.write(mdString)
f.close()
buildTime = datetime.datetime.now() - startTime
print 'Build complete.'
print 'Time elapsed:', buildTime
