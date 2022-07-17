from datetime import date



class Employee:
   #Employee class here
   name=""
   age=0
   salary=0
   employment_year=0
   
   def __init__(self,name,age,salary,employment_year) :
#     
    
    
        
        self.name=name
        self.age=age
        self.salary=salary
        self.employment_year=employment_year
   def get_working_years(self):
        
                return date.today().year - self.employment_year
        
      
   def __str__(self):
         return f'name: {self.name} ,age: {str(self.age)} ,salary: {str(self.salary)}, working_years: {str(self.get_working_years())} '.format(self=self)

   
list_Employee=[]

#   
   
        
class Manager(Employee):
    #Manager class here
    get_working_years=0
    get_bonu=0
    def __init__(self,name,age,salary,employment_year,bonus_percentage) :
#      super().__init__(self,name, age, salary, employment_year)
        self.name=name
        self.age=age
        self.salary=salary
        self.employment_year=employment_year
        self.bonus_percentage=bonus_percentage
     
    def get_bonus(self):
        return self.bonus_percentage * self.salary

    def get_working_years(self):
        
        return date.today().year - self.employment_year


    def __str__(self):
          return f'Name: {self.name} ,Age: {str(self.age)} ,Salary: {str(self.salary)}, Working_years: {str(self.get_working_years())}, Bounes:{str(self.get_bonus())}'.format(self=self)
       
       
       
list_Manager=[]
        
def main():
	# main code here
    print("Welcome to HR Pro 2019")
    print("Options:")
    print('1. Show Employees\n2. Show Managers\n3. Add An Employee\n4. Add A Manager\n5. Exit')
    user_input=(int(input("What would you like to do?")))
    if user_input == 1:
            print ("Employees")
            print (list_Employee)
    elif user_input == 2:
            print ("Managers")
            print (list_Manager)
    elif user_input == 3:
            add_employee= Employee(input("Name:"),int(input("Age:")),int(input("Salary:")),int(input("Employement Year:")))
            list_Employee.append(add_employee)
            print("Employee added succesfully")
        #     print (list_Employee[0])

       
    elif user_input == 4:
            add_manger= Manager(input("Name:"),int(input("Age:")),int(input("Salary:")),int(input("Employement Year:")),float(input("Bonus Percentage:")))
            list_Manager.append(add_manger)
            
            print("Manger added succesfully")
        #     print (list_Manager[0])
            
    elif user_input == 5:
            print("bye")
            exit()
    else:
        print("Error")
if __name__ == '__main__':
	main()
