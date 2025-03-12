'''a=2000000000
if a >= 1 and a<= 50000:
    print("low")
else:
    if a>=50001 and a<= 1500000:
        print("medium")
    else:
        print("high")
'''

'''
employee ="mohini"
company="google"
if company == "google":
    print("G-",employee)
elif company=="microsoft":
    print("M-",employee)
else:
    print("company does not exists")
'''

'''
n1=10
n2=20
n3=30
if n1>n2:
    print("n1 is greater")
elif n2>n3:
    print("n2 is greater")
else:
    print("n3 is greater")
'''

'''
age = int(input("enter the age of 1st person")) # by default input will str so we have to mention int for int
age2 = int(input("enter the age of 2st person"))

if age>age2:
    print("person 1 is elder")
else:
    print("person 2 is elder")
'''

'''
employee ="mohini"
company= input("enter company name")
if company == "google":
    print("G-",employee)
elif company=="microsoft":
    print("M-",employee)
else:
    print("company does not exists")
'''

company = input("enter the company name")
currency_type=input("enter the currency type")
salary_type=input("enter the salary type")
if company == "google":
    if currency_type =="doller":
        if salary_type == "low":
            print("100$")
        elif salary_type=="medium":
            print("200$")
        elif salary_type=="high":
            print("300$")
        else:
            print("salary type does not exists")
    elif currency_type =="rupees":
        if salary_type == "low":
            print("20 LPA")
        elif salary_type=="medium":
            print("30LPA")
        elif salary_type=="high":
            print("40LPA")
        else:
            print("salary type does not exists")
elif company == "microsoft":
    if currency_type =="doller":
        if salary_type == "low":
            print("200$")
        elif salary_type=="medium":
            print("300$")
        elif salary_type=="high":
            print("400$")
        else:
            print("salary type does not exists")
    elif currency_type =="rupees":
        if salary_type == "low":
            print("30 LPA")
        elif salary_type=="medium":
            print("40LPA")
        elif salary_type=="high":
            print("50LPA")
        else:
            print("salary type does not exists")
else:
    print("company does not exists")









