def mainfuntion():
    print("Kodaikkanal pakage ")
    print("ooty pakage")

    def kodaikkanal():
        print("Kodaikkanal is 5k per person 3days")
        exit=input("Do you want to cotinue press yes:")
        if exit=="yes":
            mainfuntion()
        else:
            print("Thanks for Visting")
    kodaikkanal
mainfuntion

print("Welcome to Green Trends beauty saloon")


def main():
    
    def menu():
        print("*********MenuList****************")
        print("HairCut","Facial","Medicure","Pedicure","HairSmoothing","Waxing","EyeBrow Triming")
        print("*********************************")
    menu()
    def typelist():
        print("***********Which You Want*************")   
        print("For Haircut Type:1")
        print("For Facial Type:2")
        print("For Medicure Type:3")
        print("For Pedicure Type:4")
        print("For HairSmooting Type:5")
        print("For Waxing  Type:6")
        print("For EyeBrow Triming Type:7")
        print("***********************************")
        user_value=int(input("Enter the Number:"))
        if user_value==1:
            haircut()      
        elif user_value==2:
            facial()
        elif user_value==3:
            medicure()
        elif user_value==4:
            pedicure()
        elif user_value==5:
            hairsmoothing()
        elif user_value==6:
            waxing()
        elif user_value==7:
            eyebrowtrimming()
        else:
            print("Thanks You Visit Again")
            
    def haircut():
        print("Types Of Hair You Want")
        print("1:Stepcut")
        print("2:Layercut")
        print("3:U Cut")
        print("4:V Cut")
        print("5:Hair Cut")
        
        user_value=int(input("Enter the Number:"))
        if user_value==1:
            print("For Stepcut Rs:300")
            stepcut_amt=300
        elif user_value==2:
            print("For Layercut Rs:400")
            layercut_amt=400
        elif user_value==3:
            print("For U Cut Rs:600")
            ucut_amt=600
        elif user_value==4:
            print("For V Cut Rs:750")
            vcut_amt=750
        elif user_value==5:
            print("For Haircut Rs:100")
            haircut_amt=100
            
        mainmenu=input("For MainMenu Please Type **Yes**:")
        if mainmenu=="yes":
            menu()
            typelist()
        else:
            print("Thanks For Visting Us ")   
    def facial():
        print("Type's of Facial ")
        print("1:Charcoal Facial")
        print("2:Fruit Facial")
        print("3:Papaya Facial")
        user_value=int(input("Enter the Number:"))
        if user_value==1:
            print("For Charcoal Facial Rs:700")
            charcoal_amt=700
        elif user_value==2:
            print("For Fruit Facial Rs:2000")
            fruitfacial_amt=2000
        elif user_value==3:
            print("For Papaya Facial Rs:2900")
            papayafacial_amt=2900
        mainmenu=input("For MainMenu Please Type **Yes**:")
        if mainmenu=="yes":
            menu()
            typelist()
        else:
            print("Thanks For Visting Us ") 

    def medicure():
        print("For Medicure Rs:500")   
        medicure_amt=500
        mainmenu=input("For MainMenu Please Type **Yes**:")
        if mainmenu=="yes":
            menu()
            typelist()
        else:
            print("Thanks For Visting Us ")
    def pedicure():
        print("For Pedicure Rs:700") 
        pedicure_amt=700
        mainmenu=input("For MainMenu Please Type **Yes**:")
        if mainmenu=="yes":
            menu()
            typelist()
        else:
            print("Thanks For Visting Us ")
    def hairsmoothing():
        print("For Hairsmoothing Rs:1500")
        hairsmoothing_amt=1500
        mainmenu=input("For MainMenu Please Type **Yes**:")
        if mainmenu=="yes":
            menu()
            typelist()
        else:
            print("Thanks For Visting Us ")
    def waxing():
        print("1:Leg Waxing")
        print("2:Hand Waxing")
        user_value=int(input("Enter the Number"))
        if user_value==1:
            print("For Leg Waxing Rs:800")
            legwaxing_amt=800
        elif user_value==2:
            print("For HandWaxing Rs:1300")
            handwaxing_amt=1300
        mainmenu=input("For MainMenu Please Type **Yes**:")
        if mainmenu=="yes":
            menu()
            typelist()
        else:
            print("Thanks For Visting Us ")
    def eyebrowtrimming():
        print("For Eyebrowtrimming Rs:790")
        eyebrowtrimming_amt=790
        mainmenu=input("For MainMenu Please Type **Yes**:")
        if mainmenu=="yes":
            menu()
            typelist()
        else:
            print("Thanks For Visting Us ")
    typelist()
main()

        