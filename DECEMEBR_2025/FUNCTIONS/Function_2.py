

##create a program to sum of three numbers from user input
##if user doesnt provide any number , use default as 100,200 and 300

num_1 = int(input("Enter first numbers\n"))
num_2 = int(input("Enter second numbers\n"))
num_3 = int(input("Enter third numbers\n"))


def sum_three(num1 = 100, num2 = 200, num3 = 300):
    return num1 + num2 + num3


Result = sum_three(num_1, num_2, num_3)
print(Result)

result = sum_three()
print(result)

result2 = sum_three (num1=12474474474646)
print(result2)

