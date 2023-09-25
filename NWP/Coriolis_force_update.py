import numpy as np

#mass and object velocity are arbitrary values.
#질량, 물체의 속도는 임의의 값 입니다.

def calculate_coriolis_force(mass, velocity, angular_velocity):
    # cross product - 외적 계산 함수 np.cross
    coriolis_force = -2 * mass * np.cross(angular_velocity, velocity)
    return coriolis_force

# mass - 물체의 질량 (kg)
mass = 100

# 물체의 속도 벡터 V (m/s)
velocity = np.array([0.0, 2000, 0])

# Earth's angular velocity - 지구의 각속도 Ω (rad/s)
angular_velocity = np.array([0.0, 0.0, 7.29e-5])

# coriolis force - 코리올리 힘 계산
coriolis_force = calculate_coriolis_force(mass, velocity, angular_velocity)

# print results
print("Coriolis force:", coriolis_force)
