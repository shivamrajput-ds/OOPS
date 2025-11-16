class employee:
    # special method /magic method /dunder method-> constructor
    def __init__(self):
        print("started executing attributes")
        self.id=123
        self.salary=50000
        self.designation="SDE"

    def travel(self,destination):
        print("this travel function is called manually ")
        print(f"Employee is now travelling to {destination}")    

# create an object or instance of the class
sam=employee()

# print(sam.id)
#sam.travel("delhi")

print(type(sam))