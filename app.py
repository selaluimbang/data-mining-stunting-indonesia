import streamlit as st
from predict import make_prediction
import pandas as pd
import folium
from streamlit_folium import st_folium
import plotly.express as px

def main():
    st.set_page_config(page_title="Dashboard Daerah Prioritas Stunting", layout="wide")
    st.markdown(
        """
        <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" rel="stylesheet">
        <style>
            body { background-color: #ffffff; }
            .stApp { background-color: #ffffff; }
            .stAppHeader { background-color: #4285f4 !important; color: #ffffff !important; }
            .container { margin: 0 auto; max-width: 1200px; padding: 20px; color: #4285f4;}
            .header { text-align: center; margin-bottom: 40px; }
            .header h1 { font-size: 2.5rem; color: #4285f4; }
            .card { padding: 20px; margin: 10px; background-color: #e0f7fa; border-radius: 8px; }
            .card h5 { color: #4285f4; }

            label {
                color: #4285f4 !important; /* Ubah warna label menjadi biru */
            }
            /* Styling label input */
            .stNumberInput > div > label, 
            .stTextInput > div > label, 
            .stSlider > div > label, 
            .stSelectbox > div > label { 
                color: #4285f4 !important; 
                font-weight: bold; 
            }

            /* Styling input field */
            .stNumberInput input, 
            .stTextInput input, 
            .stSelectbox select {
                background-color: #ffffff; 
                color: #ffffff; 
                border: 1px solid #4285f4; 
                border-radius: 5px; 
                padding: 5px;
            }

            /* Styling tombol */
            .stButton > button { 
                background-color: #4285f4; 
                color: white; 
                border-radius: 5px; 
                font-size: 16px; 
                padding: 10px 20px; 
                cursor: pointer; 
            }

            .stButton > button:hover { 
                background-color: #ffffff; 
                color: #4285f4; 
                border: 1px solid #4285f4; 
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="container">', unsafe_allow_html=True)

    st.markdown('<div class="header"><h1>Dashboard Daerah Prioritas Kasus Stunting Indonesia</h1></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

# 'prevalensi_underweight', 'persentase_akses_air_minum_layak', 'persentase_penduduk_miskin', 'garis_kemiskinan(rupiah/kapita/bulan)', 'jumlah_puskesmas', 
# 'jumlah_tenaga_kesehatan_gizi', 'luas_wilayah', 'tingkat_pengangguran', 'rata_rata_pendidikan_akhir', 'penerima_bpjs_non_pbi', 'prevalensi_wasting', 
# 'persentase_memiliki_jamban_layak', 'indeks_pembangunan_manusia', 'indeks_pembangunan_literasi', 
# 'prevalensi_ketidakcukupan_pangan', 'jumlah_penduduk', 'persentase_akses_sanitasi_layak', 
# 'kategori_kepadatan', 'rata_rata_pendapatan', 'jumlah_bencana_kekeringan'

# 'jumlah_penduduk', 'luas_wilayah', 'kategori_kepadatan',
#        'persentase_akses_air_minum_layak', 'persentase_memiliki_jamban_layak',
#        'persentase_akses_sanitasi_layak', 'tingkat_pengangguran',
#        'rata_rata_pendapatan', 'persentase_penduduk_miskin',
#        'garis_kemiskinan(rupiah/kapita/bulan)', 'indeks_pembangunan_literasi',
#        'indeks_pembangunan_manusia', 'rata_rata_pendidikan_akhir',
#        'jumlah_tenaga_kesehatan_gizi', 'jumlah_puskesmas',
#        'penerima_bpjs_non_pbi', 'prevalensi_ketidakcukupan_pangan',
#        'jumlah_bencana_kekeringan', 'prevalensi_underweight',
#        'prevalensi_wasting'

    with col1:
        st.markdown('<div class="card"><h5>Input Data</h5></div>', unsafe_allow_html=True)

        prevalensi_underweight = st.number_input("Prevalensi Underweight", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
        persentase_akses_air_minum_layak = st.number_input("Persentase Akses Air Minum Layak", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
        persentase_penduduk_miskin = st.number_input("Persentase Penduduk Miskin", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
        garis_kemiskinan = st.number_input("Garis Kemiskinan (rupiah/kapita/bulan)", min_value=0, max_value=2500000, value=50000, step=1)
        jumlah_puskesmas = st.number_input("Jumlah Puskesmas", min_value=0, max_value=2000, value=500, step=1)
        jumlah_tenaga_kesehatan_gizi= st.number_input("Jumlah Tenaga Kesehatan", min_value=0, max_value=10000, value=100, step=1)
        luas_wilayah = st.number_input("Luas Wilayah (Km2)", min_value=0.0, max_value=10000.0, value=50.0, step=0.1)
        tingkat_pengangguran = st.number_input("Tingkat Pengangguran", min_value=0.0, max_value=100.0, value=5.0, step=0.1)
        rata_rata_pendidikan_akhir = st.number_input("Rata-rata Pendidikan Akhir", min_value=0, max_value=30, value=2, step=1)
        penerima_bpjs_non_pbi = st.number_input("Penerima BPJS NON PBI", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
        prevalensi_wasting = st.number_input("Prevalensi Wasting", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
        persentase_memiliki_jamban_layak = st.number_input("Persentase Memiliki Jamban Layak", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
        indeks_pembangunan_manusia = st.number_input("Indeks Pembangunan Manusia", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
        indeks_pembangunan_literasi = st.number_input("Indeks Pembangunan Literasi", min_value=0.0, max_value=100.0, value=5.0, step=0.1)
        prevalensi_ketidakcukupan_pangan = st.number_input("Prevalensi Ketidakcukupan Pangan", min_value=0.0, max_value=20.0, value=2.0, step=0.1)
        jumlah_penduduk = st.number_input("Jumlah Penduduk", min_value=0, max_value=30000000, value=100000, step=1)
        persentase_akses_sanitasi_layak = st.number_input("Persentase Akses Sanitasi Layak", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
        kategori_kepadatan = st.number_input("Kategori Kepadatan", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
        rata_rata_pendapatan = st.number_input("Rata-rata Pendapatan", min_value=0, max_value=100000000, value=500000, step=1)
        jumlah_bencana_kekeringan = st.number_input("Jumlah Bencana Kekeringan", min_value=0, max_value=1000, value=0, step=1)

        if st.button("Prediksi"):
            # data = pd.DataFrame({
            #     'prevalensi_underweight': [prevalensi_underweight],
            #     'persentase_akses_air_minum_layak' : [persentase_akses_air_minum_layak],
            #     'persentase_penduduk_miskin' : [persentase_penduduk_miskin],
            #     'garis_kemiskinan(rupiah/kapita/bulan)': [garis_kemiskinan],
            #     'jumlah_puskesmas': [jumlah_puskesmas],
            #     'jumlah_tenaga_kesehatan_gizi': [jumlah_tenaga_kesehatan_gizi],
            #     'luas_wilayah': [luas_wilayah],
            #     'tingkat_pengangguran': [tingkat_pengangguran],
            #     'rata_rata_pendidikan_akhir': [rata_rata_pendidikan_akhir],
            #     'penerima_bpjs_non_pbi': [penerima_bpjs_non_pbi],
            #     'prevalensi_wasting': [prevalensi_wasting],
            #     'persentase_memiliki_jamban_layak': [persentase_memiliki_jamban_layak],
            #     'indeks_pembangunan_manusia': [indeks_pembangunan_manusia],
            #     'indeks_pembangunan_literasi': [indeks_pembangunan_literasi],
            #     'prevalensi_ketidakcukupan_pangan': [prevalensi_ketidakcukupan_pangan],
            #     'jumlah_penduduk': [jumlah_penduduk],
            #     'persentase_akses_sanitasi_layak': [persentase_akses_sanitasi_layak],
            #     'kategori_kepadatan': [kategori_kepadatan],
            #     'rata_rata_pendapatan': [rata_rata_pendapatan],
            #     'jumlah_bencana_kekeringan': [jumlah_bencana_kekeringan]
            # })

            data = pd.DataFrame({
                'jumlah_penduduk' : [jumlah_penduduk],
                'luas_wilayah': [luas_wilayah],
                'kategori_kepadatan': [kategori_kepadatan],
                'persentase_akses_air_minum_layak': [persentase_akses_air_minum_layak],
                'persentase_memiliki_jamban_layak': [persentase_memiliki_jamban_layak],
                'persentase_akses_sanitasi_layak': [persentase_akses_sanitasi_layak],
                'tingkat_pengangguran': [tingkat_pengangguran],
                'rata_rata_pendapatan': [rata_rata_pendapatan],
                'persentase_penduduk_miskin': [persentase_penduduk_miskin],
                'garis_kemiskinan(rupiah/kapita/bulan)': [garis_kemiskinan],
                'indeks_pembangunan_literasi': [indeks_pembangunan_literasi],
                'indeks_pembangunan_manusia': [indeks_pembangunan_manusia],
                'rata_rata_pendidikan_akhir': [rata_rata_pendidikan_akhir],
                'jumlah_tenaga_kesehatan_gizi': [jumlah_tenaga_kesehatan_gizi],
                'jumlah_puskesmas': [jumlah_puskesmas],
                'penerima_bpjs_non_pbi': [penerima_bpjs_non_pbi],
                'prevalensi_ketidakcukupan_pangan': [prevalensi_ketidakcukupan_pangan],
                'jumlah_bencana_kekeringan': [jumlah_bencana_kekeringan],
                'prevalensi_underweight': [prevalensi_underweight],
                'prevalensi_wasting': [prevalensi_wasting]
            })
            result = make_prediction(data)
            st.markdown('<div class="card"><h5>Hasil Prediksi: {}</h5></div>'.format(result), unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><h5>Visualisasi Data dan Peta</h5></div>', unsafe_allow_html=True)

        # Create pie chart for Daerah Prioritas and Bukan Daerah Prioritas
        data_pie_prior = pd.DataFrame({
            'Kategori': ['Daerah Prioritas', 'Bukan Daerah Prioritas'],
            'Jumlah': [(23 * 100 / 52), (29 * 100 / 52)]
        })
        fig = px.pie(data_pie_prior, names='Kategori', values='Jumlah', title='Distribusi Daerah Prioritas')
        st.plotly_chart(fig)

        data_pie_ev = pd.DataFrame({
            'Kategori': ['True Positive', 'False Positive', 'True Negatif', 'False Negatif'],
            'Jumlah': [(20 * 100 / 52), (3 * 100 / 52), (24 * 100 / 52), (5 * 100 / 52)]
        })
        fig = px.pie(data_pie_ev, names='Kategori', values='Jumlah', title='Distribusi Testing Model')
        st.plotly_chart(fig)

        data_pie_success_learn = pd.DataFrame({
            'Kategori': ['True Classification', 'False Classification'],
            'Jumlah': [(44 * 100 / 52), (8 * 100 / 52)]
        })
        fig = px.pie(data_pie_success_learn, names='Kategori', values='Jumlah', title='Distribusi Success Rate Model')
        st.plotly_chart(fig)

        # Add map of Indonesia
        m = folium.Map(location=[4.401489, 142.542279], zoom_start=4.2)
        st_folium(m, width=1200, height=400)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()