##Types of function


#1- They cant return  //non return ( no parameter , no return)

def chetan ():
    print("Hello World")

chetan()


#2- No return with parameter(argument) (Para  - yes and No return - no)

def greet_name (name):
    print("Hello,", name)

greet_name("John")

#3 - No return with default parameter ( # positional argument)

def Say (name = "chetan"):
    print("Hello,",name)

result = Say("Bobby")
print(result)
result2 = Say()
print(result2)


#4- Return with parameter ( yes return and yes parameter)

def my_name(name1="thakur the great", name2="always"):
    print(name1, name2)


my_name(name1 = "jack")
