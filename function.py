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


historical_data = get_3_month_bitcoin_historical_data()

# for data in historical_data:
#     print(data)  # comment only this one

# second series

def শেষ_৭_দিন_অন্তর_অন্তর_ডাটা():
    ডাটা = historical_data[0:50:7]
    return ডাটা

শেষ_৭_সপ্তাহ_ডাটা = শেষ_৭_দিন_অন্তর_অন্তর_ডাটা()
#
# for সপ্তাহ_ডাটা in শেষ_৭_সপ্তাহ_ডাটা:
#     print(সপ্তাহ_ডাটা )
#     print()

#  prediction function 
def পরবর্তী_সপ্তাহের_দাম():
    সর্বমোট_দাম = 0
    আপ = 0
    ডাউন = 0
    আপ_ডাউন_ডাটা = float(শেষ_৭_সপ্তাহ_ডাটা[0]['price_open'])
    for সপ্তাহ_ডাটা in শেষ_৭_সপ্তাহ_ডাটা:
        if আপ_ডাউন_ডাটা > float(সপ্তাহ_ডাটা['price_open']):
            ডাউন = ডাউন + 1
            আপ_ডাউন_ডাটা = float(সপ্তাহ_ডাটা['price_open'])
        elif আপ_ডাউন_ডাটা < float(সপ্তাহ_ডাটা['price_open']):
            আপ = আপ + 1 
            আপ_ডাউন_ডাটা = float(সপ্তাহ_ডাটা['price_open'])
            
        সর্বমোট_দাম = সর্বমোট_দাম + float(সপ্তাহ_ডাটা['price_open'])
    
    আজকের_দাম = float(শেষ_৭_সপ্তাহ_ডাটা[0]['price_open'])
    গত_সপ্তাহের_দাম = float(শেষ_৭_সপ্তাহ_ডাটা[1]['price_open'])
    দাম_পরিবর্তন = আজকের_দাম - গত_সপ্তাহের_দাম
    গড় = সর্বমোট_দাম / 7 
    if দাম_পরিবর্তন >= 0:
        if গড় < আজকের_দাম and আপ > ডাউন:
            বাড়বে = দাম_পরিবর্তন / 100
            return "{:.2f}% দাম বাড়বে".format(abs(বাড়বে))
        elif গড় > আজকের_দাম and আপ < ডাউন:
            কমবে = দাম_পরিবর্তন / 100
            return "{:.2f}% দাম কমবে".format(কমবে)
    if দাম_পরিবর্তন < 0 :
        if গড় >= আজকের_দাম and আপ > ডাউন:
            বাড়বে = দাম_পরিবর্তন / 100
            return "{:.2f}% দাম বাড়বে".format(abs(বাড়বে))
        elif গড় >= আজকের_দাম and আপ < ডাউন:
            কমবে = দাম_পরিবর্তন / 100
            return "{:.2f}% দাম কমবে".format(কমবে)
        elif গড় < আজকের_দাম:
            কমবে = দাম_পরিবর্তন / 100
            return "{:.2f}% দাম কমবে".format(কমবে)
        
        


print("পরবর্তী_সপ্তাহে "+পরবর্তী_সপ্তাহের_দাম())