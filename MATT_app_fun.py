from audioop import add
from MATT_sql import *
from MATT_database import *
from MATT_menu import *
from datetime import date


def add_user_func():
    print('Press Enter To Leave Blank\n')
    f_name = input('Enter First Name: ').title()
    l_name = input('Enter Last Name: ').title()
    phone = input('Enter Phone Number: ')
    email = input('Enter Email: ')
    passwd = input('Enter Password: ')
    date_created = f'{date.today()}'
    hire_date = input('Date Hired: ')
    user_type = input('Are They a Manager (y/n): ').lower()
    if user_type == 'y':
        user_type = 'manager'
    elif user_type == 'n':
        user_type = 'user'
    else:
        print('User Type Not Available')
        user_type
    values = (f_name,l_name,phone,email,passwd,date_created,hire_date,user_type)
    check = input(f'{print(values)}\nDoes This Look Correct (y/n)').lower()
    if check == 'y':
        add_user(connection, ADD_USER, values)
    elif check == 'n':
        add_user_func()

            
        
def add_comp_func():
        comp = input('Enter Name of Competency: ').title()
        date_created = f'{date.today()}'
        values = (comp, date_created)
        print(values)
        check = input('Does This Information Look Correct? (y/n)').lower()
        if check == 'y':
            add_comp(connection, ADD_COMP, values)
        elif check == 'n':
            add_comp_func()
            
            
            
def add_ass_to_comp():
    assess_name = input('Enter Assessment Name: ').title()
    date_created = f'{date.today()}'
    print_comp_name_id(connection)
    comp_id = int(input('Enter The Competency id\nWhere The Assessment Will Be Under: '))
    values = (assess_name,date_created,comp_id)
    print(values)
    check = input('Does This look correct? (y/n)').lower()
    if check == 'y':
        add_assess_to_comp(connection,ADD_ASSESS_TO_COMP,values)
        print(manager_add_menu)
    elif check == 'n':
        add_ass_to_comp()
    

def edit_user_info():
    pass