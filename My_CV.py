import streamlit as st
import pandas as pd
import numpy as np

# --- 1. 頁面基礎設定 ---
st.set_page_config(
    page_title="RF Engineer Tech Resume",
    page_icon="📡",
    layout="wide"
)

# --- 2. 進階 CSS 樣式 (海軍藍主題 + 懸浮視窗 Tooltip) ---
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
    p, div, span, li, label {
        color: #ccd6f6 !important; /* 淺灰白內文 */
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
        border-bottom: 2px dashed #64ffda; /* 底部虛線提示可互動 */
        padding-bottom: 2px;
        transition: color 0.3s;
    }
    
    .tooltip:hover {
        color: #64ffda !important;
    }

    /* 隱藏的詳細內容框 */
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 400px;
        background-color: #172a45; /* 卡片背景色 */
        color: #ccd6f6;
        text-align: left;
        border: 1px solid #64ffda;
        border-radius: 6px;
        padding: 15px;
        
        /* 定位：出現在文字上方 */
        position: absolute;
        z-index: 1000;
        bottom: 140%; 
        left: 50%;
        margin-left: -200px; /* 寬度的一半，讓它置中 */
        
        /* 動畫效果 */
        opacity: 0;
        transition: opacity 0.3s;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.7);
        font-size: 0.95rem;
        line-height: 1.6;
    }

    /* 滑鼠移上去顯示 */
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }

    /* 小三角形箭頭 */
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
    
    /* 強制 tooltip 內的文字顏色 */
    .tooltiptext strong {
        color: #64ffda !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 狀態管理 (Session State) ---
if 'active_folder' not in st.session_state:
    st.session_state.active_folder = 'Intro' # 預設首頁

def set_folder(folder_name):
    st.session_state.active_folder = folder_name

# --- 4. 標題區 ---
c1, c2 = st.columns([0.1, 0.9])
with c1:
    st.image("https://cdn-icons-png.flaticon.com/512/2906/2906274.png", width=60) # 火箭圖示
with c2:
    st.title("A RF Engineer | An AI Commander")
    st.caption("17 Years Exp. | 5G mmWave Expert | Automating RF with Code")

st.write("") # 間距

# --- 5. 導航儀表板 (Layout) ---

# 上排：三個主要區塊
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

# 下排：兩個區塊 (使用空白欄位達成置中)
st.write("")
spacer_l, col_mid1, col_mid2, spacer_r = st.columns([1, 1.5, 1.5, 1], gap="medium")
with col_mid1:
    if st.button("📁 Main\nSkill", use_container_width=True):
        set_folder("Skills")
with col_mid2:
    if st.button("📁 Personal\nStatement", use_container_width=True):
        set_folder("Statement")

st.markdown("---")

# --- 6. 內容顯示邏輯 ---
folder = st.session_state.active_folder

# === 首頁 Intro ===
if folder == 'Intro':
    st.markdown("### 👋 Welcome to My Digital Workspace")
    st.info("👆 請點擊上方導航面板，查看我的詳細履歷與技術展示。")
    st.markdown("""
    這是一個使用 **Python & Streamlit** 建構的互動式履歷。
    展示了我如何將傳統射頻工程 (RF Engineering) 與現代程式技術 (Coding) 結合，
    創造更高效的自動化工作流程。
    """)

# === 工作經歷 Experience (含 Tooltip) ===
elif folder == 'Experience':
    st.header("💼 Professional Experience")
    st.caption("💡 Tip: Hover your mouse over the **Job Titles** below to see details.")
    st.write("") # Spacer

    # 輔助函式：產生帶有 Tooltip 的 HTML
    def create_tooltip_html(title, period, company, products, responsibility):
        return f"""
        <div style="margin-bottom: 30px;">
            <div class="tooltip">
                <span style="font-size: 1.4rem; font-weight: 700;">{title}</span>
                <span style="font-size: 1rem; color: #8892b0; margin-left: 10px;">({period})</span>
                <span class="tooltiptext">
                    <strong>🏢 Company:</strong> {company}<br>
                    <strong>📡 Products:</strong> {products}<br>
                    <div style="margin: 8px 0; border-bottom: 1px solid #233554;"></div>
                    <strong>🛠 Key Responsibilities:</strong><br>
                    {responsibility}
                </span>
            </div>
        </div>
        """

    # 經歷 1: 2022 - Present
    st.markdown(create_tooltip_html(
        title="Technical Deputy Manager & Team Lead",
        period="2022 ~ Present",
        company="Wistron / FIT(Present)",
        products="5G NR Handheld Device / WiFi 6E Device/ BT wearable device",
        responsibility="• Leading a 4-person RF team.<br>• RFI/RFQ Prograss.<br>• RF System Architecture Plan.<br>• Cross-Departmental Coordination.<br>• Communicating With Customers.<br>• AI-Assisited Design Tool Development."
    ), unsafe_allow_html=True)

    # 經歷 2: 2017 - 2021
    st.markdown(create_tooltip_html(
        title="Project Lead / Independent Contributor",
        period="2017 ~ 2021",
        company="Merry / USI/ Liteon.",
        products="IoT Sensors and Gateway / RF SiP module",
        responsibility="• Schematic and layout design.<br>• Project schedule control.<br>• Zero critical bugs in mass production.<br>• Resolved critical EMI/EMC issues"
    ), unsafe_allow_html=True)

    # 經歷 3: 2008 - 2016
    st.markdown(create_tooltip_html(
        title="Senior RF Engineer & Core Member",
        period="2008 ~ 2016",
        company="FIH",
        products="4G SmartPhone",
        responsibility="• RF matching and Layout optimization.<br>• BOM control and Maitain.<br>• RF Perfromance Validation and Debug.<br>• Improved mass production yield rate to 98%."
    ), unsafe_allow_html=True)

# === 重要專案 Project ===
elif folder == 'Project':
    st.header("🏆 Important Project: 5G mmWave Array")
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        #### Project Overview
        主導開發 28GHz 毫米波陣列天線模組 (Antenna in Package, AiP)。
        克服了散熱、封裝損耗與波束成形 (Beamforming) 演算法的挑戰。
        
        #### Key Achievements
        * 🚀 **EIRP Performance:** Achieved > 30 dBm target.
        * 🌡️ **Thermal Solution:** Reduced operating temp by 15% using novel heat sink design.
        * 📉 **Cost Reduction:** Optimized PCB layers, reducing unit cost by 20%.
        """)
    with c2:
        st.info("Technical Keywords")
        st.markdown("""
        * Ansys HFSS
        * Keysight ADS
        * Beamforming
        * Over-the-Air (OTA) Testing
        """)

# === RF 工具開發 RFTool ===
elif folder == 'RFTool':
    st.header("📡 AI-Assisted RF Tool Development")
    st.write("這展示了我如何使用 Python 來輔助 RF 設計。下方是一個簡單的互動範例：")
    
    st.markdown("### 🧮 Interactive: Path Loss Calculator")
    
    # 簡單的互動工具展示
    col_input, col_chart = st.columns([1, 2])
    
    with col_input:
        freq = st.slider("Frequency (GHz)", 1.0, 40.0, 28.0)
        dist = st.slider("Distance (m)", 1, 1000, 100)
        tx_power = st.number_input("Tx Power (dBm)", value=23.0)
        st.markdown("*Uses FSPL Model*")

    with col_chart:
        # 即時計算
        # FSPL = 20log10(d) + 20log10(f) + 20log10(4pi/c)
        # Simplified: 32.44 + 20log(d_km) + 20log(f_MHz)
        d_km = np.linspace(0.01, dist/1000, 100) # x-axis
        fspl = 32.44 + 20*np.log10(d_km) + 20*np.log10(freq*1000)
        rx_power = tx_power - fspl
        
        df_chart = pd.DataFrame({"Distance (km)": d_km, "Rx Power (dBm)": rx_power})
        st.line_chart(df_chart, x="Distance (km)", y="Rx Power (dBm)")
        
        current_loss = 32.44 + 20*np.log10(dist/1000) + 20*np.log10(freq*1000)
        st.success(f"📍 Rx Power at {dist}m: **{tx_power - current_loss:.2f} dBm**")

# === 技能 Skills ===
elif folder == 'Skills':
    st.header("🛠️ Main Tech Stack")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📡 RF Domain")
        st.progress(95, text="RF Circuit Design")
        st.progress(90, text="System Analysis & Link Budget")
        st.progress(85, text="Antenna Simulation (HFSS/CST)")
        st.progress(80, text="EMI/EMC Troubleshooting")
        
    with col2:
        st.subheader("💻 Software & AI")
        st.progress(90, text="Python (Pandas, Numpy, Scikit-rf)")
        st.progress(85, text="Streamlit / Web App Dashboard")
        st.progress(70, text="Machine Learning Basics")
        st.progress(75, text="Git / Version Control")

# === 個人陳述 Statement ===
elif folder == 'Statement':
    st.header("📝 Personal Statement")
    st.markdown("""
    > *"The future of RF Engineering lies in the intersection of Physics and Code."*
    
    擁有 17 年的硬體開發經驗，我見證了通訊技術從 3G 到 5G 的演進。
    我深信未來的硬體工程師不能只懂電路，更需要懂得運用軟體力量。
    
    我的目標是擔任 **Technical Lead**，帶領團隊建立更自動化、數據驅動的研發流程，
    減少重複性工作，讓工程師能專注於真正的創新設計。
    """)