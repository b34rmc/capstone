from MATT_classes import *
from MATT_database import *
import sqlite3
import bcrypt

connection = connect()


# def f(s):
#   p,r = ('-','')
#   if len(s) < 10:
#     return '___'
#   if len(s) == 10:
#     r = '1'
#   return(f'{r}({s[0:3]}) {s[3:6]}{p}{s[6:10]}')

# print(f('4358284073'))





# menu_options = {
#     1: 'Option 1',
#     2: 'Option 2',
#     3: 'Option 3',
#     4: 'Exit',
# }

# def print_menu():
#     for key in menu_options.keys():
#         print (key, '--', menu_options[key] )

# def option1():
#      print('Handle option \'Option 1\'')

# def option2():
#      print('Handle option \'Option 2\'')

# def option3():
#      print('Handle option \'Option 3\'')

# if __name__=='__main__':
#     while(True):
#         print_menu()
#         option = ''
#         try:
#             option = int(input('Enter your choice: '))
#         except:
#             print('Wrong input. Please enter a number ...')
#         #Check what choice was entered and act accordingly
#         if option == 1:
#            option1()
#         elif option == 2:
#             option2()
#         elif option == 3:
#             option3()
#         elif option == 4:
#             print('Thanks message before exiting')
#             exit()
#         else:
#             print('Invalid option. Please enter a number between 1 and 4.')












    
# values = ('josh','Caldwell','435-621-4073','joshcal','1234','04-16-2022')
# print(values)
# add_user(connection, ADD_USER, (values,))









users = get_users(connection, GET_ALL_USERS)
for user in users:
    id = user['id']
    first = user['first_name']
    last = user['last_name']
    phone = user['phone']
    email = user['email']
    password = user['password']
    active = user['active']
    date = user['date_created']
    hire = user['hire_date']
    type = user['user_type']
    
    passwdenc = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_pw = bcrypt.hashpw(passwdenc, salt)
    
    user_tuple = (first,last,phone,email,hash_pw.decode(),active,date,hire,type,id)
    update_user_by_id(connection,UPDATE_USER_BY_ID,user_tuple)
#     def select_users_fname_like(connection, sql_query, like):
#         """
#         Parameters
#         connection - conenction variable to database
#         sql_query - string sql query
#         like - string to pass to the SQL LIKE parameter

#         return - one sql row object or none if address not found
#         """
#         with connection:
#             connection.row_factory = sqlite3.Row
#             cursor = connection.cursor()
#             cursor.execute(sql_query, (like + "%",))
#             return cursor.fetchall()

# SELECT_USERS_FNAME_LIKE = """
#     SELECT * FROM User WHERE first_name LIKE ?
# """

# db_conn = connect()
# users = select_users_fname_like(db_conn, SELECT_USERS_FNAME_LIKE, "kei")
# for user in users:
#     print(f"{user['first_name']} {user['last_name']}")
