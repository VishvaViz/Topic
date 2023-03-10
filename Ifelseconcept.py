print("***************WELCOME TO THE FRASHER DAY orIENTATION***********")
department=str(input("Enter the Department:"))
db_department1="mca"
db_department2="bca"
db_department3="staff"
db_department4="vendor"
db_department5="others"

if department==db_department1 or department==db_department2 or department==db_department3 or department==db_department4:
    print(f"*******Welcome{department}Guy************")
    if department==db_department1:
        print("MCA Department is in the 1st Floor")
        year=str(input("Enter the Your Year:"))
        mca_year1="firstyear"
        mca_year2="secondyear"
        mca_year3="thirdyear"
        if year==mca_year1 or department==db_department1:
            print=("First Floor 1st Class")
        elif department==db_department2 or department==db_department3 or department==db_department4 or department==db_department5:
            print("See the route map in the orice board")
        if year==mca_year2 or department==db_department1:
            print("First Floor 2nd Class")
        elif department==db_department2 or department==db_department3 or department==db_department4 or department==db_department5:
            print("See the route map in the orice board")
        if year==mca_year3 or department==db_department1:
            print("First Floor Last Class")
        elif department==db_department2 or department==db_department3 or department==db_department4 or department==db_department5:
            print("See the route map in the orice board") 
    elif department==db_department2 or department==db_department3 or department==db_department4 or department==db_department5:
        print("Get Clarify with the Receiption")
    if department==db_department2:
        print("BCA Department is in the 2nd Floor")
        year=str(input("Enter the Year"))
        bca_year1="firstyear"
        bca_year2="secondyear"
        bca_year3="thirdyear"
        if year==bca_year1 or department==db_department2:
            print("Second Floor 1st Class")
        elif department==db_department1 or department==db_department3 or department==db_department4 or department==db_department5:
            print("See the route map in the orice borad")
        if year==bca_year2 or department==db_department2:
            print("Second Floor 2nd Class")
        elif department==db_department1 or department==db_department3 or department==db_department4 or department==db_department5:
            print("See the route map in the orice borad")
        if year==bca_year3 or department==db_department2:
            print("Second Floor Last Class")
        elif department==db_department1 or department==db_department3 or department==db_department4 or department==db_department5:
            print("See the route map in the orice borad")
    elif department==db_department1 or department==db_department3 or department==db_department4 or department==db_department5:
        print("Get Clarify with the Receiption")
    if department==db_department3:
        print("Staff Room is in the 3rd Floor")
    elif department==db_department1 or department==db_department2 or department==db_department4 or department==db_department5:
        print("Get Clarify with the Receiption")
    if department==db_department4:
        print("Vendor Rooms are there in the basement")
    elif department==db_department1 or department==db_department2 or department==db_department3 or department==db_department5:
        print("Get Clarify with the Receiption")
    if department==db_department5:
        print("Wait in the Vistor Lounge")
    else:
        print("Contact The Authority")       
else:
    print("********Sorry Wait**********")