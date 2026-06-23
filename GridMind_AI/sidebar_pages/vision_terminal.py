import streamlit as st
import pandas as pd
import time
import joblib
import numpy as np
from functions_styles.functions import processing_mat_file
from functions_styles.styles import header_text,glowing_line_1,glowing_line_2,sub_header_text,normal_text,make_button_nice

def vision_terminal():
    

    GridMind_AI = joblib.load("GridMind_AI.pkl")

    def AI_prediction(model, row,feature):
        feature_vector = pd.DataFrame(row[feature]).T
        probablities = model.predict_proba(feature_vector)[0]
        collaspe_probablity = float(probablities[1])

        if row["Frequency_Change"] == 0.0 and row["RoCoF"] == 0.00:
            return 0.00
        
        else:
            return collaspe_probablity

    header_text("GridMind : AI") 
    glowing_line_1()
    normal_text("Modern power grids generate vast amounts of dynamic operational data," \
    " yet instability often develops before operators can react. GridMind AI bridges " \
    "this gap by continuously analyzing frequency response behavior and forecasting " \
    "future collapse risk through machine learning. Start the analysis to enter the " \
    "AI monitoring environment and observe the evolution of grid stability in real time.")
    st.markdown("<br>",unsafe_allow_html=True)
    glowing_line_2()

    data_frame = processing_mat_file("crash_1.mat",is_recovery = False)

    physical_crash_row = data_frame[data_frame["Frequency_Change"]<=-0.05]

    if "current_frame" not in st.session_state:
        st.session_state.current_frame = 0
    if "paused_triggered" not in st.session_state:
        st.session_state.paused_triggered = False
    if "ai_detection_time" not in st.session_state:
        st.session_state.ai_detection_time = None
    if "early_warning_seconds" not in st.session_state:
        st.session_state.early_warning_seconds = 0.00
    if "probablity_history" not in st.session_state:
        st.session_state.probablity_history = []


    if not physical_crash_row.empty:
        physical_crash_time = physical_crash_row["Time"].min()
    else:
        physical_crash_time = None

    make_button_nice()

    if st.button(label = "Start Analysis"):
        glowing_line_2()

        sub_header_text("",status_label="SYSTEM STATUS :")
        glowing_line_2()
        col1,col2 = st.columns([2,1])
        with col1:
            st.markdown("<br>",unsafe_allow_html=True)
            system_status_bar = st.empty()
            interactive_button_space = st.empty()

        with col2:
            st.write(
            "<span style='margin-left: 30px; font-size: 20px; font-weight: bold;'>DOMINANT FEATURES</span>"
            "<div style='margin-left: 55px; font-size: 18px; color: #58a6ff; line-height: 1.6;'>"
            "Frequency Change<br>"
            "Rolling Mean<br>"
            "Cumulative Drop"
            "</div>", 
            unsafe_allow_html=True
        )
            


        glowing_line_1()
        sub_header_text("FREQUENCY VISUALIZATION",status_label="CAPTURING - ")
        glowing_line_2()
        st.markdown("<br>",unsafe_allow_html=True)
        col1,col2 = st.columns([2,1])

        with col1:
            graph = st.empty()

        with col2 :
            value = st.empty()


        glowing_line_1()

        c1,c2 = st.columns([3,2.5])
        with c1:
            sub_header_text("VISION TERMINAl",status_label="LIVE - ")
            glowing_line_2()
            st.markdown("<br>",unsafe_allow_html=True)
            warning_timer_box = st.empty()
            st.write("---")

            probablity_value = st.empty()
            probablity_curve = st.empty()



        with c2 :
            st.markdown("<br><br>",unsafe_allow_html=True)
            st.subheader("Key Features :")
            feature_part = st.container()
            with feature_part:
                RoCoF = st.empty()
                st.write("---")
                Frequency_Accleration = st.empty()
                st.write("---")
                Cumulative_Drop = st.empty()


        glowing_line_1()
        sub_header_text("",status_label="BY SAMRAT MALLA")
        glowing_line_2()
        normal_text("ELECTRICAL ENGINEERING STUDENT")
        glowing_line_1()


        features = [
            "Frequency_Change", "RoCoF", "Frequency_Accleration",
            "df_RollingMean", "Cumulative_Drop", "RoCoF_Variance", 
            "RoCoF_Elasticity" ]

        refresh_rate = 1
        make_slow = False

        start_index = st.session_state.current_frame

        for index,row in data_frame.iloc[start_index:].iterrows():

            st.session_state.current_frame = index

            if index % refresh_rate !=0:
                continue

            collaspe = AI_prediction(GridMind_AI,row,features)
            current_time = row["Time"]
            st.session_state.probablity_history.append(np.round(collaspe*100,2))

            if collaspe < 0.2:

                system_status_bar.success(f"HEALTH : NOMINAL STATE  \nCollaspe Probablity : {collaspe*100:.4f} %")
                warning_timer_box.metric(label="AI Lead Time Window", value="0.0000 sec", delta="Monitoring Stream...")
                make_slow = False


            elif 0.20 <= collaspe < 0.70:
                system_status_bar.error(f"SYSTEM HEALTH: ANOMALOUS TRANSIENT GRADIENT DETECTED  \nCollaspe Probablity : {collaspe*100:.4f} %")
                make_slow = True

                if st.session_state.ai_detection_time is None and physical_crash_time is not None:
                    st.session_state.ai_detection_time = current_time
                    st.session_state.early_warning_seconds = physical_crash_time - st.session_state.ai_detection_time

                warning_timer_box.metric(
                    label="⏱️ AI EARLY WARNING TIME SECURED", 
                    value=f"{st.session_state.early_warning_seconds:.4f} sec",
                    delta="CRITICAL PROTECTION MARGIN",
                    delta_color="inverse"
                )

                if not st.session_state.paused_triggered:
                    with interactive_button_space:
                        if st.button("▶️ Intercept Anomaly & Continue Simulation", type="primary"):
                            st.session_state.current_frame = index + 1
                            st.session_state.paused_triggered = True
                            interactive_button_space.empty() 
                            st.rerun()
                    st.stop() 
                
            else:
                system_status_bar.error(f"SYSTEM HEALTH: COLLAPSE FORECAST DETERMINED  \nCollaspe Probablity : {collaspe*100:.4f} %")
                make_slow = True

                warning_timer_box.metric(
                    label="BREACH INTERCEPT TIME", 
                    value=f"{st.session_state.early_warning_seconds:.4f} sec",
                    delta="ACTIONABLE RESPONSE WINDOW",
                    delta_color="inverse"
                )

            window = data_frame.iloc[max(0,index-10000):index+1]
            df_value = row["Frequency_Change"]
            graph.line_chart(window["Frequency_Change"])
            value.metric(label = "Frequency Change",
                            value = f"{df_value:.4f} Hz",
                            delta=f"{row['Frequency_Change'] - data_frame.iloc[index-20]['Frequency_Change']:.4f} vs PREVIOUS FRAME")
            
            probablity_value.metric(label = "Collaspe Probablity",
                            value = f"{collaspe*100:.4f} %")
            probablity_curve.line_chart(st.session_state.probablity_history)
            

            with feature_part:
                RoCoF.metric(label = "RoCoF (Velocity)",
                            value = f"{row["RoCoF"]:.4f} Hz/sec",
                            delta=f"{row['RoCoF'] - data_frame.iloc[index-20]['RoCoF']:.4f} vs PREVIOUS FRAME")
                
                Frequency_Accleration.metric(label = "Frequency Accleration",
                            value = f"{row["Frequency_Accleration"]:.4f} Hz/sec2",
                            delta=f"{row['Frequency_Accleration'] - data_frame.iloc[index-1]['Frequency_Accleration']:.4f} vs PREVIOUS FRAME")
                Cumulative_Drop.metric(label = "Cumulative Drop (Electrical Stress)",
                                    value = f"{row["Cumulative_Drop"]:4f}",
                                    delta=f"{row['Cumulative_Drop'] - data_frame.iloc[index-1]['Cumulative_Drop']:.4f} vs PREVIOUS FRAME")        

            
            if make_slow :
                time.sleep(0.00001)
            else :
                time.sleep(0.00001)