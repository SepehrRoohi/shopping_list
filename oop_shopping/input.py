import json
from class_shopping import Item_list
from run import User


while True:
    try:
        username = input("Enter your name: ").strip().lower()
    except TypeError:
        print('username must be a string')
    try:
        password = input("Enter your password: ").strip()
    except ValueError:
        print('Character length should be more than 8')
    confirm_password = input("Enter your password again: ").strip()
    try:
        phone = input("Enter your mobile number: ")
    except TypeError:
        print('phone must be a integer')
    except Exception as e :
        print(e)
    user = User(username, password, phone)
    with open('func\data_user.json', mode='r')as file:
            users_database = json.load(file)
        if username in users_database.keys():
            
            
                            
                    

    while True:
        category_item = input('Choose your desired category: ')
        with open('oop_shopping\product.json', mode='r')as file:
            users_database = json.load(file)
        while category_item != "fruits" or category_item != "vegetables":
            print('The category is wrong')
            category_item = input('Choose your desired category: ')
        else:
        
            
    
                    
                    
                    
                        
                    
                    
                    
                    
                    #     shopping_list.append(name)
                    #     print('Your selected products have been added to the list')
                    #     item = input('Enter a item: ')
                    # else:
                    #     print('Your product is not available in the store')
                    #     item = input('Enter a item: ')
                        
                        
                        
                
    

