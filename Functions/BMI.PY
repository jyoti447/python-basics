def BMI(weight_kg, height_m):
    return weight_kg/(height_m**2)
weight_kg = float(input("Enter weight in kg : "))
height_m = float(input("Enter height in meter : "))
result = BMI(weight_kg,height_m)
print("BMI :",result)
if result<18.5:
        print("Underweight")
elif result <24:
        print("Normal")
else:
        print("Overweight")