def calc_velocity(displacement,time):
    velocity=displacement/time
    return velocity
put1=int(input("displacement"))
put2=int(input("time"))
print(calc_velocity(put1,put2))
