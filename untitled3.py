
import pandas as pd

import streamlit as st

import numpy as np


st. set_page_config(layout="wide")


col100, col200, col300, col400, col500, col600, col700 = st.columns(7)

with col100:
    pass
with col200:
    pass
with col300:
    pass
with col400:
    TEST = st.text_input("رمز ورود",type="password")
with col500:
    pass
with col600:
    pass
with col700:
    pass

if TEST == "123456" or TEST == "0000" or TEST == "1111":
    if TEST == "123456":
        st.write("آقای علی نظری زاده خوش آمدید")
    elif TEST == "0000":
        st.write("کارشناس فروش خوش آمدید")
    elif TEST == "1111":
        st.write("واحد برنامه ریزی خوش آمدید")
    


 
        
    df_etender_Estealam_0427 = pd.read_excel("etender_Estealam_0427.xlsx")
    df_etender_Monagheseh_0427 = pd.read_excel("etender_Monagheseh_0427.xlsx")
    df_hezarehinfo_Estealam_0427 = pd.read_excel("hezarehinfo_Estealam_0427.xlsx")
    df_hezarehinfo_Monagheseh_0427 = pd.read_excel("hezarehinfo_Monagheseh_0427.xlsx")
        


    st.title("سامانه جمع آوری مناقصات شرکت مفتاح رایانه افزار",)
    s = st.radio("انتخاب کنید", ["استعلام بها ایتندر" , "استعلام بها هزاره" , "مناقصه ایتندر" , "مناقصه هزاره"])
        
        
    if s == "استعلام بها ایتندر":
            
        st.dataframe(df_etender_Estealam_0427)
        df2 = df_etender_Estealam_0427['استان'].value_counts(sort=False)
            
    elif s== "استعلام بها هزاره":
        st.dataframe(df_hezarehinfo_Estealam_0427)
        df2 = df_hezarehinfo_Estealam_0427['استان'].value_counts(sort=False)
            
    elif s== "مناقصه ایتندر":
        st.dataframe(df_etender_Monagheseh_0427)
        df2 = df_etender_Monagheseh_0427['استان'].value_counts(sort=False)
            
    elif s== "مناقصه هزاره":
        st.dataframe(df_hezarehinfo_Monagheseh_0427)
        df2 = df_hezarehinfo_Monagheseh_0427['استان'].value_counts(sort=False)
            
    else:
        pass
        
        
    title2 = "-1"
    option = "کد آگهی"
    Columns = list(df_etender_Estealam_0427.columns.unique())
    col10, col20 = st.columns(2)
    with col10:
        option = st.selectbox(
        "فیلد قابل جستجو را وارد کنید",
        (Columns))

        #st.write("You selected:", option)
        
    with col20:
        title2 = st.text_input("متن جستجو", )
        
    mask_to = df_etender_Estealam_0427[option].str.contains(title2)
    v = df_etender_Estealam_0427[mask_to]
    st.dataframe(v)
        
    st.write("\n")
    st.title("گزارشات",)
    st.bar_chart(df2)
        
    

        
        
            
            
        
        
        
        
        
        
    
    
    
    
    
    
    
    
