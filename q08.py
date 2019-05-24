##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 
import pandas as pd
import numpy as np
##
pd.set_option('display.notebook_repr_html', False)
df = pd.read_csv(open('/vagrant/GitHub/lab-programacion-pandas-jlmejiav/tbl0.tsv'), delimiter='\t')
##
# fecha=[]
# fecha=df['_c3'].str.split('-')
# for x in list(range(len(fecha))):
#     año[x][0] = fecha[x][0]
###
ano=[]
ano = [ z.split('-')[0] for z in df._c3]
df['ano']=ano
print(df)