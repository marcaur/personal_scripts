#! /usr/bin/python3
import boto3
"""
CREATE A SCRIPT THAT ALLOWS USER TO CREATE, UPDATE, DELETE, AND LIST IAM USERS
USERS SHOULD BE PRESENTED WITH A LIST OF IAM USERS
USERS SHOULD THEN HAVE CHOICE OF WHAT OPTION THEY WOULD LIKE TO DO
"""
iam = boto3.client('iam')

def create_new_user():
    new_user = str(input("What is your new username?"))
    response = iam.create_user(UserName=new_user)
    print(f"A new user named {new_user} has been created".)
    print(response)

def update_user():
    current_user = str(input("What is your current username?"))
    update_user = str(input("What do you want your new username to be?"))
    iam = bot3.client('iam')
    iam.update_user(UserName=current_user, NewUserName=update_user)

def delete_user():
    print("Who do you want to delete?"); old_user = str(input())
    # check if user does not exist
    iam.delete_user(UserName=old_user)

def list_users():
    global paginator 
    # LISTING ALL USERS
    paginator = iam.get_paginator('list_users')
    for response in paginator.paginate():
        print(response)

print("What do you want to do?")
while True:
    usr_choice = str(input("Enter one of the following: L(list users), C(create user), U(update username), D(delete user)"))
    if usr_choice.lower() == "c":
        create_new_user()
    elif usr_choice.lower() == "l":
        list_users()
    elif usr_choice.lower() == "u":
        update_user()
    elif usr_choice.lower() == "d":
        delete_user()
    else:
        print("Please enter one of the options")
        continue
