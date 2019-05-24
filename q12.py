##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 
import pandas as pd
import numpy as np
##
pd.set_option('display.notebook_repr_html', False)
df0 = pd.read_csv(open('/vagrant/GitHub/lab-programacion-pandas-jlmejiav/tbl0.tsv'), delimiter='\t')
df2 = pd.read_csv(open('/vagrant/GitHub/lab-programacion-pandas-jlmejiav/tbl2.tsv'), delimiter='\t')
dfmerge = pd.merge(df2,df0,on="_c0")
print(dfmerge.groupby('_c1')['_c5b'].sum())