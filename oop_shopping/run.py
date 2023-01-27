import string
import json
import class_shopping

class User():

    def __init__(self, username: str, password: str, phone: int):
        self.username = username
        self.password = password
        self.phone = phone
    
    
    @property
    def username(self)->str:
        return self.__username

    @username.setter
    def username(self, value)->None:
        if not isinstance(value, str):
            raise TypeError('username must be string')
        if not value[0].isalpha():
            raise ValueError('username must be character')
        self.__username = value

    @property
    def password(self)->str:
        return self.__password

    @password.setter
    def password(self, value)->None:
        if len(value) < 8:
            raise ValueError('The length of the password must be more than 8 characters')
        self.__password = value
    
    @property
    def phone(self)->int:
        return self.__phone
    
    @phone.setter
    def phone(self, value):
        if not type(value) != int:
            raise TypeError('username must be integer')
        self.__phone = value
    
    @classmethod
    def register(cls, username, password, phone):
        with open('user_database.json', mode='r')as file:
            users_database = json.load(file)
        with open('user_database.json', mode='w') as f:
            users_database[username] = {
                'password': password,
                'phone': phone
            }
        json.dump(users_database, f , indent=4,separators=(', ', ': '))
    
    @classmethod
    def login(cls, username, password):
        if username

        
    

        
