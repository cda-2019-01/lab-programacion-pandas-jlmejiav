##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
##
import pandas as pd
import numpy as np
##
pd.set_option('display.notebook_repr_html', False)
df = pd.read_csv(open('/vagrant/GitHub/lab-programacion-pandas-jlmejiav/tbl0.tsv'), delimiter='\t')
##
# df.groupby('_c1').count()[['_c0']]
##
letras=sorted(set(df._c1))
for w in letras:
    print(w,',',df[df['_c1'] == w].count()['_c1'])