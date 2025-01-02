class car:
    def __init__(self,brand,color):

        self.brand=brand
        self.color=color


    def describe_car(self):
        print(f"This is a {self.brand} {self.color}")


car1=car("Toyota","Red")
car2=car("Honda","Blue")

car1.describe_car()
car2.describe_car()



