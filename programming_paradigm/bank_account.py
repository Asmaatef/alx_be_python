class BankAccount :
     def __init__(self,initial_balance=0) :
          self._account_balance =initial_balance
     def deposite(self ,amount):
       if amount>0 :
          self._amount_balance += amount
       else :
          print("Deposit amount must be positive.")
     def withdraw(self ,amount):
         if amount > self._account_balance:
             return False
         self._account_balance -= amount
         return True

     def display_balance(self):

        print(f"Current Balance: ${self._account_balance:.2f}")