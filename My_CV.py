import streamlit as st
import pandas as pd
import numpy as np

# --- 1. 頁面基礎設定 (必須放在第一行) ---
st.set_page_config(
    page_title="RF Engineer Tech Resume",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded" # 預設展開側邊欄
)

# --- 2. 進階 CSS 樣式 (海軍藍主題 + 懸浮視窗 + 側邊欄美化) ---
st.markdown("""
    <style>
    /* --- 全域配色設定 --- */
    .stApp {
        background-color: #0a192f; /* 深海軍藍背景 */
    }
    
    /* 文字顏色 */
    h1, h2, h3, h4, h5, h6 {
        color: #64ffda !important; /* 科技青色標題 */
        font-family: 'Segoe UI', sans-serif;
    }
    p, div, span, li, label, small {
        color: #ccd6f6 !important; /* 淺灰白內文 */
    }
    
    /* --- 側邊欄 (Sidebar) 樣式 --- */
    [data-testid="stSidebar"] {
        background-color: #112240; /* 比背景稍亮的深藍 */
        border-right: 1px solid #233554;
    }
    
    /* 按鈕樣式 (仿儀表板開關) */
    .stButton > button {
        background-color: #112240;
        color: #64ffda;
        border: 1px solid #233554;
        border-radius: 8px;
        padding: 15px 10px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .stButton > button:hover {
        background-color: #64ffda;
        color: #0a192f;
        border-color: #64ffda;
        transform: translateY(-2px);
    }
    
    /* 分隔線 */
    hr {
        border-color: #233554;
        margin-top: 2rem;
        margin-bottom: 2rem;
    }

    /* --- Tooltip (懸浮視窗) 核心樣式 --- */
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: help;
        border-bottom: 2px dashed #64ffda;
        padding-bottom: 2px;
        transition: color 0.3s;
    }
    
    .tooltip:hover {
        color: #64ffda !important;
    }

    /* 隱藏的詳細內容框 */
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 500px; 
        background-color: #172a45;
        color: #ccd6f6;
        text-align: left;
        border: 1px solid #64ffda;
        border-radius: 6px;
        padding: 15px;
        position: absolute;
        z-index: 1000;
        bottom: 140%; 
        left: 50%;
        margin-left: -250px;
        opacity: 0;
        transition: opacity 0.3s;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.7);
        font-size: 0.95rem;
        line-height: 1.6;
    }

    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }

    .tooltip .tooltiptext::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: #64ffda transparent transparent transparent;
    }
    
    .tooltiptext strong {
        color: #64ffda !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 側邊欄：個人資訊 ---
with st.sidebar:
    #st.image("https://api.dicebear.com/9.x/avataaars/svg?seed=Felix&clothing=blazerAndShirt&glasses=prescription02", width=150)
    
    st.title("Jacobs Ting")
    st.markdown("**Senior RF Engineer**")
    st.markdown("*Technical Deputy Manager*")
    
    st.markdown("---")
    
    st.markdown("#### 📬 Contact Info")
    st.markdown("**📍 Address:**")
    st.caption("Tucheng Dist., New Taipei City")
    
    st.markdown("**📧 Email:**")
    st.caption("ppttding0205@gmail.com")
    
    st.markdown("**📱 Mobile:**")
    st.caption("+886 0921532391")
    
    st.markdown("---")
    
    st.markdown("#### 🎓 Education")
    st.markdown("**Master's Degree**")
    st.caption("National Chung Hsing University (NCHU)")
    st.caption("Major in Electronics / Communication System")
    
    st.markdown("---")
    
    st.download_button(
        label="📄 Download PDF Resume",
        data="PDF_DATA",
        file_name="Jacobs_Ting_Resume.pdf",
        mime="application/pdf"
    )

# --- 4. 狀態管理 ---
if 'active_folder' not in st.session_state:
    st.session_state.active_folder = 'Intro'

def set_folder(folder_name):
    st.session_state.active_folder = folder_name

# --- 5. 主畫面標題區 ---
st.title("A RF Engineer | An AI Commander")
st.caption("17 Years Exp. | 5G-NR/WiFi/GNSS/NFC/RFID Expert | Automating RF tool Development with AI Vibe Code")
st.write("") 

# --- 6. 導航儀表板 ---
col1, col2, col3 = st.columns(3, gap="medium")
with col1:
    if st.button("📁 Professional\nExperience", use_container_width=True):
        set_folder("Experience")
with col2:
    if st.button("📁 Important\nProject", use_container_width=True):
        set_folder("Project")
with col3:
    if st.button("📁 AI-Assisted RF\nTool Dev", use_container_width=True):
        set_folder("RFTool")

st.write("")
spacer_l, col_mid1, col_mid2, spacer_r = st.columns([1, 1.5, 1.5, 1], gap="medium")
with col_mid1:
    if st.button("📁 Main\nSkill", use_container_width=True):
        set_folder("Skills")
with col_mid2:
    if st.button("📁 Personal\nStatement", use_container_width=True):
        set_folder("Statement")

st.markdown("---")

# --- 7. 內容顯示邏輯 ---
folder = st.session_state.active_folder

# === 首頁 Intro ===
if folder == 'Intro':
    st.markdown("### 👋 Welcome to My Digital Workspace")
    st.info("👈 左側欄位包含我的詳細聯絡資訊。")
    st.info("👆 請點擊上方導航面板，查看我的詳細履歷與技術展示。")
    st.markdown("""
    這是一個使用 **Python & Streamlit** 建構的互動式履歷。
    展示了我如何將傳統射頻工程 (RF Engineering) 與現代程式技術 (Coding) 結合，
    創造更高效的自動化工作流程。
    """)

# === 工作經歷 Experience ===
elif folder == 'Experience':
    st.header("💼 Professional Experience")
    st.caption("💡 Tip: Hover your mouse over the **Job Titles** below to see details.")
    st.write("") 

    def create_tooltip_html(title, period, company, products, responsibility, contribution):
        # 使用緊湊的 HTML 字串以避免語法錯誤
        html_content = f"""
        <div style="margin-bottom: 30px;">
            <div class="tooltip">
                <span style="font-size: 1.4rem; font-weight: 700; border-bottom: 2px solid #233554; padding-bottom: 5px;">{title}</span>
                <span style="font-size: 1rem; color: #8892b0; margin-left: 10px;">({period})</span>
                <span class="tooltiptext">
                    <strong>🏢 Company:</strong> {company}<br>
                    <strong>📡 Products:</strong> {products}<br>
                    <div style="margin: 10px 0; border-bottom: 1px solid #233554;"></div>
                    <strong>🛠 Key Responsibilities:</strong><br>
                    <span style="font-size: 0.9rem; color: #a8b2d1;">{responsibility}</span>
                    <div style="margin: 10px 0; border-bottom: 1px dashed #64ffda; opacity: 0.5;"></div>
                    <strong>🏆 Key Contribution:</strong><br>
                    <span style="font-size: 0.95rem; color: #fff;">{contribution}</span>
                </span>
            </div>
        </div>
        """
        return html_content

    # 經歷 1
    st.markdown(create_tooltip_html(
        title="Technical Deputy Manager & Team Lead",
        period="2022 ~ Present",
        company="Wistron / FIT(Present)",
        products="5G NR Handheld Device / WiFi 6E Device / BT wearable device",
        responsibility="• Leading a 4-person RF team.<br>• RFI/RFQ Process.<br>• RF System Architecture Plan.<br>• Cross-Departmental Coordination.<br>• Communicating With Customers.<br>• AI-Assisted Design Tool Development.",
        contribution="★ <b>Python Automation:</b> Developed AI-assisted tools reducing simulation time by 30%.<br>★ <b>Talent Growth:</b> Mentored 2 junior engineers to Senior level."
    ), unsafe_allow_html=True)

    # 經歷 2
    st.markdown(create_tooltip_html(
        title="Project Lead / Independent Contributor",
        period="2017 ~ 2021",
        company="Merry / USI / Liteon",
        products="IoT Sensors and Gateway / RF SiP module",
        responsibility="• Schematic and layout design.<br>• Project schedule control.<br>• Zero critical bugs in mass production.<br>• Resolved critical EMI/EMC issues.",
        contribution="★ <b>Zero Bugs:</b> Achieved mass production with zero critical RF issues.<br>★ <b>Cost Down:</b> Optimized BOM cost by 15% through alternative component sourcing."
    ), unsafe_allow_html=True)

    # 經歷 3
    st.markdown(create_tooltip_html(
        title="Senior RF Engineer & Core Member",
        period="2008 ~ 2016",
        company="FIH",
        products="4G SmartPhone",
        responsibility="• RF matching and Layout optimization.<br>• BOM control and Maintain.<br>• RF Performance Validation and Debug.<br>• Improved mass production yield rate to 98%.",
        contribution="★ <b>Yield Improvement:</b> Solved critical EMI issues, boosting yield from 85% to 98%."
    ), unsafe_allow_html=True)

# === 重要專案 Project ===
elif folder == 'Project':
    st.header("🏆 Important Project: 5G NR Rugged Device")
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        #### Project Overview
        A Smart, rugged device with 5G NR and support ENDC, 4-Tx SRS. 
        This 5G NR solution delivers industry-leading reception capabilities by combining EN-DC throughput with a High-integrated antenna array. 
        Through the implementation of 4-Tx SRS switching, the system provides superior channel estimation, ensuring stable, high-speed connectivity even in high-mobility or weak-signal scenarios.
        The system also provide long time for Emergency call and keep stable connection at extreme condition.
        
        #### Key Achievements
        * 🚀 **Low power consumption** for 5G NG operation.
        * 🌡️ **High pass yield** for MP stage.
        * 📉 **Long Life cycle** with discrete components design. 
        """)
    with c2:
        st.info("Technical Keywords")
        st.markdown("""
        * 5G NR FR1
        * Non standalone for ENDC technology
        * Sounding reference signal for 4 Tx
        * Over-the-Air (OTA) Testing
        """)

# === RF 工具開發 RFTool (已更新分頁展示) ===
elif folder == 'RFTool':
    st.header("📡 AI-Assisted RF Tool Development")
    st.markdown("""
    This section showcases the Python automation tools I developed. 
    Designed to streamline the tedious calculations and optimization processes in traditional RF design. 
    Please click the tabs below to view details of each tool：
    """)
    
    # 建立四個分頁 (Tabs)
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Link Budget", 
        "⚡ PA Nonlinear", 
        "🌊 AI Filter", 
        "🎯 Auto Matching"
    ])

    # --- Tool 1: Link Budget ---
    with tab1:
        st.subheader("1. Link Budget Evaluation Tool")
        st.caption("System-Level RF Performance Calculator")
        
        col1, col2 = st.columns([1.5, 1])
        with col1:
            # 第一個影片欄位：Tx
            st.markdown("**Tx Link Budget Analysis**")
            st.video("Tx_Link_Budget.mp4")
            
            # 第二個影片欄位：Rx
            st.markdown("**Rx Link Budget Analysis**")
            st.video("Rx_Link Budget.mp4")
            # 準備好影片後，把上面那行註解掉，換成下面這行：
            # st.video("Rx_Link_Budget.mp4")
            
            # 第三個影片欄位：大規模衰減預估
            st.markdown("**Large-Scale Fading Estimation**")
            st.video("Loss.mp4")
            # 準備好影片後，把上面那行註解掉，換成下面這行：
            # st.video("Fading_Estimation.mp4")
            
        with col2:
            # 加入了 Rx Link Budget 與 大規模衰減預估
            st.markdown("""
            **Key Features:**
            * **Cascaded Analysis:** 自動計算各級串聯後的 Gain, NF, P1dB, OIP3。
            * **Rx Link Budget:** 接收端 (Rx) 鏈路預算分析，評估系統串聯雜訊指數 (Cascaded NF) 與訊噪比 (SNR)。
            * **Sensitivity Check:** 快速評估接收機靈敏度是否符合 5G/WiFi 規範。
            * **Large-Scale Fading Estimation:** 大規模衰減預估，結合路徑損失 (Path Loss) 模型計算覆蓋範圍與通訊距離。
            * **Visualization:** 圖形化顯示各級 Power Level 變化。
            """)

    # --- Tool 2: PA Nonlinear ---
    with tab2:
        st.subheader("2. PA Nonlinear Simulation Tool")
        st.caption("Power Amplifier Behavioral Modeling & DPD")
        
        col1, col2 = st.columns([1.5, 1])
        with col1:
            st.video("PA_EVM.mp4")
            # 範例: st.video("pa_sim_demo.mp4")
            
        with col2:
            st.markdown("""
            **Key Features:**
            * **AM-AM / AM-PM Plotting:** 模擬 PA 在高功率下的非線性失真。
            * **EVM Prediction:** 預估在特定 Modulation (如 256QAM) 下的 EVM 表現。
            * **DPD Pre-simulation:** 驗證數位預失真 (Digital Pre-Distortion) 演算法效果。
            """)

    # --- Tool 3: AI Filter ---
    with tab3:
        st.subheader("3. AI Filter Design Tool")
        st.caption("Intelligent Filter Topology Synthesis")
        
        col1, col2 = st.columns([1.5, 1])
        with col1:
            st.video("Auto_Filter.mp4")
            # 範例: st.image("filter.png")
            
        with col2:
            st.markdown("""
            **Key Features:**
            * **Spec to Circuit:** 輸入頻率與抑制規格，AI 自動推薦最佳濾波器架構。
            * **Component Optimization:** 自動計算 L/C 元件值與 Q 值影響。
            * **Layout Prediction:** 初步估算微帶線 (Microstrip) 尺寸。
            """)

    # --- Tool 4: Auto Matching ---
    with tab4:
        st.subheader("4. Automatic Impedance Matching Tool")
        st.caption("Smith Chart Based Smart Matching")
        
        col1, col2 = st.columns([1.5, 1])
        with col1:
            st.video("Auto_Smith.mp4")
            # 範例: st.video("matching.mp4")
            
        with col2:
            st.markdown("""
            **Key Features:**
            * **Visual Smith Chart:** 互動式史密斯圖，即時顯示阻抗軌跡。
            * **Auto-Tuning:** 演算法自動尋找最佳 L/C 組合以達到中心頻率 50 Ohm 匹配。
            * **Broadband Opt:** 針對寬頻需求進行多節匹配優化。
            """)

# === 技能 Skills (含懸浮詳細說明) ===
elif folder == 'Skills':
    st.header("🛠️ Main Tech Stack & Soft Skills")
    
    def skill_bar(title, score, detail):
        st.markdown(f"""
        <div style="margin-bottom: 5px;">
            <div class="tooltip">
                <span style="font-size: 1rem; font-weight: 500; color: #ccd6f6; border-bottom: 1px dotted #64ffda; cursor: help;">{title}</span>
                <span class="tooltiptext" style="width: 300px; margin-left: -150px; bottom: 125%; font-size: 0.85rem;">
                    {detail}
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.progress(score)

    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.subheader("📡 RF Domain")
        st.caption("Hover over skills for details")
        skill_bar("RF Circuit Design", 95, "<strong>Schematic:</strong> ORCAD<br><strong>Layout:</strong> Allegro / PADS")
        skill_bar("System Analysis & Link Budget", 90, "<strong>Tools:</strong> Python / MATLAB<br><strong>Analysis:</strong> NF / IP3 / Gain")
        skill_bar("RF Simulation", 85, "<strong>EM Solver:</strong> Ansys HFSS<br><strong>Circuit:</strong> Keysight ADS")
        skill_bar("RF Issue Troubleshooting", 80, "<strong>Instruments:</strong> VSA, VNA, MT8000, CMW500")
        
    with col2:
        st.subheader("💻 Software & AI")
        st.caption("Hover over skills for details")
        skill_bar("AI LLM Application", 90, "<strong>API:</strong> OpenAI / Claude<br><strong>Framework:</strong> LangChain")
        skill_bar("Prompt Engineering", 85, "<strong>Techniques:</strong> CoT, Few-Shot, ReAct")
        skill_bar("Machine Learning Basics", 70, "<strong>Libraries:</strong> Scikit-learn, Pandas")
        skill_bar("Git / Version Control", 75, "<strong>Platform:</strong> GitHub / GitLab")

    st.markdown("---")
    
    col3, col4 = st.columns(2, gap="medium")
    with col3:
        st.subheader("🧠 Soft Skills")
        st.write("🗣️ **Communication & Coordination**")
        st.progress(90)
        st.write("🦁 **Leadership & Mentoring**")
        st.progress(85)
        st.write("💡 **Logical Analysis**")
        st.progress(95)

    with col4:
        st.subheader("🌐 Languages")
        st.write("🇹🇼 **Mandarin Chinese** (Native)")
        st.progress(100)
        st.write("🇺🇸 **English** (Professional)")
        st.progress(80)

# === 個人陳述 Statement ===
elif folder == 'Statement':
    st.header("📝 A RF Engineer in the Age of AI")
    st.markdown("""
    I joined the RF system design field in 2008. At that time, the most advanced commercial communication technology was UMTS, offering data rates of around 12 Mbps, while Wi-Fi 802.11a/g provided up to 54 Mbps. Back then, it genuinely felt as though these technologies were approaching the practical limits of commercial wireless systems.

Seventeen years later, the landscape has transformed dramatically. Today, 5G NR systems can deliver peak throughputs of nearly 20 Gbps, and Wi-Fi 7 (802.11be) pushes this even further to around 40 Gbps. Throughout this journey, I have witnessed—firsthand—the rapid adoption of increasingly sophisticated technologies and theories: MIMO, OFDM, massive antenna arrays, and ultra-high-order modulation schemes such as 1024-QAM and 4096-QAM. Each generation has brought exponential gains in performance, but also exponential growth in system complexity.

This rising complexity presents a fundamental challenge. Traditional “trial-and-error” approaches, or optimization driven purely by engineering intuition, are no longer sufficient for systems governed by thousands of tightly coupled parameters. This is where Artificial Intelligence enters the RF domain—not as a replacement for RF engineers, but as a powerful and necessary partner.

To truly master modern RF systems, engineers must evolve from manual tuning toward intelligent automation. Machine learning techniques, for example, can accurately model the strong nonlinear behavior of power amplifiers operating under 4096-QAM waveforms, enabling Digital Pre-Distortion (DPD) performance far beyond what conventional polynomial methods can achieve. Similarly, AI-based surrogate models can dramatically shorten design cycles by predicting EM simulation results or optimizing impedance-matching networks in seconds rather than hours.

In this new era, the value of an RF engineer is no longer defined solely by circuit intuition or analytical derivations. It lies in the ability to curate meaningful data, understand the underlying physics, and architect AI models that can tame system-level complexity—transforming the apparent chaos of 5G and Wi-Fi 7 into precise, reliable, and manufacturable performance.
    """)