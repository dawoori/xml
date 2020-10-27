import pandas as pd

#########################################
# series 생성
height = [183, 179, 170, 178, 184]
s = pd.Series(height)
print(s)
print(s.dtypes)
print()

#########################################
# data frame 생성

playersCW = {           # 딕셔너리 형태의 data frame (column-wise)
    'PLAYER_ID': ['2020001', '2020002', '2020003', '2020004', '2020005'],
    'PLAYER_NAME': ['손홍민', '호날두', '메시', '박지성', '차범근'],
    'TEAM_ID': ['K01', 'K02', 'K03', 'K03', 'K01'],
    'POSITION': ['FW', 'FW', 'FW', 'MF', 'FW'],
    'HEIGHT': [183, 179, 170, 178, 184],
    'WEIGHT': [82, 77, 69, 78, 85]
}
df = pd.DataFrame(playersCW)        # index가 정의되지 않으면, 인덱스는 행번호와 같음.
print(df)
print(df.dtypes)
print()

playersRW = [           # 리스트 형태의 data frame (row-wise)
    ['2020001', '손홍민', 'K01', 'FW', 183, 82],
    ['2020002', '호날두', 'K02', 'FW', 179, 77],
    ['2020003', '메시', 'K03', 'FW', 170, 69],
    ['2020004', '박지성', 'K03', 'MF', 178, 78],
    ['2020005', '차범근', 'K01', 'FW', 184, 85]
]
dfRW = pd.DataFrame(
    playersRW,
    index = [2, 4, 5, 8, 11],
    columns = ['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'POSITION', 'HEIGHT', 'WEIGHT']
)
print(dfRW)
print()

#########################################
# data frame 정보 읽기
print(df.index)
print(df.columns)
print(df.columns.values.tolist())
print()

print(df.values)            # 값 사이에 콤마가 없음에 주의함.
print(df.values.tolist())
print()

print(df.describe())        # 숫자 열에 대한 통계치
print()

#########################################
# data frame 열 읽기
print(df.PLAYER_NAME)
print()

print(df['PLAYER_NAME'])        # 위 명령과 동일한 결과
print()

#########################################
# data frame 행 읽기
print(df.loc[2])            # 인덱스(문자열, 숫자)를 기준
print()

print(df.iloc[2])           # 행번호(연속된 숫자), 즉 integer position을 기준
print()

print(df.iloc[[0, 2]])      # 행번호 0와 2만 출력 ([] 안에 []가 나옴)
print()

#########################################
# data frame 복합 읽기 (Boolean indexing)
print(df.loc[df['WEIGHT'] > 70])
print()

print(df.loc[:, ['PLAYER_ID', 'PLAYER_NAME']])      # 모든 행에 대해, 두 컬럼만 가져오기.
print()

print(df.iloc[:, :3])      # 모든 행에 대해, 처음 세 컬럼만 가져오기.
print()

print(df.loc[[0, 2], ['PLAYER_ID', 'PLAYER_NAME']])
print()

#########################################
# 유용한 메쏘드
print(df.head())            # 처음 5개 행
print()

print(df.tail())            # 마지막 5개 행
print()

sum = df['HEIGHT'].sum()
avg = df['HEIGHT'].mean()
print(sum, avg)