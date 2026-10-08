class human:
    def __init__(self,name,age,email = "unknown"):
        self.name=name
        self.age=age
        self.email=email


p1_=human("ali",20)
print(p1_.email)
def decorator(func):
    def wrraper():
        print("berfore")
        func()
        print("after")
    return wrraper
@decorator
def sayHello():
    print("hello world")
sayHello()




