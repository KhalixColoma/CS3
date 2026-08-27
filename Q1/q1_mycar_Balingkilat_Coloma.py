class car:
    def __init__(self,brand,model,battery=50):
        self.brand=brand
        self.model=model
        self.battery=battery
    def go(self,distance):
        self.battery -= distance/25
        print("You have travlled",distance,"km")
        print("Your",self.brand,
              self.model, "has" ,self.battery, "wH left.")
    def charge(self,wH):
        self.battery += wH
        print("You've charged your car ")
brand=input("What brand is your car? ")
model=input("WHat is the mdoel of you car? ")
Mycar=car(brand, model)
while Mycar.battery>0:
    option=input("Do you want to charge or drive? ").lower()
    if option == "drive":
        distance = int(input("How far do you want to drive? "))
        Mycar.go(distance)
    elif option =="charge":
        wH = int(input("How much do you wnat to charge? "))
        Mycar.charge(wH)
    else:
        print("Invalid input")
    
print("Your battery is fully drained.")             
