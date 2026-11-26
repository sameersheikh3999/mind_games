# class is the blue print to create objects
class Employee:
    name="Sameer Sheikh"
    language="python"
    salary="2000000000000000"

    def getInfo(self): #camel case
        print(f"the language is {self.language}. The salary is {self.salary}")
    
    @staticmethod #decorator
    def greet():
        print("Good Morning")


sameer=Employee()
print(f"My name is {sameer.name} and my salary is {sameer.salary}")
sameer.getInfo()
sameer.greet()


harry=Employee()

harry.name="Harry"
harry.pajamas="Green"
print(f"My name is {harry.name} and my salary is {harry.salary} and his pajamas are {harry.pajamas} ")


