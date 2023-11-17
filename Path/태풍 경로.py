# 좌표를 편의상 x, y로 설정 나중에 위도, 경도로 바뀔 수 있음
# nx (now_x) ny (now_y) : 현재 좌표 / ox (old_x) oy (old_y) : 이전 좌표
# typ 태풍 좌표의 grad 값을 모은 리스트

# ------------------------------------------------------
# func
# ------------------------------------------------------

import sys
input = sys.stdin.readline
INF = 100

# 두 점 사이 기울기 계산
def path_grad(nx, ny, ox, oy):
    if (nx-ox) != 0:
        grad = (ny-oy)/(nx-ox)
    else:
        grad = INF
    return grad

# 거리 계산
def cal_dist(nx, ny, ox, oy):
    return ((nx-ox)**2 + (ny-oy)**2)**0.5

# 경로 변동성
def path_diff(grads):

    # 태풍 데이터 여러 개를 돌려서 threshold 적절한 값 찾기
    threshold = 4
    g_size = len(grads)

    plus_to_minus = []
    th_exceed = []

    for i in range(g_size-1):

        # 서로 부호가 다를 때 (두 곱의 값이 음수)
        if grads[i+1] * grads[i] < 0 and abs(grads[i+1]-grads[i]) <= threshold:
            plus_to_minus.append([i, grads[i+1], grads[i]])

        # threshold 값 초과할 때
        if abs(grads[i+1]) - abs(grads[i]) >= threshold:
            th_exceed.append([i, grads[i+1], grads[i]])

    return plus_to_minus, th_exceed

def cal_grad_diff(typ):
    t_len = len(typ)
    new_grads = []

    for i in range(t_len-1):
        new_grads.append(path_grad(typ[i+1][1], typ[i+1][2], typ[i][1], typ[i][2]))

    print(new_grads)
    return new_grads


# 우선 태풍 데이터를 빼와서
# 태풍 데이터를 가지고 path_grad 함수를 돌리고, 그 결과를 list에 저장
# list를 path_diff 함수에 보내서 경로 변동성이 심한 구간을 print 한다
# 변동성 어떻게 detect 하지? -> grad 부호가 바뀔 때? 차이가 클 때? (여러 가지 시도)
# 이 grad plot 할 수 있는 방법?

# 1. CSV 파일 열기 (상대 경로)
import csv
def read_data(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader) # 헤더 행 skip

        typ_point = []
        for row in reader:
            if float(row[1]) == 0:  # 2번째 열이 0인 경우
                typ_point.append([row[0], float(row[2]), float(row[3])]) #날짜(시간), 위도, 경도 순으로 리스트 추출
                print(typ_point[-1])
    return typ_point

# 2. 직접 입력 받기
def input_data():
    now_point = list(map(float, input().rstrip().split()))

# 3. 변동성 구간 plot 함수
def plot_typhoon_path(new_typ, p_to_m, th_ex):
    # new_typ: [날짜, 위도, 경도] 리스트
    dates = [point[0] for point in new_typ]
    latitudes = [point[1] for point in new_typ]
    longitudes = [point[2] for point in new_typ]

    # plt 스타일
    plt.style.use({
        'axes.facecolor': 'lightblue',  # 그래프 영역 배경색
        'axes.edgecolor': 'gray',  # 그래프 영역 테두리 색
        'axes.grid': True,  # 그리드 표시 여부
        'grid.color': 'white',  # 그리드 색상
        'grid.linestyle': '--',  # 그리드 선 스타일
        'grid.alpha': 0.7,  # 그리드 투명도
        'xtick.color': 'black',  # x축 눈금 색상
        'ytick.color': 'black',  # y축 눈금 색상
        'text.color': 'black'  # 텍스트 색상
    })

    # 경로 plot
    plt.figure(figsize=(5, 8))
    plt.plot(longitudes, latitudes, marker='o', linestyle='-', color='black')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('23-06-KHANUN')

    # 변동성이 발생한 지점을 빨간색으로 표시
    for idx, grad1, grad2 in p_to_m:
        plt.scatter(longitudes[idx+1], latitudes[idx+1], color='red', s=100)  # s는 마커의 크기

        # 그 지점과 이전 지점을 연결
        plt.plot([longitudes[idx], longitudes[idx+1], longitudes[idx+2]], [latitudes[idx], latitudes[idx+1], latitudes[idx+2]], linestyle='--', color='orange')

    # threshold를 초과한 지점 표시
    #for idx, grad1, grad2 in th_ex:
        #plt.scatter(longitudes[idx], latitudes[idx], color='Green', s=100)

    plt.grid(True)
    plt.show()


# ------------------------------------------------------
# main
# ------------------------------------------------------

import matplotlib.pyplot as plt
typhoon_file_name = ['23-06.csv'] # input 할 file name 리스트 만들기

for name in typhoon_file_name:
    new_typ = read_data(name) # 리스트 반환
    print("number of points: " + str(len(new_typ))) # 좌표 개수
    new_grads = cal_grad_diff(new_typ)
    p_to_m, th_ex = path_diff(new_grads)
    plot_typhoon_path(new_typ, p_to_m, th_ex)
