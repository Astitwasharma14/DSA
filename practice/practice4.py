
lst =  list()

lst = ['a','b','c','d','e','f']
print(len(lst))

print(lst[0],lst[2], lst[-1])

mixed_data_types = ['astitwa','23', '5.10','single', 'indore']

it_companies = ['Facebook', 'Google','Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
print(it_companies)
print("the total number of companies :",len(it_companies))
print(it_companies[0],it_companies[3],it_companies[6])
it_companies[4] = 'infosys'
print(it_companies)
it_companies.insert(7,'TCS')
print(it_companies)
it_companies.insert(3 , 'Gammaedge')
print(it_companies)

it_companies = ['Facebook', 'Google','Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
it_companies[1] = it_companies[1].upper()
print(it_companies)
print("#".join(it_companies))

does_exist = 'Facebook' in it_companies
print(does_exist)

it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[0:3])
print(it_companies[4::])
print(it_companies[3])
del it_companies[0]
del it_companies[3]
it_companies.pop()
it_companies.pop(-1)

it_companies.clear()
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

middle_stack = ['python', 'SQL']

full_stack = front_end + middle_stack + back_end
print(full_stack)