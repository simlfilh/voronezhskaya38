import streamlit as st

st.title("🏠 Общежитие СПбГЭУ №7")
st.divider()

st.subheader("Приветствуем вас, дорогие студенты, в нашем общежитии!")
st.subheader("Мы рады, что вы стали частью нашей дружной студенческой семьи!")
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
        <style>
            .colored-container {
               background-color: #FFFFFF;  
               border-radius: 10px;      
               padding: 20px;            
               margin-bottom: 10px;      
               color: black !important;  
               line-height: 1.0;
               font-size: 21px;
            }
            .image-container {
               background-color: #FFFFFF; 
               border-radius: 10px;      
               padding: 20px;            
               margin-bottom: 10px;      
               height: 100%;           
               display: flex;
               align-items: center;     
               justify-content: center; 
            }
            .image-container img {
               max-width: 100%;
               max-height: 100%;
               border-radius: 5px;     
               object-fit: contain;    
            }
            .highlight-green {
                background-color: #C8E6C9; 
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
                position: relative;
            }
            .highlight-blue {
                background-color: #B3E5FC;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
                position: relative;
            }
            .text-indent-content {
                position: relative;
                color: black;
                line-height: 1.4;
            }
        </style>
        <div class="colored-container">
            <h3>Адрес: Санкт-Петербург, Воронежская ул., д. 38</h3>
                <div class="text-indent-content">
                    <p class="highlight-blue">Наиболее удобный маршрут:</p>
                </div>
            <br>
            <p>→ от м. Обводный канал 3 минуты пешком</p>  
            <br>
        </div>
                """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class="colored-container">
            <h3>Мы в Google Maps ⬇️</h3>
        </div>
                """, unsafe_allow_html=True)
    st.components.v1.html("""
        <div style="position:relative;overflow:hidden;">
            <a href="https://yandex.ru/maps/2/saint-petersburg/?utm_medium=mapframe&utm_source=maps" 
                style="color:#eee;font-size:12px;position:absolute;top:0px;">
                Санкт‑Петербург
            </a>
            <a href="https://yandex.ru/maps/2/saint-petersburg/?ll=30.349274%2C59.914342&mode=routes&rtext=59.914713%2C30.349703~59.914434%2C30.348826&rtt=mt&ruri=ymapsbm1%3A%2F%2Ftransit%2Fstop%3Fid%3Dstation__9805886~ymapsbm1%3A%2F%2Forg%3Foid%3D1256557715&utm_medium=mapframe&utm_source=maps&z=20.8" 
                style="color:#eee;font-size:12px;position:absolute;top:14px;">
                Яндекс Карты
            </a>
            <iframe 
                src="https://yandex.ru/map-widget/v1/?ll=30.349274%2C59.914342&mode=routes&rtext=59.914713%2C30.349703~59.914434%2C30.348826&rtt=mt&ruri=ymapsbm1%3A%2F%2Ftransit%2Fstop%3Fid%3Dstation__9805886~ymapsbm1%3A%2F%2Forg%3Foid%3D1256557715&z=20.8" 
                width="100%" 
                height="400" 
                frameborder="1" 
                allowfullscreen="true" 
                style="position:relative;border-radius: 10px;border: none;">
            </iframe>
        </div>
                    """, height=440)
st.divider()

col3, col4 = st.columns([1, 2])
with col4:
    st.markdown("""
        <div class="colored-container">
            <h3>Об общежитии</h3>
            <p>• Коридорный тип проживания (размещение по 2-4 человека в комнате)</p>  
            <p>• 4 этажа | 376 мест</p>
            <p>• На каждом этаже кухня, оснащенная электрическими плитами и столами</p>
            <p>• Общая прачечная</p>
            <p>• Интернет</p>
            <p>• 1-5 минут пешком от метро</p>
        </div>
                """, unsafe_allow_html=True)
with col3:
    st.image("здание_общежития_в38.jpg",
             use_container_width=True)
st.divider()

st.markdown("*❗️ Пожалуйста, прежде чем связываться с администрацией, ознакомьтесь со всей информацией на сайте.*")
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

st.markdown("🆘 Свяжитесь со студенческим советом через соответствующий раздел")
