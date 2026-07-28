import streamlit as st

st.title("📲 Наши социальные сети")
st.divider()

st.markdown("""
    <style>
        .colored-container {
           background-color: #FFFFFF; 
           border-radius: 10px;     
           padding: 10px;          
           margin-bottom: 20px;     
           color: black !important;
           line-height: 1.0;
           font-size: 21px;
        }
        .fab {
           font-size: 24px;
           color: #0088cc; /* Цвет иконок Telegram */
        }
        .custom-links a {
            color: white !important;
            text-decoration: none; 
        }
        .custom-links a:hover {
            color: #ccc !important;  
            text-decoration: underline; 
        }
        .support-container {
            background-color: #e8f4f8;
            border-radius: 10px;
            padding: 15px;
            margin-top: 10px;
            border-left: 4px solid #0088cc;
        }
        .support-container p {
            margin: 5px 0;
            font-size: 16px;
        }
        .support-container a {
            color: #0088cc !important;
            text-decoration: none;
        }
        .support-container a:hover {
            text-decoration: underline;
        }
    </style>
    <div class="colored-container">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 20px;">
                    <a href="https://max.ru/id7840483155_gos17" target="_blank">
                        <i class="fas fa-comment-dots fa-2x" style="color: #00BFFF;"></i>
                    </a>
                    <h3>Канал «Общежития СПбГЭУ» в MAX.</h3>
                </div>
        </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("**Контакты для связи:**")
st.write("Заведующий общежитием: Малышева Елена Андреевна 👩🏼‍💼")
st.markdown("""
    <style>
        .custom-links a {
            color: white !important;
            text-decoration: none; 
        }
        .custom-links a:hover {
            color: #ccc !important;  
            text-decoration: underline; 
        }
    </style>
    <div class="custom-links">
        <p>📞 <a href="tel:+78124589730,4961">(812) 458-97-30 (внутр. 4961)</a></p>
    </div>
""", unsafe_allow_html=True)
st.divider()

st.markdown("""
    <div class="support-container">
        <p><strong>🛠️ Техническая поддержка</strong></p>
        <p>📧 <a href="mailto:savchenko.va@unecon.ru">savchenko.va@unecon.ru</a></p>
        <p>📞 <a href="tel:+78124589730,4299">(812) 458-97-30, доб. 4299</a></p>
    </div>
""", unsafe_allow_html=True)

