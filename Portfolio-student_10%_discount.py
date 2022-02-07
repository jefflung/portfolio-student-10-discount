#student gets 10% discount

user=str(input("Please tell me your status:"))

if(user=="student" or user=="Student"):
    CoI=float(input("Cost of your item:"))
    charge=CoI*0.9
    print("You get a 10% discount for student. Thank you for £",charge)
elif(user=="staff" or user=="Staff"):
    CoI=float(input("Cost of your item:"))
    print("Thank you for £",CoI)
else:
    CoI=float(input("Cost of your item:"))
    print(user, " is unknown")
    print("You do not qualify for any discount. Thank you for £",CoI)
