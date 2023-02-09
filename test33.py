from prettytable import PrettyTable
Products = []
def read_text_from_file():
    f = open('E:\Education\Rio stuff\Python\Session7\database.txt', 'r')
    for line in f:
        result = line.split(',')
        my_dict= {"ID":result[0], "name":result[1], "price":result[2], "count":result[3].replace('\n','')}
        Products.append(my_dict)

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
        x = ','.join([product['ID'],product['name'],product['price'],product['count']+"\n"])
        f.write(x)

def delete():
    I = input("Enter ID:")
    for product in Products:
        if product["ID"] == I:
            Products.remove (product)
            print("The product was deleted successfully!")

def edit():
    show_list()
    I = input('Enter ID:')
    for product in Products:
        if product["ID"] == I:
            print("1-Edit Name")
            print("2-Edit Price")
            print("3-Edit Count")
            n = int(input("Which part do you want to edit?"))
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
   Products_table = PrettyTable(['ID', 'Name', 'Price', 'Count'])
   for product in Products:
    Products_table.add_row([product['ID'], product['name'], product['price'], product['count']])
    print(Products_table)


def buy():
    show_list()
    I = input("enter id :")
    for product in Products:
        if product["ID"] == I:
            amount = input("How much?")
            if amount <= product['count']:
                Shopping_list = []
                Shopping_dict= {"ID":I, "name":product['name'], "price":int(product['price'])*amount, "count":int(amount)}
                Shopping_list.append(Shopping_dict)
                print(Shopping_list)
            elif amount > product['count']: 
                print('we do not have enough of this product!')
    else:
        print('We do not have this product!')

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