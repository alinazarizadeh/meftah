import pandas as pd
import streamlit as st
import numpy as np
import openpyxl

st.set_page_config(layout="wide", page_title='مفتاح رایانه افزار')
col100, col200, col300, col400, col500, col600, col700 = st.columns(7)

Database = pd.read_excel("Database\Database_0514.xlsx")
        
# header
col1, col2, col3 = st.columns(3)
with col1:
    pass
with col2:
    st.title("سامانه جمع آوری مناقصات شرکت مفتاح رایانه افزار",)
with col3:
    pass

s = st.radio("انتخاب کنید", [  "همه" , "مناقصه" , "استعلام"], )   
if s == "استعلام":
    temp = Database[Database['نوع آگهی'] == 'استعلام']
    st.dataframe(temp)
    City = Database['استان'].value_counts(sort=False)
 
elif s == "مناقصه":
    temp = Database[Database['نوع آگهی'] == 'مناقصه']
    st.dataframe(temp)
    City = Database['استان'].value_counts(sort=False)
    
elif s == "همه":
    temp = Database
    st.dataframe(temp)
    City = Database['استان'].value_counts(sort=False)
    
else:
    pass
        

