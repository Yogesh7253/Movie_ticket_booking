from functions import bookmyshow

print("Welcome to Bookmymovieticket.com")
str = """Enter 1. To show the seats\n Enter 2. To Book a ticket\n Enter 3. To Show the statistics
Enter 4. To Show Booked tickets info\n Enter 0. To exit"""
obj = bookmyshow()
choice = 1
while choice!=0:
    print(str)
    choice = int(input("Enter your Choice : "))
    if choice == 1:
        obj.display_seats()

    elif choice == 2: 
        name = input("Enter your name")
        gender = input("Enter your gender")
        age = int(input("Enter your age"))
        phone = input("Enter your mobile number")
        obj.book_ticket(name,gender,age,phone)

    elif choice == 3:
        obj.statistics()

    elif choice == 4:
        obj.show_booked_tickets()

    elif choice == 0:
        break