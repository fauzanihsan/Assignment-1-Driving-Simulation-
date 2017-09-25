time_spent = int(input("Input the time spent on the road :"))
acceleration = int(input("Input the acceleration :"))
distance = int(input("Input the distance :"))

velocity = 0 + (time_spent*acceleration)
distance = 0 + (acceleration*time_spent*time_spent)/2
distance = (time_spent*(velocity + 0))/2
velocity2 = (2*acceleration*distance)
dist = (acceleration*time_spent*time_spent)/2



if velocity > 60 :
    print("The person went over the speed limit", velocity, "m/s")
else :
    print("The person did not go over the speed limit", velocity, "m/s")
if distance > dist :
    print("The person reached the destination", distance, "m")
else :
    print("The person did not reached the destination", distance, "m")

for i in range (0, time_spent+1):
    print("duration",i)
    velocity= acceleration*i
    distance=1/2*i*velocity
    print("distance:", "*"*int(distance/10))

if distance >= dist:
    print("The person reached the destination")
else:
    print("The person did not reached the destination")











