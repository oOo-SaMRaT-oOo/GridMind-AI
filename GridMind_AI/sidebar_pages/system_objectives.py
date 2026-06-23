import streamlit as st
from functions_styles.styles import header_text,glowing_line_1,glowing_line_2,sub_header_text,normal_text


def system_objectives():
    
    header_text("SYSTEM OBJECTIVES")
    glowing_line_1()

    sub_header_text("Continuously tracks frequency response behavior and key" \
    " stability indicators during changing grid operating" \
    " conditions.",status_label="Real-Time Grid Monitoring : ")

    glowing_line_2()


    sub_header_text("Uses machine learning to forecast future collapse risk "
    "and identify instability before critical thresholds are reached.",
    status_label= "Predictive Stability Intelligence : ")

    glowing_line_2()

    sub_header_text("Transforms complex power system dynamics into clear visual" \
    " insights and actionable early-warning alerts.",
    status_label="Operator Decision Support : ")

    glowing_line_2()

    sub_header_text("SaMRaT MALLA",status_label="CREATOR : ")
    glowing_line_2()
    normal_text("ELECTRICAL ENGINEERING STUDENT")
    glowing_line_1()

    

