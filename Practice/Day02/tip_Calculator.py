total_Bill = int (input ("please insert your total bill with tip?"))
numberOfPeople = int (input ("please insert the number of consumers?"))

def split_bill (total_bill,numberOfPeople,tiprate=0.10):
    result = (total_Bill/numberOfPeople)
    tip = result * tiprate
    totalsharedbill =result + tip
    return totalsharedbill

bill =split_bill(total_Bill,numberOfPeople)

while numberOfPeople > 0:
    customer = input ("Please insert customer name?")
    print (f"The payment for {customer} is, {bill}")
    numberOfPeople -= 1
    
