import streamlit as st
from cyk import *

st.subheader("Sentences")

file = open('terima.txt', 'r')
list_sentences = file.read().splitlines()

for sentence in list_sentences:
    string1 = sentence
    string12 = string1.lower()
    rest = parse(string12)
    if rest == True:
        st.write(string1)
        st.success('Kalimat anda Valid')
    else:
        st.write(string1)
        st.error('Kalimat anda Invalid')
    st.write('  ')
    st.markdown('---')
    st.write('  ')
    st.write('  ')
    st.write('  ')