# a=int(input("Enter your age: "))
# print("your age is:",a)
# coditional operators
# >,<,>=,<=,==,!=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

# if..else
# if(a>18):
#     print("you can drive")
# else:
#     print("you cannot drive")
# elif
# num=0
# if(num<0):
#     print("Number is negative")
# elif(num==0):
#     print("Number is Zero.")
# else:
#     print("Number is positive")

    # nested if statement

num=18
if(num<0):
    print("Number is negative")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num>10 and num <=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
