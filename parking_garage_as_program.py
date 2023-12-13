class parkingGarage:
    '''
    parkingGarage has the following attributes:
    ticketCount expects an int (default 5)
    spaceCount expects an int (default 56)'''
    tickets = []
    parkingSpaces = []
    currentTicket = {}

    def __init__(self,ticketCount = 5,spaceCount = 5):
        self.ticketCount = ticketCount
        self.spaceCount = spaceCount
        parkingGarage.takeTicket(self)

    def takeTicket(self):
        ticket = input("Welcome to the garage. Will you be parking with us today? ").lower()
        if ticket == 'y' or ticket == 'yes':
            if self.spaceCount > 0:
                self.ticketCount -= 1
                self.spaceCount -= 1
                parkingGarage.currentTicket['paid'] = 'no'
                print("\nPlease take your ticket and find a parking space.\nGo to one of our pay stations before leaving.")
                parkingGarage.payForParking(self)
            else:
                print("We're sorry, but the garage is currently full.\nPlease drive forward and carefully perform a U-turn to exit the garage.")
        else:
            print("Please drive forward and carefully perform a U-turn to exit the garage.")

    def payForParking(self):
        print("\n(  ...at the pay station...  )\n")
        self.ready = input("Are you ready to check out? You will have 15 minutes to remove your vehicle from the garage: ").lower()
        if self.ready == 'y' or self.ready =='yes':
            self.paid = int(input('BEEP BOOP... reading credit card. Please enter the payment amount: '))
            if self.paid > 0:
                parkingGarage.currentTicket['paid'] = 'yes'
                print('Your payment has been processed. You have 15 minutes to leave the garage.')
                parkingGarage.leaveGarage(self)
            else:
                print("That didn't work. Your credit card has not been charged.\nPlease try again.\n")
                parkingGarage.payForParking(self)
        else:
            self.rebel = input('Will you be leaving without paying? ').lower()
            if self.rebel == 'y' or self.rebel == 'yes':
                parkingGarage.leaveGarage(self)
            else:
                parkingGarage.payForParking(self)

    def leaveGarage(self):
        if parkingGarage.currentTicket['paid'] == 'yes':
            print("Thank you and have a nice day")
            self.ticketCount += 1
            self.spaceCount += 1
        else:
            self.temp = input("Your ticket has not yet been paid. Please swipe a valid credit card, then press enter.")
            parkingGarage.payForParking(self)

parkingGarage()
    
