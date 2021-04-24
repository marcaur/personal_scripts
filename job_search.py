#!/usr/bin/python3

import csv
import pprint
"""
This will create/update a document that allows me to update my job search
The spreadsheet will have fields for:
-----------------------------------------------
company | date applied | email | company site |
-----------------------------------------------
"""
myHeaders = ['Company','City','State','Address','Job Title']
def newFile():
    print("Enter your headers")
    while len(myHeaders) < 5:
        newHeader = input("Enter a header")
        myHeaders.append(newHeader)
    print("These are your headers" + str(myHeaders))
    newDataFile = open("example.csv",'w', newline='')
    iniitalDataFile = csv.DictWriter(newDataFile,myHeaders)
    initialDataFile.writeheader()



# for reading my previous applications
def readObject():
    jobFile = open('applications.csv')
    readJobFile = csv.DictReader(jobFile)
    print("This is your current document")
    for row in readJobFile:
        print("#" + str(readJobFile.line_num) +""+ row['Company']+row['City'])
    usrDone = input("Enter 'q' to close")
    if usrDone == 'q':
        jobFile.close()

jobList = {'Company':'','City':'', 'City':'','State':'','Address':'','Job Title':''}
def writeObject():
    fileToWrite = open('applications.csv','w',newline='')
    writerObject = csv.DictWriter(fileToWrite, myHeaders)
    writerObject.writeheader()
    while True:
        jobCompany = input("What is the name of the company?")
        jobList['Company'] = jobCompany

        jobCity = input("What city is the job in?")
        jobList['City'] = jobCity

        jobState = input("What state is the job in?")
        jobList['State'] = jobState


        jobAddy = input("What is the address?")
        jobList['Address'] = jobAddy

        jobTitle = input("What is the position?")
        jobList['Job Title'] = jobTitle

        writerObject.writerow(jobList)
        print("Press 'q' to quit or 'enter' to continue")
        usrChoice = input()
        if usrChoice == 'q':
            break
        else:
            continue
    fileToWrite.close()

    # print("Options: r - read , e - edit")
    # doc_action = input("What do you want to do with this document?")

writeObject()
readObject()
