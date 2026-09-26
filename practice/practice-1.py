def mul() -> int:
    number = input("enter your number: ")
    try : 
        number = int(number)
        return 5*number
    except:
        print("please enter an integer")
        return 

x = mul()
print(x)