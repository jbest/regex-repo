import uuid
import yaml
import datetime

"""
Create a new regex repository document template in YAML format named
as [uuid].yaml and stored in the ./regex directory.
"""
regexUUID = uuid.uuid4()
today = datetime.date.today()
#TODO Use an external template file instead of data in code. 
#templateData = {'title': "titleHere",'uuid': str(regexUUID), 'description': "DescriptionHere"}
templateData = {'regex': 'RegExStringHere', 'updated': str(today), 
'description': 'DescriptionHere', 'title': 'TitleHere', 'notes': 'NotesHere', 
'created': str(today), 'sampleNonMatches': ['sample1', 'sample2'], 
'testString': 'Sample string.', 'version': 'VersionHere', 'testResults': ['result1', 'result2', 'result3'], 
'authors': ['author1', 'author2'], 'keywords': ['key1', 'key2'], 'sampleMatches': ['sample1', 'sample2'],
 'uuid':  str(regexUUID)}
templateString = yaml.dump(templateData, default_flow_style=False)
templateFileName = str(regexUUID) + '.yaml' 
#TODO Make sure file name is unique. Yeah, most likely is, but still gotta make sure.
f = open('./regex/' + templateFileName, 'w+')
f.write(templateString)
f.close()
print 'Template created at:', './regex/' + templateFileName