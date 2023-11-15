!pip install xarray
import numpy as np
import xarray as xr
import pandas as pd
#import netCDF4 as nc
import matplotlib.pyplot as plt
import imageio

from google.colab import drive
drive.mount('/content/drive/', force_remount=True)

import os
os.chdir('/content/drive/MyDrive/NWP 수치모델링/')
os.getcwd()

data_name = ["p20", "m20", "0", "m10", "p10"]
var = ["U", "V", "W", "T", "QVAPOR", "TSK", "U10", "V10", "QFX", "ACHFX", "HFX", "LH", "MU", "UST"]

for d in data_name:
    for v in var:
        globals()[v +"_" + d ] =eval("data_" + d)[v]

from datetime import datetime
def change_time(data, time_index):
    timeset = data.XTIME.values[time_index]
    datetime_obj = datetime.utcfromtimestamp(timeset.tolist() / 1e9)
    formatted_datetime = datetime_obj.strftime('%Y-%m-%d %H:%M')
    return formatted_datetime

# ----------------------------------------------------------------------------
# 그리기 시작
# ----------------------------------------------------------------------------

min = []
max = []

for d in data_name:
    south_north_index = 0
    U_data = eval("data_" + d)['U'][:, :, south_north_index, 1:].values
    min.append(np.min(U_data))
    max.append(np.max(U_data))
vmin = np.min(min)
vmax = np.max(max)

data_name = ["p20"]

for d in data_name:
    south_north_index = 0
    output_filename = d + '_U.gif'
    base_filename = d + '_U'


    # U 변수 가져오기
    U_data = eval("data_" + d)['U'][:, :, south_north_index, 1:].values

    # GIF 이미지를 저장할 빈 목록 생성
    images = []

    # Time 차원의 길이 가져오기
    time_length = eval("data_" + d).dims['Time']

    # 각 Time 스텝에 대한 그래프 이미지 생성
    for time_index in range(time_length):
        # 이미지 생성
        plt.figure()

        # 벡터 그래프 (quiver plot)
        x = range(0, U_data.shape[2], 3)  # x 좌표 띄엄띄엄 설정
        y = range(0, U_data.shape[1], 2)  # y 좌표 띄엄띄엄 설정
        X, Y = np.meshgrid(x, y)

        # contourf plot (U 값 나타내기)
        if abs(vmin) < vmax:
            contourf_levels = np.linspace(-vmax, vmax)  # 나타낼 레벨 수
        else:
            contourf_levels = np.linspace(vmin, -vmin)  # 나타낼 레벨 수

        if abs(vmin) < vmax:
            contourf_plot = plt.contourf(X, Y, U_data[time_index][y][:, x], levels=contourf_levels, cmap='seismic', vmin=-vmax, vmax=vmax)  # U 값을 contourf plot으로 나타냄
        else:
            contourf_plot = plt.contourf(X, Y, U_data[time_index][y][:, x], levels=contourf_levels, cmap='seismic', vmin=vmin, vmax=-vmin)  # U 값을 contourf plot으로 나타냄
        plt.colorbar(contourf_plot)  # 컬러바 추가
        time_str = change_time(eval("data_" + d),time_index)
        plt.title(f'{d} - Time: {time_str}')

        # 이미지 파일로 저장
        image_path = f'{base_filename}_time_{time_index}.png'
        plt.savefig(image_path)
        plt.close()

        # 이미지를 GIF 이미지 목록에 추가
        images.append(imageio.imread(image_path))

        # 이미지 파일 삭제 (선택 사항)
        #os.remove(image_path)


    # GIF 파일에 루프 설정 (반복)
    imageio.mimsave(output_filename, images, duration=1, loop=0)  # loop 매개변수 설정

    # Google Colab에서 파일 다운로드
    #from google.colab import files
    #files.download(output_filename)
