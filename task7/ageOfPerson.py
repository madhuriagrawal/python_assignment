class Person:

    def __init__(self,age):
        if age >=0:
            self.age = age
        else:
            self.age=0
            print("Age is not valid, setting age to 0")

    def yearPasses(self,yearincreased):
        self.age=self.age+yearincreased
        print(self.age)

    def amIOld(self):
        if self.age>0 and self.age<13:
            print("You are young")
        elif self.age>= 13 and self.age<=19:
            print("You are a teenager")
        else:
            print("You are old")

obj=Person(38)

obj.amIOld()
obj.yearPasses(4)



