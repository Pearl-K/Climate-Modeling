from path_grad import new_typ
import matplotlib.pyplot as plt

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

# new_typ: [날짜, 위도, 경도] 리스트
dates = [point[0] for point in new_typ]
latitudes = [point[1] for point in new_typ]
longitudes = [point[2] for point in new_typ]

# 경로 plot
plt.figure(figsize=(5, 8))
plt.plot(longitudes, latitudes, marker='o', linestyle='-', color='black')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('23-06-KHANUN')
plt.grid(True)
plt.show()
