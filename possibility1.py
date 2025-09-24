# List of Rwanda's provinces
weather = "Today in Rwanda"
print(weather)
provinces = ("Kigali", "Northern", "Southern", "Eastern", "Western")
nationality = ("rwanda")
print(provinces)
def login():
    province = input("\nselect your province : ")
    nationality = input("Enter your nationality :")
    if nationality == "rwanda":
        return  " welcome to " + province + " weather forecast news today"
    else:
        return ("access denied. please make sure your nationality is rwanda")
print(login())
              
