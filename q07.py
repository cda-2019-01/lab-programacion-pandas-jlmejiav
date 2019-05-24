##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 
import pandas as pd
import numpy as np
##
pd.set_option('display.notebook_repr_html', False)
df = pd.read_csv(open('/vagrant/GitHub/lab-programacion-pandas-jlmejiav/tbl0.tsv'), delimiter='\t')
##
df['suma'] = df['_c0'] + df['_c2']
print(df)