class Voiture:
    wheels = 4 
    energy = 'oil'
    nb_door = 4
    nb_place = 4

    def __init__(self, brand:str, model:str, distance:float=0, control:bool=True):
        self.brand = brand
        self.model = model
        self.distance = distance
        self.control = control


    def passenger(self, driver, copilot=None, passenger_1=None, passenger_2=None):
        self.driver = driver
        self.copilot = copilot
        self.passenger1 = passenger_1
        self.passenger2 = passenger_2


    def input_code_pin_user(self, password:str='0000') -> bool:
        input_user = input('Please enter your password')

        tentative = 3

        while input_user != password and tentative > 0:

            if input_user == 'exit':
                return False

            tentative -=1
            print('Tentatives restantes : {}'.format(tentative))

            try:
                int(input_user)
                print('Wrong Password')
                input_user = input('Please enter your password')
                
            except:
                print('Wrong input, please entre numbers')
                input_user = input('Please enter your password')

        if input_user == password:
            print('Successful connection')
            return True
        else:
            print('Connexion denied')
            return False


    def driving(self, depart:str, destination:str, miles:float): 
        try:
            self.driver
            if self.input_code_pin_user():            
                self.distance += miles
                print("I'm driving !", True)

                if self.distance > 5000:
                    self.control = False

        except:
            print('There is no driver')


def input_code_pin_user(password:str='0000') -> bool:
    input_user = input('Please enter your password')

    tentative = 3

    while input_user != password and tentative > 0:

        if input_user == 'exit':
            return False

        tentative -=1
        print('Tentatives restantes : {}'.format(tentative))

        try:
            int(input_user)
            print('Wrong Password')
            input_user = input('Please enter your password')
            
        except:
            print('Wrong input, please entre numbers')
            input_user = input('Please enter your password')

    if input_user == password:
        print('Successful connection')
        return True
    else:
        print('Connexion denied')
        return False
