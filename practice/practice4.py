
# lst =  list()

# lst = ['a','b','c','d','e','f']
# print(len(lst))

# print(lst[0],lst[2], lst[-1])

# mixed_data_types = ['astitwa','23', '5.10','single', 'indore']

# it_companies = ['Facebook', 'Google','Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
# print(it_companies)
# print("the total number of companies :",len(it_companies))
# print(it_companies[0],it_companies[3],it_companies[6])
# it_companies[4] = 'infosys'
# print(it_companies)
# it_companies.insert(7,'TCS')
# print(it_companies)
# it_companies.insert(3 , 'Gammaedge')
# print(it_companies)

# it_companies = ['Facebook', 'Google','Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
# it_companies[1] = it_companies[1].upper()
# print(it_companies)
# print("#".join(it_companies))

# does_exist = 'Facebook' in it_companies
# print(does_exist)

# it_companies.sort()
# print(it_companies)
# it_companies.reverse()
# print(it_companies)
# print(it_companies[0:3])
# print(it_companies[4::])
# print(it_companies[3])
# del it_companies[0]
# del it_companies[3]
# it_companies.pop()
# it_companies.pop(-1)

# it_companies.clear()
# print(it_companies)

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

# middle_stack = ['python', 'SQL']

# full_stack = front_end + middle_stack + back_end
# print(full_stack)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print("the min age is : ", ages[0],"the max age is : ", ages[-1])
if len(ages)%2 == 0:
    n = len(ages)
    x = (ages[int(n/2)] + ages[int(((n)+1)/2)])/2
else:
    x = ages[int((n +1)/2)]
print(x)


sum = 0
for i in range(len(ages)):
    sum = sum + ages[i]

x = sum / 10
print("the average of the ages : ", int(x))

y = ages[0] - ages[-1]
print("the range is :", int(y))
print((ages[0] -x )== (ages[-1] - x))
