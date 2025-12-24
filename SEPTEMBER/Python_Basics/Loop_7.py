

##for i in range (0,10,1):
    ##if i == 6 or i ==5:
        ##print(i)
   ## else:
       # continue

 ## write a user define program that print number 1 to 100 ,However for multiple of 3 , print "fizz"
 ## instead of number and for multiple of 5 ,print "buzz" for number that are multiple of 3 and 5 ,print fizzbuzz.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
