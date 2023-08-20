import math
from SerialCapture import UWB3000Serial

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

input("measure side b")
side_b = float(ser.read_distance())

input("measure side c")
side_c = float(ser.read_distance())

side_a = float(input("input side a in meter: "))
(tangential_dist, normal_dist) = calculate_dist(side_a, side_b, side_c)
print("tangential in meter: ", tangential_dist)
print("normal in meter: ", normal_dist)




# go tangential distance
# TODO
input("go tangential")

# try turn right
input("turn right")
# TODO
dist1 = float(ser.read_distance())
input("measure test1")
print(ser.read_distance())
# go some distance
# TODO
dist2 = float(ser.read_distance())
input("measure test2")
print(ser.read_distance())

if dist2 > dist1:
    input("turn back!!")
    # turn back
    # TODO
    pass

input("go straight")

while True:
    input("measure")
    print(float(ser.read_distance()))
# now the direction is correct
# go forward until dist < 30



ser.close()