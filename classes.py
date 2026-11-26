# class is the blue print to create objects
class Employee:
    name="Sameer Sheikh"
    language="python"
    salary="2000000000000000"

    def getInfo(self): #camel case
        print(f"the language is {self.language}. The salary is {self.salary}")

    def __init__(self, name, salary, language): #dunder method which is automatically called starts with __
        print("I am creating an object")
        self.name=name
        self.salary=salary
        self.language=language
        print(f"My name is {self.name}, my salary is {self.salary} and my language is {self.language}")
    
    @staticmethod #decorator
    def greet():
        print("Good Morning")


# sameer=Employee()
# print(f"My name is {sameer.name} and my salary is {sameer.salary}")
# sameer.getInfo()
# sameer.greet()


harry=Employee("Harry",13000000,"JavaScript")






