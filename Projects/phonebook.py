class PhoneBook:
    phone_directory=[]
    def __init__(self,name,phone_number):
        self.name=name
        self.phone=phone_number
        PhoneBook.phone_directory.append(self)

    def show_contact(self):
        print(f"Name:{self.name}\nContact Number:{self.phone}")    
    
    @classmethod
    def show_all_contact(cls):
        if len(cls.phone_directory)==0:
            print("No contacts found")
        else:
            for contact in cls.phone_directory:
                print(contact.show_contact())
    @classmethod
    def search_contact(cls,search_name):
        for contact in cls.phone_directory:
            if contact.name==search_name:
                return contact.phone
        return f"No contact found for {search_name}"    
    
    @staticmethod
    def vaildate_number(number):
        if len(number)>=8 and number.isdigit():
            return True
        else:
            return False
        
n_contact=int(input("how many contacts you want to add?:"))
for i in range(n_contact):
    name=input("Enter your name:")
    phone_number=(input("Enter your number:"))
    if PhoneBook.vaildate_number(phone_number):
        PhoneBook(name,phone_number)
PhoneBook.show_all_contact()