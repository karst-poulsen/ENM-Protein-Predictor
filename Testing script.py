import pandas as pd

df1=pd.DataFrame({'key':['1','2','3','4'], 'Col2':['st1', ' st2', 'st3', 'st4']})
df2=pd.DataFrame({'key':['1','2','3','4'], 'Col3':['sta', ' stb', 'stc', 'std']})
print(df1)
print(df2)
df1.set_index('key').join(df2.set_index('key'))
print(df1)
df1.join(df2.set_index('key'), on='key')
print(df1)