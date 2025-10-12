## write  a  user define program to alot marks to students
##based on grades


##logic build fromula

##input = data type for score is integer
##output = string for the given score

score = int(input("Enter your score\n"))

if score >= 90 and score <= 100:
    print("You score is","A")
elif score >= 80 and score <= 89:
    print("You score is","B")
elif score >= 70 and score <= 79:
    print("You score is","C")
elif score >= 60 and score <= 69:
    print("You score is","D")
elif score >=100:
    print("You are a superman")
else:
    print("You score is", "F")






