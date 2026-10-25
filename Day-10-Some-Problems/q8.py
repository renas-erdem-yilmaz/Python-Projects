h = int(input("Departure Hour: "))
m = int(input("Departure Minute: "))
t = int(input("Duration: "))
d = int(input("Delay: "))

landinghour = h + (t+d)//60
landingminute = m + (t+d)%60

if landingminute >= 60:
    landingminute -= 60
    landinghour += 1

if landinghour >= 24:
    landinghour -= 24

print(landinghour, landingminute)
