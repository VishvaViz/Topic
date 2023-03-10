print("**************WELCOME TO HOTEL*************")

menus=["dhosa","idly","parotta","pizza","burger"]
print("***********Available menus dosa,idly,parota,pizza,burger*****")

dhosa_amt=50
idly_amount=20
parotta_amt=20
pizza_amt=200
burger_amt=100

user_order=input("Enter Your Order:").lower()

if user_order in menus:
    print(f"{user_order}is avaiable")
    how_many=int(input(f"How many{user_order}you want:"))
    if user_order=="dhosa":
        total=dhosa_amt*how_many
        print(f"one dhosa is rs 50\n you ordered {how_many} dhosa's\n,your total bill is {total}")
        if total>=1000:
            print("reduce 200 rupees for diwali offer")
            offer_amt=total-200
            print(f"final total is {offer_amt}")
    elif user_order=="idly":

        total=idly_amount*how_many
        print(f"one idly amount is rs20 \nyou orded is {how_many}idly's\n,your bill is {total}")
        if total>=1000:
            print("reduce 200 for diwali offer")
            offer_amt=total-200
            print(f"final total is {offer_amt}")
            
else:
    print(f"{user_order}is not available now")       
    
