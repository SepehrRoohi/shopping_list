import os
import json




class Item_list():
    
    def __init__(self, name_item, price, stock):
        self.name_item = name_item
        self.price = price
        self.stock = stock
    
    @classmethod
    def add_product(cls, item):
        with open('oop_shopping\product.json', mode='r') as f:
            user_database = json.load(f)
            for category,dict_1 in user_database.items():
                for title_product,dict_2 in dict_1.items():
                    if title_product == item:
                        shopping_list = list()
                        shopping_list.append(item)
                        
                
            

    
    



    
