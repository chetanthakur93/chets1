## write  program to clasifies triangle based on sides of triangle based on user input
##equilateral triangle ( all sides equal)
##isosceles triangle ( two sides equal)
##scalene triangle ( no sides equals)

##input = data type  of sides of triangle is (float)
##output = string ( for types of triangle )

##logic build

s1 = float(input("enter side1 of triangle\n"))
s2 = float(input("enter side2 of triangle\n"))
s3 = float(input("enter side3 of triangle\n"))

if s1 == s2 == s3:
    print("Triangle is equilateral type")
elif s1 == s2 >= s3:
    print("Triangle is isosceles")
elif s1 == s3 <= s2:
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")




