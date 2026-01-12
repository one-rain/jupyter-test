
import pandas as pd

dates = pd.date_range('20130101', periods=6)
print(dates)

print('居中打印'.center(50, '='))

print('')
print(format('居中打印', '=>50'))
print(format('居右打印', '=^50'))
print(format('居左打印', '=<50'))
print('')