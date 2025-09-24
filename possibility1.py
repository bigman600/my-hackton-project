# List of Rwanda's provinces
provinces = ["Kigali", "Northern", "Southern", "Eastern", "Western"]
nationality =( "rwanda")
def login():
    province =input ("\nselect your province : ")
    nationality = input("Enter your nationality :")
    if nationality != "rwanda":
        print("welcome to weather today! ")
        return True
    else:
        print("access denied. please make sure your nationality is rwanda")
              