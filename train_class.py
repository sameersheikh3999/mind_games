from re import S


class Train():
    fare=2000
    ticket=3123

    def book_ticket(self):
        print("Your ticket is booked")

    def get_status(self):
        print(f"This shows the status of the ticket no {self.ticket} ")

    def get_fare(self):
        print(f"Your fare is {self.fare}")


sameer=Train()

sameer.book_ticket()
sameer.get_status()
sameer.get_fare()

