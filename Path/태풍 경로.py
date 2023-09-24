
# 좌표를 편의상 x, y로 설정 나중에 위도, 경도로 바뀔 수 있음
# nx (now_x) ny (now_y) : 현재 좌표 / ox (old_x) oy (old_y) : 이전 좌표
# typ 태풍 좌표의 grad 값을 모은 리스트

point = [] #emuarate를 사용해서

# 두 점 사이 기울기 계산
def path_grad(nx, ny, ox, oy):
    grad = (ny-oy)/(nx-ox)
    return grad

# 경로 변동성
def path_diff(typ):

    # 태풍 데이터 여러 개를 돌려서 threshold 적절한 값 찾기
    threshold = 0
    t_size = len(typ)

    for i in range(t_size-1):

        #threshold 값 초과할 때
        if typ[i+1] - typ[i] > threshold:
            print(typ[i+1], typ[i])

        #서로 부호가 다를 때 (두 곱의 값이 음수)
        if typ[i+1]*typ[i-1] < 0:
            print(typ[i+1], typ[i])


# 우선 태풍 데이터를 빼와서
# 태풍 데이터를 가지고 path_grad 함수를 돌리고, 그 결과를 list에 저장
# list를 path_diff 함수에 보내서 경로 변동성이 심한 구간을 print 한다
# 변동성 어떻게 detect 하지? -> grad 부호가 바뀔 때? 차이가 클 때? (여러 가지 시도)
# 이 grad plot 할 수 있는 방법이 있을까?
