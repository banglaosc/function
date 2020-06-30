# understand about function syntax
def ফাঙ্কশনের_নাম():
    print('ফাঙ্কশনের কাজ ও ফলাফল প্রদান')
    
# এখন ফাঙ্কশন কল করা
ফাঙ্কশনের_নাম()


# fisrly we know about simple prb

# if a = 10 and b = 20 ,then what will be the output of (a+b)^2

a= 10
b = 20
# we know about  (a+b)^2 = a^2 + 2ab + b^2
উত্তর_১  = a*a + 2*a*b + b*b

print(উত্তর_১)
# if i want to again change the number and see the result then
a= 30
b = 6
# we know about  (a+b)^2 = a^2 + 2ab + b^2
উত্তর_২  = a*a + 2*a*b + b*b

print(উত্তর_২)


# we can change this repetation by function

def সুত্র_প্রয়োগ(a,b):
    সমাধান = a*a + 2*a*b + b*b
    print(সমাধান)
    

সুত্র_প্রয়োগ(10,20)
সুত্র_প্রয়োগ(30,6)

# same things we can do it using return function

def সুত্র_প্রয়োগ(a,b):
    সমাধান = a*a + 2*a*b + b*b
    return সমাধান
    

উত্তর_১ =  সুত্র_প্রয়োগ(10,20)

উত্তর_২ = সুত্র_প্রয়োগ(30,6)

print(উত্তর_১)
print(উত্তর_২)


# 