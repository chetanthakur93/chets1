##loop
from unittest import case

#print("chetan")

## for loop - repetation of block of code multiple times ( to repeat something)

##for i in range (1,10,2):
    ##print(i)
##for i in range (1,25,4):
    ##print(i)
   ## if i >10:
     ##   print("chetan is great")

for i in range (1,50):
    if i==25:
        print("i is 25")
    else:
        pass
for i in range(1, 50):
    if i == 25:
        print("i is 25")
        break

for i in range (2,24):
    if i==12 or i==18:
        print("chetan")
        break

##print even no using for loop

for i in range (1,101):
    if i % 2 == 0:
        print(i)


## BREAK - move out of loop
## PASS- placeholder
## continue
## match

## write a program to ask user which browser he want to run automation

##input
##output
browser_name = input("Enter the browser name\n")
match browser_name:
  case  "chrome":
      print("able to run")
  case "firefox":
      print("able to run")
  case "safari":
      print("able to run")
  case "edge":
      print("able to run")
  case _:
      print("cannot run")