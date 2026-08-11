# passoword system 
users = {}

def create_account():
    username=input("create a username : ")
    if username in users :
        print("username already exists.")
        return 
    password =input("create a password : ")

    if len(password) < 6:
        print("password must be at least 6 characters.")
        return 
    users[username] = password
    print("account has been successfully created !!")

def sign_in():
    username = input("username : ")
    password = input("passsword :")
    if username in users and users[username] == password :
        print(f" welcome {username}")
    else :
        print("invalid username or incorrcet password")

def menu():
    while True :
        print("1. create an account")
        print("2. sign in")
        print("3. Exit")

        choice=input("pls choose an option : ")
        if choice =="1" :
            create_account()
        elif choice =="2":
            sign_in()
        elif choice =="3":
            print("GOOD BYE !!!")
            break 
        else :
            print("invalid option")
menu()