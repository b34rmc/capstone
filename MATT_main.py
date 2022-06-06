from MATT_classes import *
from MATT_database import *
from MATT_menu import *
from MATT_sql import *
from MATT_app_fun import *
from getpass import getpass
import sys
import time
import bcrypt
from datetime import date
connection = connect()

def load_user(email):
    db_user = select_user_by_email(connection, SELECT_USER_BY_EMAIL, (email,))
    if db_user:
        email = str(db_user['email']).lower()
        
        if db_user['user_type'] == 'manager':
            return Manager(
            db_user['id'],
            db_user['first_name'],
            db_user['last_name'],
            db_user['phone'],
            email,
            db_user['password'],
            db_user['active'],
            db_user['date_created'],
            db_user['hire_date'],
            db_user['user_type']
        )
        else:
            return User(
                db_user['id'],
                db_user['first_name'],
                db_user['last_name'],
                db_user['phone'],
                email,
                db_user['password'],
                db_user['active'],
                db_user['date_created'],
                db_user['hire_date'],
                db_user['user_type']
            )
    return None




def login():
    email = input("Enter Email: ")
    if email.lower() == "q":
        print("Goodbye")
        return "quit"
    password = getpass("Enter Password: ")
    current_user = load_user(email.lower())

    if current_user:
        db_hash = current_user.password
        db_hash_enc = db_hash.encode("utf-8")
        password_enc = password.encode("utf-8")

        if bcrypt.checkpw(password_enc, db_hash_enc):
            current_user.authorized = 1
            return current_user
        else:
            return None
    else:
        return None


def manager_view():
    print(manager_view_menu)
    while True:
        try:
            user_input = int(input('Enter Number: '))
        except:
            print('Invalid Input')
        if user_input == 1:
            print(current_user)
            
        elif user_input == 2:
            view_all_users(connection)
            print(f'\n\n{manager_view_menu}')
            
        elif user_input ==  3:
            while True:
                search_term = input('\nPress q To Return To Menu\nSearch For User By First: ').lower()
                if search_term != 'q':
                    search_for_user_by_first(connection, search_term)
                elif search_term == 'q':
                    return manager_view()
     
        elif user_input == 4:
            while True:
                search_term = input('\nPress q To Return To Menu\nSearch For User By Last:').lower()
                if search_term != 'q':
                    search_for_user_by_last(connection, search_term)
                elif search_term == 'q':
                    return manager_view()

        elif user_input == 5:
            pass
        elif user_input == 6:
            pass
        elif user_input == 7:
            pass
        elif user_input == 8:
            manager_main()
        else:
            print('Invalid Input')
    
    
def manager_add():
    print(manager_add_menu)
    while True:
        try:
            user_input = int(input('Enter Number: '))
        except:
            print('Invalid Input')
        if user_input == 1:
            add_user_func()
        elif user_input == 2:
            add_comp_func()
        elif user_input ==  3:
            add_ass_to_comp()
        elif user_input == 4:
            def add_assess_result_for_user():
                user_id = input('Enter ID of Student: ')
                assessment_id = input('Enter assessment ID: ')
                score = int(input('Enter Score For Student: '))
                if score in range(5):
                    score = score
                else:
                    print('invalid score entered\n\n')
                    return add_assess_result_for_user()
                date_taken = (f'{date.today()}')
                manager_id = current_user.id
                values = (user_id,assessment_id,score,date_taken,manager_id)
                print(values)
                check = input('Does This look correct? (y/n)').lower()
                if check == 'y':
                    add_result_for_user(connection,ADD_ASSESS_RESULT_FOR_USER,values)
                    return manager_add()
                elif check == 'n':
                    print('\n\n')
                    add_assess_result_for_user()
                else:
                    print('Invalid Input\n\n')
                    return add_assess_result_for_user()
            add_assess_result_for_user()
                
        elif user_input == 5:
            manager_main()
        else:
            print('Invalid Input')
    
    
def manager_edit():
    print(manager_edit_menu)
    while True:
        try:
            user_input = int(input('Enter Number: '))
        except:
            print('Invalid Input')
        if user_input == 1:
            edit_user_info()
        elif user_input == 2:
            pass
        elif user_input ==  3:
            pass
        elif user_input == 4:
            pass
        elif user_input == 5:
            manager_main()
        else:
            print('Invalid Input')

    
    
def manager_delete():
    print(manager_delete_menu)
    while True:
        try:
            user_input = int(input('Enter Number: '))
        except:
            print('Invalid Input')
        if user_input == 1:
            pass
        elif user_input == 2:
            manager_main()
        else:
            print('Invalid Input')
    
    
def user_menu():
    print(user_option_menu)
    while True:
        try:
            user_input = int(input('Enter Number: '))
        except:
            print('Invalid Input')
        if user_input == 1:
            print(current_user)
        elif user_input == 2:
            pass
        elif user_input ==  3:
            pass
        elif user_input == 4:
            pass
        elif user_input == 5:
            pass
        elif user_input == 6:
            pass
        elif user_input == 7:
            pass
        elif user_input == 8:
            pass
        elif user_input == 9:
            sys.exit()
        else:
            print('Invalid Input')
    


def manager_main():
    print(manager_main_menu)
    while True:
        try:
            user_input = int(input('Enter Number: '))
        except:
            print('Invalid Input')
        if user_input == 1:
            manager_view()
        elif user_input == 2:
            manager_add()
        elif user_input == 3:
            manager_edit()
        elif user_input == 4:
            manager_delete()
        elif user_input == 5:
            sys.exit()
        else:
            print('Invalid Input')
            
            
            
print(login_menu)
login_attempts = 0
delay = 30
while login_attempts <= 5:
    current_user = login()
    if current_user == "quit":
        break
    elif current_user:
        break
    else:
        print("Incorrect Login, Please Try Again!")
        login_attempts += 1
        if login_attempts == 5:
            print(
                f"Too Many Failed Attempts, You Must Wait {delay} Seconds Before Trying Again!"
            )
            time.sleep(delay)
            delay *= 2
            login_attempts = 4

if current_user:
    if current_user == "quit":
        pass
    elif current_user.authorized == 1:
        print(f"\nWelcome {current_user.first_name}\n\nWhat Would You Like To Do\n-------------------------")
        if current_user.user_type == 'manager':
            manager_main()
        elif current_user.user_type == 'user':
            user_menu()
            
            
# def view_my_competency():
#         pass

# def view_my_assessment():
#     pass

# def change_first(self, connection, sql_query, values):
#     pass

# def change_last(self, connection, sql_query, values):
#     pass

# def change_pass(self, connection, sql_query, values):
#     pass

# def change_email(self, connection, sql_query, values):
#     pass

# def change_phone(self, connection, sql_query, values):
#     pass

# new_first = input('Enter New Name: ')
# print(new_first)
# save = input('Press 1 To Save or 2 To Cancel: ')
# if save == '1':
#     user.first_name = new_first
# elif save == '2':
#     print('No Changes Have Been Made')
#     return user_option_menu
# else:
#     print('Wrong Command')