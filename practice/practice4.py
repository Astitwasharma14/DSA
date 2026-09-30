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