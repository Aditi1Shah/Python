#Concept : 1
#Return area of triangle by taking base and height as parameters to the function and then add areas of two
#triangles and display the result

#Function to calculate area of a trianglr :
def area_calculate(height,base):
    return(base*height)/2

area_a = area_calculate(2,3)        #area = 3 sq units
area_b = area_calculate(4,5)        #area = 10 sq units
sum = area_a+area_b
print("Output of Concept 1 : ")
print("Sum of areas : "+ str(sum))  #should print 13

#Functions in python can return mre than one value!

#Concept 2 : Convert time in seconds to hrs,mins and seconds
def Convert_Seconds(seconds):
    hours = seconds//3600
    minutes = (seconds-hours*3600)//60      #Floor division operator divies a num and takes int part as result
    remaining_sec = seconds-(hours*3600)-(minutes*60)
    return hours,minutes,remaining_sec
print("Output of Concept 2 : ")
hours,minutes,seconds = Convert_Seconds(4500)
print(hours,minutes,seconds)

#its possible to return nothing from a function
def greeting(name, department):
    print("Welcome "+ name)
    print("Your are a part of "+ department)

print("Output of concept 3 :")
result = greeting("Alisha","IT Support")
print(result)
 #None is a very special data type in Python used to indicate that things are empty or that they return nothing.