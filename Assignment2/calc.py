class Calculator :
    
    def __init__(self) -> None:
        self.num1 = 0
        self.num2 = 0
        
    # Addition function
    def add(self):
        return self.__num1 + self.__num2
    
    # Subtraction function
    def subtract(self):
        return self.__num1 - self.__num2
    
    # Multiplication function
    def multiply(self):
        return self.__num1 * self.__num2
    
    # Division function
    def divide(self):
        if self.__num2 == 0:
            raise ValueError("Division by zero is not valid.")
        return self.__num1 / self.__num2
    
    # Floor division function
    def floor_division(self):
        if self.__num2 == 0:
            raise ValueError("Division by zero is not valid.")
        return self.__num1 // self.__num2
    
    # Exponential function
    def exponential(self):
        return self.__num1 ** self.__num2
    
    # Modulus function
    def modulus(self):
        if self.__num2 == 0:
            raise ValueError("Modulus by zero is not valid.")
        return self.__num1 % self.__num2
    
    
    def set_numbers(self):
        try:
            self.__num1 = float(input("Enter first number for task : "))
            self.__num2 = float(input("Enter second number for task : "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return False
                
        return True
    
    def get_num1(self):
        return self.__num1
    
    def get_num2(self):
        return self.__num2

# working    
obj = Calculator()
print("Welcome to the Simple Calculator Application :")


switch = '0'

while(switch!='8') :
    print()
    print("1 -> Addition")
    print("2 -> Subtraction")
    print("3 -> Multiplication")
    print("4 -> Division")
    print("5 -> Floor_division")
    print("6 -> Exponenetial")
    print("7 -> Modulus")
    print("8 -> Exiting the Application")
    print()
    
    
    switch = input("Pick the number according to the task you want to perform : ")
    print()
    
    
    if switch == '1':
        #For taking two numbers
        if not obj.set_numbers() :
            continue
        print()
        print(f"Result : {obj.get_num1()} + {obj.get_num2()} = {obj.add()}")
    elif switch == '2':
        if not obj.set_numbers() :
            continue
        print()
        print(f"Result : {obj.get_num1()} - {obj.get_num2()} = {obj.subtract()}")
    elif switch == '3':
        if not obj.set_numbers() :
            continue
        print()
        print(f"Result : {obj.get_num1()} * {obj.get_num2()} = {obj.multiply()}")
    elif switch == '4':
        if not obj.set_numbers() :
            continue
        print()
        print(f"Result : {obj.get_num1()} / {obj.get_num2()} = {obj.divide()}")
    elif switch == '5':
        if not obj.set_numbers() :
            continue
        print()
        print(f"Result : {obj.get_num1()} // {obj.get_num2()} = {obj.floor_division()}")
    elif switch == '6':
        if not obj.set_numbers() :
            continue
        print()
        print(f"Result : {obj.get_num1()} ** {obj.get_num2()} = {obj.exponential()}")
        
    elif switch == '7':
        if not obj.set_numbers() :
            continue
        print()
        print(f"Result : {obj.get_num1()} % {obj.get_num2()} = {obj.modulus()}")
    
    elif switch == '8':
        print()
        print("Exiting ...")
    
    else :
        print("Select among the above mentioned tasks only.")


    


    
