contact={}
def display_contact():
   print("Name \t\t Contact Number")
   for key in contact :
       print("{}\t\t{}".format(key,contact.get(key)))
while True:
    choice=int(input("1. Add contact \n 2.search contact\n 3.display contact \n 4.edit contact \n 5.delete contact \n  Enter your choice:"))
    
    if choice ==1:
        name=input("enter the new contact Name:")
        phone=input("enter the new mobile Number:")
        contact[name]=phone
    elif choice==2:
        search_name=input("search the Name:")
        if search_name in contact:
            print(search_name,"'s contact number is",contact[search_name])
        else:
            print("no contact found:")
    elif choice==3:
        if not contact:
            print("empty contact book:")
        else:
            display_contact()    
    elif choice==4:
        edit_contact=input("enter the contact name here: ")
        if edit_contact in contact:
            phone= input("entert the mobile number here:")
            contact[edit_contact]=phone
            print("contact updated successfully")
            display_contact()
        else:
            print("name is not found:")
                
    elif choice==5:
        del_contact= input("enter the contact name you want to delete:")
        if del_contact in contact:
             confirm=input("do you want to delete contact y/n?:")
             if confirm=='y' or confirm=='Y':
                contact.pop(del_contact)
             display_contact() 
        else:
             
            print("name not found:")
    # else:
    #     break  
        new_runmore = input("Do you want to Exit? (yes/no): ")
        if new_runmore.lower() != 'no':
          break           