import json

class bookmyshow:
    def __init__(self):
        self.rows = 10
        self.col = 8
        self.total = self.rows * self.col
        self.price = 10
        try:
            with open("user_data.json","a+") as file:
                self.user_data = json.load(file)
                print(self.user_data)
        except:
            self.user_data = {}

    def display_seats(self):

        for i in range(self.rows+1):
            for j in range(self.col+1):
                if i==0:
                    if j==0:
                        print(" ",end = " ")
                    else:
                        print(j,end = " ")
                else:
                    if j==0:
                        print(i, end = " ")
                    else:
                        seat = str(i) + str(j)
                        if seat in self.user_data.keys():
                            print("B", end = " ")
                        else:
                            print("S", end = " ")
            print()

    def book_ticket(self,name,gender,age,phone):
        user = {}
        row = input("\n------------>> Enter the row number")
        col = input("\n---------->>Enter the seat in selected row")
        seat_no = row+col
        if self.is_available(row,col):
            if self.total>60:
                if int(row) > self.rows//2:
                    self.price = 8
                else:
                    self.price = 10
            else:
                self.price = 10
            print("Price of this seat is : ",self.price)
            print("Do you wish to continue")
            cont = input("Enter Y to continue and N to exit : ")
            if cont.lower() == 'y' : 
                user['Name'] = name
                user['Gender'] = gender
                user['Age'] = age
                user['Phone_number'] = phone
                user['Price'] = self.price
                self.user_data[seat_no] = user
                with open("user_data.json","w") as file:
                    json.dump(self.user_data, file)
                    print("-----------------------Booked successfully-------------------------")

        else:
            print("-----------------Seat not available----------------------------")

    def is_available(self,row,col):
        seat = row+col
        if seat in self.user_data.keys():
            return False
        else:
            return True
        
    def statistics(self):
        purchased_tickets = len(self.user_data.keys())
        percentage = (purchased_tickets/self.total)*100
        current_income = 0
        for k,v in self.user_data.items():
            current_income += v['Price']

        if self.total>60:
            half = self.rows//2
            total1 = (half*self.col) * 10
            total2 = (self.rows - half) *self.col * 8
            total_income = total1 + total2
        else:
            total_income = 10 * self.total

        stats = f"Number of purchased tickets : {purchased_tickets}\n Percentage of Tickets purchased : {percentage}\n Current Income : {current_income}\n Total Income : {total_income}"
        print(stats)

    def show_booked_tickets(self):
        for k,v in self.user_data.items():
            print("Seat no : ",k, end = "---> ")
            print("user_info :",v)
