
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
print(company[0])
print(company[-1])
print(company[10])


print("".join([company[0].upper() for company in company.split(" ")]))
print("".join([company1[0].upper() for company1 in company1.split(" ")]))

print(company.find('C'))
print(company.find('f'))
print(company.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
sentence =  'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind('because'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
start_pharse =sentence.find('because because because')
end_pharse = sentence.rfind('because because because')
sliced_pharse = sentence[start_pharse:end_pharse]
print(sliced_pharse)
print(f"start_pharse: {start_pharse}, end_pharse: {end_pharse}")

# my solution
sentance = "You cannot end a sentence with because because because is a conjunction"
phrase = "because because because "

index = sentance.find(phrase)
print(sentence[index:len(phrase)+index])
print(sentence.find('because'))


sentance = "You cannot end a sentence with because because because is a conjunction"
phrase = "because because because "

start_index = sentence.find(phrase)
end_index = start_index + len (phrase)

target_index = sentence [start_index : end_index]
print(target_index)

print(company.startswith('Coding'))
print(company.endswith('Coding'))

sen = '30DaysOfPython'
sent = 'thirty_days_of_python'
print(sen.isidentifier())
print(sent.isidentifier())

list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon' ]
print('#'.join(list))

print("I am enjoying this challenge.\nI just wonder what is next.")

print('Name\tAge\tcountry\tcity')
print('astitwa\t23\tindia\tindore')

radius = 10
area = 3.14 * radius ** 2
print('the are of a circle whos {} is {}'.format(radius, area))

a = 8
b = 6 
print (f'{a}+{b} = {a + b }')
print (f'{a} - {b} = {a - b }')
print (f'{a}*{b} = {a * b }')
print (f'{a}/{b} = {a / b }')
print (f'{a}%{b} = {a % b }')
print (f'{a}//{b} = {a // b }')
print (f'{a}**{b} = {a ** b }')