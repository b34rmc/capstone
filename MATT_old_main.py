# from MATT_classes import *
# from MATT_database import *
# from MATT_menu import *
# from MATT_main import *
# from MATT_sql import *
# from getpass import getpass
# import time
# import bcrypt



# def load_user(email):
#     db_conn = connect()
#     db_user = select_user_by_email(db_conn, SELECT_USER_BY_EMAIL, (email,))
#     if db_user:
#         email = str(db_user['email']).lower()
        
#         if db_user['user_type'] == 'manager':
#             return Manager(
#             db_user['id'],
#             db_user['first_name'],
#             db_user['last_name'],
#             db_user['phone'],
#             email,
#             db_user['password'],
#             db_user['active'],
#             db_user['date_created'],
#             db_user['hire_date'],
#             db_user['user_type']
#         )
#         else:
#             return User(
#                 db_user['id'],
#                 db_user['first_name'],
#                 db_user['last_name'],
#                 db_user['phone'],
#                 email,
#                 db_user['password'],
#                 db_user['active'],
#                 db_user['date_created'],
#                 db_user['hire_date'],
#                 db_user['user_type']
#             )
#     return None




# def login():
#     email = input("Enter Email: ")
#     if email.lower() == "q":
#         print("Goodbye")
#         return "quit"
#     password = getpass("Enter Password: ")
#     current_user = load_user(email.lower())

#     if current_user:
#         db_hash = current_user.password
#         db_hash_enc = db_hash.encode("utf-8")
#         password_enc = password.encode("utf-8")

#         if bcrypt.checkpw(password_enc, db_hash_enc):
#             current_user.authorized = 1
#             return current_user
#         else:
#             return None
#     else:
#         return None


# print(login_menu)
# login_attempts = 0
# delay = 30
# while login_attempts <= 5:
#     current_user = login()
#     if current_user == "quit":
#         break
#     elif current_user:
#         break
#     else:
#         print("Incorrect Login, Please Try Again!")
#         login_attempts += 1
#         if login_attempts == 5:
#             print(
#                 f"Too Many Failed Attempts, You Must Wait {delay} Seconds Before Trying Again!"
#             )
#             time.sleep(delay)
#             delay *= 2
#             login_attempts = 4

# if current_user:
#     if current_user == "quit":
#         pass
#     elif current_user.authorized == 1:
#         print(
#             f"\nWelcome {current_user.first_name}\n\nWhat Would You Like To Do\n-------------------------"
#         )
#         if current_user.user_type == 'manager':
#             manager_main()
#         elif current_user.user_type == 'user':
#             user_menu()