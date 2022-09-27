admin = ["Ahmed", "khaled", "Dan", "Amin", "Mosaad"]

name = input("enter your name: ").strip().capitalize()

def put():
    new_name = input("Update Your name. Enter Your new name:").strip().capitalize()
    if new_name in admin:
        print(f"{new_name} already exists ")
    else:
        admin[admin.index(name)] = new_name
        print("Updated ==> ", admin)

def add():
    your_name = input("Enter your name: ").strip().capitalize()
    if your_name in admin:
        print(f"{your_name} already exists ")
    else:
        admin.append(your_name)
        print("Updated ==> ", admin)
        
def delete():
    admin.remove(admin[admin.index(name)])
    print("Updated ==>", admin)
       
if name in admin:
    print(f"welcome {name}")
    print(admin)
    option = int(input("Enter your option: 1- update  2- add new admin 3- delete admin: "))
    if option == 1:
        put()
    elif option == 2:
        add()
    elif option == 3:
        delete()
    else:
        print("Sorry Wrong choose")
else:
    print("Sorry this name is not an admin")