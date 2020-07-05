# # understand about function syntax
# def ফাঙ্কশনের_নাম():
#     print('ফাঙ্কশনের কাজ ও ফলাফল প্রদান')
#
# # এখন ফাঙ্কশন কল করা
# ফাঙ্কশনের_নাম()


# fisrly we know about simple prb

# if a = 10 and b = 20 ,then what will be the output of (a+b)^2

# a = 10
# b = 20
# # we know about  (a+b)^2 = a^2 + 2ab + b^2
# উত্তর_১  = a*a + 2*a*b + b*b
#
# print(উত্তর_১)


# # if i want to again change the number and see the result then
# a = 30
# b = 6
# # we know about  (a+b)^2 = a^2 + 2ab + b^2
# উত্তর_২  = a*a + 2*a*b + b*b
#
# print(উত্তর_২)


# # we can change this repetation by function
#
# def সুত্র_প্রয়োগ(a,b):
#     সমাধান = a*a + 2*a*b + b*b
#     print(সমাধান)
#
#
# সুত্র_প্রয়োগ(10,20)
# সুত্র_প্রয়োগ(30,6)

# # same things we can do it using return function
#
# def সুত্র_প্রয়োগ(a,b):
#     সমাধান = a*a + 2*a*b + b*b
#     return সমাধান
#
#
# উত্তর_১ =  সুত্র_প্রয়োগ(10,20)
#
# উত্তর_২ = সুত্র_প্রয়োগ(30,6)
#
# print(উত্তর_১)
# print(উত্তর_২)


# first series
from historical_script import get_3_month_bitcoin_historical_data


শেষ_৩_মাসের_ডাটা = get_3_month_bitcoin_historical_data()

# for ডাটা in শেষ_৩_মাসের_ডাটা:
#     print(ডাটা)  # comment only this one



#  prediction function 
def পরবর্তী_দিনের_দাম():
    সর্বমোট_দাম = 0
    for ডাটা in শেষ_৩_মাসের_ডাটা:  
        সর্বমোট_দাম = সর্বমোট_দাম + float(ডাটা['price_open'])
    
    আজকের_দাম = float(শেষ_৩_মাসের_ডাটা[0]['price_open'])
   
    গড় = সর্বমোট_দাম / len(শেষ_৩_মাসের_ডাটা)
    দাম_পরিবর্তন = আজকের_দাম - গড় 
    
    if দাম_পরিবর্তন >= 0 : 
        বাড়বে = দাম_পরিবর্তন / 100
        return "{:.2f}% দাম বাড়বে".format(abs(বাড়বে))      
    elif দাম_পরিবর্তন < 0 :
        কমবে = দাম_পরিবর্তন / 100
        return "{:.2f}% দাম কমবে".format(abs(কমবে))
   
           

print("পরবর্তী_দিনের "+পরবর্তী_দিনের_দাম())



# গত_৭_দিনের_ডাটা prediction


গত_৭_দিনের_ডাটা = শেষ_৩_মাসের_ডাটা[0:7]

#  prediction function 
def পরবর্তী_দিনের_দাম():
    সর্বমোট_দাম = 0
    for ডাটা in গত_৭_দিনের_ডাটা:  
        সর্বমোট_দাম = সর্বমোট_দাম + float(ডাটা['price_open'])
    
    আজকের_দাম = float(গত_৭_দিনের_ডাটা[0]['price_open'])   
    
    গড় = সর্বমোট_দাম / len(গত_৭_দিনের_ডাটা)
    দাম_পরিবর্তন = আজকের_দাম - গড় 
    # if দাম_পরিবর্তন is positive
    if দাম_পরিবর্তন >= 0 : 
        বাড়বে = দাম_পরিবর্তন / 100
        return "{:.2f}% দাম বাড়বে".format(abs(বাড়বে))      
    elif দাম_পরিবর্তন < 0 : #  # if দাম_পরিবর্তন is negetive
        কমবে = দাম_পরিবর্তন / 100
        return "{:.2f}% দাম কমবে".format(abs(কমবে))
            

print("পরবর্তী_দিনের "+পরবর্তী_দিনের_দাম())