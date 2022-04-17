import os

names = []

def newContact(name, lastname, tel, email):
    names.append("%s_%s" % (name, lastname))
    file = open("%s_%s.txt" % (name, lastname), 'w')
    file.write("Name: %s %s\n" % (name, lastname))
    file.write("Telephone: %s\n" % tel)
    file.write("Email: %s\n" % email)
    file.close()
    return "Nice! Contact created, for see your data type 2"

def find(name, lastname):
    completeName = "%s_%s" % (name, lastname)
    if completeName in names:
        file = open("%s.txt" % completeName, 'r')
        for data in file.readlines():
            print(data)
        file.close()
        return True
    else:
        return "Contact not found ):"

def update(name, lastname, tel, email):
    completeName = "%s_%s" % (name, lastname)
    if completeName in names:
        file = open("%s.txt" % completeName, 'w')
        file.write("Name: %s %s\n" % (name, lastname))
        file.write("Telephone: %s\n" % tel)
        file.write("Email: %s\n" % email)
        file.close()
        return "Contact was updated!"
    else:
        return "Contact not found ):"

def delete(name, lastname):
    os.remove("%s_%s.txt" % (name, lastname))
    return "Contact was removed!"

while True:
    option = int(input("1 - New contact\n2 - Find (by name)\n3 - Update contact\n4 - Delete contact\n0 - exit\n"))

    if option == 1:
        print("Let's create your contact: ")
        name = input("Name: ").lower()
        lastname = input("Last Name: ").lower()
        tel = input("Phone Number: ")
        email = input("E-mail: ").lower()
        message = newContact(name, lastname, tel, email)
        print(message)

    elif option == 2:
        print("Find contact by name: ")
        name = input("Name: ").lower()
        lastname = input("Last Name: ").lower()
        result = find(name, lastname)
        if result != True:
            print(result)

    elif option == 3:
        exist = find(name, lastname)
        if (exist):
            print("Let's update your contact: ")
            name = input("Name: ").lower()
            lastname = input("Last Name: ").lower()
            tel = input("Phone Number: ")
            email = input("E-mail: ").lower()
            message = update(name, lastname, tel, email)
            print(message)

    elif option == 4:
        print("Remove a contact: ")
        name = input("Name: ").lower()
        lastname = input("Last Name: ").lower()
        message = delete(name, lastname)
        print(message)

    elif option == 0:
        break