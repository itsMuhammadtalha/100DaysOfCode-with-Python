# see readme for explanation    

a="1"
b="2"

# a and b are both strings
print(a+b) 

#converting it to integers

print(int(a) + int(b))

#typecasting will work provided the data type is valid
# for example -> a = "1talha" is an invalid type

# TYPES OF TYPECASTING 

# explicit typecasting 

string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)

# implicit typecasting

float_num = 1.9
int_num = 8

sum = float_num+int_num 

print("The type of float_num is : ",type(float_num))
print("The type of int_num is : ",type(int_num))
print("The type of sum is : ",type(sum))






