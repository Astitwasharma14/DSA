
a ='thirty '
b ='days '
c = 'of '
d = 'python '
full_str = a +  b  +  c  +  d
print(full_str)


a1 = 'coding '
b1 = 'for '
c1 = 'all'
print(a1+b1+c1)

company = a1+b1+c1
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

cut = company[0:6]
print(cut)

print(company.find('coding'))

company = "coding,for,all"
print(company.split(','))

print(company.replace('coding','python'))
company1 = 'Python for everyone'
print(company1.replace('everyone','All'))

company = 'Coding for all'
print(company.split(' '))

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))
