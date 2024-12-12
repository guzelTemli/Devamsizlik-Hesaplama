import streamlit as st
import joblib
import numpy as np

# Modeli yükleme
model = joblib.load('svm_model.joblib')

# Streamlit web arayüzü
st.title("Öğrenci Katılım Tahmin Uygulaması")

# Kullanıcıdan veri girişi alma
hava_durumu = st.selectbox("Hava Durumu", ["güneşli", "yağmurlu", "karlı"])
uyku_suresi = st.slider("Uyku Süresi (Saat)", 4, 10, 7)
motivasyon = st.slider("Motivasyon (1-10)", 1, 10, 5)
mesafe = st.number_input("Okula Mesafe (km)", 0.5, 20.0, 5.0)
gecmis_katilim = st.slider("Geçmiş Katılım Yüzdesi", 50, 100, 80)

# Hava durumu kodlaması
if hava_durumu == "güneşli":
    hava_durumu_encoded = [1, 0, 0]
elif hava_durumu == "yağmurlu":
    hava_durumu_encoded = [0, 1, 0]
else:
    hava_durumu_encoded = [0, 0, 1]

# Modelin tahmin yapabilmesi için gerekli veriyi hazırlama
input_data = np.array([[uyku_suresi, motivasyon, mesafe, gecmis_katilim] + hava_durumu_encoded])

# Tahmin yapma
if st.button("Tahmin Et"):
    prediction = model.predict(input_data)
    st.write("Tahmin edilen katılım durumu:", prediction[0])

