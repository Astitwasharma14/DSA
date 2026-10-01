empty_tuple = tuple()

family = ('astitwa','angel','sanidhya','sankalp','vishal','dev')

sisters = ('angel','palak','paneer')
brothers = ('dev','devdas','sanidhya')

siblings = sisters + brothers 
print(siblings)
print("total number of siblings : ", len(siblings))
family = ('anil', 'anita')
family_members = siblings + family
print(family_members)

siblings = family_members[0:6]
print(siblings)
parents = family_members[6:8]
print(parents)




fruits = ('mangoes','pineapple','banana')
vegetables = ('onion', ' tomato','potato')
animal_product = ('milk','curd','cheeze',' paneer')

food_stuff_tp = fruits + vegetables + animal_product
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

middle_item = food_stuff_lt[5:6]
print(middle_item)
first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[-4: -1]
print("the first three items :",first_three,"\nthe last three items :", last_three)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('estania' in nordic_countries)
print('Iceland' in nordic_countries)