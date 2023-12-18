# import database module

# define a function called initializing

import csv
from database import Table, Database

database = Database()


def data_file(f):
    with open(f) as variable:
        old_data = []
        for data in csv.DictReader(variable):
            old_data.append(data)
        return old_data


def initializing():
    table = Table('persons', data_file('persons.csv'))
    table2 = Table('login', data_file('login.csv'))
    table3 = Table('project', data_file('project.csv'))
    table4 = Table('advisor-request', data_file('advisor-request.csv'))
    table5 = Table('member-request', data_file('member-request.csv'))
    print('table', table)
    database.insert(table)
    database.insert(table2)
    database.insert(table3)
    database.insert(table4)
    database.insert(table5)


def login():
    user_name = input("Please enter your user name: ")
    passw = input("Please enter your password: ")
    for name in data_file('login.csv'):
        if user_name in name.values() and passw in name.values():
            return [name['ID'], name['role']]
    return None


def exit():
    for i in database.database:
        with open(i.table_name + '.csv', 'w') as variable:
            csv_reader = csv.writer(variable)
            csv_reader.writerow(i.table[0].keys())
            for data in i.table:
                csv_reader.writerow(data.values())


# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()
print(val)

if val[1] == 'admin':
    from admin import Admin
    admin = Admin(database)
    admin.display_choice()
elif val[1] == 'student':
    from student import Student
    student = Student(database, val[0])
    role = student.display_choice()
    if role == 'lead':
        from lead import LeadStudent
        lead = LeadStudent(database, val[0])
        lead.display_choice()
elif val[1] == 'member':
    from member import Member
    member = Member(database, val[0])
    member.display_choice()
elif val[1] == 'lead':
    from lead import LeadStudent
    lead = LeadStudent(database, val[0])
    lead.display_choice()
elif val[1] == 'faculty':
    from faculty import Faculty
    faculty = Faculty(database, val[0])
    faculty.display_choice()
elif val[1] == 'advisor':
    from advisor import Advisor
    advisor = Advisor(database, val[0])
    advisor.display_choice()
for i in database.database:
    print(i.table_name, i.table)
# once everyhthing is done, make a call to the exit function
exit()
