import numpy as np
import pandas as pd
import os

dates = pd.date_range('20130101', periods=6)
print(dates)

df2 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
})

print(df2)

print(os.path.abspath('.'))

print('居中打印'.center(50, '='))

print('')
print(format('居中打印', '=>50'))
print(format('居右打印', '=^50'))
print(format('居左打印', '=<50'))
print('')
