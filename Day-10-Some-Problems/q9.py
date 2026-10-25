d = int(input("Distance: "))
a = int(input("Order amount: "))
m = int(input("Membership flag (yes or no): "))

if (not 1<=d<=100) or a<0:
    print("Invalid input")
else:
    base_fee = 0
    if d<= 3:
        base_fee = 20
    elif 4<=d<=10:
        base_fee = 20 + (d-3)*5
    elif d>10:
        base_fee = (d-10)*8 + 55
        
    if a>= 300:
        base_fee -= 10
    
    if m == 1:
        base_fee *= 0.8
    
    if base_fee <= 5:
        base_fee = 5
    
    print("Fee:", round(base_fee, 2))
    
    
