from random import randint


class Train():

    def __init__(self, trainNo):
        self.trainNo=trainNo
    
    def book(self, fro, to):
        print(f"The ticket is booked in train No {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train No {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(1999,2026)}")


t=Train(1299)
t.book("Lahore", "Islamabad")
t.getStatus()
t.getFare("Lahore", "Islamabad")