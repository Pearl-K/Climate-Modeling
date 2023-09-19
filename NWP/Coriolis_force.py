import sys
input = sys.stdin.readline

#Coriolis force of Northern Hemisphere

def init_value():
    # Input initial values
    print("Input mass")
    mass = float(input())

def cal_velo():
    # Calculate the object velocity
    # 물의 velo? 중력 가속도, 물의 질량, 관 통과하는 압력?
    res = 0
    return res


def cal_angular_velocity(mass):
    # Calculate earth rotation angular velocity
    res = 0
    return res

def cal_coriolis(mass, velo, angular_velo):
    F_cor = 2*mass*angular_velo*velo
    return F_cor

