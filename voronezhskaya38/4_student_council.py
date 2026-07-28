import streamlit as st

st.title("👫 Студенческий совет общежития СПбГЭУ №7")
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
            padding: 10px;
            margin-bottom: 20px;
            position: relative;
        }
        .highlight-blue-2 {
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
        <p><b>Студенческий совет общежития</b> является органом студенческого самоуправления в общежитии СПбГЭУ, 
        образованным по инициативе обучающихся в целях учета мнения обучающихся по вопросам реализации молодежной 
        политики и воспитательной деятельности в сфере социальной поддержки и социальной защиты обучающихся, 
        проживающих в общежитиях, и утвержденный решением администрации Университета.</p> 
        <p>Целями деятельности органов студенческого самоуправления в общежитиях СПбГЭУ являются формирование у 
        обучающихся активной гражданской позиции, сознательного и ответственного отношения к возможностям своей 
        социальной самоорганизации и культурно-нравственного саморазвития, развитие умений и навыков самоуправления 
        и подготовка обучающихся к компетентному и ответственному участию в жизни общества.</p> 
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <p><b>Задачами деятельности органов студенческого самоуправления в общежитиях СПбГЭУ являются:</b></p>
                </div>
            </div>
        <p>—  учет мнения обучающихся, проживающих в общежитии;</p>
        <p>—  организация взаимодействия администрации СПбГЭУ и студенческих общежитий в части улучшения 
        жилищных условий проживания обучающихся совместно с ПО;</p>
        <p>—  содействие обучающимся в решении социальных вопросов, связанных с проживанием в общежитии 
        совместно с ПО;</p>
        <p>—  организация просветительских, культурно-досуговых, спортивно-оздоровительных и адаптационных 
        мероприятий для обучающихся, проживающих в общежитии;</p>
        <p>—  противодействие деструктивной идеологии в студенческой среде.</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.header("Председатель студенческого совета")
col1, col2 = st.columns([1, 3])
with col1:
    st.image("администрация_в38/председатель_в38.jpg", width=250)
with col2:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Староста общежития</h3> 
                    </div>
                </div>
            <p><b>Макарова Светлана Денисовна</b></p>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/swetik2636" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;">Связаться в VK</p>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://t.me/svetik3626" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-telegram"></i></a>
                    <p style="margin: 0; font-size: 23px;">Связаться в TG</p>
                </div>
            <p>📞 <a href="tel:+79040200888">+79040200888</a></p>
            <br>
        </div>
                """, unsafe_allow_html=True)
st.divider()

# 2 ЭТАЖ
col7, col8 = st.columns([1, 3])
with col7:
    st.image("администрация_в38/староста_2_в38.jpg", width=250)
with col8:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Староста 2 этажа</h3> 
                    </div>
                </div>
            <p><b>Коньшунова Анастасия Сергеевна</b></p>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/konshunova" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;">Связаться в VK</p>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://t.me/knshnv" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-telegram"></i></a>
                    <p style="margin: 0; font-size: 23px;">Связаться в TG</p>
                </div>
            <p>📞 <a href="tel:+79136694212">+79136694212</a></p>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 3 ЭТАЖ
col9, col10 = st.columns([1, 3])
with col9:
    st.image("администрация_в38/староста_3_в38.jpg", width=250)
with col10:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Староста 3 этажа</h3> 
                    </div>
                </div>
            <p><b>Грицюк Анна Валентиновна</b></p>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/anik0321" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;">Связаться в VK</p>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://t.me/anechka0321" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-telegram"></i></a>
                    <p style="margin: 0; font-size: 23px;">Связаться в TG</p>
                </div>
            <p>📞 <a href="tel:+79149652360">+79149652360</a></p>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 4 ЭТАЖ
col11, col12 = st.columns([1, 3])
with col11:
    st.image("администрация_в38/староста_4_в38.jpg", width=250)
with col12:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Староста 4 этажа</h3> 
                    </div>
                </div>
            <p><b>Винокуров Михаил Владимирович</b></p>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/id_3322" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;">Связаться в VK</p>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://t.me/opiummg" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-telegram"></i></a>
                    <p style="margin: 0; font-size: 23px;">Связаться в TG</p>
                </div>
            <p>📞 <a href="tel:+79126444412">+79126444412</a></p>
            <br>
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
