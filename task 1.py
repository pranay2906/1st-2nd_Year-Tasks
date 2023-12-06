import hashlib
import csv
def register():
    username=input("Enter the username:")
    create_password=input("enter password")
    confirm_password=input("re enter password")
    if create_password==confirm_password:
        hashed_username=hash(username)
        hashed_password=hash(confirm_password)
        with open("list of users.txt","a") as f:
            f.write(f"{hashed_username},{hashed_password}" + "\n")
        print("registered sucessfully")
    else:
        print("create_password and confirm_password must be same")

def login():
    username=input("Enter the username:")
    password=input("enter password")
    hashed_username=hash(username)
    hashed_password=hash(password)
    with open("list of users.txt","r") as f:
        for line in f:
            hashed_username,hashed_password=line.split(",")
            if hashed_username==hashed_username and hashed_password==hashed_password:
                print("login sucessfull")
            else:
                print("unsucessfull")

def main():
    choice = input("Do you want to register (r) or login (l)? ")
    if choice == "r":
        register()
    elif choice == "l":
        login()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()