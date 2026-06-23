# py -m streamlit run practice.py

import streamlit as st
from functions_styles.styles import header_text,sub_header_text,glowing_line_1,glowing_line_2,normal_text

header_text("SAMRAT MALLA")
glowing_line_1()

st.markdown("<br>",unsafe_allow_html=True)
sub_header_text("",status_label="ABOUT ME")
glowing_line_2()

normal_text("Hi, I'm Samrat Malla, an Electrical Engineering student at" \
" Pulchowk Campus with a passion for power systems, artificial intelligence, and" \
" software-driven engineering. Through projects like GridMind AI, I explore " \
"how machine learning, simulation, and real-time analytics can be combined to build" \
" smarter and more resilient energy systems.")

st.markdown("<br>",unsafe_allow_html=True)


glowing_line_1()
