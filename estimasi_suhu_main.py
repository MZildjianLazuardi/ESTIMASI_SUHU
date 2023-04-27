import pickle
import streamlit as st

model = pickle.load(open('estimasi_suhu.sav', 'rb'))

st.title('Estimasi Suhu Udara')

#UTC, Humidity_percent, TVOC_ppb, eCO2_ppm, Raw_H2, Raw_Ethanol, Pressure_hPa, PM1_0, PM2_5, NC0_5, NC1_0, NC2_5, CNT
UTC = st.number_input('Input UTC(Universal Coordinated Time)')
Humidity_percent = st.number_input('Input Kelembaban Udara (%)')
TVOC_ppb = st.number_input('Input Senyawa Organik Volatil (ppb)')
eCO2_ppm = st.number_input('Input konsentrasi setara CO2 (ppm)')
Raw_H2 = st.number_input('Input molekul hidrogen mentah (H2)')
Raw_Ethanol = st.number_input('Input gas etanol mentah')
Pressure_hPa = st.number_input('Input Tekanan udara (hPa)')
PM1_0 = st.number_input('Input ukuran partikel < 1,0 µm (PM1.0)')
PM2_5 = st.number_input('Input ukuran partikel < 2,5 µm (PM2.5)')
NC0_5 = st.number_input('Input Jumlah konsentrasi partikel (NC0.5)')
NC1_0 = st.number_input('Input Jumlah konsentrasi partikel (NC1.0)')
NC2_5 = st.number_input('Input Jumlah konsentrasi partikel (NC2.5)')
CNT = st.number_input('Input seberapa banyaknya yg akan jadi sampel')

predict = ''

if st.button('Estimasikan Suhu Udara'):
    predict = model.predict(
        [[UTC, Humidity_percent, TVOC_ppb, eCO2_ppm, Raw_H2, Raw_Ethanol, Pressure_hPa, PM1_0, PM2_5, NC0_5, NC1_0, NC2_5, CNT]]
    )
    st.write ('Estimasi Suhu Udara (Celcius) : ', predict)