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
            print("1. Update a person's information")
            print("2. Update a project's information")
            print("3. Update a login's information")
            print("4. Update an advisor request")
            print("5. Update a member request")
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                self.display_input('persons')
            elif choice == 2:
                self.display_input('project')
            elif choice == 3:
                self.display_input('login')
            elif choice == 4:
                self.display_input('advisor')
            elif choice == 5:
                self.display_input('member')
            if self.update_information(choice):
                break

    def display_input(self, file):
        # Input correct column na
        self.column = input("Please enter the column name: ")
        self.id = input(f"Please enter the {file}'s ID: ")
        self.value = input("Please enter the new value: ")

    def update_information(self, choice):
        if choice == 1:
            # Check data that have correct
            # check column
            print('xxx', self.person.table)
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
            self.project.update(
                column=self.column,
                id=self.id,
                value=self.value
            )
        elif choice == 3:
            self.login.update(
                column=self.column,
                id=self.id,
                value=self.value
            )
        elif choice == 4:
            self.advisor_request.update(
                column=self.column,
                id=self.id,
                value=self.value
            )
        elif choice == 5:
            self.member_request.update(
                column=self.column,
                id=self.id,
                value=self.value
            )


