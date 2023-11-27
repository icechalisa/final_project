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
    database.insert(table)
    database.insert(table2)


def login():
    user_name = input("Please enter your user name: ")
    passw = input("Please enter your password: ")
    for name in data_file('login.csv'):
        if user_name in name.values() and passw in name.values():
            return [name['ID'], name['role']]
    return None


def exit(f):
    new_data = []
    with open(f, mode='w') as variable:
        x = database.search('person').table.index(0)
        csv_reader = csv.writer(variable)
        csv_reader.writerow(x.keys())
        for data in database.search('person').table:
            csv_reader.writerow(data.values())

    """
    
    open file name with wrtie mode
        loop table to get all element
        writerows()
    """
    pass

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:
   
   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()
print(val)
# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
    # see and do admin related activities
# elif val[1] = 'student':
    # see and do student related activities
# elif val[1] = 'member':
    # see and do member related activities
# elif val[1] = 'lead':
    # see and do lead related activities
# elif val[1] = 'faculty':
    # see and do faculty related activities
# elif val[1] = 'advisor':
    # see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit('f')
