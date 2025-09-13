'''You are tasked with designing a simple system for managing hourly
employees in a company. The program uses two classes: Employee and
HourlyEmployee. The base class Employee stores general information about
employees. It includes the following attributes and methods:
▪ name: The employee's name.
▪ emp_id: The employee's unique ID.
▪ net_pay: The employee's calculated net pay.
▪ A constructor to initialise name, emp_id, and net_pay.
▪ Getter methods (using decorator) for name, emp_id, and net_pay.
▪ Setter methods (using decorator) for name, emp_id, and net_pay.
▪ A method print_salary_slip to display the employee's name, ID & net pay.
The derived class HourlyEmployee extends the Employee class and adds
specific details about hourly workers. It includes the following additional
attributes and methods:
▪ wage_rate: The hourly wage rate of the employee.
▪ num_hours: The number of hours worked by the employee.
▪ A constructor to initialise all attributes, including inherited ones.
▪ Getter methods (using decorator) for wage_rate and num_hours.
▪ Setter methods (using decorator) for`wage_rate and num_hours.
▪ An overridden print_salary_slip method to display the employee's
details, including wage rate and hours worked.
a. Implementthe Employee and HourlyEmployee classes, ensuring that all
specified attributes and methods are included.
b. Write instructions to input data for n hourly employees. Calculate the net
pay and store all the data in a list.
c. Write instructions to search and display the ID and net pay of all hourly
employees who earn more than Rs 20000.'''

class Employee:
    def __init__(self,name,emp_id,net_pay):
        self._name = name
        self._emp_id = emp_id
        self._net_pay = net_pay
    
    @property 
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        self._name = value

    @property 
    def emp_id(self):
        return self._emp_id
        
    @emp_id.setter
    def emp_id(self, value):
        self._emp_id = value

    @property 
    def net_pay(self):
        return self._net_pay
        
    @net_pay.setter
    def net_pay(self, value):
        self._net_pay = value
        
    def print_salary_slip(self):
        return(f"The salary of {self._name} with employee ID {self._emp_id} is {self._net_pay}")


class HourlyEmployee(Employee):
    def __inti__(self,wage_rate,num_hours):
        self._wage_rate = wage_rate
        self._num_hours = num_hours
    
    @property 
    def wage_rate(self):
        return self._wage_rate
        
    @wage_rate.setter
    def wage_rate(self, value):
        self._wage_rate = value
    
    @property 
    def num_hours(self):
        return self._num_hours
        
    @num_hours.setter
    def num_hours(self, value):
        self._num_hours = value
        

def main():
    n=int(input("Enter the number of employees you will add to the list: "))
    print("Noted, you can start!")
    for i in range(n):
        HourlyEmployee_checker=str(input("Is this an hourly employee(Y/N): "))
        HourlyEmployee_checker.upper()
        if HourlyEmployee_checker=="N":
            
        