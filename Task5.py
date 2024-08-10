#Contact Book

contact={}

def display_contact():
  print("Name\t\tContact Number")
  for key in contact:
    print("{}\t\t{}".format(key,contact.get(key)))
while True:
  choice=int(input("1.Add contact\n2.Search contact\n3.Display contact\n4.Update contact\n5.Delete contact\n6.Exit\nEnter your choice:"))

  if choice == 1:
      name= input("Enter name:")
      phone= int(input("Enter phone number:"))
      contact[name]=phone
  elif choice == 2:
      search_name= input("Enter name to search:")
      if search_name in contact:
          print(search_name,"'s contact number is",contact[search_name])
      else:
          print("Contact not found")
  elif choice == 3:
      if not contact:
          print("Contact book is empty")
      else:
          display_contact()
  elif choice == 4:
      edit_contact= input("Enter name to update:")
      if edit_contact in contact:
        phone= int(input("Enter new phone number:"))
        contact[edit_contact]=phone
        print("contact updated")
        display_contact()
      else:
        print("Contact not found")
  elif choice == 5:
      delete_contact= input("Enter name to delete:")
      if delete_contact in contact:
        confirm= input("Are you sure you want to delete this contact? (y/n):")
        if confirm == 'y':
          del contact[delete_contact]
          print("Contact deleted")
          display_contact()
        else:
           print("Contact not found")
  else:
    break

