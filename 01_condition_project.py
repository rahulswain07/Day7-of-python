#Q.Movie Ticket based on age
age=int(input("Enter your age :"))
if age<=5:
    print("Free")
elif age >5 and age<=18:
    print("$50")
elif age >18 and age<=60:
    print("$100")
elif age>60:
    print("$70")
