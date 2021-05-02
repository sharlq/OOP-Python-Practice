class user():
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

johan = user('johan',21,'mal')
johan.show_Detailes()