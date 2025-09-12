
class InsufficeintAmountException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class Account:

    balance=0

    def get_balance(self):
        print("current balaance is : ",self.balance)
    
    def deposite(self,amt):
        self.balance+=amt

    def withdrow(self,amt):
        if amt>self.balance:
            raise InsufficeintAmountException("you need more in your account : ",amt-self.balance)
        else:
            self.balance-=amt



ac = Account()
ac.get_balance()
ac.deposite(5000)
ac.deposite(5000)
ac.get_balance()

try :
    ac.withdrow(15000)
except Exception as e:
    print(e)



ac.get_balance()
