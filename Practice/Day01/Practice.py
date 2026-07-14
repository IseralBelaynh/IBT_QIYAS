#Exercise 1 Temprature lable 

Temprature = float(input("Enter Temprature in celsius:"))
if Temprature < 15:
    print("Cold")
elif Temprature >= 15 and Temprature < 28:
    print("Normal")
else:
    print("Hot")

#Exercise 2 Recipit loop

RecipitNumeber = {1, 2, 3, 4, 5, 6, 7, 8, 9,10}
for i in RecipitNumeber:
    print("Recipit Number:", i)

#Exercise Even numbers 

number = {1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20}
for i in number:
    if i % 2 == 0:
        print("Even Number:", i)

#Exercise Discount Fusnction

def apply_discount (price, percentage = 10):
    return price - (price * percentage / 100)

price= float(input("Enter the price: "))
discounted_price = apply_discount(price)
print(f"The discounted price is {discounted_price}")

#Exercise 5 Countdown loop
n=0
while n< 5:
    print ("number:", 1+n)
    n+=1