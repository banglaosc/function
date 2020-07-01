# # understand about function syntax
# def ফাঙ্কশনের_নাম():
#     print('ফাঙ্কশনের কাজ ও ফলাফল প্রদান')
    
# # এখন ফাঙ্কশন কল করা
# ফাঙ্কশনের_নাম()


# # fisrly we know about simple prb

# # if a = 10 and b = 20 ,then what will be the output of (a+b)^2

# a= 10
# b = 20
# # we know about  (a+b)^2 = a^2 + 2ab + b^2
# উত্তর_১  = a*a + 2*a*b + b*b

# print(উত্তর_১)
# # if i want to again change the number and see the result then
# a= 30
# b = 6
# # we know about  (a+b)^2 = a^2 + 2ab + b^2
# উত্তর_২  = a*a + 2*a*b + b*b

# print(উত্তর_২)


# # we can change this repetation by function

# def সুত্র_প্রয়োগ(a,b):
#     সমাধান = a*a + 2*a*b + b*b
#     print(সমাধান)
    

# সুত্র_প্রয়োগ(10,20)
# সুত্র_প্রয়োগ(30,6)

# # same things we can do it using return function

# def সুত্র_প্রয়োগ(a,b):
#     সমাধান = a*a + 2*a*b + b*b
#     return সমাধান
    

# উত্তর_১ =  সুত্র_প্রয়োগ(10,20)

# উত্তর_২ = সুত্র_প্রয়োগ(30,6)

# print(উত্তর_১)
# print(উত্তর_২)


# first series
from historical_script import get_3_month_bitcoin_historical_data


historical_data = get_3_month_bitcoin_historical_data()

# print(historical_data)  # comment only this one

# second series

def শেষ_৭_দিন_অন্তর_অন্তর_ডাটা():
    ডাটা = historical_data[0:50:7]
    return ডাটা

# শেষ_৭_সপ্তাহ_ডাটা = শেষ_৭_দিন_অন্তর_অন্তর_ডাটা()

# for সপ্তাহ_ডাটা in শেষ_৭_সপ্তাহ_ডাটা:
#     print(সপ্তাহ_ডাটা )
#     print()
    
def ভবিস্যত_৭_দিনের_দাম():
    সর্বমোট_দাম = 0
    for সপ্তাহ_ডাটা in শেষ_৭_সপ্তাহ_ডাটা:
        সর্বমোট_দাম = সর্বমোট_দাম + float(সপ্তাহ_ডাটা['price_open'])
    
    আজকের_দাম = float(শেষ_৭_সপ্তাহ_ডাটা[0]['price_open'])
    গড় = সর্বমোট_দাম / 7
    if গড় >= আজকের_দাম:
        return "দাম বাড়বে"
    elif গড় < আজকের_দাম:
        return "দাম কমবে"
print(ভবিস্যত_৭_দিনের_দাম())