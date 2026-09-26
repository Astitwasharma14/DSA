
age = 23
height = 5.10
complex_number = 1 + 1j

base = input(int('enter the base :'))
height = input(int('enter the height:'))
area = (0.5)*base*height
print(area)

side_a,side_b,side_c = input(int('enter the side a:')), input(int('enter side b :')), input(int('enter side c'))
perimeter = side_a + side_b + side_c
print("the perimeter of the triangle is :",perimeter)

length = input(int('enter the length of rectangle:'))
bredth = input(int('enter the bredth of rectangle:'))
area1 = length*bredth
perimeter1 = 2*(length+bredth)
print("the area of rectangle :",area1,"perimeter of rectangle :",perimeter1)

r = input(int('enter the radius of a circle:'))
area_of_circle = 3.14*r*r
perimeter_of_circle = 2*(3.14)*r
print("area of circle :", area_of_circle,"perimeter of a circle :", perimeter_of_circle)

x = input(int('enter the x'))
y = (2*(x)) - 2

x1 , y1 = input(int('enter the value of x1:')), input(int('enter the value of y1'))
x2 , y2 = input(int('enter the value of x2:')), input(int('enter the value of y2'))
m = (y2 - y1)/ (x2 - x1)
print("the slope is: ", m)

#question 11
x3 = input(int('enter the value of x'))
y3 = (x3**2) + (6*x3) + 9
print("the value of y:",y3)

print(len("dragon")!=len("python"))
print('on' in "python"and "dragon")
print('jargon 'in'i hope this course is not full of jargon')
print('on' not in "python"and "dragon")

length1 = len("python")
flt = float(length1) 
star = str(flt)

even = input(int('Enter a number:'))
if even%2 ==0:
    
    print("it is divisible by 2")
else:
    print("please enter a even number")



print('7//3'==int(2.7))
print(type('10')==type(10))
print(int('9.8')== (10))

enter_hour =input("Enter the hours:")
rate_per_hour = input("enter the rate per hour")
print( "the total salary you worked in this week :",enter_hour*rate_per_hour)


number_of_years = input("enter the number of years")
print("you have lived",number_of_years*86400*365)

for i in range(6):
    if i == 0:
        pass 
    else:
        print(f"{i**1} {i ** 0} {i**1} {i**2} {i**3}")

