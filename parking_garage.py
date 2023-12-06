class Parking_garage:
    '''
    Parking_garage has the following attributes:
    ticketCount expects an int (default 5)
    spaceCount expects an int (default 56)'''
    tickets = []
    parkingSpaces = []
    currentTicket = {}

    def __init__(self,ticketCount = 5,spaceCount = 5):
        self.ticketCount = ticketCount
        self.spaceCount = spaceCount

    def takeTicket(self):
        if self.spaceCount > 0:
            self.ticketCount -= 1
            self.spaceCount -= 1
        else:
            print("We're sorry, but the garage is currently full.\nPlease drive forward and carefully perform a U-turn to exit the garage.")

    def payForParking(self):
        self.paid = int(input('BEEP BOOP... reading credit card. Please enter the payment amount: '))
        if self.paid > 0:
            Parking_garage.currentTicket['paid'] = True
            print('Your payment has been processed. You have 15 minutes to leave the garage.')
        else:
            print("That didn't work. Your credit card has not been charged.\nPlease try again.\n")
            Parking_garage.payForParking(self)

    def leaveGarage(self):
        if Parking_garage.currentTicket['paid'] == True:
            print("Thank you, have a nice day")
            self.ticketCount += 1
            self.spaceCount += 1
        else:
            self.temp = input("Your ticket has not yet been paid. Please swipe a valid credit card, then press enter.")
            Parking_garage.payForParking(self)


joeIsParking = Parking_garage()
joeIsParking.takeTicket()
joeIsParking.takeTicket()
joeIsParking.takeTicket()
joeIsParking.payForParking()
joeIsParking.leaveGarage()
print(joeIsParking.currentTicket)
print(f'Ticket Count: {str(joeIsParking.ticketCount)}')
print(f'Space Count: {str(joeIsParking.spaceCount)}')
        
    
