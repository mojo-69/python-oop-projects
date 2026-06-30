class student_info():
    def __init__(self):
        self.id=int(input("enter id-"))
        self.name=(input("enter name-"))
        self.age=int(input("enter age-"))
        self.course=(input("enter course-"))
    def details(self):
        print(f"id is:{self.id}")
        print(f"name is:{self.name}")
        print(f"age is:{self.age}")
        print(f"course is:{self.course}")
    def check_adult(self):
        if self.age>=18:
            print(f"{self.name} is adult")
        else:
            print(f"{self.name} is child")

s1=student_info()
s1.details()
s1.check_adult()
    
