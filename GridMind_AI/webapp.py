# py -m streamlit run webapp.py


# NOTE : Load hits at around 350 frame
# NOTE : Streamlit Pauses at around 0.0472 Hz df

from functions_styles.functions import custom_sidebar
from sidebar_pages.vision_terminal import vision_terminal
from sidebar_pages.system_objectives import system_objectives
from sidebar_pages.about_author import about_author
from functions_styles.functions import custom_sidebar

options = custom_sidebar()

def show_vision_terminal():
    vision_terminal()

def show_system_objectives():
    system_objectives()

def show_about_author():
    about_author()

if options == "VISION TERMINAL":
    show_vision_terminal()

if options == "SYSTEM OBJECTIVES":
    show_system_objectives()

if options == "ABOUT AUTHOR":
    show_about_author()

