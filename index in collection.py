number=[13,21,6,7,90]
okpa_list=["bambara",
           "maggie",
           "palm oil",
           "vegetable"]
print(okpa_list)
okpa_list.append("fish")
print(okpa_list)

ingredient=input("enter the ingredient")
for item in okpa_list:
    if item==ingredient:
        print(item,"is in the list")
