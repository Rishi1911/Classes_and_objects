"""1. Write a program to print the area of a rectangle by creating a class named 
'Area' having two methods. First method named as 'setDim' takes length 
and breadth of rectangle as parameters and the second method named as 
'getArea' returns the area of the rectangle. Length and breadth of 
rectangle are entered through keyboard.

2. Create a class named 'Student' with String variable 'name' and integer 
variable 'roll_no'. Assign the value of roll_no as '2' and that of name as 
"John" by creating an object of the class Student.

3. Assign and print the roll number, phone number and address of two 
students having names "Sam" and "John" respectively by creating two 
objects of class 'Student'.

4. Print the average of three numbers entered by user by creating a class 
named 'Average' having a method to calculate and print the average.

5. Write a program that would print the information (name, year of joining, 
salary, address) of three employees by creating a class named 'Employee'. 
The output should be as follows:
Name Year of joining Address
Robert 1994 64C- WallsStreat
Sam 2000 68D- WallsStreat
John 1999 26B- WallsStreat

6. Design a program in Java to calculate the tax for the people living in 
Mango city. Specify a class taxpayer whose class description is given 
below:
 Class name: TaxCalculator
Data members:
int PAN
 String name
 double taxableIncome
 double tax
Member methods: 
 inputData ()
 displayData ()
computeData ()
The tax is calculated according to the following rules:
Total Annual Taxable Income Rate of Taxation
Up to 60000 0%
Above 60000 but up to 150000 5%
Above 150000 but up to 500000 10%
Above 500000 15%"""


'''class area:
    def setdim(self):
        self.length = int(input("enter the length"))
        self.breath = int(input("enter the number"))
    def getarea(self):
        return self.length*self.breath
a = area()
a.setdim()
print(a.getarea())

class student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
    def display(self):
        print("name:",self.name)
        print("roll_no:",self.roll_no)
name  = input("enter the name")
roll_no = int(input("enter the roll no"))
s = student(name,roll_no)
s.display()

class student:
    def __init__(self,roll,phone,address):
        self.roll = roll
        self.phone = phone
        self.address = address
    def sam(self):
        print(self.roll)
        print(self.phone)
        print(self.address)
    def john(self):
        print(self.roll)
        print(self.phone)
        print(self.address)
s = student(2,1254639870,"dipka")
s.sam()
s = student(3,5424136987,"korba")
s.john()

class average:
    def calculate(self):
        self.a = int(input("enter the number"))
        self.b = int(input("enter the number"))
        self.c = int(input("enter the number"))
        self.d = (self.a+self.b+self.c)/3
    def printavg(self):
        print(self.d)
a = average()
a.calculate()
a.printavg()

class employee:
    def info(self):
        self.name = input()
        self.year_joining = input()
        self.salary = input()
        self.address = input()
        print(self.name)
        print(self.year_joining)
        #print(self.salary)
        print(self.address)
e = employee()
n = int(input("enter the number of student"))
for i in range(n):
    e.info()

class taxpayer:
    def inputdata(self):
        self.pan = int(input("enter the pan number"))
        self.name = input("enter the name")
        self.taxableincome = int(input("enter taxable amount"))
    def computedata(self):
        if self.taxableincome<= 60000:
            self.tax = 0
        elif self.taxableincome>60000 and self.taxableincome<=150000:
            self.tax = 5
        elif self.taxableincome>150000 and self.taxableincome<=500000:
            self.tax = 10
        else:
            self.tax = 15
        return self.tax
    def displaydata(self):
        print(self.pan)
        print(self.name)
s1 = taxpayer()
s1.inputdata()
print(s1.computedata())
s1.displaydata()'''




        