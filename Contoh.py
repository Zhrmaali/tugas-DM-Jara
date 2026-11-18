import streamlit as st

# Page Header
st.title("Our Team")
st.write("Meet the people behind this final project.")
st.divider()

# Create 3 side-by-side columns
col1, col2, col3 = st.columns(3)

# --- TEAM MEMBER 1 ---
with col1:
    with st.container(border=True):
        st.image("foto jara.jpeg", use_container_width=True)
        st.subheader("Zahra Amalia Putri")
        st.subheader("021202600034")
        st.caption("Lead Data Scientist")
        st.write("Responsible for data preprocessing, exploratory analysis, and machine learning modeling.")
        if st.button("Contact Jara", key="btn1", use_container_width=True):
            st.info("zahra.putri@student.president.ac.id")

# --- TEAM MEMBER 2 ---
with col2:
    with st.container(border=True):
        st.image("https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300", use_container_width=True)
        st.subheader("Muhammad Thariq Afriansyah")
        st.caption("Backend Engineer")
        st.write("Handles system integration, database architecture, and cloud deployment pipelines.")
        if st.button("Contact Alex", key="btn2", use_container_width=True):
            st.info("Email: alex@example.com")

# --- TEAM MEMBER 3 ---
with col3:
    with st.container(border=True):
        st.image("https://images.unsplash.com/photo-1517841905240-472988babdf9?w=300", use_container_width=True)
        st.subheader("Kayla Libna Ayuma")
        st.caption("UI/UX Designer")
        st.write("Designs clean, user-friendly interfaces and interactive data visualizations.")
        if st.button("Contact Sarah", key="btn3", use_container_width=True):
            st.info("Email: sarah@example.com")
import streamlit as st

# --- MEMBUAT JUDUL / KONTEN DI DALAM SIDEBAR ---
st.sidebar.title("Navigasi Menu")
st.sidebar.write("Silakan pilih menu di bawah ini:")

# Contoh menu pilihan (selectbox) di sidebar
pilihan_menu = st.sidebar.selectbox("Pilih Halaman:", ["Home", "Team Profile", "Tentang Kami"])

# Contoh slider atau input di dalam sidebar
nilai_slider = st.sidebar.slider("Pilih Nilai:", 0, 100, 50)


# --- KONTEN UTAMA DI LAYAR UTAMA (MAIN AREA) ---
if pilihan_menu == "Home":
    st.title("Halaman Utama (Home)")
    st.write(f"Anda memilih menu Home. Nilai slider di sidebar adalah: {nilai_slider}")

elif pilihan_menu == "Team Profile":
    st.title("Halaman Tim Pengembang")
    st.write("Ini adalah tampilan profil anggota tim.")