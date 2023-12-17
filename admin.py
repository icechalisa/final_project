from database import Database
from database import Table


class Admin:

    def __init__(self, database):
        self.database = database
        self.column = None
        self.id = None
        self.value = None
        self.person: Table = self.database.search('persons')  # Return Table
        # person.update()
        self.login: Table = database.search('login')
        self.project: Table = database.search('project')
        self.advisor_request: Table = database.search('advisor-request')
        self.member_request: Table = database.search('member-request')

    def display_choice(self):
        while True:
            print('-----Welcome to admin page-----')
            print("1. Update a person's information")
            print("2. Update a project's information")
            print("3. Update a login's information")
            print("4. Update an advisor request")
            print("5. Update a member request")
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                self.display_input('persons', self.person)
            elif choice == 2:
                self.display_input('project', self.project)
            elif choice == 3:
                self.display_input('login', self.login)
            elif choice == 4:
                self.display_input('advisor', self.advisor_request)
            elif choice == 5:
                self.display_input('member', self.member_request)
            if self.update_information(choice):
                break

    def display_input(self, file, table):
        self.column = input("Please enter the column name: ")
        while True:
            if self.column in table.table[0].keys():
                break
            else:
                print("Column is not exist")
                self.column = input("Please enter the column name: ")
        self.id = input(f"Please enter the {file}'s ID: ")
        while True:
            if self.id in table.table[0].values():
                break
            else:
                print(f"{file}'s ID is not exist")
                self.id = input(f"Please enter the {file}'s ID: ")
        self.value = input("Please enter the new value: ")
        while True:
            if self.value != '':
                break
            else:
                print("Value is not exist")
                self.value = input("Please enter the new value: ")

    def update_information(self, choice):
        if choice == 1:
            print('Table person', self.person.table)
            if self.column in self.person.table[0].keys():
                self.person.update(
                    column=self.column,
                    id=self.id,
                    value=self.value
                )
                print(self.person.table)
                return True
            else:
                print("Column is not exist")
                return False
        elif choice == 2:
            print('Table project', self.project.table)
            if self.column in self.project.table[0].keys():
                self.project.update(
                    column=self.column,
                    id=self.id,
                    value=self.value
                )
                print(self.project.table)
                return True
            else:
                print("Column is not exist")
                return False
        elif choice == 3:
            print('Table login', self.login.table)
            if self.column in self.login.table[0].keys():
                self.login.update(
                    column=self.column,
                    id=self.id,
                    value=self.value
                )
                print(self.login.table)
                return True
            else:
                print("Column is not exist")
                return False
        elif choice == 4:
            print('Table advisor', self.advisor_request.table)
            if self.column in self.advisor_request.table[0].keys():
                self.advisor_request.update(
                    column=self.column,
                    id=self.id,
                    value=self.value
                )
                print(self.advisor_request.table)
                return True
            else:
                print("Column is not exist")
                return False
        elif choice == 5:
            print('Table member', self.member_request.table)
            if self.column in self.member_request.table[0].keys():
                self.member_request.update(
                    column=self.column,
                    id=self.id,
                    value=self.value
                )
                print(self.member_request.table)
                return True
            else:
                print("Column is not exist")
                return False
        else:
            print("Choice is not exist")
            return False


