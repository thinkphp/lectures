---
layout: post
disqus: n
title: Class Inheritance
---

1. Introduction

   Inheritance is a core feature of Object-Oriented Programming. It allows one class to inherit data or behaviour from another class and is one of the key ways in which reuse is enabled within classes. This chapter introduces inheritance between classes in Python.

2. What is Inheritance?

   Inheritance allows features defined in one class to be inherited and reused in the definition of another class. For example, a Person class might have the attributes name and age. It might also have behaviour associated with a Person such as birthday().

   We might then decide that we want to have another class Employee
   and that employees also have a name and an age and will have birthday. However, in addition an Employee may have an employee
   ID attribute and a calculate_pay() behaviour.

   At this point we could duplicate the definition of the name and age attributes and the birthday() behaviour in the class Employee
   (for example by cutting and pasting the code between the two classes).

   However, this is not only inefficient; it may also cause problems in the futures. For example we may realize that there is a problem or bug in the implementation of birthday() and may correct it in the class Person; however, we may forget to apply the same fix to the class Employee.

   In general, in software design and development it is considered best practice to define something once and to reuse that something
   when required.

   In an object-oriented system we can achive that reuse of data or
   behaviour via inheritance. That is one class (in the case the Employee class) can inherit features from another class (in this case Person). This is shown pictorially below:

   Person

   name
   age
   birthday()


   Employee
   id
   calculate_pay()

   In this diagram the Employee class is shown as inheriting from then Person class. This means that the Employee class obtains all the data and behaviour of the Person class. It is therefore as though the Employee class has defined three attributes name, age and id and two methods birthday() and calculate_pay().

   A class that is defined as extending a parent class has the
   following syntax:

   ```python
   class SubClassName(BaseClassName):
         class-body
   ```

   Note that the parent class is specified by providing the name of the class in round brackets after the name of the new child class.

   We can define the class Person as before:

   ```python
   class Person:
         def __init__(self, name, age):
             self.name = name
             self.age = age
         def birthday(self):
             print("Happy birthday you were!", self.age)
             self.age += 1
             print("You are now", self.age)             
   ```

   We could now define the class Employee as being a class whose
   definition builds on (or inherits from) the class Person:

   ```python
        class Employee(Person):
           def __init__(self, name, age, id):
             super().__init__(name, age)
             self.id = id
        clss calculate_pay(self, hours_worked):
             rate_of_pay = 7.50
             if self.age >= 21:
               rate_of_pay ++ 2.50
             return hours_worked * rate_of_pay            
   ```

   Here we do several things:

   1. The class is called Employee but it extends the class Person.
   This is indicated by including the name of the class being inherits
   in parentheses after the name of the class being defined (e.g. Employee(Person)) in class declaration.
   2. Inside the __init__ method we reference the __init__() method defined in the class Person and used to initialise instances of that class (via the super().__init__() reference). This allows whatever initialisation is required for Person to happen. This is called from within the Employee class's __init__() which then allows any initialisation required by the Employee to occur. Note
   that the call to the super().__init__() initialiser can come everywhere within the Employee.__init__() method; but by convention it comes first to ensure that whatever the class Person does during initialisation does not over write what happens in the Employee class.
   3. All instances of the class Person have a name, and age and have the bevaviour birthday().
   4. All instances of the class Employee have a name, and age and an ID and have the behaviour birthday() and calculate_pay(house_worked).
   5. The method calculate_pay() defined in the Employee class can access the attributes name and age just as it can access the attribute ID. In fact, it uses the employee's age to determine la rate of pay to apply.

   We can go further, and we can subclass Employee, for example with the class SalesPerson:

   ```python
   class SalesPerson(Employee):
         def __init__(self, name, age, id, region, sales):
             super().__init__(name, age, id)
             self.region = region
             self.sales = sales
         def bonus(self):
             return      self.sales * 0.5
   ```

   Now we can say that the class SalesPerson has a name, an age and an Id as well as a region and a sales total. It also has the methods birthday(), calculate_pay(hours_worked) and bonus().

   In this case the SalesPerson.__init__() method calls the Employee.__init__() method as that is the next class up hierarchy and thus we want to run that classes initialisation behaviour before we set up the SalesPerson class (which of course in turn runs the Person classes initialisation behavoir).

   We can now write code such as:

   ```python
   print('Person')
   p = Person('John', 55)
   print(p)
   print('-' * 25 )
   print('Employee')
   e = Employee('Denise', 51, 7468)
   e.birthday()
   print('e.calculate_pay(40):', e.calculate_pay(40))
   print('-' * 25 )
   print('SalesPerson')
   s = SalesPerson('Steve', 21, 1468, 'UK', 30000.0)
   s.birthday()
   print('e.calculate_pay(40):', e.calculate_pay(40))
   print('e.bonus():', s.bonus())
   ```

   with the output being:

   ```
   Person
John is 54
-------------------------
Employee
Happy birthday you were 51
You are now 52
e.calculate_pay(40): 400.0
-------------------------
SalesPerson
Happy birthday you were 21
You are now 22
s.calculate_pay(40): 400.0
s.bonus(): 15000.0
   ```
