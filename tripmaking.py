print("********** WELCOME TO TRIPMAKING*********")
menus1=["kerala","bangalore","goa","kasmir","dheli"]
menus2=["madurai","tricy","poundicherry","tanjavur","rajapalaiyam"]
print(f"****** AVAILABLE TRIPS ARE {menus1}{menus2}**********")


kerala_amt=5000
bangalore_amt=2500
goa_amt=7000
kasmir_amt=100000
dheli_amt=8000

madurai_amt=10000
tricy_amt=1500
poundicherry_amt=20000
tanjavur_amt=1700
rajapalaiyam_amt=2200

user_order=str(input("Enter The Place:"))
if user_order in menus1 or menus2:
    print("**1 Other State Over India **")
    print("**2 Other District Over Tamilnadu")
    choose=int(input("Select Which Location You Want To Go:"))
    if choose==1:
        print(f"Other State Over India{menus1}")
        user_choose=str(input("Enter Where You Want To Go:"))
        how_many=int(input("Enter how many you ticket you want:"))
        if user_choose=="kerala":
            total_amt=how_many*kerala_amt
            print(f"One kerala Box is 100\n Your Ticket Rate is{how_many} kerala's\n Your Total Bill is:{total_amt} ")
            if total_amt>=10000:
                print("Reduce 2000 for diwali offer")
                offer_amt=total_amt-2000
                print(f"Your Total Bill is :{offer_amt}")
        elif user_choose=="bangalore":
            total_amt=how_many*bangalore_amt
            print(f"One bangalore is 2000\n Your Ticket Rate  is {how_many}bangalore's\n Your Total Bill is:{total_amt}")
            if total_amt>=10000:
                print("Reduced 2000 for diwali offer")
                offer_amt=total_amt-2000
                print(f"Your Total Bill is:{offer_amt}")
        elif user_choose=="goa":
            total_amt=how_many*goa_amt
            print(f"One goa is 500\n Your Ticket Rate  is{how_many} goaoom's\n Your Total Bill is:{total_amt} ")
            if total_amt>=10000:
                print("Reduced 2000 for diwali offer")
                offer_amt=total_amt-2000
                print(f"Your Total Bill is{offer_amt}")
        elif user_choose=="laksmi":
            total_amt=how_many*kasmir_amt
            print(f"One Laksmi 600 \nYour Ticket Rate  is {how_many} Laksmi's\n Your Total Bill is:{total_amt}")
            if total_amt>=10000:
                print("Reduced 2000 For diwali Offer")
                offer_amt=total_amt-2000
                print(f"Your Total bill is:{offer_amt}")
        elif user_choose=="dheli":
            total_amt=how_many*dheli_amt
            print(f"One dheli is 800\nYour Orderded is {how_many} dheli's\nYour Total Bill is :{total_amt}")
            if total_amt>=10000:
                print("Reduced 2000 For diwali offer")
                offer_amt=total_amt-2000
                print(f"Your Total Bill is:{offer_amt}")        
 
    elif choose==2:
        print(f"Other District Over Tamilnadu:{menus2}")
        user_choose=str(input("Enter Where You Want To Go:"))
        how_many=int(input("Enter how many ticket you want"))
        if user_choose=="madurai":
            total_amt=how_many*madurai_amt
            print(f"One madurai is Box is {madurai_amt}\n Your Ticket Rate is{how_many} madurai's\n Your Total Bill is:{total_amt} ")
            if total_amt>=10000:
                print("Reduce 2000 for diwali offer")
                offer_amt=total_amt-2000
                print(f"Your Total Bill is :{offer_amt}")
        elif user_choose=="tricy":
            total_amt=how_many*tricy_amt
            print(f"One  is 2000\n Your Ticket Rate  is {how_many}bangalore's\n Your Total Bill is:{total_amt}")
            if total_amt>=10000:
                print("Reduced 2000 for diwali offer")
                offer_amt=total_amt-2000
                print(f"Your Total Bill is:{offer_amt}")
        elif user_choose=="rajapalaiyam":
            total_amt=how_many*rajapalaiyam_amt
            print(f"One rajapalaiyam  is{rajapalaiyam_amt}\n Your Ticket Rate is is{how_many} Onerajapalaiyam's\n Your Total Bill is:{total_amt} ")
            if total_amt>=10000:
                print("Reduced 2000 for diwali offer")
                offer_amt=total_amt-2000
                print(f"Your Total Bill is{offer_amt}")
        elif user_choose=="poundicherry":
            total_amt=how_many*poundicherry_amt
            print(f"One poundicherry is {poundicherry_amt} \nYour Ticket Rate is is {how_many} poundicherry's\n Your Total Bill is:{total_amt}")
            if total_amt>=10000:
                print("Reduced 2000 For diwali Offer")
                offer_amt=total_amt-2000
                print(f"Your Total bill is:{offer_amt}")
        elif user_choose=="tanjavur":
            total_amt=how_many*tanjavur_amt
            print(f"One tanjavur is {tanjavur_amt}\nYour Orderded is {how_many} tanjavur's\nYour Total Bill is :{total_amt}")
            if total_amt>=10000:
                print("Reduced 2000 For diwali offer")
                offer_amt=total_amt-2000
                print(f"Your Total Bill is:{offer_amt}")
else:
    print("Ticket  is Not Available")

