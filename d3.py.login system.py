username=input("enter username:")
password=input("enter password:")

if username=="admin":
    if password=="1234":
        print("login successful")
    else:
        print("wrong password")
else:
    print("invalid username")
        
