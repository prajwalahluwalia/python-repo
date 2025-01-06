class Bank:
    def __init__(self, id, name, balance):
        self.__id = id
        self.name = name
        self.__balance = balance
        
    def getId(self):
        return f"Id of the user is {self.__id}"
    
    def __getBalance(self):
        return f"Cuurent balance is {self.__balance}"
    
    def makeTransaction(self, amount, type=""):
        if type not in ["deposit", "withdraw"]:
            return f"Please enter valid transaction type."
        
        if amount<0:        
            return f"Please select valid amount."
        
        if type == 'deposit':
            return self.__updateBalance(amount)
        
        elif type == "withdraw":
            return self.__updateBalance(-amount)
                
    def __updateBalance(self, amount):
        self.__balance+=amount
        return f"Update balance is {self.__balance}"
    
    
user = Bank(1,"Prajwal", 20000)
print(user.makeTransaction(-12))    #Please enter valid transaction type.
print(user.makeTransaction(-12,"deposit"))      #Please select valid amount.
print(user.makeTransaction(12000,"deposit"))    #Update balance is 32000
print(user.makeTransaction(2000, "withdraw"))   #Update balance is 30000

print(user.__getBalance())      #Throws error