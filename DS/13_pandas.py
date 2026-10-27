"""Converted from pandas.ipynb."""

import pandas as pd

a=[1,2,3]
as1=pd.Series(a,index=['a','b','c'])

as1

d={"name":["Abc","def","ghi"],"age":[1,2,3]}

x=pd.DataFrame(d,index=['a','b','c'])
x

x.loc['a']['name']
