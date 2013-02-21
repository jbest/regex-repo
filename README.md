regex-repo
==========

A regular expression repository for natural history collection data.

My goal is to create a repository of regular expressions that are focused on parsing strings commonly found in records of natural history collections. There are many regex repositories avaiable on the web but this repository will not only focus on the most relevant expressions, but will also include documentation and tests to verify each regular expression.

This project is in a very early stage and will rely on the contributions of regexperts (hello iDigBio Hackathoners).

[Here](/docs/repo-contents.md) is a sample of how the contents of the repository might be displayed. This document is generated in the build and test process (see below).


## RegEx Documents 
Each regular expression has a YAML-formatted document in the ./regex directory. Below is a sample of the document contents.


    authors:
    - author1
    - author2
    created: date
    description: DescriptionHere
    keywords:
    - key1
    - key2
    notes: NotesHere
    regex: RegExStringHere
    sampleMatches:
    - sample1
    - sample2
    sampleNonMatches:
    - sample1
    - sample2
    testResults:
    - result1
    - result2
    - result3
    testString: Sample string.
    title: TitleHere
    updated: date
    uuid: uuid
    version: VersionHere

## Build 
The [build.py](build.py) script reads all the regex documents in the ./regex directory and writes a summary of each into [./docs/repo-contents.md](/docs/repo-contents.md). Eventually other documents will be created to list regexes by keyword, etc. The critical testing process has not been written yet, but that is next.

## Make Template 
The [make-template.py](make-template.py) script will create a YAML-formatted document in the ./regex directory with boilerplate keys and values as well as a datestamp. The script generates a UUID for naming the file.
