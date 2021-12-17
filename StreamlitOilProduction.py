from numpy import int0
import pandas as pd
import json
import pylab.pyplot as plt
import streamlit as st
import time


file_json = open('kode_negara_lengkap.json')
data_json = json.load(file_json)
excell = pd.read_csv('produksi_minyak_mentah.csv')
data_excel = pd.DataFrame(excell)

nama_negara_untuk_selectbox = []
selectboxnama = []
def fungsi_menyamakan_nama_json_dengan_csv():
    for i in range(len(data_excel.kode_negara)):
        for nama in data_json:
            if nama['alpha-3'] in data_excel.kode_negara[i]:
                nama_negara_untuk_selectbox.append(nama['name'])

    for i in range(0, len(nama_negara_untuk_selectbox)):
        count = 1                                   #untuk setiap i pada range 0 sampai panjang list nama_negara_untuk_selectbox nilai count = 1

        for j in range(i+1, len(nama_negara_untuk_selectbox)):            #looping j dengan range i+1 sebagai list yang satu kali lebih besar urutannya dari i
            if(nama_negara_untuk_selectbox[i] == (nama_negara_untuk_selectbox[j])):             #jika pada nama_negara_untuk_selectbox ke-i sama dengan nama_negara_untuk_selectbox ke-j dengan j = i+1 atau kata setelah i
                count = count + 1                   #maka nilai count akan bertambah 1
                nama_negara_untuk_selectbox[j] ='tasama'                  #dan perlu dioutputkan sebuah string pada nama_negara_untuk_selectbox looping j kedalam list agar menghindari pengulangan kata yang sudah terdeteksi sama 
                    
        if(count > 1 and nama_negara_untuk_selectbox[i] != 'tasama'):   #jika count > 1 artinya ada count bertambah dan terjadi kesamaan huruf di nama_negara_untuk_selectbox i = nama_negara_untuk_selectbox j
                                                        #dan nama_negara_untuk_selectbox[i] tidak sama dengan tasama
            selectboxnama.append(nama_negara_untuk_selectbox[i])

fungsi_menyamakan_nama_json_dengan_csv()

      

#Streamlit Interface

st.set_page_config(layout="wide", page_title="Uas Prokom")
plt.style.use('seaborn-dark-palette')


st.header("Program Streamlit Oil Production")

st.subheader("Perbandingan Jumlah Produksi Tiap Negara pada Tahun ke-T")

nama_negara = st.selectbox("Pilih Negara yang diinginkan: ", (selectboxnama))


@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return a * b

a = 2
b = 210  # 👈 Changed this
res = expensive_computation(a, b)

st.write("Result:", res)

#Soal A
#Menampilkan Grafik Suatu Produksi Minyak total pada suatu Negara-N tertentu

for tiap_kode in data_json:
    if nama_negara == tiap_kode['name']:
        kode = tiap_kode['alpha-3']


diagram_garis = data_excel[data_excel['kode_negara'] == kode][['tahun', 'produksi']]
x_garis = data_excel[data_excel['kode_negara'] == kode].tahun
y_garis = data_excel[data_excel['kode_negara'] == kode].produksi
fig_1, ax1 = plt.subplots()
ax1.plot(x_garis, y_garis)
ax1.set_title(f'Nilai Produksi dari {nama_negara}')
st.pyplot(fig_1)



#Soal B

st.subheader("N negara dengan Produksi Terbesar")
st.markdown('''Program N negara dengan Produksi Terbesar, jika ingin 
melihat grafik geser slider sesuai yang diinginkan''')

banyaknegara = st.slider(label = "Banyak Negara", min_value = 1, max_value= 142)
tahun = st.slider(label = "Tahun: ", min_value = 1970, max_value = 2015)


def ubah_kode_ke_nama(kode_negara):
    for tiap_negara in data_json:
        if tiap_negara['alpha-3'] == kode_negara:
            negara.append(tiap_negara['name'])

negara = []

produksi_terbanyak = data_excel[data_excel.tahun == tahun].produksi.sort_values(ascending = False)[:banyaknegara].values 

fig2, ax = plt.subplots()

for tiap_produksi in produksi_terbanyak:
    negara_produksi_terbanyak = data_excel[(data_excel.tahun == tahun) & (data_excel.produksi == tiap_produksi)].kode_negara.item()
    nama_negara_sebenarnya = ubah_kode_ke_nama(negara_produksi_terbanyak)

    ax.barh(negara_produksi_terbanyak, tiap_produksi)

ax.set_title(f'{banyaknegara} Negara dengan produksi terbesar pada tahun {tahun}')

st.pyplot(fig2)
    

#Soal C

st.subheader("N negara dengan jumlah Produksi Terbesar Sepanjang 1970 - 2015")

banyaknegaratotal = st.slider(label = "Banyak Negara untuk Produksi Total", min_value = 1, max_value= 142)
jumlah_total = data_excel.groupby(['kode_negara']).sum().sort_values(by = 'produksi', ascending=False).produksi[:banyaknegaratotal].values
jumlah_total_index_negara = data_excel.groupby(['kode_negara']).sum().sort_values(by = 'produksi', ascending=False).produksi[:banyaknegaratotal].index

x_bar = jumlah_total_index_negara
y_bar = jumlah_total

fig3, ax = plt.subplots()
ax.barh(jumlah_total_index_negara, jumlah_total)
ax.set_title(f'{banyaknegaratotal} negara dengan produksi terbesar dalam periode 1970-2015')
st.pyplot(fig3)




#Soal D
tahunelite = st.slider(label = "Tahun yang Anda inginkan untuk mencari Data dari suatu negara yang paling mencolok data-nya: ", min_value = 1970, max_value = 2015)


produksi_terbanyakelite = data_excel[data_excel.tahun == tahunelite].produksi.sort_values(ascending = False).values 
