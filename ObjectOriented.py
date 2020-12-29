class Dog:
    #method is a function in a class 
    def __init__(self,name,age):
        self.name =name 
        self.age =age 
       
    def meow(self,x):
        return x+1
    def get_nme(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age =age
    def bark(self):
        print("bark")
d = Dog("Vinny",22)
d2 =Dog("Billy",45)
#print(d2.get_nme())
d2.set_age(9)
#print(d2.get_age())

##Example of a class 
class Student:
    def __init__(self,name,age,grade):
        self.name =name
        self.age =age 
        self.grade =grade 
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name,max_students):
        self.name =name 
        self.max_students = max_students
        self.students =[]
    def add_student(self,Student):
        if len(self.students) < self.max_students:
            self.students.append(Student)
            return True
        return False 
    def get_average_student(self):
        value = 0 
        for student in self.students:
            value = value + student.get_grade()
        return value / len(self.students)
        

s1 =Student("Vinny",21,65)
s2 = Student("Jane",45,78)
s3= Student("karimi",23,76)

course =Course("Science",2)
course.add_student(s1)
course.add_student(s2)
#print(course.get_average_student())


#inheritance 
class Pet:
    def __init__(self,name,age):
        self.name =name 
        self.age =age 
    def show(self):
        print(f"I am {self.name} and am {self.age}")
    def speak(self):
        print("what??")

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color =color 
   
    def speak(self):
        print("meow")

    def show(self):
        print(f"I am {self.name}  and am {self.age} and color {self.color}")
class Dog(Pet):
    def speak(self):
        print("Bark")
class Fish(Pet):
    pass

p =Pet("Vinny",19)
#p.show()
#p.speak()
d= Dog("Bill",34)
#d.show()
#d.speak()
f =Fish("gerr",56)
#f.speak()
c =Cat("king",23,"blue")
#c.show()

#static
#  class attributes 

class Person:
    number_of_people = 0
    def __init__(self,name):
        self.name =name 
        Person.add_people()
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    @classmethod
    def add_people(cls):
        cls.number_of_people +=1
p1 = Person("Vinny")
p2 =Person("Gill")
print(Person.number_of_people_())

#class methods

class Math:
    @staticmethod
    def add5(x):
        return x+5
    @staticmethod
    def pr():
        print("run")
print(Math.add5(9))
Math.pr()

