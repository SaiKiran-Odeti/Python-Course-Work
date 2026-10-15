#temp =int(input("enter the temperature:"))
# if temp % 33 == 0:
#     print("celsius")
# elif temp % 25 == 0:
#     print("fahrenheit")
# else:
#     print("vice versa")


# num1 = float(input("enter the number:"))
# operator=input("enter the operator(+,-,*,/)")
# num2 = float(input("enter the number:"))
# if operator =="+":
#     print(num1 + num2)
# elif operator =="-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# else:
#     print(num1 / num2)
# import random
# user = input("enter the number:")
# random_num=random.randint(1,10)
# if user ==random_num:
#     print("you win")
# else:
#     print("you lose")
# print(random_num)        

# password = input("enter the password:")
# if len(password) >= 8 and \
#      any(char.isupper() for char in password) and \
#      any(char.islower()for char in password)  and \
#      any(char.isdigit() for char in password) and \
#      any(not c.isalnum() for c in password):
    

#     print("strong password")
# else:

#     print("weak password")


# amount = float(input("enter the purchase amount:"))
# if amount >= 5000:
#     discount = amount *0.20
# elif amount >=2000:
#     discount = amount *0.10
# else:
#     discount = 0
#     final_ammount = amount -discount
#     print("Purchase Amount:",amount)
#     print("Discount:",discount)
#     print("Final Price:",final_ammount)

# from datetime import datetime
# current_hour = datetime.now().hour
# if current_hour <12:
#     print("good morning!")
# elif current_hour < 17:
#     print("good afternoon!")
# else:
#     print("good evening!")
# price = float(input("enter the item price:"))
# coupon= input("enter the coupon code:")
# if coupon =="123a":
#     discount = 12
# elif coupon =="123b":
#     discount =  10
# else:
#         discount = 0
#         print("invalid coupon  code. no discount applied")
# discount_amount = price * discount / 100
# final_price = price - discount_amount

# print("Original price: ₹", price)
# print("Discount:", discount, "%")
# print("Discount amount: ₹", discount_amount)
# print("Final price: ₹", round(final_price)

# grade =float(input("enter the grade:"))
# if grade>=9 and grade <10 :
#     print("grade A")
# elif grade>=8 and grade <9:
#     print("grade B")
# elif grade>=7 and grade <8:
#     print("grade C")
# elif grade>6 and grade <7:
#     print("grade d")
# else:
#     print("grade f")


# body =float(input("enter the body:"))
# if body <=30 and body >20:
#     print("underweight")
# elif body <=60 and body >50:
#     print("normalweight")
# elif body <=80 and body >70:
#     print("overweight")
# else:
#     print("obese")


days = input("enter the number of days:")
if days == 0 and days == 7:
    print("monday")
elif days == 1 and days ==7:
    print("tuesday")
elif days == 2 and days ==3:
    print("wednesday")
else:
    print("weekdays")



