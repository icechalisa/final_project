from database import Table


class Member:

    def __init__(self, database, _id):
        self.my_project = None
        self.id_list = None
        self.database = database
        self.column = None
        self.id = None
        self.value = None
        self.project: Table = database.search('project')
        self.persons: Table = database.search('persons')
        self.member_request: Table = database.search('member-request')
        self.person_id = _id

    def check_status(self):
        check_name = self.person_id
        for project in self.project.table:
            if check_name in project.values():
                print(f'-{project["Title"]}: {project["Status"]}')

    def check_response(self):
        requests = []
        for request in self.member_request.table:
            if self.person_id == request['to_be_member']:
                requests.append(request)
        return requests

    def display_project(self):
        self.id_list = []
        check_name = self.person_id
        for project in self.project.table:
            if check_name in project.values():
                self.id_list.append(project['ID'])
                print(f'Detail: {project}')

    def display_choice(self):
        while True:
            print("1. Project's status")
            print("2. Display a project's information")
            print("3. Update a project's information")
            print("4. All requests")
            print("5. Exit")
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                print('-----Project status-----')
                self.check_status()
                print('')
            elif choice == 2:
                print('-----Project information-----')
                self.display_project()
                print('')
            elif choice == 3:
                print('-----Update project information-----')
                # choice = int(input('Please choose your project: '))
                self.id_list = []
                check_name = self.person_id
                self.my_project = []
                n = 1
                for project in self.project.table:
                    if check_name in project.values():
                        self.id_list.append(project['ID'])
                        print(f'{n}. Detail: {project}')
                        self.my_project.append(project)
                        n += 1

                self.display_input('project', self.project, self.my_project)
                self.update_information()
                print('')
            elif choice == 4:
                print('-----All requests-----')
                for request in self.check_response():
                    print('Your request: ', request['ID'] + ' ' + request['Response'] + ' ' + request['Response_date'])
                print('')
            elif choice == 5:

                break

    def display_input(self, file, table, my_project):
        while True:
            selected_project = int(input('Please choose your project: '))
            if 0 < selected_project <= len(my_project):
                self.id = my_project[selected_project - 1]['ID']
                while True:
                    self.column = input("Please enter the column name: ")
                    if self.column in table.table[0].keys():
                        break
                    else:
                        print("Column is not exist")
                while True:
                    self.value = input("Please enter the new value: ")
                    if self.value != '':
                        break
                    else:
                        print("Value is not exist")
                break
            else:
                print('Please choose your project again')
                print('--------------------------------')

    def update_information(self):
        print('New information', self.project.table)
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
