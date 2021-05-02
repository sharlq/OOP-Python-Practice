class User():
   def __init__(self,name,age,gender):
       self.name = name
       self.age = age
       self.gender = gender
    
   def show_Detailes(self):
       print("personal details")
       print("")
       print("Name ", self.name)
       print("Age " , self.age)
       print("Gender " ,self.gender)

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Accuont balance has been updated : $",self.balance)

    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient Funds ! Balance Available : $",self.balance)
        else:
            self.balance = self.balance - amount
            print("Accuont balance has been updated : $",self.balance)
    def view_balance(self):
        self.show_Detailes()
        print("Accuont balance is : $",self.balance)


jo = Bank("jo",21,"male")
jo.deposit(200)
jo.deposit(10)
jo.withdraw(5)
jo.withdraw(2000)
jo.view_balance()



