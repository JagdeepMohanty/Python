#Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.


class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            print("Ticket booked successfully")
        else:
            print("Sorry, train is full")

    def get_status(self):
        print(f"Seats available: {self.seats}")

    def get_fare(self):
        print(f"Fare: ₹{self.fare}")


t = Train("Rajdhani Express", 2, 1500)
t.get_status()
t.book_ticket()
t.get_status()
t.get_fare()
