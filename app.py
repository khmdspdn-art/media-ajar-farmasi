import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
# KONFIGURASI HALAMAN STREAMLIT
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="PharmaEntrepreneurship - Dasar-Dasar Farmasi",
    page_icon="💊",
    layout="wide"
)

# Initialize Session State untuk Gamifikasi
if "score_pharm" not in st.session_state:
    st.session_state.score_pharm = 0
if "badge_pharm" not in st.session_state:
    st.session_state.badge_pharm = "Calon Asisten Farmasi 🥼"
if "sim_points" not in st.session_state:
    st.session_state.sim_points = 0

def update_badge_pharm():
    score = st.session_state.score_pharm
    if score >= 90:
        st.session_state.badge_pharm = "Master Technopreneur Farmasi 🏆💊"
    elif score >= 70:
        st.session_state.badge_pharm = "Inovator Kefarmasian 🥈✨"
    elif score >= 50:
        st.session_state.badge_pharm = "Wirausahawan Muda Farmasi 🥉🌿"
    else:
        st.session_state.badge_pharm = "Calon Asisten Farmasi 🥼"

# -----------------------------------------------------------------------------
# HEADER & CAPAIAN PEMBELAJARAN
# -----------------------------------------------------------------------------
st.title("💊 Technopreneurship Kefarmasian: Pengenalan Wirausaha Farmasi")

with st.container():
    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-radius: 10px; border-left: 6px solid #2e7d32; margin-bottom: 20px;">
        <h3 style="color: #1b5e20; margin-top:0;">🎯 Tujuan Pembelajaran</h3>
        <p style="font-size: 16px; color: #2e7d32; margin-bottom: 0;">
            <strong>Peserta didik mampu:</strong> Menjelaskan pengertian, peran, dan sikap/karakteristik dasar seorang wirausahawan (<em>entrepreneur</em>) secara umum dan di bidang kefarmasian.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION & GAMIFIKASI STATUS
# -----------------------------------------------------------------------------
st.sidebar.title("🎮 Menu Pembelajaran")
menu = st.sidebar.radio(
    "Pilih Zona Pembelajaran:",
    [
        "📘 Modul Interaktif",
        "🎮 Game Simulasi: Pharma-Entrepreneur",
        "🎯 Kuis Evaluasi (5 Soal)",
        "📋 Rubrik Assessment as Learning"
    ]
)

st.sidebar.divider()
st.sidebar.subheader("🏆 Status Gamifikasi")
st.sidebar.metric("Total XP Pembelajaran", f"{st.session_state.score_pharm} XP")
st.sidebar.metric("Poin Simulasi Bisnis", f"{st.session_state.sim_points} Pts")
st.sidebar.info(f"Lencana: **{st.session_state.badge_pharm}**")

# -----------------------------------------------------------------------------
# ZONA 1: MODUL INTERAKTIF
# -----------------------------------------------------------------------------
if menu == "📘 Modul Interaktif":
    st.header("📘 Pengertian, Peran, dan Karakter Kewirausahaan Farmasi")

    tab1, tab2, tab3 = st.tabs([
        "1. Pengertian Entrepreneurship Farmasi",
        "2. Peran Wirausahawan di Bidang Farmasi",
        "3. Karakteristik Utama (Sikap Entrepreneur)"
    ])

    with tab1:
        st.subheader("💡 Apa itu Entrepreneur & Pharmapreneur?")
        col1, col2 = st.columns(2)
        with col1:
            st.info("🌐 **Wirausahawan (Entrepreneur) Secara Umum**")
            st.markdown("""
            Seseorang yang memiliki keberanian untuk mengambil risiko, mengidentifikasi peluang, serta mengorganisasikan sumber daya untuk menciptakan usaha baru yang memberikan nilai tambah (*value added*).
            """)
        with col2:
            st.success("💊 **Pharmapreneur / Technopreneur Farmasi**")
            st.markdown("""
            Wirausahawan yang memanfaatkan pengetahuan kefarmasian, teknologi, dan regulasi kesehatan untuk menciptakan produk/layanan farmasi yang aman, bermutu, serta solutif bagi masyarakat.
            """)

    with tab2:
        st.subheader("🔑 4 Peran Utama Wirausahawan di Bidang Kefarmasian")
        st.markdown("""
        1. **Penyedia Solusi Kesehatan (*Health Solution Provider*):** Membuka akses obat, alat kesehatan, dan suplemen berkualitas bagi masyarakat.
        2. **Inovator Produk Herbal & Obat (*Inovator*):** Mengembangkan potensi kekayaan alam lokal (seperti herbal/jamu) menjadi produk kefarmasian bernilai ekonomis tinggi.
        3. **Pencipta Lapangan Kerja (*Job Creator*):** Membuka peluang kerja bagi Tenaga Teknis Kefarmasian (TTK) dan tenaga pendukung lainnya.
        4. **Edukator & Penggerak Literasi Obat (*Public Educator*):** Memberikan edukasi terkait penggunaan obat yang benar (DAGUSIBU: Dapatkan, Gunakan, Simpan, Buang).
        """)

    with tab3:
        st.subheader("⭐ 5 Karakteristik Dasar (Sikap Wirausaha Farmasi)")
        st.markdown("""
        * **1. Teliti & Taat Regulasi (*Compliance*):** Memahami aturan standar mutu farmasi (BPOM, Kemenkes).
        * **2. Berani Mengambil Risiko Terukur (*Risk Taker*):** Memperhitungkan kelayakan usaha tanpa mengorbankan keselamatan pasien/konsumen.
        * **3. Inovatif & Kreatif:** Mampu menciptakan variasi produk kesehatan (misal: handsanitizer herbal, teh celup herbal).
        * **4. Pantang Memyerah (*Resilience*):** Gigih menghadapi persaingan pasar dan kegagalan formulasi/uji.
        * **5. Berintegritas & Etis:** Mengutamakan kejujuran terkait khasiat dan mutu produk farmasi.
        """)

# -----------------------------------------------------------------------------
# ZONA 2: GAME SIMULASI INTERAKTIF (GAMIFIKASI)
# -----------------------------------------------------------------------------
elif menu == "🎮 Game Simulasi: Pharma-Entrepreneur":
    st.header("🎮 Mini Game Simulasi: 'Keputusan Sang Pharmapreneur'")
    st.write("Uji kemampuan pengambilan keputusan berkarakter wirausaha dalam kasus nyata dunia kefarmasian!")

    st.markdown("""
    <div style="background-color: #fff3e0; padding: 15px; border-radius: 8px; border-left: 5px solid #ff9800;">
        <strong>Skenario Kasus:</strong> Anda baru saja lulus SMK Farmasi dan berencana meluncurkan produk inovasi <em>Hand Sanitizer Herbal Ekstrak Daun Sirih</em>.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Tantangan 1: Menghadapi Izin Edar BPOM")
    q1_sim = st.radio(
        "Biaya uji laboratorium dan perizinan BPOM cukup tinggi. Apa keputusan yang akan Anda ambil?",
        [
            "Tetap mengurus izin resmi BPOM demi keamanan konsumen dan legalitas usaha jangka panjang.",
            "Menjual produk tanpa izin edar secara sembunyi-sembunyi agar cepat balik modal.",
            "Membatalkan seluruh rencana usaha karena takut mengalami kerugian."
        ]
    )

    st.subheader("Tantangan 2: Menghadapi Keluhan Konsumen")
    q2_sim = st.radio(
        "Seorang pembeli mengeluh bahwa aroma hand sanitizer buatan Anda terlalu menyengat. Apa reaksi Anda?",
        [
            "Abaikan keluhan tersebut karena merasa formula Anda sudah paling sempurna.",
            "Menerima masukan dengan lapang dada dan melakukan evaluasi formula (Inovatif & Pantang Menyerah).",
            "Marah dan memblokir kontak pembeli tersebut."
        ]
    )

    if st.button("Kirim Keputusan Bisnis 🚀"):
        points = 0
        if q1_sim.startswith("Tetap mengurus"):
            points += 50
        if q2_sim.startswith("Menerima masukan"):
            points += 50

        st.session_state.sim_points = points
        st.success(f"🎉 Hasil Keputusan Bisnis Anda: **{points} / 100 Poin Simulasi**")
        
        if points == 100:
            st.balloons()
            st.info("Luar biasa! Anda menunjukkan sikap wirausahawan farmasi yang taat regulasi, berorientasi kualitas, dan pantang menyerah!")
        else:
            st.warning("Evaluasi kembali keputusan Anda! Seorang Pharmapreneur harus taat regulasi dan terbuka terhadap masukan konsumen.")

# -----------------------------------------------------------------------------
# ZONA 3: KUIS EVALUASI (5 SOAL PG)
# -----------------------------------------------------------------------------
elif menu == "🎯 Kuis Evaluasi (5 Soal)":
    st.header("🎯 Kuis Evaluasi Pemahaman Materi (5 Soal PG)")
    st.write("Jawablah pertanyaan di bawah ini untuk menguji pemahaman Anda!")

    questions = [
        {
            "q": "1. Seseorang yang memanfaatkan pengetahuan kefarmasian dan teknologi untuk menciptakan peluang usaha produk/jasa kesehatan disebut...",
            "options": ["Apoteker Penguji", "Pharmapreneur", "Asisten Laboratorium", "Konsumen Farmasi"],
            "answer": "Pharmapreneur"
        },
        {
            "q": "2. Mengapa seorang wirausahawan di bidang farmasi WAJIB memiliki sikap taat regulasi (compliance)?",
            "options": [
                "Agar cepat kaya tanpa perlu izin",
                "Karena produk kefarmasian menyangkut keselamatan dan kesehatan jiwa manusia",
                "Agar dapat menaikkan harga obat sebebas-bebasnya",
                "Hanya sebagai formalitas agar tidak ditutup polisi"
            ],
            "answer": "Karena produk kefarmasian menyangkut keselamatan dan kesehatan jiwa manusia"
        },
        {
            "q": "3. Ketika formulasi teh herbal yang Anda buat gagal uji stabilitas, sikap pantang menyerah (resilience) ditunjukkan dengan cara...",
            "options": [
                "Menghentikan usaha dan mencari pekerjaan lain",
                "Menganalisis penyebab kegagalan dan memperbaiki formula sampai berhasil",
                "Tetap menjual produk gagal tersebut ke pasar",
                "Menyalahkan bahan baku yang dibeli dari supplier"
            ],
            "answer": "Menganalisis penyebab kegagalan dan memperbaiki formula sampai berhasil"
        },
        {
            "q": "4. Salah satu peran wirausahawan farmasi dalam masyarakat terkait konsep DAGUSIBU adalah...",
            "options": [
                "Pencipta Lapangan Kerja",
                "Edukator & Penggerak Literasi Obat",
                "Pengambil Risiko Usaha",
                "Penyedia Bahan Baku Impor"
            ],
            "answer": "Edukator & Penggerak Literasi Obat"
        },
        {
            "q": "5. Di bawah ini yang BUKAN merupakan karakteristik dasar seorang wirausahawan farmasi yang baik adalah...",
            "options": [
                "Teliti dan taat aturan BPOM",
                "Kreatif dan inovatif",
                "Menghalalkan segala cara demi mendapat keuntungan instan",
                "Berani mengambil risiko terukur"
            ],
            "answer": "Menghalalkan segala cara demi mendapat keuntungan instan"
        }
    ]

    with st.form("quiz_pharm_form"):
        user_answers = []
        for i, q in enumerate(questions):
            st.markdown(f"**{q['q']}**")
            ans = st.radio(
                f"Pilih jawaban soal nomor {i+1}:",
                q["options"],
                key=f"q_pharm_{i}",
                index=None
            )
            user_answers.append(ans)
            st.divider()

        submitted = st.form_submit_button("Kirim Jawaban & Hitung Skor 🏆")

    if submitted:
        score_counter = 0
        unanswered = False

        for i, q in enumerate(questions):
            if user_answers[i] is None:
                unanswered = True
            elif user_answers[i] == q["answer"]:
                score_counter += 20  # Total 5 Soal x 20 = 100 XP

        if unanswered:
            st.warning("Harap jawab semua 5 soal terlebih dahulu!")
        else:
            st.session_state.score_pharm = score_counter
            update_badge_pharm()

            st.balloons()
            st.success(f"🎉 Kuis Selesai! Skor Anda: **{st.session_state.score_pharm} / 100 XP**")
            st.info(f"Lencana Anda saat ini: **{st.session_state.badge_pharm}**")

            recap_data = {
                "No": [i+1 for i in range(5)],
                "Jawaban Anda": [str(ans) if ans is not None else "Belum dijawab" for ans in user_answers],
                "Jawaban Benar": [q["answer"] for q in questions],
                "Status": ["✅ Benar" if user_answers[i] == questions[i]["answer"] else "❌ Salah" for i in range(5)]
            }

            df_recap = pd.DataFrame(recap_data)
            st.subheader("📊 Rekapitulasi Hasil Evaluasi")
            st.dataframe(df_recap, use_container_width=True, hide_index=True)

# -----------------------------------------------------------------------------
# ZONA 4: RUBRIK ASSESSMENT AS LEARNING (PENILAIAN DIRI)
# -----------------------------------------------------------------------------
elif menu == "📋 Rubrik Assessment as Learning":
    st.header("📋 Rubrik Evaluasi Diri (Assessment as Learning)")
    st.write("Gunakan lembar refleksi mandiri ini untuk mengukur pemahaman dan kesiapan mental kewirausahaan Anda!")

    st.markdown("### 📝 Lembar Refleksi Diri Siswa")

    indicators = [
        "Saya dapat menjelaskan perbedaan wirausahawan secara umum dengan Pharmapreneur.",
        "Saya memahami pentingnya ketaatan pada regulasi (BPOM/Kemenkes) dalam wirausaha farmasi.",
        "Saya mampu mengidentifikasi minimal 3 peran penting wirausahawan farmasi bagi masyarakat.",
        "Saya dapat menjelaskan sikap pantang menyerah dan berani mengambil risiko terukur.",
        "Saya tertarik untuk mencari peluang ide produk/jasa di bidang kefarmasian."
    ]

    scores = []
    with st.form("self_assessment_form"):
        for i, ind in enumerate(indicators):
            st.markdown(f"**{i+1}. {ind}**")
            score = st.select_slider(
                f"Tingkat Penguasaan Indikator {i+1}:",
                options=["Sangat Belum Mampu (1)", "Cukup Mampu (2)", "Mampu (3)", "Sangat Mampu (4)"],
                key=f"rubric_{i}"
            )
            scores.append(score)
            st.divider()

        submit_rubric = st.form_submit_button("Simpan Refleksi Diri 💾")

    if submit_rubric:
        st.success("✅ Refleksi diri Anda berhasil disimpan. Terus kembangkan potensi kewirausahaan Anda!")
