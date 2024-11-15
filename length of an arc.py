def calculate_length_of_an_arc(radius,degrees):
    length_of_an_arc=(degrees/360)*2*22/7*radius
    return length_of_an_arc
put1=float(input("radius"))
put2=int(input("degrees"))
print(calculate_length_of_an_arc(put1,put2))