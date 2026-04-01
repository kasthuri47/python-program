a=int(input("enter side 1:"))
b=int(input("enter side 2:"))
c=int(input("enter side 3:"))

if a+b>c and a+c>b and b+c>a:
    if a== b == c:
        print("equilateral triangle")
    elif a == b or b == c or a==c:
        print("isosceles triangle")
    else:
        print("scalene triangle")
else:
    print("not a valid triangle")
    
