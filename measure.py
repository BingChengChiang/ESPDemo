import math
import time
from SerialCapture import UWB3000Serial
from Circle import Circle



FORWARD = 0.3
TURN = 30
PUSH = 2
RADIUS = 0.5

clockwise_flag = True

def calculate_dist(a, b, c):
    # 使用余弦定理計算角A
    cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
    sin_B = math.sqrt(1 - cos_B**2)
    
    # 計算角度（以弧度為單位）
    angle_B = math.acos(cos_B)
    
    # 轉換弧度為角度
    # angle_degrees = math.degrees(angle_B)
    
    # 計算外角
    # external_angle = 180 - angle_degrees

    normal_dist = c * sin_B
    tangential_dist = -c * cos_B
    
    return (tangential_dist, normal_dist)



ser = UWB3000Serial('/dev/ttyUSB0',115200)
ser.reset_input_buffer()

input("Press enter to start process")

time.sleep(1)
side_b = float(ser.read_distance())
input("Go Forward " + str(PUSH) +" steps then press enter")

time.sleep(1)
side_c = float(ser.read_distance())
input("Press enter")

(tangential_dist, normal_dist) = calculate_dist(PUSH*FORWARD, side_b, side_c)
print("Go forward in meter: ", tangential_dist)
print("Normal in meter: ", normal_dist)
# go tangential distance
input("go forward " + str(round(tangential_dist/FORWARD)) + " steps then press enter")

# try turn right
input("turn right then press enter")

print("measuring...")
time.sleep(1)
dist1 = float(ser.read_distance())
print("distance test 1 = ", dist1, " m")
input("back 2 steps then press enter")

print("measuring...")
time.sleep(1)
dist2 = float(ser.read_distance())
print("distance test 2= ", dist2, " m")
input("2 steps forward and press enter")

if dist2 < dist1:
    clockwise_flag = False
    print('you have opposite direction')
    print('U turn and press enter')
else:
    print("you have correct direction")


# go normal distance
input("go forward " + str(round(normal_dist/FORWARD)-1) + " steps then press enter")


while True:
    radius = float(ser.read_distance())
    if radius <= RADIUS:
        break

    else:
        time.sleep(1)
        side_b = float(ser.read_distance())
        input("Go Forward 1 step then press enter")

        time.sleep(1)
        side_c = float(ser.read_distance())
        input("Press enter")
        
        (tangential_dist, normal_dist) = calculate_dist(FORWARD, side_b, side_c)
        print("Go forward in meter: ", tangential_dist)
        print("Normal in meter: ", normal_dist)
        # go tangential distance
        input("go forward " + str(round(tangential_dist/FORWARD)) + " steps then press enter")
       
        #turn
        if clockwise:
            input("turn right then press enter")
        else:
            input("turn left then press enter")

        # go normal distance
        input("go forward " + str(round(normal_dist/FORWARD)) + " steps then press enter")

print('good! distance satisfied')
ser.close()
