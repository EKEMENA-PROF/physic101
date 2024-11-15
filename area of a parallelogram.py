def calculate_area_of_a_parallelogram(length1,length2,height):
    area_of_parallelogram=1/2*(length1+length2)*height
    return area_of_parallelogram
put1=int(input("first length"))
put2=int(input("second length"))
put3=int(input("height"))
print(calculate_area_of_a_parallelogram(put1,put2,put3))