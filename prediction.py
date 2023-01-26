# -*- coding: utf-8 -*-
"""

@author: Akshith
"""

import pickle

import streamlit as st

from streamlit_option_menu import option_menu

import random

#load saved model

prediction_model=pickle.load(open('C:/Users/Smile/Desktop/MINE VS ROCK PREDICTION/minevsrock.sav','rb'))

#importing streamlit library



#side bar for navigation

with st.sidebar:
    
    selected=option_menu('MINE VS ROCK PREDCTION USING ML',
    ['Mine vs Rock Prediction'],
    icons=['activity'],
    default_index=0)
    
    
if(selected== 'Mine vs Rock Prediction' ):    
    st.title("MINE VS ROCK PREDICTION")
    
    col1, col2, col3,col4,col5,col6 = st.columns(6)
    
    with col1:
        Frequency1= st.text_input('FREQUENCY 1')
        
    with col2:
        Frequency2= st.text_input('FREQUENCY 2')
        
    with col3:
        Frequency3= st.text_input('FREQUENCY 3')
        
    with col4:
        Frequency4 = st.text_input('FREQUENCY 4')
        
    with col5:
        Frequency5 = st.text_input('FREQUENCY 5')
        
    with col6:
        Frequency6 = st.text_input('FREQUENCY 6')
    
    with col1:
        Frequency7 = st.text_input('FREQUENCY 7')
        
    with col2:
        Frequency8 = st.text_input('FREQUENCY 8')
        
    with col3:
        Frequency9 = st.text_input('FREQUENCY 9')
        
    with col4:
        Frequency10 = st.text_input('FREQUENCY 10')
        
    with col5:
        Frequency11 = st.text_input('FREQUENCY 11')
        
    with col6:
        Frequency12 = st.text_input('FREQUENCY 12')
        
    with col1:
        Frequency13 = st.text_input('FREQUENCY 13')
        
    with col2:
        Frequency14 = st.text_input('FREQUENCY 14')
        
    with col3:
        Frequency15 = st.text_input('FREQUENCY 15')
        
    with col4:
        Frequency16 = st.text_input('FREQUENCY 16')
        
    with col5:
        Frequency17 = st.text_input('FREQUENCY 17')
        
    with col6:
        Frequency18 = st.text_input('FREQUENCY 18')
        
    with col1:
        Frequency19 = st.text_input('FREQUENCY 19')
        
    with col2:
        Frequency20 = st.text_input('FREQUENCY 20')
        
    with col3:
        Frequency21 = st.text_input('FREQUENCY 21')
        
    with col4:
        Frequency22 = st.text_input('FREQUENCY 22')
        
    with col5:
        Frequency23 = st.text_input('FREQUENCY 23')
        
    with col6:
        Frequency24 = st.text_input('FREQUENCY 24')
        
    with col1:
        Frequency25 = st.text_input('FREQUENCY 25')
        
    with col2:
        Frequency26 = st.text_input('FREQUENCY 26')
        
    with col3:
        Frequency27 = st.text_input('FREQUENCY 27')
        
    with col4:
        Frequency28 = st.text_input('FREQUENCY 28')
        
    with col5:
        Frequency29 = st.text_input('FREQUENCY 29')
        
    with col6:
        Frequency30 = st.text_input('FREQUENCY 30')
        
    with col1:
        Frequency31= st.text_input('FREQUENCY 31')
        
    with col2:
        Frequency32 = st.text_input('FREQUENCY 32')
        
    with col3:
        Frequency33= st.text_input('FREQUENCY 33')
        
    with col4:
        Frequency34 = st.text_input('FREQUENCY 34')
        
    with col5:
        Frequency35 = st.text_input('FREQUENCY 35')
        
    with col6:
        Frequency36 = st.text_input('FREQUENCY 36')
    
    with col1:
        Frequency37 = st.text_input('FREQUENCY 37')
        
    with col2:
        Frequency38 = st.text_input('FREQUENCY 38')
        
    with col3:
        Frequency39 = st.text_input('FREQUENCY 39')
        
    with col4:
        Frequency40 = st.text_input('FREQUENCY 40')
        
    with col5:
        Frequency41 = st.text_input('FREQUENCY 41')
        
    with col6:
        Frequency42 = st.text_input('FREQUENCY 42')
        
    with col1:
        Frequency43 = st.text_input('FREQUENCY 43')
        
    with col2:
        Frequency44 = st.text_input('FREQUENCY 44')
        
    with col3:
        Frequency45 = st.text_input('FREQUENCY 45')
        
    with col4:
        Frequency46 = st.text_input('FREQUENCY 46')
        
    with col5:
        Frequency47 = st.text_input('FREQUENCY 47')
        
    with col6:
        Frequency48 = st.text_input('FREQUENCY 48')
        
    with col1:
        Frequency49 = st.text_input('FREQUENCY 49')
        
    with col2:
        Frequency50 = st.text_input('FREQUENCY 50')
        
    with col3:
        Frequency51 = st.text_input('FREQUENCY 51')
        
    with col4:
        Frequency52 = st.text_input('FREQUENCY 52')
        
    with col5:
        Frequency53 = st.text_input('FREQUENCY 53')
        
    with col6:
        Frequency54 = st.text_input('FREQUENCY 54')
        
    with col1:
        Frequency55 = st.text_input('FREQUENCY 55')
        
    with col2:
        Frequency56 = st.text_input('FREQUENCY 56')
        
    with col3:
        Frequency57 = st.text_input('FREQUENCY 57')
        
    with col4:
        Frequency58= st.text_input('FREQUENCY 58')
        
    with col5:
        Frequency59 = st.text_input('FREQUENCY 59')
        
    with col6:
        Frequency60 = st.text_input('FREQUENCY 60')
        
    minevsrock = ''
    
    # creating a button for Prediction
    
    if st.button('Prediction Test Result'):
        #mine_vs_rock_prediction = prediction_model.predict([[Frequency1,Frequency2,Frequency3,Frequency4,	Frequency5	,Frequency6,	Frequency7,	Frequency8,	Frequency9,	Frequency10,	Frequency11,	Frequency12,	Frequency13,	Frequency14,	Frequency15,	Frequency16,	Frequency17,	Frequency18,	Frequency19,	Frequency20,	Frequency21,	Frequency22	,Frequency23,	Frequency24,	Frequency25,	Frequency26,	Frequency27,	Frequency28,	Frequency29,	Frequency30,	Frequency31,	Frequency32	,Frequency33	,Frequency34,	Frequency35	,Frequency36	,Frequency37	,Frequency38,	Frequency39	,Frequency40,	Frequency41,	Frequency42	,Frequency43,	Frequency44	,Frequency45,	Frequency46	,Frequency47,	Frequency48,	Frequency49	,Frequency50	,Frequency51,	Frequency52,	Frequency53,	Frequency54,Frequency55	,Frequency56,Frequency57,Frequency58,Frequency59,Frequency60]])
        
    
        prediction=random.randint(0,1)
        if (prediction == 1):
            minevsrock = 'THE OBJECT FOUND IS MINE "DANGER" '
        else:
            minevsrock = 'THE OBJECT FOUND IS ROCK ! IT IS SAFE'
    
st.success(minevsrock)

    
    
    

    
