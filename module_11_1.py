import pandas as pd
# библиотека pandas:
# создание фрейма(таблицы) из словарей
d = {'a': [2, 3, 5, 7], 'b': [0, 1, 2, 3], 'c': [2, 4, 6, 8]}
ser = pd.DataFrame(d)#0,1,2,3 - индексы каждой строки
print(ser)
ser.info()
#можно вызывать отдельно какую-либо колонку или срез строк:
print(ser['a'])
print(ser[1: 3])
print(ser[['b', 'c']].head(2))
print(ser[['a', 'c']].tail(1))
print(ser.loc[[1, 3], ['a', 'b']])
print(ser.iloc[0: 3, :3])
# фильтрация:
print(ser[ser['a'] > 3])
print(ser[ser['b'].isin([1, 3])])