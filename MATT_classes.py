import sqlite3
from MATT_sql import *
connection = sqlite3.connect('MATT.db')
cursor = connection.cursor()

class Authentication:
    def __init__(self,id,first_name,last_name,phone,email,password,active,date_created,hire_date,user_type):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = password
        self.active = active
        self.date_created = date_created
        self.hire_date = hire_date
        self.user_type = user_type
        self.authorized = 0

    def __str__(self):
        head = f"{'ID':<3}{'First Name':<12.12}{'Last Name':<12.12}{'Phone':<15.15}{'Email':<25.25}{'User Type':<9}"
        line = '-'*76
        info = f"{str(self.id):<3}{self.first_name:<12.12}{self.last_name:<12.12}{self.phone:<15.15}{self.email:<25.25}{self.user_type:<9}"
        return f'{head}\n{line}\n{info}'
    
    
    

class User(Authentication):
    pass
    

class Manager(User):
    pass
    