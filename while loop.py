age=float(input("insert age"))
while age<7:
    print("not old enough")
    age = float(input("insert age"))
else:
    print(f"you are {age} years old dude")

food=input("the food you like (press q to escape):")
while not food=="q":
    print(f"the food you choose is {food}")
    food=input("the food you like(press q to escape):")
print("see you later")

num=int(input("put a integer btw 1-10:"))
while num<1 or num>10:
        print("no go area")
        num=int(input("put a integer btw 1-10:"))
else:
    print(f"your number is {num} and is ok")





