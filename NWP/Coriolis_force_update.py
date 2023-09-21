import numpy as np

def calculate_coriolis_force(mass, velocity, angular_velocity):
    # 외적 (cross product) 계산
    coriolis_force = -2 * mass * np.cross(angular_velocity, velocity)
    return coriolis_force

# 물체의 질량 (예: 1 kg)
mass = 1.0

# 물체의 속도 벡터 V (예: [1.0, 2.0, 3.0] m/s, x, y, z 축 방향의 속도)
velocity = np.array([1.0, 2.0, 3.0])

# 지구의 각속도 벡터 Ω (북극 방향으로 가리킴, 예: [0.0, 0.0, Ωz] rad/s)
angular_velocity = np.array([0.0, 0.0, Ωz])

# 코리올리 힘 계산
coriolis_force = calculate_coriolis_force(mass, velocity, angular_velocity)

# 결과 출력
print("코리올리 힘:", coriolis_force)
