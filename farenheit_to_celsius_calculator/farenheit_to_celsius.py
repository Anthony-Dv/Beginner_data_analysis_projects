# This program will convert farenheit to celsius and via versa

farenheit_celsius = input("""If you want to convert farenheith to celsius enter: 1
If you want to convert celsius to farenheith enter: 2\n""")

# get temperature to convert
temp = None
while temp == None:
    try:
        temp = int(input("What is the temperature you want to conver?(type only number)\n"))
    except:
        print("Not a acceptable value!")

# define temperature converter
def temp_converter(farenheit_celsius, temp):
    result = None
    if farenheit_celsius == "1":
        result = (temp - 32) / 1.8
    elif farenheit_celsius == "2":
        result = (1.8 * temp) + 32
        pass
    return result

# call temp_converter function
result_temp = str(temp_converter(farenheit_celsius, temp))

# print result
if farenheit_celsius == "1":
    print("Result is: " + result_temp + "°C")
elif farenheit_celsius == "2":
    print("Result is: " + result_temp + "°F")


