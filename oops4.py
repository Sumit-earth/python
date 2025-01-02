class bankaccount:
    def __init__(self,name,initial_balance):
        
        self.name=name
        self.__balance=initial_balance

    def deposit(self,amount):
        self.__balance+=amount



    def withdraw(self,withdraw):
        if withdraw <=self.__balance:
            self.__balance-=withdraw

            print(f"withdwan Amount {withdraw}, Remaining Balance:{self.__balance}")

        else:
            print("Insufficient Balance")


    def get_balance(self):
        return self.__balance
    



account=bankaccount("John doe",1200)
account.deposit(300)
account.withdraw(600)
print(account.get_balance())