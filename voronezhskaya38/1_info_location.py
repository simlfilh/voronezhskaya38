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
                    <p class="highlight-blue">Наиболее удобный маршрут от м. Ладожская:</p>
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
        <iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d1000.0343624735921!2d30.347849476135128!3d59.914406765191515!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x4696304c97ab5355%3A0x66d8c4333f3a046c!2z0J7QsdCy0L7QtNC90YvQuSDQutCw0L3QsNC7LCDQodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQsywgMTkyMDA3!3m2!1d59.91303!2d30.351233899999997!4m5!1s0x4696304ceca92f83%3A0xf3e6cbbbeff992de!2z0JLQvtGA0L7QvdC10LbRgdC60LDRjyDRg9C70LjRhtCwLCAzOCwg0KHQsNC90LrRgi3Qn9C10YLQtdGA0LHRg9GA0LM!3m2!1d59.9146272!2d30.3481731!5e0!3m2!1sru!2sru!4v1751464734667!5m2!1sru!2sru" 
            width="600" 
            height="430" 
            style="border:0; border-radius: 10px;" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade">
        </iframe>
                    """, height=440)
st.divider()

col3, col4 = st.columns([1, 2])
with col4:
    st.markdown("""
        <div class="colored-container">
            <h3>Об общежитии</h3>
            <p>• Коридорный тип проживания (размещение по 2-5 человек в комнате)</p>  
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
    <p>📞 <a href="tel:+78124589730,4961">(812) 458-97-30 (внутр. 4961)</a></p>
            """, unsafe_allow_html=True)

st.markdown("🆘 Свяжитесь со студенческим советом через соответствующий раздел")
