import streamlit as st
from cyk import *

st.title("F3 ParseApp")

st.subheader("Check your Indonesian Sentence Valid Or Invalid")
st.write(" ")
string = st.text_input("Write your sentence here")
string2 = string.lower()
btn = st.button("Check")

#string = input('String: ')
hasil = ''
if btn:
    hasil = parse(string2)
    
    if hasil == True:
        #print("Kalimat anda Valid")
        st.write('Kalimat anda: ', string)
        st.success('Kalimat anda Valid')
    else:
        #print("Kalimat anda Invalid")
        st.write('Kalimat anda: ', string)
        st.error('Kalimat anda Invalid')
