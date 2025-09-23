# class
# object
# self
# constructors
# inh
# enc
# abs
# polymorp

# Icici bank :--
# blueprint :-- iciciAccount :-- withdraw,deposit,check_bal,atm,loan,checkbook,netbanking,customer
# object creation :-- min:-- 0 , 15000,setters, getters
# savingsAccount(iciciAccount):
# super().
# personal_loan
# currentAccount (iciciAccount):
# bussinessloan()

class HDFCBankAccount:
    def __init__(self,cuName,cuPswd,cuANumber,cuFisrtAmt):
        self.name=cuName
        self.__pin=cuPswd
        self.__Bal=0
        self.__aCNumber=cuANumber
        self.__firstAmt=cuFisrtAmt
        self.__loanLimitAmt=400000
    # print(cuFisrtAmt)

    def __checkLoanAmtValidation(self,qTAmt):
        return qTAmt <= self.__loanLimitAmt

    def __validateAcNumber(self,an):
        return self.__aCNumber == an


    def __validatePin(self,pin):
        return self.__pin == pin


    def  withdraw(self,wAmt,pin):
        if self.__validatePin(pin):
            if wAmt > self.__Bal:
                print(f"insufficient funds cause you are drawing{wAmt} but main bal is {self.__Bal}")
            else:
                self.__Bal -= wAmt
                print(f"{wAmt} drawn successfullyyy.. main bal {self.__Bal}")    

        else:
            print("wring password...")  

    def deposit(self,dAmt,aNumber):
        if self.__validateAcNumber(aNumber):
            self.__Bal +=dAmt
            print(f"{self.__Bal} is main bal after deposting {dAmt}")
        else:
            print("wrong account number")    


    def check_bal(self):
        return self.__Bal

    def vamsi_Bal(self):
        if self.__firstAmt <0:
            print("muts be postive amount >0")
        else:
            self.__Bal=self.__firstAmt
            print(self.__Bal,"bal")     

    def loanRaise(self,qTAmt):
        if self.__checkLoanAmtValidation(qTAmt):
            print("loan granted")
        else:
            print("pls bid in limit amount")    


    def atmCardRaise(self):
        pass

    def netBanking(self):
        pass               

class savingsAccount(HDFCBankAccount):
    def __init__(self,name,pswd,aN,bal):
        super().__init__(name,pswd,aN,bal)
        

sAcc=savingsAccount("vamsi","vamsi@123123123","87654545663",15000)
print(sAcc.check_bal())
sAcc.vamsi_Bal()
# amount=int(input("entyer amount :-- "))
# pin=input("enter pin :--  ")
# accNUm=input("enter a/c number :--- ")
# sAcc.withdraw(amount,pin)

# sAcc.deposit(amount,accNUm)
qTAmt=int(input("enetr qAmt here :--   "))
sAcc.loanRaise(qTAmt)
