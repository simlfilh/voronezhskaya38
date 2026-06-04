import streamlit as st

def create_button(url, text):
    return f"""
    <div class="custom-button">
        <a href="{url}" style="text-decoration: none;">
            <button style="
                width: 100%;
                color: white;
                background-color: #DC3545;
                border: none;
                padding: 10px 0;
                border-radius: 5px;
                font-weight: bold;
                cursor: pointer;
            ">{text}</button>
        </a>
    </div>
    """

st.title("🧺 Бытовое пространство")
st.divider()

st.markdown("""
        <style>
            .colored-container {
               background-color: #FFFFFF; 
               border-radius: 10px;      
               padding: 20px;           
               margin-bottom: 20px;     
               color: black !important; 
               line-height: 1.0;
               font-size: 21px;
            }
            .highlight-green {
                background-color: #C8E6C9; 
                border-radius: 10px;
                padding-left: 20px;
                margin-bottom: 20px;
                position: relative;
            }
            .highlight-red {
                background-color: #FFCDD2; 
                border-radius: 10px;
                padding-left: 20px;
                margin-bottom: 20px;
                position: relative;
            }
            .highlight-blue {
                background-color: #B3E5FC;
                border-radius: 10px;
                padding-left: 20px;
                margin-bottom: 20px;
                position: relative;
            }
            .text-indent-content {
                position: relative;
                color: black;
                line-height: 1.4;
            }
        </style>
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>🛌 Бельевая | 1 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>В бельевой можно получить/поменять:</p>  
            <p>• подушку</p>
            <p>• одеяло</p>
            <p>• покрывало</p>
            <p>• шторы</p>
            <p>• наматрасник</p>
            <p>• полный комплект постельного белья</p>
            <br>
            <p>Постельное белье меняется 1 раз в неделю бесплатно: отдали грязное - тут же получили чистое.</p>
        </div>
                """, unsafe_allow_html=True)
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.image("рекреации_в38/прачечная_в38.jpg")
with col2:
    st.markdown("""
            <div class="colored-container">
                    <div class="highlight-blue">
                        <div class="text-indent-content">
                            <h3>🧺 Прачечная | 2 ЭТАЖ</h3> 
                        </div>
                    </div>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                    <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                        <a href="https://t.me/Landromaticbot" target="_blank" style="margin-left: 5px; font-size: 25px;">
                        <i class="fab fa-telegram"></i></a>
                        <p style="margin: 0; font-size: 21px;">Оплата: в банкомате на 1-ом этаже или через 
                        телеграм-бот "Ландроматик"</p>
                    </div>
            </div>
                    """, unsafe_allow_html=True)
st.divider()

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>🔐 Камера хранения | ЦОКОЛЬНЫЙ ЭТАЖ</h3> 
                </div>
            </div>
    </div>
            """, unsafe_allow_html=True)
st.divider()
# убрать st.markdown(create_button("https://requestsunecondorms.streamlit.app/", "Оставить электронную заявку"), unsafe_allow_html=True)
# убрать st.divider()

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

st.markdown("🆘 Свяжитесь со студенческим советом через соответствующий раздел")
