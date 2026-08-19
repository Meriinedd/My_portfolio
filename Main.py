import streamlit as st
import random 
import requests
from streamlit_option_menu import option_menu # ไลบรารีสำหรับทำเมนูสวยๆ
from streamlit_lottie import st_lottie # ไลบรารีสำหรับแอนิเมชัน

# --- ฟังก์ชันสำหรับโหลดแอนิเมชัน Lottie ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# 1. ตั้งค่าหน้าเว็บให้ดูกว้างขึ้นและมีไอคอน
st.set_page_config(page_title="Portfolio | PEEMPOT GUAKUL", page_icon="💻", layout="wide")

# โหลดแอนิเมชัน (คุณสามารถเปลี่ยน URL เป็นแอนิเมชันอื่นจาก lottiefiles.com ได้)
lottie_coding = load_lottieurl("https://lottie.host/8061df43-1698-4c91-a185-181514736f1c/J77626tI7y.json")

# --- ส่วนหัว (Header) ---
col1, col2 = st.columns([1, 2.5])
with col1:
    if lottie_coding:
        # ใช้แอนิเมชันเคลื่อนไหวแทนภาพนิ่ง
        st_lottie(lottie_coding, height=220, key="coding")
    else:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=220) 
with col2:
    st.title("Peempot guakul (Fluke)")
    st.subheader("Full Stack Developer & Game Designer 💻")
    st.write("""
    ผสมผสานทักษะงานบริหารเข้ากับความหลงใหลในเทคโนโลยีและการพัฒนาซอฟต์แวร์ 
    มีประสบการณ์ทั้งการจัดการระบบหลังบ้าน การพัฒนา Web Application และการสร้างระบบอัตโนมัติเพื่อลดขั้นตอนการทำงาน
    """)

st.write("---")

# --- ใช้ Option Menu แบบแนวนอนแทน Tabs แบบเดิม ---
selected = option_menu(
    menu_title=None,  # ไม่ต้องแสดงชื่อเมนูหลัก
    options=["ประสบการณ์ & การศึกษา", "โปรเจกต์ & ทักษะ", "มินิเกม", "ติดต่องาน"], # ชื่อเมนู
    icons=["briefcase", "rocket", "controller", "envelope"], # ไอคอนจาก Bootstrap Icons
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "transparent"},
        "icon": {"color": "#ffaa00", "font-size": "20px"}, 
        "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#333333"},
        "nav-link-selected": {"background-color": "#e63946"}, # สีตอนกดเลือกเมนู
    }
)

# --- ส่วนที่ 1: ประวัติ ---
if selected == "ประสบการณ์ & การศึกษา":
    st.markdown("### 💼 ประสบการณ์ทำงาน")
    st.write("- **2022 : ปัจจุบัน:** Software Developer, Front End")
    st.write("- ผู้สอน และออกแบบสื่อการเรียนการสอนเขียนโปรแกรมพื้นฐาน (Roblox Studio / Lua), Scratch, Thunkable, Blockly, C#, C++, Python")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 🎓 การศึกษา")
    st.write("• **2016 - 2020:** Computer Engineering, Dhurakij Pundit University (DPU)")

# --- ส่วนที่ 2: โปรเจกต์และทักษะ ---
if selected == "โปรเจกต์ & ทักษะ":
    st.markdown("### 🛠️ ทักษะ (Skills)")
    # ใช้กล่องข้อความสีๆ เพื่อเน้นทักษะให้ดูโดดเด่นขึ้น
    st.info("**Programming & Tech:** Python, React, Firebase, Vercel, n8n, Scratch")
    st.success("**Interests:** Web Development, Data Automation, Photography (Canon EOS R50)")

    st.markdown("### 🌟 ผลงานเด่น (Projects)")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        with st.container(border=True):
            st.markdown("#### 💰 WealthFlow Web App")
            st.write("พัฒนาเว็บไซต์สำหรับบันทึกรายรับ-รายจ่าย และติดตามพอร์ตการลงทุนส่วนตัว โดยใช้ React และเชื่อมต่อฐานข้อมูลด้วย Firebase เพื่อการจัดการการเงินอย่างเป็นระบบ")
    with col_p2:
        with st.container(border=True):
            st.markdown("#### 🤖 Data Automation System")
            st.write("สร้างระบบประมวลผลข้อมูลอัตโนมัติด้วย n8n (ตั้งค่า MQTT nodes) ร่วมกับ Scratch เพื่อดึงและบันทึกข้อมูลทางการเงินลงใน Google Sheets อัตโนมัติ")
            
    col_p3, col_p4 = st.columns(2)
    with col_p3:
        with st.container(border=True):
            st.markdown("#### ✈️ Travel Diary Web App")
            st.write("เว็บแอปพลิเคชันสำหรับบันทึกเรื่องราวและไดอารี่การท่องเที่ยว พัฒนาด้วย React ช่วยให้เก็บความทรงจำ สถานที่ และรูปภาพได้อย่างเป็นระเบียบ")
    with col_p4:
        with st.container(border=True):
            st.markdown("#### 🌳 Family Tree Web App")
            st.write("เว็บแอปพลิเคชันสร้างและแสดงแผนผังครอบครัว พัฒนาด้วย React เพื่อจัดการความสัมพันธ์และประวัติข้อมูลของสมาชิกในครอบครัวได้อย่างง่ายดายและสวยงาม")

# --- ส่วนที่ 3: มินิเกม (Mini Games) ---
if selected == "มินิเกม":
    st.markdown("### 🎮 มินิเกม Python สำหรับคลายเครียด")
    st.write("ทดลองเล่นมินิเกมที่เขียนขึ้นด้วยภาษา Python และทำงานบน Streamlit ได้เลยครับ!")
    
    game_col1, game_col2 = st.columns(2)
    
    # เกมที่ 1: เป่ายิ้งฉุบ
    with game_col1:
        with st.container(border=True):
            st.markdown("#### ✌️✊✋ เกมเป่ายิ้งฉุบ")
            choices = ["ค้อน ✊", "กรรไกร ✌️", "กระดาษ ✋"]
            user_choice = st.radio("เลือกอาวุธของคุณ:", choices, horizontal=True)
            
            if st.button("เป่ายิ้งฉุบ!"):
                bot_choice = random.choice(choices)
                
                st.write(f"🤖 บอทเลือก: **{bot_choice}**")
                
                if user_choice == bot_choice:
                    st.info("เสมอ! ใจตรงกันเลย 😲")
                elif (user_choice == "ค้อน ✊" and bot_choice == "กรรไกร ✌️") or \
                     (user_choice == "กรรไกร ✌️" and bot_choice == "กระดาษ ✋") or \
                     (user_choice == "กระดาษ ✋" and bot_choice == "ค้อน ✊"):
                    st.success("คุณชนะ! 🎉")
                else:
                    st.error("คุณแพ้! ลองใหม่นะ 😭")

    # เกมที่ 2: ทายตัวเลข
    with game_col2:
        with st.container(border=True):
            st.markdown("#### 🔢 เกมทายใจตัวเลข (1-50)")
            
            if 'target_num' not in st.session_state:
                st.session_state.target_num = random.randint(1, 50)
                st.session_state.attempts = 0

            guess = st.number_input("ใส่ตัวเลขที่ทาย:", min_value=1, max_value=50, step=1)
            
            col_btn1, col_btn2 = st.columns([1, 1])
            with col_btn1:
                if st.button("ทายตัวเลข!"):
                    st.session_state.attempts += 1
                    if guess < st.session_state.target_num:
                        st.warning(f"ครั้งที่ {st.session_state.attempts}: น้อยไปครับ! 🔼")
                    elif guess > st.session_state.target_num:
                        st.warning(f"ครั้งที่ {st.session_state.attempts}: มากไปครับ! 🔽")
                    else:
                        st.success(f"🎉 ถูกต้อง! คำตอบคือ {st.session_state.target_num} (คุณทายไป {st.session_state.attempts} ครั้ง)")
                        st.balloons() 
            with col_btn2:
                if st.button("เริ่มเกมใหม่ 🔄"):
                    st.session_state.target_num = random.randint(1, 50)
                    st.session_state.attempts = 0
                    st.info("รีเซ็ตเกมเรียบร้อย! เริ่มทายใหม่ได้เลย")

# --- ส่วนที่ 4: ช่องทางการติดต่อ ---
if selected == "ติดต่องาน":
    st.markdown("### 📫 ช่องทางการติดต่องาน")
    st.write("ยินดีรับโอกาสใหม่ๆ และการร่วมงานในโปรเจกต์ที่น่าสนใจ สามารถติดต่อพูดคุยกันได้ตามช่องทางด้านล่างนี้เลยครับ")
    
    st.info("**📧 Email:** Yokinezz1997@gmail.com") 
    st.write("")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.link_button("💼 LinkedIn Profile", "https://linkedin.com", use_container_width=True)
    with c2:
        st.link_button("💻 GitHub Repository", "https://github.com", use_container_width=True)
    with c3:
        st.link_button("📷 Portfolio ผลงานถ่ายภาพ", "https://instagram.com", use_container_width=True)

st.write("---")
st.caption("© 2026 Peempot Guakul | Built with ❤️ using Streamlit & Python")