
# default argument
# def average(a=9,b=1):
#     print("The average is ",(a+b)/2)

# average(4,6)
# average(1,3) 
# average()
# average(3)

# keyword argument
# average(b=9 ,a=21)

# required argument
# def average(a,b=1):
#     print("The average is ",(a+b)/2)

# average(5)

# keyword arguments
# def average(*numbers):
#     # print(type(numbers))
#     sum=0
#     for i in numbers:
#         sum = sum +i
#         print("Average is:",sum/len(numbers))
    
# average(5,6)
 
# return
def average(*numbers):
 
     sum=0
     for i in numbers:
         sum = sum +i
        
     return sum/len(numbers) 
c=average(5,6,7,1)
print(c)

