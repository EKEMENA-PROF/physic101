def calculate_work(force,distance):
    work=force*distance
    return work

def calculate_length_of_an_arc(radius,degrees):
    length_of_an_arc=(degrees/360)*2*22/7*radius
    return length_of_an_arc


def calculate_impulse(force,time):
    impulse=force*time
    return impulse


def volume_of_a_cuboid(length,breadth,height):
    volume_of_cuboid= length * breadth * height
    return volume_of_cuboid

def calculate_perimeter_of_a_square(length,breath):
    perimeter=2*(length+breath)
    return perimeter

def calculate_velocity(displacement,time):
    velocity=displacement/time
    return velocity

putALPHA=input(" input a,b,c,d,e,f")
if putALPHA=='a':
    put1=int(input("force"))
    put2=int(input("distance"))
    print(calculate_work(put1,put2))
elif putALPHA=='b':
    put3=int(input("radius"))
    put4=float(input("degrees"))
    print(calculate_length_of_an_arc(put3,put4))
elif putALPHA=="c":
      put5=int(input("force"))
      put6=int(input("time"))
      print(calculate_impulse(put5,put6))
elif putALPHA=="d":
      put7=int(input("length"))
      put8=int(input("breadth"))
      put9=int(input("height"))
      print(volume_of_a_cuboid(put7,put8,put9))
elif putALPHA=="e":
     put10=int(input("length"))
     put11=int(input("breadth"))
     print(calculate_perimeter_of_a_square(put10,put11))
elif putALPHA=="f":
    put12=int(input("displacement"))
    put13=int(input("time"))
    print(calculate_velocity(put12,put13))
else:
    print('incorrect value')


