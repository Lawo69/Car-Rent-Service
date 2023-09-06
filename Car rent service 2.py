#declaring
print('Welcome to Car Rent Service')
class Vehilist:
    def __init__(self):
        self._make = ''
        self._model = ''
        self._year = 0
        self._color = ''
        self._num = ''
        self._passenger = 0
        self._ac = ''
    def addVehicle(self):
        try:
            self._make = input('Enter vehicle Type (Car, Van, 3-Wheeler, Lorry, Truck): ')
            self._model = input('Enter vehicle model: ')
            self._year = int(input('Enter vehicle mileage: '))
            self._color = input('Enter vehicle color: ')
            self._num = input('Enter vehicle registration Number: ')
            self._passenger = int(input('Enter Passenger Count: '))
            self._ac = input('Is there AC or not?(YES or NO): ')
            
            return True
        except ValueError:
            print('Please try entering vehicle information again using only whole numbers for Vehicle number and mileage')
            return False
    def __str__(self):
        return '\t'.join(str(x) for x in [self._make, self._model, self._year, self._color, self._num, self._passenger, self._ac])

class Cab:
    def __init__(self):
        self.vehicles = []
    def addVehicle(self):
        vehicle = Vehilist()
        if vehicle.addVehicle() == True:
            self.vehicles.append(vehicle)
            print ()
            print('This vehicle has been added, Thank you')
    def viewCab(self):
        print('\t'.join(['','Type', 'Model','Year', 'Color', 'Vehicle', 'Passengers', 'Condition']))
        for idx, vehicle in enumerate(self.vehicles) :
            print(idx + 1, end='\t')
            print(vehicle)

cab = Cab()
class Data:
    def __init__(self):
        self._name = ''
        self._location = ''
        self._drop = ''
        self._sv = 0
        self._tel = 0
        
    def addCustomer(self):
        try:
            self._name = input('Enter Your Name: ')
            self._location = input('Enter Your pick up location: ')
            self._drop = input('Enter Your droping: ')
            self._sv = int(input('Enter Selected vehicle: '))
            self._tel = int(input('Enter Your Phone no: '))
            
            return True
        except ValueError:
            print('Please try entering vehicle')
            return False
    def __str__(self):
        return '\t'.join(str(x) for x in [self._name, self._location, self._drop, self._sv, self._tel])


class Pick:
    def __init__(self):
        self.customers = []
    def addCustomer(self):
        customer = Data()
        if customer.addCustomer() == True:
            self.customers.append(customer)
            print ()
            print('This vehicle has been added, Thank you')
    def viewPick(self):
        print('\t'.join(['', 'Name', 'Get-Drop', 'V.No', 'Phone No']))
        for idx, customer in enumerate(self.customers) :
            print(idx + 1, end='\t')
            print(customer)

pick = Pick()
while True:
    print('Press [1] to Add a new vehicle to the system')
    print('Press [2] to Remove a vehicle from the system')
    print('Press [3] to View Currently Available Vehicles')
    print('Press [4] to Assign a job (hire)')
    print('Press [5] to Release form assigned job (hire) after completing')
    print('Press [6] to See available vehicles in each category')
    print('Press [7] to EXIT')
    userInput=input('Please Select an option from above: ')

    #add a vehicle
    if userInput=="1": 
        cab.addVehicle()

    #delete a vehicle
    elif userInput=='2':
        if len(cab.vehicles) < 1:
            print('Sorry there are no vehicles currently in Cab Service')
            continue
        cab.viewCab()
        item = int(input('Please enter the number associated with the vehicle to be removed: '))
        if item - 1  > len(cab.vehicles):
            print('This is an invalid number')
        else:
            cab.vehicles.remove(cab.vehicles[item - 1])
            print ()
            print('This vehicle has been removed')
            
    #list all the vehicles        
    elif userInput == '3':
        if len(cab.vehicles) < 1:
            print('Sorry there are no vehicles currently in Cab Service')
            continue
        cab.viewCab()
        
    #add a Customer   
    if userInput=="4":
            pick.addCustomer()
            
    #delete a Customer
    elif userInput=='5':
        if len(pick.customers) < 1:
            print('There are no customers currently in Cab Service')
            continue
        pick.viewPick()
        item = int(input('Please enter the number associated with the customer to be removed: '))
        
        if item - 1  > len(pick.customers):
            print('This is an invalid number')
        else:
            pick.customers.remove(pick.customers[item - 1])
            print ()
            print('This customer has been removed')
            
    #exit the loop        
    elif userInput == '6':
        if len(pick.customers) < 1:
            print('No one rented a vehicle yet!')
            continue
        pick.viewPick()
        
    #exit the loop    
    elif userInput == '7':
        print('Thank You, Come Again!')
        break

#invalid user input
else:
        print('This is an invalid input. Please try again.')
