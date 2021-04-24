#! /usr/bin/python3

"""

requirements:
- time module
- regex module for input validation
- save feature so users can perform CRUD operations

values:
- the results will be in minutes, hours, days, weeks, and months
- the input variables are hours and days a week.
- job start date
- job end date

This is a program that will calculate the amount of time you spend at work.
Users will be able to track the amount of time they spend at work.
Although this program was intended to encourage mindfulness of how much time
you spend at your company, the meanings of the values can change

Given that a person worked 05/1-05/31, works x amount of hours and y amount of days a week,
figure out how much time they have spent in minutes at work.

Constraints:
- hrs_worked <= 24
- days_wrked <= 7
- can not work more than 168 hours in a week 

"""
print("Let's calculate how much time you spend at work.")

job_start = input("When did you start the job? ")
job_end = input("When did you stop working? ")

hrs_wrked = int(input("How many hours do you work in a day? "))
days_wrked = int(input("How many days do you work in a week? "))

min_wrked = (hrs_wrked*days_wrked/60)

while True:
    val = input("Please enter a number")
    try:
        workDays = int(val)
        if int(val) > 7:
            print("Enter a number less than 7")
            continue
        break
    except ValueError:
        print("Please enter a number")
        continue
print("You work " + str(workDays) + " days a week")
