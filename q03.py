##
## Imprima el maximo de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
import pandas as pd
import numpy as np
##
pd.set_option('display.notebook_repr_html', False)
df = pd.read_csv(open('/vagrant/GitHub/lab-programacion-pandas-jlmejiav/tbl0.tsv'), delimiter='\t')
##
print(df.groupby('_c1')['_c2'].max())