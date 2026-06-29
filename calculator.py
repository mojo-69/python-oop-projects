class calculator():
    def __init__(self):
        self.value1=int(input("enter value 1"))
        self.value2=int(input("enter value 2"))
    def calculation(self):
    self.choice=input("choice")
     if self.choice=="add":
        print(self.value1+self.value2)
     elif self.choice=="sub":
        print(self.value1-self.value2)
     elif self.choice=="mul":
        print(self.value1*self.value2)
     elif self.choice=="div":
        print(self.value1/self.value2)
     else:
        print("bewloff ho kya")
   
        

a=calculator()
a.calculation()
