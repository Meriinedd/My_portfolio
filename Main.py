import streamlit as st

# 1. ตั้งค่าหน้าเว็บให้ดูกว้างขึ้นและมีไอคอน
st.set_page_config(page_title="Portfolio | อัศญาวิณี บัวเล็ก", page_icon="✨", layout="wide")

# --- ส่วนหัว (Header) ---
col1, col2 = st.columns([1, 2.5])
with col1:
    # เปลี่ยน URL ด้านล่างเป็นลิงก์รูปโปรไฟล์ของคุณได้เลย
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=220) 
with col2:
    st.title("อัศญาวิณี บัวเล็ก (Som)")
    st.subheader("Administrative Officer & Tech Enthusiast 💻")
    st.write("""
    ผสมผสานทักษะงานบริหารเข้ากับความหลงใหลในเทคโนโลยีและการพัฒนาซอฟต์แวร์ 
    มีประสบการณ์ทั้งการจัดการระบบหลังบ้าน การพัฒนา Web Application และการสร้างระบบอัตโนมัติเพื่อลดขั้นตอนการทำงาน
    """)

st.divider() # เส้นคั่นแบบสวยงาม

# --- ใช้ Tabs เพื่อแบ่งหน้าเนื้อหาให้ดูไม่รกตา ---
tab1, tab2, tab3 = st.tabs(["💼 ประสบการณ์ & การศึกษา", "🚀 โปรเจกต์ & ทักษะ", "📫 ติดต่องาน"])

# --- แท็บที่ 1: ประวัติ ---
with tab1:
    st.markdown("### 💼 ประสบการณ์ทำงาน")
    st.write("• **2024 - ปัจจุบัน:** Administrative Officer ที่ KAWATA (THAILAND) CO., LTD.")
    st.write("• **งานสอนพิเศษ:** ผู้สอนและออกแบบสื่อการเรียนการสอนเขียนโปรแกรมพื้นฐาน (Roblox Studio / Lua) สำหรับเด็กนักเรียนชั้น ป.4")
    
    st.markdown("<br>", unsafe_allow_html=True) # เว้นบรรทัด
    
    st.markdown("### 🎓 การศึกษา")
    st.write("• **2016 - 2020:** Bachelor of Business, University of the Thai Chamber of Commerce")

# --- แท็บที่ 2: โปรเจกต์และทักษะ ---
with tab2:
    st.markdown("### 🛠️ ทักษะ (Skills)")
    st.write("**Programming & Tech:** Python, React, Firebase, Vercel, n8n, Scratch")
    st.write("**Interests:** Web Development, Data Automation, Photography (Canon EOS R50)")

    st.markdown("### 🌟 ผลงานเด่น (Projects)")
    
    # ใช้คอลัมน์และกรอบเพื่อทำเป็นการ์ดโชว์ผลงาน
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        with st.container(border=True):
            st.markdown("#### 💰 WealthFlow Web App")
            st.write("พัฒนาเว็บไซต์สำหรับบันทึกรายรับ-รายจ่าย และติดตามพอร์ตการลงทุนส่วนตัว โดยใช้ React และเชื่อมต่อฐานข้อมูลด้วย Firebase เพื่อการจัดการการเงินอย่างเป็นระบบ")
    
    with col_p2:
        with st.container(border=True):
            st.markdown("#### 🤖 Data Automation System")
            st.write("สร้างระบบประมวลผลข้อมูลอัตโนมัติด้วย n8n (ตั้งค่า MQTT nodes) ร่วมกับ Scratch เพื่อดึงและบันทึกข้อมูลทางการเงินลงใน Google Sheets อัตโนมัติ")

# --- แท็บที่ 3: ช่องทางการติดต่อ ---
with tab3:
    st.markdown("### 📫 ช่องทางการติดต่องาน")
    st.write("ยินดีรับโอกาสใหม่ๆ และการร่วมงานในโปรเจกต์ที่น่าสนใจ สามารถติดต่อพูดคุยกันได้ตามช่องทางด้านล่างนี้เลยครับ/ค่ะ:")
    
    # ใช้กล่องข้อความสีฟ้าเน้นอีเมล
    st.info("**📧 Email:** som.asayawinee@example.com") 
    st.write("")
    
    # สร้างปุ่มกดที่ลิงก์ไปยังโซเชียลต่างๆ
    c1, c2, c3 = st.columns(3)
    with c1:
        st.link_button("💼 LinkedIn Profile", "https://linkedin.com", use_container_width=True)
    with c2:
        st.link_button("💻 GitHub Repository", "https://github.com", use_container_width=True)
    with c3:
        st.link_button("📷 Portfolio ผลงานถ่ายภาพ", "https://instagram.com", use_container_width=True)

st.write("---")
st.caption("© 2026 Asayawinee B. | Built with ❤️ using Streamlit")