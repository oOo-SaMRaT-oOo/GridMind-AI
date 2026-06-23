import streamlit as st

def header_text(text, font_size="clamp(32px, 6vw, 75px)"):
    """
    Renders an engineering-grade sci-fi cyber header with intensified glowing properties,
    and a synchronized electrical shock loop that flashes yellow lightning emojis (⚡) 
    at the exact moment of a power surge.
    """
    st.markdown(
        f"""
        <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">

        <style>
        /* Container cleanup to override default Streamlit card metrics padding */
        [data-testid="stVerticalBlock"] > div:has(div.stMarkdown) {{
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            padding: 0 !important;
        }}

        .cyber-title {{
            position: relative;
            font-family: 'Share Tech Mono', monospace !important;
            font-size: {font_size} !important; 
            font-weight: 700;
            line-height: 1.1;
            margin: 0;
            padding: 15px 0;
            text-align: center;
            letter-spacing: 3px;
            text-transform: uppercase;
            display: inline-block;
            width: 100%;
            
            /* High-Contrast Cyber Matrix Gradient */
            background: linear-gradient(90deg, #00f0ff, #38b6ff, #ffffff, #38b6ff, #00f0ff);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            
            /* ENHANCED GLOW CORE: Layering drop-shadows straight onto the text base */
            filter: drop-shadow(0 0 8px rgba(0, 240, 255, 0.6)) 
                    drop-shadow(0 0 20px rgba(0, 114, 255, 0.4));
            
            /* Multi-layered Laser and Electric Shock Core Animations */
            animation: 
                cyberBoot 1.2s cubic-bezier(0.15, 0.85, 0.45, 1) forwards,
                laserSurge 5s linear infinite,
                electricShock 4s linear infinite; 
        }}

        /* 🌟 SYNCHRONIZED LIGHTNING SHOCK SPARKS (Left & Right) */
        .cyber-title::before, .cyber-title::after {{
            content: "⚡";
            position: absolute;
            top: 50%;
            transform: translateY(-50%) scale(0);
            font-size: 0.8em;
            opacity: 0;
            filter: drop-shadow(0 0 10px #ffea00) drop-shadow(0 0 20px #ff9900);
            pointer-events: none;
            transition: all 0.1s ease;
            
            /* Attaching the exact same 4s structural animation engine */
            animation: lightningBurst 4s linear infinite;
        }}
        
        /* Position left side spark */
        .cyber-title::before {{
            left: 5%;
        }}
        
        /* Position right side spark */
        .cyber-title::after {{
            right: 5%;
        }}

        /* Boot up slide-in with digital artifact opacity settling */
        @keyframes cyberBoot {{
            0% {{
                opacity: 0; 
                transform: translateY(-20px) scale(0.95);
                filter: blur(5px) drop-shadow(0 0 0px transparent);
            }}
            100% {{
                opacity: 1; 
                transform: translateY(0) scale(1);
                filter: blur(0) drop-shadow(0 0 8px rgba(0, 240, 255, 0.6));
            }}
        }}

        /* Energy/Electricity surge passing through the text smoothly */
        @keyframes laserSurge {{
            to {{ background-position: 200% center; }}
        }}

        /* OPTIMIZED HIGH-ILLUMINATION SHOCK ENGINE */
        @keyframes electricShock {{
            0%, 90%, 94%, 98%, 100% {{
                transform: skew(0deg) scale(1);
                filter: drop-shadow(0 0 8px rgba(0, 240, 255, 0.7)) 
                        drop-shadow(0 0 20px rgba(0, 114, 255, 0.4));
                -webkit-text-fill-color: transparent;
                opacity: 1;
            }}
            /* First shock wave: Extreme high-voltage plasma overload */
            91% {{
                transform: skew(4deg) translateX(-2px);
                filter: drop-shadow(-3px 0 #ffffff) 
                        drop-shadow(0 0 25px #00f0ff) 
                        drop-shadow(0 0 50px #0072ff);
                -webkit-text-fill-color: #ffffff; 
                opacity: 1;
            }}
            /* Second shock wave: High frequency grid warp */
            92% {{
                transform: skew(-6deg) translateX(3px);
                filter: drop-shadow(3px 0 #00f0ff) 
                        drop-shadow(0 0 35px #00f0ff)
                        drop-shadow(0 0 60px #0072ff);
                -webkit-text-fill-color: transparent;
                opacity: 0.95;
            }}
            /* Micro-flicker: Stable radiant illumination */
            93% {{
                opacity: 0.85;
                transform: skew(0deg);
                filter: drop-shadow(0 0 15px #ffffff) drop-shadow(0 0 30px #00f0ff);
            }}
            /* Recovery arc snapshot */
            95% {{
                transform: skew(8deg) scaleY(1.05);
                filter: drop-shadow(-2px 0 #ffffff) drop-shadow(0 0 25px #00f0ff);
                opacity: 1;
            }}
            /* Quick final trace stabilization */
            96% {{
                opacity: 0.90;
                transform: skew(-1deg);
                filter: drop-shadow(0 0 20px #00f0ff);
            }}
        }}

        /* 🌟 LIGHTNING TIMELINE SYNCHRONIZATION */
        @keyframes lightningBurst {{
            0%, 90%, 97%, 100% {{
                transform: translateY(-50%) scale(0);
                opacity: 0;
            }}
            /* Surge Hit: Emojis grow rapidly and glow intensely */
            91% {{
                transform: translateY(-50%) scale(1.3) rotate(-10deg);
                opacity: 1;
            }}
            /* Alternating arc movement */
            93% {{
                transform: translateY(-52%) scale(1.1) rotate(15deg);
                opacity: 0.9;
            }}
            /* Snap layout recovery */
            95% {{
                transform: translateY(-48%) scale(1.4) rotate(-5deg);
                opacity: 1;
            }}
        }}
        </style>

        <div class="cyber-title">{text}</div>
        """,
        unsafe_allow_html=True
    )

def glowing_line_1(color_vibe="nominal"):
    """
    Renders an animated, glowing laser-line divider instead of a standard st.write("---").
    :param color_vibe: "nominal" (cyan/blue), "warning" (orange), or "critical" (red/magenta)
    """
    # Map the color vibe to matching cyber palettes
    if color_vibe == "warning":
        primary_color = "#ff9900"
        secondary_color = "#ff5500"
        glow_color = "rgba(255, 153, 0, 0.6)"
        far_glow = "rgba(255, 85, 0, 0.3)"
    elif color_vibe == "critical":
        primary_color = "#ff0055"
        secondary_color = "#990033"
        glow_color = "rgba(255, 0, 85, 0.7)"
        far_glow = "rgba(153, 0, 51, 0.4)"
    else:  # nominal state
        primary_color = "#00f0ff"
        secondary_color = "#0072ff"
        glow_color = "rgba(0, 240, 255, 0.6)"
        far_glow = "rgba(0, 114, 255, 0.3)"

    st.markdown(
        f"""
        <style>
        .laser-container {{
            padding: 10px 0;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }}

        .laser-line {{
            height: 2px;
            width: 100%;
            border-radius: 99px;
            
            /* High-voltage energy core gradient mapping */
            background: linear-gradient(90deg, 
                transparent 0%, 
                {primary_color} 15%, 
                #ffffff 50%, 
                {secondary_color} 85%, 
                transparent 100%
            );
            background-size: 200% auto;
            
            /* Concentrated neon tube emission shadows */
            box-shadow: 
                0 0 6px #ffffff,
                0 0 12px {glow_color},
                0 0 25px {far_glow};
                
            /* Kinetic flow animation to mimic active current running across the wire */
            animation: currentFlow 4s linear infinite;
        }}

        @keyframes currentFlow {{
            0% {{ background-position: 0% center; }}
            100% {{ background-position: 200% center; }}
        }}
        </style>

        <div class="laser-container">
            <div class="laser-line"></div>
        </div>
        """,
        unsafe_allow_html=True
    )


def sub_header_text(text, font_size="clamp(18px, 3.5vw, 28px)", status_label="HELLO"):
    """
    Renders a tactical telemetry-style sci-fi subheader with a unique runtime ID
    to ensure multiple instances maintain separate, distinct status labels.
    """
    # Create a clean, safe unique string key using the text and label hashes
    unique_id = f"sub-{abs(hash(text + status_label))}"
    
    st.markdown(
        f"""
        <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
        
        <style>
        /* Target ONLY this specific instance's container wrapper */
        .{unique_id}-container {{
            width: 100%;
            padding: 8px 0 0 0;
            margin-top: 5px;
            text-align: left;
        }}
        
        .{unique_id} {{
            position: relative;
            font-family: 'Share Tech Mono', monospace !important;
            font-size: {font_size} !important;
            font-weight: 600;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: #38b6ff;
            display: inline-block;
            margin: 0;
            filter: drop-shadow(0 0 4px rgba(56, 182, 255, 0.4));
        }}
        
        /* 🛰️ TELEMETRY PREFIX TARGETED EXACTLY TO THIS ID */
        .{unique_id}::before {{
            content: "{status_label} "; 
            font-size: 0.85em;
            vertical-align: middle;
            color: #00f0ff;
            margin-right: 12px;
            display: inline-block;
            
            /* Crucial text core shadows layered directly onto the prefix text */
            text-shadow: 0 0 4px #00f0ff, 0 0 10px rgba(0, 240, 255, 0.6);
            
            animation: rapidGlowFlicker 2s infinite linear;
        }}
        
        /* Keep keyframes global since they share the math engine layout */
        @keyframes rapidGlowFlicker {{
            0%, 100% {{ 
                opacity: 1; 
                text-shadow: 0 0 4px #00f0ff, 0 0 12px #00f0ff, 0 0 20px #0072ff;
                transform: skew(0deg);
            }}
            25% {{ 
                opacity: 0.85; 
                text-shadow: 0 0 2px #00f0ff, 0 0 6px #00f0ff;
            }}
            50% {{ 
                opacity: 0.95; 
                text-shadow: 0 0 6px #ffffff, 0 0 16px #00f0ff, 0 0 25px #38b6ff;
                transform: skew(0.5deg);
            }}
            75% {{ 
                opacity: 0.70; 
                text-shadow: 0 0 1px #00f0ff, 0 0 4px rgba(0, 240, 255, 0.3);
            }}
        }}
        </style>
        
        <div class=".{unique_id}-container">
            <h3 class="{unique_id}">{text}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

def glowing_line_2():
    """
    Renders a dedicated, asymmetric sci-fi laser underline that scales smoothly 
    on boot-up to complement the subheader telemetry deck layout.
    """
    st.markdown(
        """
        <style>
        .laser-sub-container {
            width: 100%;
            padding: 0;
            margin: 4px 0 12px 0;
            display: flex;
            justify-content: flex-start; /* Aligns line setup directly under left-justified text */
        }
        
        .laser-sub-line {
            height: 1px;
            width: 0%; /* Spawns at zero length for boot-up sweep animation */
            background: linear-gradient(90deg, #00f0ff, rgba(0, 240, 255, 0.3) 60%, transparent 100%);
            box-shadow: 0 0 8px rgba(0, 240, 255, 0.8);
            animation: subScannerDeploy 1.4s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
        }
        
        @keyframes subScannerDeploy {
            to { width: 45%; } /* Sweeps out to a deliberate tactical width profile */
        }
        </style>
        
        <div class="laser-sub-container">
            <div class="laser-sub-line"></div>
        </div>
        """,
        unsafe_allow_html=True
    )


def normal_text(text, font_size="clamp(14px, 2vw, 18px)"):
    """
    Renders a matching tactical telemetry-style sci-fi body text 
    without the flickering status prefix, maintaining style consistency.
    """
    st.markdown(
        f"""
        <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
        
        <style>
        .cyber-normal-container {{
            width: 100%;
            padding: 4px 0 0 0;
            margin-top: 2px;
            text-align: left;
        }}
        
        .cyber-normal {{
            font-family: 'Share Tech Mono', monospace !important;
            font-size: {font_size} !important;
            font-weight: 400;
            letter-spacing: 1px;
            color: #38b6ff;
            display: inline-block;
            margin: 0;
            filter: drop-shadow(0 0 4px rgba(56, 182, 255, 0.4));
        }}
        </style>
        
        <div class="cyber-normal-container">
            <p class="cyber-normal">{text}</p>
        </div>
        """,
        unsafe_allow_html=True
    )






def glowing_line_1(color_vibe="nominal"):
    """
    Renders an animated, glowing laser-line divider instead of a standard st.write("---").
    :param color_vibe: "nominal" (cyan/blue), "warning" (orange), or "critical" (red/magenta)
    """
    # Map the color vibe to matching cyber palettes
    if color_vibe == "warning":
        primary_color = "#ff9900"
        secondary_color = "#ff5500"
        glow_color = "rgba(255, 153, 0, 0.6)"
        far_glow = "rgba(255, 85, 0, 0.3)"
    elif color_vibe == "critical":
        primary_color = "#ff0055"
        secondary_color = "#990033"
        glow_color = "rgba(255, 0, 85, 0.7)"
        far_glow = "rgba(153, 0, 51, 0.4)"
    else:  # nominal state
        primary_color = "#00f0ff"
        secondary_color = "#0072ff"
        glow_color = "rgba(0, 240, 255, 0.6)"
        far_glow = "rgba(0, 114, 255, 0.3)"

    st.markdown(
        f"""
        <style>
        .laser-container {{
            padding: 10px 0;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }}

        .laser-line {{
            height: 2px;
            width: 100%;
            border-radius: 99px;
            
            /* High-voltage energy core gradient mapping */
            background: linear-gradient(90deg, 
                transparent 0%, 
                {primary_color} 15%, 
                #ffffff 50%, 
                {secondary_color} 85%, 
                transparent 100%
            );
            background-size: 200% auto;
            
            /* Concentrated neon tube emission shadows */
            box-shadow: 
                0 0 6px #ffffff,
                0 0 12px {glow_color},
                0 0 25px {far_glow};
                
            /* Kinetic flow animation to mimic active current running across the wire */
            animation: currentFlow 4s linear infinite;
        }}

        @keyframes currentFlow {{
            0% {{ background-position: 0% center; }}
            100% {{ background-position: 200% center; }}
        }}
        </style>

        <div class="laser-container">
            <div class="laser-line"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

def normal_text(text, font_size="clamp(14px, 2vw, 18px)"):
    """
    Renders a matching tactical telemetry-style sci-fi body text 
    without the flickering status prefix, maintaining style consistency.
    """
    st.markdown(
        f"""
        <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
        
        <style>
        .cyber-normal-container {{
            width: 100%;
            padding: 4px 0 0 0;
            margin-top: 2px;
            text-align: left;
        }}
        
        .cyber-normal {{
            font-family: 'Share Tech Mono', monospace !important;
            font-size: {font_size} !important;
            font-weight: 400;
            letter-spacing: 1px;
            color: #38b6ff;
            display: inline-block;
            margin: 0;
            filter: drop-shadow(0 0 4px rgba(56, 182, 255, 0.4));
        }}
        </style>
        
        <div class="cyber-normal-container">
            <p class="cyber-normal">{text}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def make_button_nice(font_style="modern"):
    """
    Renders an engineering-grade tactical console button with high-frequency 
    neon cyan glow matrix layouts and clean structural line geometry.
    
    Font options:
    - "modern": 'Orbitron' high-tech sans (Default)
    - "terminal": 'Share Tech Mono' digital data layout array
    """
    fonts = {
        "modern": {
            "family": "'Orbitron', sans-serif",
            "size": "20px",
            "weight": "700",
            "spacing": "3px"
        },
        "terminal": {
            "family": "'Share Tech Mono', monospace",
            "size": "22px",
            "weight": "600",
            "spacing": "2px"
        }
    }
    
    # Fallback default directly to dashboard design engine matrix
    font = fonts.get(font_style, fonts["terminal"])
    
    st.markdown(f"""
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800&family=Share+Tech+Mono&display=swap" rel="stylesheet">
    
    <style>
    /* IMPROVE TEXT RENDERING FOR ELECTRONIC CHASSIS INTEGRATION */
    div[data-testid="stButton"] > button {{
        text-rendering: geometricPrecision !important;
        -webkit-font-smoothing: antialiased !important;
        -moz-osx-font-smoothing: grayscale !important;
    }}

    /* STRUCTURE ALIGNMENT PASS CONTAINER BUFFER */
    div[data-testid="stButton"] {{
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        margin: 16px auto !important;
        padding: 0px !important;
        width: 100% !important;
    }}

    div.element-container:has(div[data-testid="stButton"]) {{
        margin: 0rem !important;
        padding: 0rem !important;
    }}

    /* TACTICAL SWITCH ASSEMBLY - HARDWARE TERMINAL FORM FACTOR */
    div[data-testid="stButton"] > button {{
        width: 340px !important;
        height: 65px !important;
        border-radius: 4px !important; /* Sharp industrial corners replace soft pill shapes */
        
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        text-align: center !important;
        
        /* Matte dark composite chassis core background */
        background: rgba(10, 18, 32, 0.95) !important;
        
        /* SYNCHRONIZED NEON REACTION GLOWS */
        color: #ffffff !important;
        text-shadow: 0 0 8px rgba(0, 240, 255, 0.8), 0 0 15px rgba(0, 114, 255, 0.4) !important;
        border: 1px solid rgba(0, 240, 255, 0.4) !important;
        
        position: relative !important;
        overflow: hidden !important;
        
        /* CORE PARAMETER ASSIGNMENT DATA STRINGS */
        font-family: {font['family']} !important;
        font-size: {font['size']} !important;
        font-weight: {font['weight']} !important;
        letter-spacing: {font['spacing']} !important;
        text-transform: uppercase !important;
        line-height: 1.2 !important;
        
        box-shadow: 0 0 12px rgba(0, 240, 255, 0.15),
                    inset 0 0 10px rgba(0, 240, 255, 0.05) !important;
        
        transition: all 0.25s cubic-bezier(0.15, 0.85, 0.45, 1) !important;
        cursor: pointer !important;
        white-space: nowrap !important;
        padding: 0 24px !important;
    }}

    /* Downstream styling pass over standard Streamlit markup sub-wrappers */
    div[data-testid="stButton"] > button *,
    div[data-testid="stButton"] > button span,
    div[data-testid="stButton"] > button p {{
        font-family: {font['family']} !important;
        color: #ffffff !important;
        text-align: center !important;
        display: inline-block !important;
        line-height: 1.2 !important;
    }}

    /* Dynamic high-frequency flicker overlay mirroring status label indicators */
    div[data-testid="stButton"] > button::before {{
        content: '' !important;
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        background: linear-gradient(180deg, transparent 0%, rgba(0, 240, 255, 0.03) 50%, transparent 100%) !important;
        opacity: 1;
        animation: consoleScanline 4s infinite linear;
        pointer-events: none !important;
    }}

    /* HOVER RECONGIGURATION DECK ATTACK */
    div[data-testid="stButton"] > button:hover {{
        transform: scale(1.02) !important;
        background: rgba(0, 114, 255, 0.08) !important;
        border-color: #00f0ff !important;
        text-shadow: 0 0 12px #00f0ff, 0 0 20px #0072ff !important;
        box-shadow: 0 0 25px rgba(0, 240, 255, 0.4),
                    inset 0 0 12px rgba(0, 240, 255, 0.2) !important;
    }}

    /* OPERATIONAL CLICK TRIGGER PHASE DEPLOYMENT */
    div[data-testid="stButton"] > button:active {{
        transform: scale(0.98) !important;
        background: rgba(0, 240, 255, 0.15) !important;
        border-color: #ffffff !important;
        box-shadow: 0 0 30px rgba(0, 240, 255, 0.6) !important;
        transition: all 0.05s ease !important;
    }}

    /* ACCESSIBILITY DECK LOCK BOUNDS */
    div[data-testid="stButton"] > button:focus {{
        outline: none !important;
        box-shadow: 0 0 0 2px rgba(0, 240, 255, 0.3), 0 0 20px rgba(0, 240, 255, 0.4) !important;
    }}

    /* Terminal monitor screen grid refresh line animation cycle */
    @keyframes consoleScanline {{
        0% {{ transform: translateY(-100%); }}
        100% {{ transform: translateY(100%); }}
    }}
    </style>
    """, unsafe_allow_html=True)
