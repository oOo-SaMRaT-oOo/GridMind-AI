from scipy.io import loadmat
import pandas as pd
import numpy as np
import streamlit as st

def processing_mat_file(file_name,is_recovery):

    raw_data = loadmat(file_name)
    t = raw_data["t"].squeeze()
    df = raw_data["df"].squeeze()
    df_set = pd.DataFrame({"Time": t, "Frequency_Change": df})
    dt = df_set["Time"].diff().mean()
    df_set["RoCoF"] = df_set["Frequency_Change"].diff() / dt
    df_set["Frequency_Accleration"] = df_set["RoCoF"].diff() / dt
    df_set["df_RollingMean"] = df_set["Frequency_Change"].ewm(span=20,
                                                                  adjust=False).mean()
    df_set["Cumulative_Drop"] = df_set["Frequency_Change"].ewm(span = 50,
                                                    adjust = False).mean() * dt * 50
    df_set["RoCoF_Variance"] = df_set["RoCoF"].ewm(span = 5,adjust = False).var().fillna(0)
    df_set["RoCoF_Elasticity"] = df_set["Frequency_Accleration"]/df_set["RoCoF"]
    df_set["RoCoF_Elasticity"] = df_set["RoCoF_Elasticity"].replace([np.inf, -np.inf], 0).fillna(0)

    if is_recovery:
        df_set["Collaspe_Risk"] = 0

    else:
        threshold = df_set[df_set["Frequency_Change"] <= -0.05]["Time"].min()
        df_set["Collaspe_Risk"] = (df_set["Time"]>=threshold).astype(int)

    return df_set.dropna()



def custom_sidebar():
    """
    Renders an engineering-grade, hover-expanding tactical sidebar navigation panel 
    synchronized with the 'Share Tech Mono' cyber matrix design. Default state initialized as open.
    """
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
    
    <style>
        /* =========================================================
            REMOVE STREAMLIT DEFAULT UI CHASSIS ELEMENTS
        ========================================================= */
        button[kind="header"],
        [data-testid="stSidebarNavCollapseButton"],
        [data-testid="collapsedControl"],
        [data-testid="baseButton-header"],
        [data-testid="stSidebarCollapseButton"],
        header[data-testid="stHeader"],
        header[data-testid="stSidebarHeader"],
        div[role="tooltip"] {
            display: none !important;
            visibility: hidden !important;
        }

        /* =========================================================
            TACTICAL SIDEBAR CHASSIS BASE STYLING (DEFAULT: OPEN)
        ========================================================= */
        [data-testid="stSidebar"] {
            width: 300px !important;
            min-width: 300px !important;
            background: rgba(10, 18, 32, 0.95) !important;
            backdrop-filter: blur(25px);
            border-right: 2px solid rgba(0, 240, 255, 0.6);
            box-shadow: 0 0 30px rgba(0, 240, 255, 0.25),
                        0 0 60px rgba(0, 114, 255, 0.1);
            overflow-x: hidden !important;
            transition: width 0.3s cubic-bezier(0.15, 0.85, 0.45, 1), 
                        min-width 0.3s cubic-bezier(0.15, 0.85, 0.45, 1), 
                        box-shadow 0.3s ease,
                        border-right 0.3s ease;
            padding-top: 20px;
        }

        /* =========================================================
            COLLAPSED STATE ONCE MOUSE LEAVES (ANTI-CUTOFF DETECT)
        ========================================================= */
        [data-testid="stSidebar"]:not(:hover) {
            width: 80px !important;
            min-width: 80px !important;
            box-shadow: none !important;
            border-right: 2px solid rgba(0, 240, 255, 0.25);
        }

        /* =========================================================
            GLOBAL MATRIX FONT INTEGRATION
        ========================================================= */
        [data-testid="stSidebar"] * {
            font-family: 'Share Tech Mono', monospace !important;
            color: #38b6ff !important;
        }

        [data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
            display: none !important;
        }

        /* =========================================================
            CYBER RADIO DECK MODULES
        ========================================================= */
        .stRadio > div {
            gap: 14px;
            padding: 20px 10px 0 10px !important;
        }

        .stRadio label {
            display: flex !important;
            align-items: center !important;
            justify-content: flex-start !important;
            width: 100% !important;
            min-height: 60px !important;
            height: 60px !important;
            background: rgba(0, 114, 255, 0.04);
            border: 1px solid rgba(0, 240, 255, 0.15);
            padding: 10px 16px !important;
            border-radius: 8px;
            transition: all 0.3s cubic-bezier(0.15, 0.85, 0.45, 1);
            cursor: pointer;
            margin-bottom: 8px;
            box-sizing: border-box !important;
            overflow: hidden !important;
            filter: blur(0px);
            opacity: 1;
        }

        .stRadio label:hover {
            transform: translateX(4px);
            background: rgba(0, 240, 255, 0.08);
            border: 1px solid rgba(0, 240, 255, 0.5);
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.3);
        }

        .stRadio label:has(input:checked) {
            background: rgba(0, 240, 255, 0.12);
            border: 1px solid #00f0ff;
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.4), inset 0 0 8px rgba(0, 240, 255, 0.2);
        }

        .stRadio p {
            font-size: 16px !important;
            font-weight: 600 !important;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: #ffffff !important;
            text-shadow: 0 0 8px rgba(0, 240, 255, 0.6);
            margin: 0 0 0 15px !important;
            white-space: pre !important;
            opacity: 1;
            transition: opacity 0.2s ease, transform 0.2s ease;
        }

        /* =========================================================
            REMOVE RADIO BUTTON INDICATORS COMPLETELY
        ========================================================= */
        .stRadio input[type="radio"] {
            display: none !important;
        }

        .stRadio label > div:first-child {
            display: none !important;
        }

        .stRadio label {
            gap: 0 !important;
        }

        /* =========================================================
            DYNAMIC CONCENTRIC BLUR & FADE WHEN NOT ENGAGED
        ========================================================= */
        [data-testid="stSidebar"]:not(:hover) .stRadio label {
            justify-content: center !important;
            align-items: center !important;
            padding: 0 !important;
            transform: none !important;
            width: 45px !important;
            height: 45px !important;
            margin-left: auto !important;
            margin-right: auto !important;
            
            background: rgba(0, 240, 255, 0.01) !important;
            border-color: rgba(0, 240, 255, 0.08) !important;
            box-shadow: none !important;
            filter: blur(2px);
            opacity: 0.35;      
        }

        [data-testid="stSidebar"]:not(:hover) .stRadio label:has(input:checked) {
            background: rgba(0, 240, 255, 0.05) !important;
            border-color: rgba(0, 240, 255, 0.3) !important;
            filter: blur(1.5px);
            opacity: 0.6;
        }

        [data-testid="stSidebar"]:not(:hover) .stRadio p {
            opacity: 0 !important;
            display: none !important;
            width: 0 !important;
            margin: 0 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        selection = st.radio(
            "Navigation",
            ["VISION TERMINAL", "SYSTEM OBJECTIVES", "ABOUT AUTHOR"],
            label_visibility="collapsed"
        )

    return selection