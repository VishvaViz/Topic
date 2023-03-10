print("********** WECOLME TO ABC CRACKERS*********")
menus1=["bigily","yanai","atomboom","laskmi","kuruvi",]
menus2=["flowerpot","chakaras","rocket","sprinkes","matches",]
print(f"****** AVAILABLE CRACKERS ARE {menus1}{menus2}**********")


bigily_amt=100
yanai_amt=300
atomb_amt=500
laskmi_amt=600
kuruvi_amt=800

flowerpot_amt=700
chakaras_amt=900
sprinkes_amt=1000
matches_amt=20
rocket_amt=400

user_order=str(input("Enter your order"))
if user_order in menus1 or menus2:
    print("**1 Day Time Crackers**")
    print("**2 Night Time Cracker")
    choose=int(input("Select the Crakers Which Type  You want:"))
    if choose==1:
        print(f"Day Time Crackers Are{menus1}")
        user_choose=str(input("Enter Which Cracker you want:"))
        how_many=int(input("Enter how many you want:"))
        if user_choose=="bigily":
            total_amt=how_many*bigily_amt
            print(f"One Bigily Box is 100\n You Ordered{how_many} Bigily's\n Your Total Bill is:{total_amt} ")
            if total_amt>=1000:
                print("Reduce 300 for diwali offer")
                offer_amt=total_amt-300
                print(f"Your Total Bill is :{offer_amt}")
        elif user_choose=="yanai":
            total_amt=how_many*yanai_amt
            print(f"One Yanai is 300\n You Ordered is {how_many}Yanai's\n Your Total Bill is:{total_amt}")
            if total_amt>=1000:
                print("Reduced 300 for diwali offer")
                offer_amt=total_amt-300
                print(f"Your Total Bill is:{offer_amt}")
        elif user_choose=="atomboom":
            total_amt=how_many*atomb_amt
            print(f"One AtomBoom is 500\n You Ordered is{how_many} Atomboom's\n Your Total Bill is:{total_amt} ")
            if total_amt>=1000:
                print("Reduced 300 for diwali offer")
                offer_amt=total_amt-300
                print(f"Your Total Bill is{offer_amt}")
        elif user_choose=="laksmi":
            total_amt=how_many*laskmi_amt
            print(f"One Laksmi 600 \nYou Ordered is {how_many} Laksmi's\n Your Total Bill is:{total_amt}")
            if total_amt>=1000:
                print("Reduced 300 For diwali Offer")
                offer_amt=total_amt-300
                print(f"Your Total bill is:{offer_amt}")
        elif user_choose=="kuruvi":
            total_amt=how_many*kuruvi_amt
            print(f"One Kuruvi is 800\nYou Orderded is {how_many} Kuruvi's\nYour Total Bill is :{total_amt}")
            if total_amt>=1000:
                print("Reduced 300 For diwali offer")
                offer_amt=total_amt-300
                print(f"Your Total Bill is:{offer_amt}")        
 
    elif choose==2:
        print(f"Night Time Cracker Are:{menus2}")
        user_choose=str(input("Enter Which Cracker you want:"))
        how_many=int(input("Enter how many you want"))
        if user_choose=="flowerpot":
            total_amt=how_many*flowerpot_amt
            print(f"One Flowerpot is Box is {flowerpot_amt}\n You Ordered{how_many} Flowerpot's\n Your Total Bill is:{total_amt} ")
            if total_amt>=1000:
                print("Reduce 300 for diwali offer")
                offer_amt=total_amt-300
                print(f"Your Total Bill is :{offer_amt}")
        elif user_choose=="chakaras":
            total_amt=how_many*chakaras_amt
            print(f"One  is 300\n You Ordered is {how_many}Yanai's\n Your Total Bill is:{total_amt}")
            if total_amt>=1000:
                print("Reduced 300 for diwali offer")
                offer_amt=total_amt-300
                print(f"Your Total Bill is:{offer_amt}")
        elif user_choose=="rocket":
            total_amt=how_many*rocket_amt
            print(f"One Rocket  is{rocket_amt}\n You Ordered is{how_many} OneRocket's\n Your Total Bill is:{total_amt} ")
            if total_amt>=1000:
                print("Reduced 300 for diwali offer")
                offer_amt=total_amt-300
                print(f"Your Total Bill is{offer_amt}")
        elif user_choose=="sprinkes":
            total_amt=how_many*sprinkes_amt
            print(f"One Sprinkes is {sprinkes_amt} \nYou Ordered is {how_many} Sprinkes's\n Your Total Bill is:{total_amt}")
            if total_amt>=1000:
                print("Reduced 300 For diwali Offer")
                offer_amt=total_amt-300
                print(f"Your Total bill is:{offer_amt}")
        elif user_choose=="matches":
            total_amt=how_many*matches_amt
            print(f"One Matches is {matches_amt}\nYou Orderded is {how_many} Matches's\nYour Total Bill is :{total_amt}")
            if total_amt>=1000:
                print("Reduced 300 For diwali offer")
                offer_amt=total_amt-300
                print(f"Your Total Bill is:{offer_amt}")
else:
    print("Your Order is Not Available")











