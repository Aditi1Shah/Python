
name = "Alisha"
num = len(name)*9
print("Hi "+name +" Your Lucky number is : "+ str(num))
name = "Priyanka"
num = len(name)*9
print("Hi "+name +" Your Lucky number is : "+ str(num))

#We are printing and declaring same things again and again better way is to use function to do the same

def Lucky_Number(name):
    number = len(name)*9
    print("Hi "+name +" Your Lucky number is : "+ str(number))

Lucky_Number("Alisha")
Lucky_Number("Roy")
