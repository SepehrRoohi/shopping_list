from typing import List, Dict
import os
from enum import Enum
from tabulate import tabulate
import json
import pyfiglet
import logging
import logging.config

print(pyfiglet.figlet_format("welcome to store"))
# To exit the list
EXIT_COMMANDS = ["q", "ex", "exit", "quit"]
# To list items
logging.config.fileConfig(
    fname="logging_setting.toml", disable_existing_loggers=False
)  # noqa E501
logger = logging.getLogger("custom_log.log")


def check_password(pw, confirm_pw):
    while len(pw) < 8:
        print("The password is 8 characters")
        pw = input("Enter your password: ").strip()
        confirm_pw = input("Enter your password again: ").strip()
    while pw != confirm_pw:
        print("Passwords are not the same")
        pw = input("Enter your password: ").strip()
        confirm_pw = input("Enter your password again: ").strip()


def check_phone_number(ph):
    while len(ph) != 11:
        print("The phone number is wrong")
        try:
            ph = input("Enter your mobile number: ")
            int_got_num = int(ph)
        except ValueError:
            print("you need to enter correct phone")


def add_data_user(username, password, phone):
    with open("data_user.json", mode="r") as f:
        data = json.load(f)
        info = {
            "username": f"{username}",
            "password": f"{password}",
            "phone": f"{phone}",
        }
        data[f"{username}"] = info
        new_info = json.dumps(data, indent=4)
    with open("data_user.json", mode="w") as f:
        f.write(new_info)


def register():
    username = input("Enter your name: ").strip().lower()
    while username is False:
        print("The username is entered incorrectly")
        username = input("Enter your name: ").strip().lower()
    password = input("Enter your password: ").strip()
    confirm_password = input("Enter your password again: ").strip()
    check_password(password, confirm_password)
    phone = input("Enter your mobile number: ")
    check_phone_number(phone)
    print("successful")
    return username, password, phone


def question_from_the_user():
    ask_user = input("Login Or Register? ")
    if ask_user == "register":
        register()


shopping_list: List[str] = list()
fruits_commodity = {
    "banana": 200,
    "apple":  500,
    "orange":  400,
    "pear": 750,
    "cucumber":  450,
    "watermelon": 200,
    "tangerine":  800
}
fruits_prices: dict = {
    "banana": 10,
    "apple":  6,
    "orange":  4,
    "pear": 7.5,
    "cucumber":  3.5,
    "watermelon": 1.6,
    "tangerine":  8
}
vegetables_commodity: dict = {
    'cabbage': 200,
    'eggplant': 300,
    'onion': 100,
    'tomato': 150
}
vegetables_price: dict = {
    'cabbage': 2,
    'eggplant': 3,
    'onion': 1,
    'tomato': 1.5
}

print('Fruits')
print('=================')
for product in fruits_commodity:
        print(product.title())
        print(f'price: {fruits_prices[product]}$')
        print(f'stoke: {fruits_commodity[product]}')
        print('=================')
print('vegetables')
for product in vegetables_commodity:
        print(product.title())
        print(f'price: {vegetables_price[product]}$')
        print(f'stoke: {vegetables_commodity[product]}')
        print('=================')


def search_shopping_list(list_Products, item):
    """
    Parameters
    ----------
    list_Products : User shopping list
    item : User product input
    -------
    """
    if item in list_Products:
        print(f"there is {item} in list")
    else:
        print(f"sorry,there is no {item} in list")


def remove_item(list_Products, item):
    """

    Parameters
    ----------
    list_Products : user list
    item : User product input
    Returns
    -------

    """
    if item not in list_Products:
        print("item that you are trying to remove is not in the list")
    else:
        list_Products.remove(item)
    return list_Products


# To show


def show_help():
    """ """
    print("enter `quit` to exit the app and see your list")
    print("enter `help` to see help")
    print("enter `edit` to edit item")
    print("enter `search` to search item in list")
    print("enter `remove` to remove list")
    print("enter `show ` to show shopping list")
    print("enter `calories` to show calorie products")
    print("================================")


# To show the edit


def edit_item(list_Products, previous_item, new_item):
    """

    Parameters
    ----------
    list_Products :user list
    previous_item : user item
    new_item : edit item
    Returns
    -------
    """
    if previous_item not in list_Products:
        print("the item you are trying to edit is not in the list")
    else:
        index_item = list_Products.index(previous_item)
        list_Products[index_item] = new_item
        return list_Products


def beautify_shopping_list(list_products):
    """

    Parameters
    ----------
    list_Products : user list
    Returns
    -------

    """
    for shopping_list in list_products:
        print(f"> {shopping_list}")


def add_item(list_Products, item):
    """

    Parameters
    ----------
    list_Products : user list
    item : item user
    Returns
    -------

    """
    if item not in shopping_list:
        shopping_list.append(item)
        return list_Products
    else:
        print("This product is in your shopping list")


def clear_screen():
    """ """
    return os.system("cls")


username, password, phone = register()
logger.info("new user registered")
add_data_user(username, password, phone)

while True:
    item: str = input("Enter a item: ").casefold()
    item_check = item.isalpha()
    if item_check is True:
        clear_screen()
        if item in EXIT_COMMANDS:
            beautify_shopping_list(shopping_list)
            break
        match item:
            case "show":
                beautify_shopping_list(shopping_list)
            case "calories":
                class Calories(Enum):
                    banana = 89
                    apple = 52
                    orange = 47
                    pear = 57
                    cucumber = 50
                    watermelon = 30
                    cabbage = 25
                    eggplant = 25
                    onion = 40
                    tomato = 18

                print("calories")
                for calories in Calories:
                    print("================")
                    print(f"{calories.name} = {calories.value}")
            case  'help':
                show_help()
            case  'remove':
                item_to_remove = input('please enter the item you want to remove: ') # noqa E501
                remove_item(shopping_list, item_to_remove)
            case 'search':
                search_item = input('enter a item: ')
                search_shopping_list(shopping_list, search_item)
            case'edit':
                previous_item = input('enter the item you want to edit: ')
                new_item = input('enter the name you want to replace: ')
                if new_item in fruits_commodity and new_item in vegetables_commodity: # noqa E501
                    edit_item(shopping_list, previous_item, new_item)
                else:
                    print('this product is not available')
            case _:
                if item in fruits_commodity and item in vegetables_commodity:
                    print(input('item is already in your list'))
                elif item not in shopping_list and item in vegetables_commodity or item in fruits_commodity: # noqa E501
                    add_item(shopping_list, item)
                    print(f'add in list {item} number of lists {len(shopping_list)}') # noqa E501
                else:
                    print('this product is not available')
    else:
        print('Please enter the correct item name')
