from os import write
import streamlit as st;

st.title('Calculadora de IMC')
with st.form(key="Calcular IMC"):
    input_nome = st.text_input(label='Insira seu nome')
    input_altura = st.number_input(label="Insira sua altura")
    input_peso = st.number_input(label='Insira seu peso')
    input_button_submit = st.form_submit_button('enviar')
    if input_button_submit:
        st.write(' {} '.format(input_nome) + " Seu IMC é: {0:.4f} ".format(input_peso / input_altura**2))
    