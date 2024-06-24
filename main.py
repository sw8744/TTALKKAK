import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.stats import norm
import warnings

warnings.simplefilter(action='ignore', category=UserWarning)

# 데이터 로딩
print('------TTALKKAK------')
filelist = os.listdir('./Datasets')
print("파일 리스트 : " + str(filelist))
while True:
    try:
        fileName = input("파일명을 입력하세요 : ")
        data = pd.read_csv('./Datasets/' + fileName)

    except FileNotFoundError:
        print("파일이 존재하지 않습니다.")

    else:
        break
print('-------------------')
print(data)
print('-------------------')
drop_columns = input("제거할 컬럼명을 입력하세요(없으면 빈칸) : ").split()
if drop_columns != '':
    for i in drop_columns:
        del(data[i])
print('-------------------')
print(data)
print('-------------------')
drop_rows = list(map(int, input("제거할 행번호를 입력하세요(없으면 빈칸) : ").split()))
if drop_rows != '':
    data = data.drop(drop_rows, axis=0)
print('-------------------')
print(data)
print('-------------------')
for row in data.itertuples():
    print(row[1], end=' ')
    print('이 항목의 데이터는 B(' + str(row[2]) + ', ' + str(row[3]) + ') 분포를 따릅니다.')
    Ex = int(row[2]) * float(row[3])
    Vx = int(row[2]) * float(row[3]) * float(row[4])
    sigma = (Vx) ** 0.5
    print('또한 이 항목의 평균은 ' + str(Ex) + '이고, 분산은 ' + str(Vx) + '이고, ' + '표준편차는 ' + str(sigma) + '입니다.')
    print('따라서 이 항목은 근사적으로 N(' + str(Ex) + ', ' + str(Vx) + ') 분포를 따릅니다.')
    plt.title(row[1])
    x = [i for i in range(int(Ex) - 3 * int(sigma), int(Ex) + 3 * int(sigma))]
    y = [norm.pdf(i, Ex, sigma) for i in x]
    plt.plot(x, y)
    plt.show()
    plt.title(row[1] + "_standard")
    x = [(i - Ex) / sigma for i in range(int(Ex) - 3 * int(sigma), int(Ex) + 3 * int(sigma))]
    y = [norm.pdf(i, 0, 1) for i in x]
    plt.plot(x, y)
    plt.show()
    print('-------------------')