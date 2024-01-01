"""
Project Name  : Shopping Cart Project
Developer     : Tharun
Date          : 29-12-2023
Description   : In this project we are going to built the customer's online retail shopping list by using tasks like create the products, add to cart, customize cart, apply discount & get the bill
Version       : v1.8
"""
global cart
cart=[]
def e_shopping():
    print("="*50)
    print("\t******Shopping Cart******") 
    print("="*50)
    print("1. Create Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Edit cart")
    print("5. Clear Cart")
    print("6. Apply Discount")
    print("7. Get the Bill")
    print("8. Purchase Date")
    print("9. Number of Visits")
    print("-"*50)

def select_products():
     try:
          product = input("Enter the product details: ")
          quantity = int(input("Enter the number of products required: "))
          price = int(input("Enter the amount for the product: "))
          expiry_date = input("Enter the expiry date of the product [YYYY-MM-DD]:")
          cart.append({"Product_Name":product,"Quantity":quantity,"Total_Amount":price,"Validity":expiry_date})
          print("The prodcuts have been choosen successfully")
          print("-"*50)
          verify=input("Do you want to check the product details [yes or no]:")
          if verify.lower()=='yes':
               # print(cart)
               view_cart()
     except ValueError:
          print("Please do enter valid information")

def add_to_cart():
     try:
        cart.append({"select_products"})
        print("The selection of the product has been successful")
        verify=input("Want to re-check the product details:")
        if verify.lower() == "yes":
                print(cart)
     except ValueError:
        print("Please Enter the Valid Information")

def view_cart():
     i=1
     if not cart:
          print("No items present in the cart")
     else:
          for itm in cart:
               print("---------------------")
               print("Product:",i,"Details")
               print("---------------------")
               for key,value in itm.items():
                    print(f"{key}\t-->\t{value}")
          i=i+1

def discount():
     print("="*50)
     print("\t****The Discount offers are as Mentioned Below: ")
     print("="*50)
     print("1. For Purchase greater than Rs.10,000, 40% discount")
     print("2. For purchase ranging between Rs.7,001 to Rs.10,000, 30% discount")
     print("3. For purchase ranging between Rs.4,001 to Rs.7,000, 20% discount")
     print("4. For purchase ranging between Rs.1,001 to Rs.4,000, 10% discount")
     print("5. For purchase ranging between Rs.500 to Rs.1,000, 5% discount")
     print("-"*50)
     purchase_amount=int(input("Enter your total purchase amount [positive number] ]: "))
     if purchase_amount<=499:
          print("Sorry, no discounts available on your purchase amount")
     elif purchase_amount>=500:
          if purchase_amount>10000:
               print("The discount you avail on this purchase is:", (40/100)*purchase_amount)
          elif 10000<=purchase_amount>7000:
               print("The discount you avail on this purchase is:",(30/100)*purchase_amount)
          elif 7000<=purchase_amount>4000:
               print("The discount you avail on this purchase is:",(20/100)*purchase_amount)
          elif 4000<=purchase_amount>1000:
               print("The discount you avail on this purchase is:",(10/100)*purchase_amount)
          else:
               print("The discount you avail on this purchase is:",(5/100)*purchase_amount)

def purchase_bill():
     purchase=int(input("Enter the amount of purchase you made [positive number]:"))
     if purchase>=500:
          print("The final bill amount on your purchase after applying the discount is:", purchase)
     elif 10000<=purchase>7000:
          print("The final bill amount on your purchase after applying the discount is:", purchase-(40/100)*purchase)
     elif 7000<=purchase>10000:
          print("The final bill amount on your purchase after applying the discount is:", purchase-(30/100)*purchase)
     elif 4000<=purchase>7000:
          print("The final bill amount on your purchase after applying the discount is:", purchase-(20/100)*purchase)
     elif 1000<=purchase>4000:
          print("The final bill amount on your purchase after applying the discount is:", purchase-(10/100)*purchase)
     elif 1000<=purchase>500:
          print("The final bill amount on your purchase after applying the discount is:", purchase-(5/100)*purchase)

def purchase_date():
     date=int(input("Enter the date of your purchase [date-month-year]: "))
     print("The date of your purchase is: ", date)

def no_of_vists():
     visits = int(input("Enter your number of visits: "))
     print("The number of visits:", visits)

def edit_cart():
     print("="*50)
     print("\t******Edit Your Cart******") 
     print("="*50)
     print("1. Create Products")
     print("2. Add to Cart")
     print("3. View Cart")
     print("4. Apply Discount")
     print("5. Get the Bill")
     print("6. Purchase Date")
     print("7. Number of Visits")
     print("8. Clear Cart")
     print("-"*50)
     choice=int(input("Enter your choice of Edit: "))
     try:
          if choice==1:
               select_products()
          elif choice==2:
               add_to_cart()
          elif choice==3:
               view_cart()
          elif choice==4:
               discount()
          elif choice==5:
               purchase_bill()
          elif choice==6:
               purchase_date()
          elif choice==7:
               no_of_vists()
     except ValueError:
          print("Please do enter valid information")


def main():
     e_shopping()
     option=int(input("Enter your option: "))
     if option==1:
          select_products()
     elif option==2:
          add_to_cart()
     elif option==3:
          view_cart()
     elif option==4:
          discount()
     elif option==5:
          purchase_bill()
     elif option==6:
          purchase_date()
     elif option==7:
          no_of_vists()
     elif option==8:
          print("Erasing the existing data from your data base: ")
          cart.clear()
     continuestate=input("\n Do you want to continue Again(Y or N ):")
     if continuestate=='Y' or continuestate=='y':
          main()
     elif continuestate == 'N' or continuestate=='n':
          print("Thank you, Visit Again")

if "__init__"==main():
     main()

        
