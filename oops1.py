class employee:
    # special method /magic method /dunder method-> constructor
    def __init__(self):
        print(id(self))
        # print("started executing attributes")
        self.id=123
        self.salary=50000
        self.designation="SDE"

    def travel(self,destination):
        print("this travel function is called manually ")
        print(f"Employee is now travelling to {destination}")    

# create an object or instance of the class
sam=employee()
sam.name="Sam Rajput"
print(sam.name)
# jam=employee()
# print(id(sam))
# print(id(jam))

# print(sam.id)
#sam.travel("delhi")

# print(type(sam))