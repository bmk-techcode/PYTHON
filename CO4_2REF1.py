class bank:
    __acname=""
    __acno = ""
    __actype = ""
    __acbal = 0
    
    def __init__(self,na,no,t,b):
        self.__acame = na
        self.__acno = no
        self.__acype = t
        self.__acbal= b
        
    def deposite(self,adep):
        print("Initial balance is  : ",self.__acbal)
        print("Deposite is  : ",adep)
        self.__acbal += adep
        print("Current balance is  : ",self.__acbal)
        
    def withdraw(self):
        print("Current balance is  : ",self.__acbal)
        self.amount = int(input("How much amount need to withdraw : "))
        if self.amount > self.__acbal:
            print("You don't have enough balance to withdraw !!")
            print("Current balance is  : ",self.__acbal)
        else:
            print(self.amount," is withrawed .")
            self.__acbal -= self.amount
            print("Current balance is  : ",self.__acbal)
            
    def acc_info(self):
         print("\n\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n\n")
         print("Account holder name  :  ",self.__acame)
         print("Account number         :  ",self.__acno)
         print("Account type              :  ",self.__acype)
         print("Account Balance is      :  ",self.__acbal)
         print("\n\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n\n")
         
        
def main():
    
    name  = input("Enter Account holder name : ")
    no      = input("Enter Account number        : ")
    atype  = input("Enter Account type             : ")
    bal      = int(input("Enter Account initial balance : "))
    holder = bank(name,no,atype,bal)

    while(True):
        print("\n\n.........................................................\n\n")
        opt = int(input("1)Deposite \n2)Withdraw \n3)Account info \n0)Exit\nChoose your option :: "))
        print("\n\n.........................................................\n\n")
        if opt == 1:
            amount = int(input("Deposite amount : "))
            holder.deposite(amount)
        elif opt == 2:
            holder.withdraw()
        elif opt == 3:
            holder.acc_info()
        elif opt == 0:
            break
        else:
            print("Invalid Option !")
            
if __name__ == "__main__":
    while(True):
        main()
