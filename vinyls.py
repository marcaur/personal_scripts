#!/usr/bin/python3

import csv
"""
This will program will keep track of the vinyl records we have
The spreadsheet will have fields for:
-----------------------------------------------
song | artist | album | year |
-----------------------------------------------
"""

defHeaders = ["Song","Artist","Album","Year"]

# function to create a new CSV document with headers
def newFile():
    global fileName
    global newDataFile
    global myHeaders
    print("Enter your headers ")
    myHeaders = []
    while len(myHeaders) < 4:
        newHeader = input("Enter a header ")
        myHeaders.append(newHeader)
    print("These are your headers " + str(myHeaders))
    usrAns = input("Do you want to keep these headers?(y/n) ")
    while True:
        if usrAns == 'y':
            break
        else:
            newFile()
    fileName = input("What do you want to name the file? ")
    fileName += ".csv"
    newDataFile = open(fileName,'w', newline='')
    readDataFile = csv.DictWriter(newDataFile,myHeaders)
    readDataFile.writeheader()
    print("The name of your file is {}".format(fileName))





# for reading my previous applications
# used DictReader instead of regular read object

def readObject():
    musicFile = open('vinyls.csv')
    readMusicFile = csv.DictReader(musicFile,defHeaders, delimiter='\t', lineterminator='\n\n')
    print("This is your current document")
    # jobData = list(readJobFile)
    # looping through
    for row in readMusicFile:
        print(row["Song"],row["Artist"],row["Album"],row["Year"])
        #print("Row # " + str(readJobFile.line_num) + str(row))
    usrDone = input("Enter 'q' to quit ")
    if usrDone == 'q':
        musicFile.close()


def writeObject():
    fileToWrite = open('vinyls.csv','a',newline='')
    writeFile = csv.DictWriter(fileToWrite,defHeaders)
    while True:
        song = input("What is the name of the song? ")
        artist = input("Who is the artist? ")
        album = input("What album is this? ")
        year = input("What year was the song released? ")
        writeFile.writerow({"Song":song,"Artist":artist,"Album":album,"Year":year})
        askMe = input("Do you want to add another? ")
        if askMe == "n":
            break
        elif askMe == "y":
            continue
    fileToWrite.close()

writeObject()
