'''pandas numpy сумма все числовых значений в df'''
import numpy as np
import pandas as pd


def sm(df):
    s = 0
    print('Все не включенные значения для проверки:')
    for i in df.index:
        for j in df.columns:
            if isinstance(df.loc[i, j], (int, np.int64, float)):
                s += df.loc[i, j]
            else:
                print(df.loc[i, j], type(df.loc[i, j]))
    return s


df = pd.DataFrame({'Год': [1, 2, 3, 4, 5],
                   'Товар': ['a', 'b', 'c', 'd', 'e'],
                   'Шт': [10, 20, 30, 40, -50],
                   'Цена': [100, 'int', 30.5, 20, 5]})

print('Сумма =', sm(df))
