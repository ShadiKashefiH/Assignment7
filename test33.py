Products = []
def read_text_from_file():
    f = open('E:\Education\Rio stuff\Python\Sessin7\database.txt','r')
    for line in f:
        result = line.split(',')
        my_dict= {"id":result[0], "name":result[1], "price":result[2], "count":result[3]}
        Products.append(my_dict)

def add():
    id= input("Enter id:")
    name= input("Enter name:")
    price= input("Enter price:")
    count= input("Enter count:")

    new_product : {"id":id , "name":name, "price":price, "count":count}
    Products.append(new_product)

def write_to_database():
    pass

def delete():
    old_product = int(input(print("Please enter id:")))
    Products . remove (old_product)
    print("The product was deleted successfully!")

def edit():
    old_product= int(input(print("Please enter id:")))

    def menu():
        print("1-Name")
        print("2-Price")
        print("3-Count")
    menu()

    choice2 = int(input("Enter your choice:"))

    def change_name():
        new_name = input("Type the new name:")
        Products[choice2]= new_name
        print("The name was changed successfully!")

    def change_price():
        new_price = int(input("Type the new price:"))
        Products[choice2]= new_price
        print("The price was changed successfully!")

    def change_count():
        new_count = int(input("Type the new count:"))
        Products[choice2]= new_count
        print("The count was changed successfully!")

    if choice2 == 1:
        change_name()

    if choice2 == 2:
        change_price()

    if choice2 == 3:
        change_count()

def search():
    user_choice = input ("Enter your keyword:")
    for product in Products:
        if product['id' == user_choice] or product['name' == user_choice]:
            print(product)
            break
    else:
        print("Not found!")

def show_list():
    print("id \t name \t name \t price \t count")
    for product in Products:
        print(product["id"], "\t", product["name"], "\t", product["price"], "\t", product["count"])

def buy():
    List = []
    choice2 = int(input("Enter your choice:"))
    if Products[choice2]==0:
        print("The product doesn't exist!")
    else:
        amount = int(input("How many of it do you want?"))
        if Products[choice2]<amount:
            print("The count of the good you have chosen is not enough!")
        else:
            List. append(choice2,amount)
        choice3 = input("Press 1 to continue your shop, Press 2 to see your check:")
        if choice3 == 1:
            buy()
        else:
            print(choice2)



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