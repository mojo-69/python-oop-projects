class EmployeeManagement:
    def __init__(self):
        self.emp_id=int(input("enter Emp id"))
        self.name=input("enter emp name")
        self.department=input("enter emp department")
        self.salary=int(input("enter emp salary"))
    
    def details(self):
        print(f"\n employee id is:  {self.emp_id}")
        print(f"\nemployee name is : {self.name}")
        print(f"\nemployee department is:  {self.department}")
        print(f"\nemployee salary is : {self.salary}")
    
    def annual_salary(self):
        self.anu_sal=self.salary*12
        print(f"annual salary of employee is {self.anu_sal}")
    def salary_status(self):
        if self.salary>50000:
            print(f"{self.name} has a high salary")
        elif self.salary>30000:
            print(f"{self.name} has a medium salary")
        else:
            print(f"{self.name} has a low salary")

emp1=EmployeeManagementnagement()
emp1.details()
emp1.annual_salary()
emp1.salary_status()
