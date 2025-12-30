##write a program to classified a leap year which is exactly divisible by 4 ,
## except for years evenly divisible by 100 but not 400



##logic build formula

##input = data type for leap year is (integer)
##output = to define whether its leap year or not (string)

year = int(input("Enter year\n"))

if year/4 and year/400:
    print("its leap year")
elif year/100:
    print("its NOT a leap year")
else:
    print("its NOT a leap year")

