# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:38:54 2025

@author: Claudio
"""

import streamlit as st

st.title("Chatbot de Equipos Médicos")

user_input = st.text_input("Escribe tu pregunta:")
if user_input:
    st.write(f"Respuesta del chatbot para: {user_input}")
