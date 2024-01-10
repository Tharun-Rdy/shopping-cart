"""
Project Name  : Shopping Cart Project using exception handling and data types like list and dictionary
Developer     : Tharun
Date          : 10-01-2023
Description   : In this project we are going to built the customer's online retail shopping details by using tasks like
                1. Creating the User
                2. Login to the Application
                3. create the products 
                4. add to cart 
                5. View cart
                6. apply discount 
                7. get the bill
                8. Purchase Date
                9. Number of Visits
                10. Return the Product
                11. Edit the Cart
                12. Clear the Cart
                13. Exit Shopping
Version       : v2.0
"""
global cart
cart=[]
def e_shopping():
    print("="*50)
    print("\t******Shopping Cart******") 
    print("="*50)
    print("1. Creating User")
    print("2. Login into the App")
    print("3. Create Products")
    print("4. Add to Cart")
    print("5. View Cart")
    print("6. Apply Discount")
    print("7. Get the Bill")
    print("8. Purchase Date")
    print("9. No of visits")
    print("10. Return the product")
    print("11. Edit cart")
    print("12. Clear Cart")
    print("13. Exit the shopping")
    print("-"*50)

user_details=[]
def create_user():
     try:
          new_user=input("Enter whether you are new user or not [yes/no]: ")
          if new_user.lower()=="no":
               print("please do click on the login button: ")
               login()
          else:
               print("Please do register your account details: ")
               first_name=input("Enter your first Name: ")
               last_name=input("Enter your last name: ")
               mobile_no = int(input("Enter your mobile number: "))
               email = input("Enter your email id: ")
               user_details.append({'First Name':first_name, 'Last Name':last_name, 'Phone Number':mobile_no, 'Email Id':email})
               print("please do click on the register button ")
               print("Congrats, Your user account has been created successfully")
               user_login=input("Enter whether you want to login to your account or not [yes/no]: ")
               if user_login.lower()=='yes':
                    login()
               else:
                    main()
     except ValueError:
          print("Please do enter valid details")

def login():
     try:
          user=input("Enter whether you are existing user or not [yes/no]: ")
          if user.lower()=='no':
               print("Please do register your account details first: ")
               create_user()
          else:
               print("Please do login with your credentials")
               user_name=input("Enter your user name: ")
               password=input("Enter your password: ")
               user_details.append({'User Name':user_name, 'Password':password})
               print("You're login has been successful ")
               continue_state=input("Do you want to visit the products on the site [yes/no]: ")
               if continue_state.lower()=="yes":
                    select_products()
               else:
                    main()
     except ValueError:
          print("Please do enter valid details")


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
               main()
     except ValueError:
          print("Please do enter valid information")

def add_to_cart():
     try:
        cart.append({"select_products"})
        print("The selection of the product has been successful")
        verify=input("Want to re-check the product details:")
        if verify.lower() == "yes":
                print(cart)
                main()
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
          main()

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
     main()

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
     main()

def purchase_date():
     date=int(input("Enter the date of your purchase [date-month-year]: "))
     print("The date of your purchase is: ", date)
     main()

def no_of_vists():
     visits = int(input("Enter your number of visits: "))
     print("The number of visits:", visits)
     main()

def return_product():
     return_back=input("Enter whether you want to return back the product or not[yes/no]: ")
     if return_back.lower=='yes':
          reason_of_return=input("Select an option given below for the return of the product: ")
          print("wrong product delivered")
          print("Damaged product delivered")
          print("You find better product or price")
          print("product is of poor quality")
          print("Not sastisified with the product delivered")
          if reason_of_return==True:
               print("Your product will be collelcted by amazon agent within short time")
          else:
               print("Sorry, we cannot return back the product")
          main()

def edit_cart():
     print("="*50)
     print("\t******Edit Your Cart******") 
     print("="*50)
     print("1. Creating User")
     print("2. Login into the App")
     print("3. Create Products")
     print("4. Add to Cart")
     print("5. View Cart")
     print("6. Apply Discount")
     print("7. Get the Bill")
     print("8. Purchase Date")
     print("9. No of visits")
     print("10. Return the product")
     print("-"*50)

     choice=int(input("Enter your choice of Edit: "))
     try:
          if choice==1:
               create_user()
          elif choice==2:
               login()
          elif choice==3:
               select_products()
          elif choice==4:
               add_to_cart()
          elif choice==5:
               view_cart()
          elif choice==6:
               discount()
          elif choice==7:
               purchase_bill()
          elif choice==8:
               purchase_date()
          elif choice==9:
               no_of_vists()
          elif choice==10:
               return_product()
     
     except ValueError:
          print("Please do enter valid information")
     main()

def main():
     e_shopping()
     option=int(input("Enter your option: "))
     if option==1:
          create_user()
     elif option==2:
          login()
     elif option==3:
          select_products()
     elif option==4:
          add_to_cart()
     elif option==5:
          view_cart()
     elif option==6:
          discount()
     elif option==7:
          purchase_bill()
     elif option==8:
          purchase_date()
     elif option==9:
          no_of_vists()
     elif option==10:
          return_product()
     elif option==11:
          edit_cart()
     elif option==12:
          print("Erasing the existing data from your data base: ")
          cart.clear()

def exit_shopping():
     shopping=True
     while shopping:
          e_shopping
          continue_shopping=input("\n Do you want to continue the shopping(yes or no ):")
          if continue_shopping.lower()=='yes' :
               main()
          else:
               print("Thank you for shopping with us, Please do Visit Again")
               shopping=False

if "__init__"==main():
     main()

        
