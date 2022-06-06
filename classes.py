from datetime import date
import uuid


class User:
    def __init__(self, first_name, last_name, city, state, email, password, user_id = None, date_created = None):
        if not user_id:
            id = uuid.uuid1()
            uuid_string = str(id)
            self.user_id = uuid_string
        else:
            self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.isManager = 0
        self.city = city
        self.state = state
        self.email = email
        self.password = password
        if not date_created:
            self.date_created = date.today()
        else:
            self.date_created = date_created
        
    def __str__(self):
        return f'{self.user_id}\n{self.first_name}\n{self.last_name}\n{self.city}\n{self.state}\n{self.email}\n{self.password}\n{self.date_created}'
        
    def change_password(self, new_pswd):
        self.password = new_pswd

        
    def update_email(self, new_email):
        self.email = new_email
        
        
    def write(self):
        query = f"""INSERT INTO User (user_id,first_name,last_name,city,state,email,password,date_created)
        VALUES('{self.user_id}','{self.first_name}','{self.last_name}','{self.city}','{self.state}','{self.email}','{self.password}','{self.date_created}')"""
        cursor.execute(query)
        connection.commit()


    def load(id):
        select = f"SELECT * FROM User WHERE user_id = '{id}' "  
        cursor.execute(select)
        row = cursor.fetchone()
        return User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            
            

# user = User.get('3f1cf4dc-b2c8-11ec-985b-3a7a5518b506')
# print(user)

# user = User.get_user()
# matt = User('Matt', 'caldwell', 'vernal', 'utah', 'mac.muscleman@gmail.com', '')
# keith = User('Keith', 'Caldwell', 'Vernal', 'Utah', 'keithcal@yahoo.com', 'passw0rd')
# keith.write()
# keith = User.load('9a900328-b2e0-11ec-9cdf-3a7a5518b506')
# matt.update_email()
# print(keith)
# print(matt)