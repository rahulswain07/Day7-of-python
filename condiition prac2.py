# check triangle validity 
#Q.input 3 angles and check if they from a valid triangle( sum must be 180 degree)
angle1=int(input("Enter angle one :"))
angle2=int(input("Enter angle two :"))
angle3=int(input("Enter angle three :"))
angle_sum=angle1+angle2+angle3
if angle_sum==180:
    print('triangle is valid')
else:
    print("triangle is not valid")
