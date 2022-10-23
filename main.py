print("Utility Bill Calculator")
print("1.Electricity")
print("2. Water")

bill = int(input("Enter the type of bill you want to calculate: "))

if bill == 1:
        amount = int(input("Enter your electric meter reading in kwH: "))
        print('Calculating Electricity bill...')

        if amount <= 100:
            bill_rate = amount * 5
            print('Your total Electricity bill is $',bill_rate )
        
        elif amount > 100 and amount <= 1000:
            bill_rate = amount * 5
            print('Your total Electricity bill is $',bill_rate )
           
        elif amount > 1000:
            bill_rate = amount * 5
            print('Your total Electricity bill is $',bill_rate )

if bill == 2:
    try:
          amount = int(input("Enter your water meter reading in m^3: "))
          print('Calculating Water bill...')
          
          if amount <= 500:
            bill_rate = amount * 50
            print('Your total Electricity bill is $',bill_rate )
          
          elif amount > 500 and amount <= 2500:
            bill_rate = amount * 60
            print('Your total Electricity bill is $',bill_rate )
          
          elif amount > 2500:
            bill_rate = amount * 70
            print('Your total Electricity bill is $',bill_rate )
    
            
    except:
          print('Error: Please enter a numerical meter reading')

else:
      print('Error: enter a number to choose a bill type from the list')

# Electricity Unit Price
# TODO: Define electricity price constants here

# Water Unit Price
# TODO: Define Water price constants here

# Implementation

# Input 1 Validation
# TODO: get the bill type from user
# TODO: check if bill type is valid

# Input 2 Validation
# TODO: get the meter reading from the user
# TODO: check if meter reading is valid

# Bill Calculation
# TODO: calculate and display the bill

