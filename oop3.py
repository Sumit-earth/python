class student:

    def __init__(self,name,age):
        

        self.name=name
        self.age=age


    def display_details(self):
        print(f"Name {self.name} Age {self.age}")


student1=student("Alice",22)
student1.display_details()