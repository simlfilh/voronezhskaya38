import streamlit as st

st.title("🧮 Перерасчёт проживания")
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
            padding: 15px;
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
        <div class="highlight-blue">
                <div class="text-indent-content">
                    <p><b>Если Вы отсутствуете в общежитии 5 ДНЕЙ И БОЛЕЕ (без учета дня отъезда и прибытия), 
                    Вы можете подать заявление на перерасчет за коммунальные услуги:</b></p> 
                </div>
            </div>
        <p><b>1.</b> Рядом с охраной в тетради «ВЫЕЗД» пишите ФИО, блок и дату выезда.</p>
        <p><b>2.</b> Вернувшись, Вы записываете в тетради «ЗАЕЗД» ФИО, блок и дату заезда.</p>
        <p><b>3.</b> Заполняете заявление, где пишите СЛЕДУЮЩИЙ ДЕНЬ ПОСЛЕ ВЫЕЗДА и ДЕНЬ ДО ПРИЕЗДА.</p>
        <p><b>4.</b> К заявлению прикладываете копии билетов или документов, подтверждающих ваше 
        отсутствие.</p>
        <p><b>5.</b> Заявление заполняется на имя заведующего общежитием, Малышевой Елены Андреевны.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-red">
                <div class="text-indent-content">
                    <h3>ВАЖНО❗️</h3> 
                </div>
            </div>
        <p>• Заявления находятся у заведующего общежитием.</p>
        <p>• Перерасчет будет произведен только в случае отсутствия задолженности.</p>
        <p>• Перерасчет ≠ возврат денежных средств на карту. Просто пересчитают оплату за последующие месяцы 
        проживания.</p>
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

# st.markdown("🆘 Свяжитесь со студенческим советом через соответствующий раздел")
