import json

def main():

    api_data='{"chennai":"30c","mumbai":"46c"}'

    my_data=json.loads(api_data)

    user=input("Enter the city:")
    
    print(my_data[user])
main()