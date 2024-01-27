tom_exp_list = [2100 , 3400 , 3500]
jow_exp_list = [200 , 500 , 700]

# for tom
total = 0 
for items in tom_exp_list:
    total += items

print("tom's total expense is : " , total)   

# for joe 

total = 0 
for items in jow_exp_list:
    total += items

print("joe's total expense is : " , total)   

# let's write it using functions 

def calculate_total(exp):
    total = 0 
    for items in exp:
        total += items 
    return total
toms_total = calculate_total(tom_exp_list )
jow_total = calculate_total(jow_exp_list)        

print("tom's total expense is :" , toms_total)
print("joe's total expense is :" , jow_total)

# another example is let's sum two numbers

def sum(a , b):
    c = a + b
    return c 
sum_value = sum(2 , 3 )
print(sum_value)

# you can do this as 

def sum(a = 2 , b = 3 ):
    c = a + b 
    return c 
print(sum())

# or you can do this as 

def sum(a , b ):
    c = a + b
    return c 

print(sum(a= int(input("Enter a value for a  : ")) , b= int(input("Enter a value for b : "))))
