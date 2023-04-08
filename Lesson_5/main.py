import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')

print(df.head(n=10))
print('*' * 79)

print(df.tail(n=2))
print('*' * 79)

# Иногда заранее неизвестно сколько строк и столбцов находится внутри таблицы,
# чтобы это сделать необходимо воспользоваться специальной функцией.
print(df.shape)

print('*' * 79)
# Чтобы обнаружить пустые значения в таблице данных необходимо воспользоваться
# функцией .isnull().

print('*' * 79)
print(df.isnull())
# sum(). Данная
# функция выведет количество null-значений в каждой ячейке по столбцам.
"""
       longitude  latitude  ...  median_income  median_house_value
0          False     False  ...          False               False
1          False     False  ...          False               False
2          False     False  ...          False               False
3          False     False  ...          False               False
4          False     False  ...          False               False
...          ...       ...  ...            ...                 ...
16995      False     False  ...          False               False
16996      False     False  ...          False               False
16997      False     False  ...          False               False
16998      False     False  ...          False               False
16999      False     False  ...          False               False

[17000 rows x 9 columns]
"""

print('*' * 79)
print(df.isnull().sum())
"""
longitude             0
latitude              0
housing_median_age    0
total_rooms           0
total_bedrooms        0
population            0
households            0
median_income         0
median_house_value    0
dtype: int64
"""

# у каждого столбца есть свой тип данных, чтобы это узнать, нужно
# применить функцию .dtypes.
print('*' * 79)
print(df.dtypes)
"""
longitude             float64
latitude              float64
housing_median_age    float64
total_rooms           float64
total_bedrooms        float64
population            float64
households            float64
median_income         float64
median_house_value    float64
dtype: object
"""

# Чтобы узнать название всех столбцов в таблице, воспользуйтесь функцией
# .columns.
print('*' * 79)
print(df.columns)
"""
Index(['longitude', 'latitude', 'housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income',
       'median_house_value'],
      dtype='object')
"""

# Выборка данных

# вся таблица
print('*' * 79)
print(df)
"""
       longitude  latitude  ...  median_income  median_house_value
0        -114.31     34.19  ...         1.4936             66900.0
1        -114.47     34.40  ...         1.8200             80100.0
2        -114.56     33.69  ...         1.6509             85700.0
3        -114.57     33.64  ...         3.1917             73400.0
4        -114.57     33.57  ...         1.9250             65500.0
...          ...       ...  ...            ...                 ...
16995    -124.26     40.58  ...         2.3571            111400.0
16996    -124.27     40.69  ...         2.5179             79000.0
16997    -124.30     41.84  ...         3.0313            103600.0
16998    -124.30     41.80  ...         1.9797             85800.0
16999    -124.35     40.54  ...         3.0147             94600.0

[17000 rows x 9 columns]
"""

print('*' * 79)
# если хочу вывести только этот столбец "latitude"
print(df.latitude)
"""
0        34.19
1        34.40
2        33.69
3        33.64
4        33.57
         ...  
16995    40.58
16996    40.69
16997    41.84
16998    41.80
16999    40.54
Name: latitude, Length: 17000, dtype: float64
"""

print('*' * 79)
# если нужно вывести несколько столбцов, создаем список внутри списка
print(df[['latitude', 'population']])
"""
       latitude  population
0         34.19      1015.0
1         34.40      1129.0
2         33.69       333.0
3         33.64       515.0
4         33.57       624.0
...         ...         ...
16995     40.58       907.0
16996     40.69      1194.0
16997     41.84      1244.0
16998     41.80      1298.0
16999     40.54       806.0

[17000 rows x 2 columns]

"""

print('*' * 79)
# Задание: Необходимо вывести столбец total_rooms, у которого медианный возраст
# здания(housing_median_age) меньше 20.
print(df[df['housing_median_age'] < 20])
"""
       longitude  latitude  ...  median_income  median_house_value
0        -114.31     34.19  ...         1.4936             66900.0
1        -114.47     34.40  ...         1.8200             80100.0
2        -114.56     33.69  ...         1.6509             85700.0
3        -114.57     33.64  ...         3.1917             73400.0
10       -114.60     33.62  ...         2.6797             86500.0
...          ...       ...  ...            ...                 ...
16983    -124.19     41.78  ...         1.6654             74600.0
16987    -124.21     41.77  ...         2.5795             68400.0
16991    -124.23     41.75  ...         2.4805             73200.0
16997    -124.30     41.84  ...         3.0313            103600.0
16998    -124.30     41.80  ...         1.9797             85800.0

[4826 rows x 9 columns]
"""

print('*' * 79)
print(df[df['housing_median_age'] < 20]['total_rooms'])
"""
0        5612.0
1        7650.0
2         720.0
3        1501.0
10       3741.0
          ...  
16983    3140.0
16987    3461.0
16991    3159.0
16997    2677.0
16998    2672.0
Name: total_rooms, Length: 4826, dtype: float64
"""

print('*' * 79)
# усложним условие
# & - выполнение одновременно всех условий.
# | - выполнение хотя бы одного из условия.
print(df[(df['housing_median_age'] < 20) & (df['housing_median_age'] > 10)][
          'total_rooms'])
"""
0        5612.0
1        7650.0
2         720.0
3        1501.0
10       3741.0
          ...  
16983    3140.0
16987    3461.0
16991    3159.0
16997    2677.0
16998    2672.0
Name: total_rooms, Length: 3513, dtype: float64
"""

print('*' * 79)
# если хотим чтобы выводилось сразу несколько столбцов
print(df[(df['housing_median_age'] < 20) & (df['housing_median_age'] > 10)][
          ['total_rooms', 'housing_median_age']])
"""
0           5612.0                15.0
1           7650.0                19.0
2            720.0                17.0
3           1501.0                14.0
10          3741.0                16.0
...            ...                 ...
16983       3140.0                15.0
16987       3461.0                17.0
16991       3159.0                11.0
16997       2677.0                17.0
16998       2672.0                19.0

[3513 rows x 2 columns]
"""
print('*' * 79)
# Простая статистика

# Максимальное значение:
print(df['population'].max())
"""
35682.0
"""

print('*' * 79)
# Минимальное значение:
print(df['population'].min())
"""
3.0
"""

print('*' * 79)
# Среднее значение:
print(df['population'].mean())
"""
1429.5739411764705
"""

print('*' * 79)
# Сумма:
print(df['population'].sum())
"""
24302757.0
"""

print('*' * 79)
# Медианное значение::
print(df[['population', 'total_rooms']].median())
"""
population     1167.0
total_rooms    2127.0
dtype: float64
"""

# Перцентиль - это показатель, используемый в статистике,
# показывающий значение, ниже которого падает определенный процент
# наблюдений в группе наблюдений
# Получить общую картину можно простой командой describe
print('*' * 79)
print(df.describe())
"""
          longitude      latitude  ...  median_income  median_house_value
count  17000.000000  17000.000000  ...   17000.000000        17000.000000
mean    -119.562108     35.625225  ...       3.883578       207300.912353
std        2.005166      2.137340  ...       1.908157       115983.764387
min     -124.350000     32.540000  ...       0.499900        14999.000000
25%     -121.790000     33.930000  ...       2.566375       119400.000000
50%     -118.490000     34.250000  ...       3.544600       180400.000000
75%     -118.000000     37.720000  ...       4.767000       265000.000000
max     -114.310000     41.950000  ...      15.000100       500001.000000

[8 rows x 9 columns]
"""
# count - Общее кол-во не пустых строк
# mean - среднее значение в столбце
# std - стандартное отклонение от среднего значения
# min - минимальное значение
# max - максимальное значение
# Числа 25%, 50%, 75% - перцентили



