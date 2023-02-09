Products = []
id_list = []
def read_text_from_file():
    f = open('E:\Education\Rio stuff\Python\Session7\database.txt', 'r')
    for line in f:
        result = line.split(',')
        my_dict= {"ID":result[0], "name":result[1], "price":result[2], "count":result[3]}
        Products.append(my_dict)
        id_list.append(result[0])

def add():
    I = input("Enter ID:")
    name = input("Enter name:")
    price = input("Enter price:")
    count = input("Enter count:")

    new_product = {"ID":I , "name":name, "price":price, "count":count}
    Products.append(new_product)
    print("Your product has been successfully added to the list!")

def write_to_database():
    f = open('E:\Education\Rio stuff\Python\Session7\database.txt', 'w+')
    for product in Products:
        x = ','.join([product['ID'],product['name'],product['price'],product['count']])
        f.write(x)

def delete():
    I = input("Enter ID:")
    for product in Products:
        if product["ID"] == I:
            Products.remove (product)
            print("The product was deleted successfully!")

def edit():
    print(Products)
    I = input('Enter ID:')
    for product in Products:
        if product["ID"] == I:
            print("1-Edit Name")
            print("2-Edit Price")
            print("3-Edit Count")
            n = input("Which part do you want to edit?")
            if n == 1:
                x = input('new name:')
                product['name'] = x
                print('Successfuly edited!')
            elif n == 2:
                x = input('new price:')
                product['price'] = x
                print('Succesfuly edited!')
            elif n == 3:
                x = input('new count')
                product['count'] = x
                print('Succesfuly edited!')


def search():
    user_choice = input ("Enter your keyword:")
    for product in Products:
        if product["ID"] == user_choice or product["name"] == user_choice:
            print(product)
            break
    else:
        print("Not found!")

def show_list():
    print(Products)

def buy():
    Shopping_list = []
    shopping_dict = {"ID": choice1, "name":product['name'], "price":choice2*product['price'], "count":choice2}
    Shopping_list.append(shopping_dict)
    choice1 = input("Enter ID:")
    for product in Products:
        if product['ID'] == choice1:
            choice2 = input('Enter count:')
            if choice2 <= product['count']:
                y = product['count']-choice2
            else:
                print('We do not have enough of this product!')
        else:
            print("The product doesn't exist!")
    

def show_menu():
    print("1- Add")
    print("2- Delete")
    print("3- Edit")
    print("4- Search")
    print("5- Show List")
    print("6- Buy")
    print("7- Exit")

read_text_from_file()
while True:
    show_menu()
    choice = int(input("Enter your choice:"))

    if choice == 1:
        add()

    if choice == 2:
        delete()

    if choice == 3:
        edit()

    if choice == 4:
        search()

    if choice == 5:
        show_list()

    if choice == 6:
        buy()

    if choice == 7:
        write_to_database()
        exit(0)