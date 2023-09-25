# This project will calculate your BMI(body mass index)

# gather weight and height information
height = float(input("Please enter your height in cm:\n"))
weight = float(input("Please enter you weight in kg:\n"))

# def bmi calculator function
def bmi_index(height, weight):
    bmi = weight / ((height / 100)** 2)
    bmi_type = ""
    if bmi <= 18.5:
        bmi_type = "You are underweight!"
    elif bmi < 25 and bmi > 18.5:
        bmi_type = "You are healthy!"
    elif bmi < 30 and bmi >= 25:
        bmi_type = "You are overweight!"
    elif bmi >= 30:
        bmi_type = "You are severely overweight!"
    return(bmi, bmi_type)

# print results
print("You body mass index is: " + str(round(bmi_index(height, weight)[0], 4)))
print(bmi_index(height, weight)[1])