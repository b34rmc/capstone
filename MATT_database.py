from MATT_classes import *
from MATT_sql import *
from datetime import date
import bcrypt
import sqlite3


all_users_header = f"\n{'ID':<4}{'First Name':<12}{'Last Name':<12}{'Phone':<25}{'Email':<27.25}{'Active':<9}{'Date Created':<15}{'Hire Date':<15}{'user_type':<8}"
add_comp_header = f'\n{"ID":<4}{"First Name":<12}{"Last Name":<12}'
    


#______________________Connection_And_Table_Creation______
def connect():
    return sqlite3.connect('MATT.db')


    
def create_schema(connection, sql_query):
    cursor = connection.cursor()
    return cursor.execute(sql_query)


#______________________For_Verifying_Users_In_DataBase____________
def select_user_by_email(connection, sql_query, email):
    with connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(sql_query, email)
        return cursor.fetchone()
    

#********************____________________________Manager_SQL_Functions__________________________**********************

#__________________View_Menu___________________________________
def view_all_users(connection):
    with connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        db_users = cursor.execute(VIEW_ALL_USERS).fetchall()
        print('\n\n')
        print(all_users_header)
        print('-'*(len(all_users_header)+2))
        for row in db_users:
            print(f"\n{row['id']:<4}{row['first_name']:<12}{row['last_name']:<12}{row['phone']:<25}{row['email']:<27.25}{row['active']:<9}{row['date_created']:<15}{row['hire_date']:<15}{row['user_type']:<8}")
            
        print('\n\n')


def search_for_user_by_first(connection, LIKE):
    with connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM User WHERE first_name LIKE ?", (LIKE + "%",))
            rows = cursor.fetchall()
            print('\n\n')
            print(all_users_header)
            print('-'*(len(all_users_header)+2))
            for row in rows:
                print(f"\n{row['id']:<4}{row['first_name']:<12}{row['last_name']:<12}{row['phone']:<25}{row['email']:<27.25}{row['active']:<9}{row['date_created']:<15}{row['hire_date']:<15}{row['user_type']:<8}")
            
            print('\n\n')
        
def search_for_user_by_last(connection, LIKE):
    with connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM User WHERE last_name LIKE ?", (LIKE + "%",))
            rows = cursor.fetchall()
            print('\n\n')
            print(all_users_header)
            print('-'*(len(all_users_header)+2))
            for row in rows:
                print(f"\n{row['id']:<4}{row['first_name']:<12}{row['last_name']:<12}{row['phone']:<25}{row['email']:<27.25}{row['active']:<9}{row['date_created']:<15}{row['hire_date']:<15}{row['user_type']:<8}")

            print('\n\n')
            
def print_comp_name_id(connection):
    with connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute('SELECT id, name FROM Competency')
        rows = cursor.fetchall()
        print('\n\n')
        print(f"{'Id':<4}{'Name':<28}")
        for row in rows:
            print(f"\n{row['id']:<4}{row['name']:<28}")
        print('\n\n')
    
#______________Add_Menu____________________________________
    
    
    

def add_user(connection, sql_query, values):
    values_list = list(values)
    pw = values[4]
    passwdenc = pw.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_pw = bcrypt.hashpw(passwdenc, salt)
    values_list[4] = hash_pw.decode()
    values = tuple(values_list)
    with connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(sql_query,values)
    return cursor
    
    
def add_comp(connection, sql_query, values):
    with connection:
        cursor = connection.cursor()
        cursor.execute(sql_query, values)
        
        
def add_assess_to_comp(connection, sql_query, values):
    with connection:
        cursor = connection.cursor()
        cursor.execute(sql_query,values)
        
def add_result_for_user(connection, sql_query, values):
    with connection:
        cursor = connection.cursor()
        cursor.execute(sql_query,values)
        
#--------Test add_user() function--------------
# values = ('josh','Caldwell','435-621-4073','joshcal','1234','04-16-2022')
# dbconn = connect()
# add_user(dbconn, ADD_USER, values)

# INSERT INTO User(first_name, last_name, phone, email, password, date_created)
# VALUES(?,?,?,?,?,?)
    
def update_user_by_id(connection,sql_query,values):
    
    with connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(sql_query,values)
        return cursor


def update_user_in_database():
    pass


# UPDATE Users SET phone_number = "555-555-5553" WHERE user_id='12345';