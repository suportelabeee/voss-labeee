from configurate import *

create_top(big_text_title='Puxa, encontramos um problema com a qualidade do ar interno...', img_url=r'static/Q3a.png', use_progress=True, progress_percentage=45)

st.subheader('Com relação ao ar interno próximo à sua estação de trabalho, com qual frequência você costuma identificar algum dos itens ou sintomas a seguir?')
opt = ['sempre', 'muitas vezes', 'às vezes', 'poucas vezes', 'nunca']
width_choosen = [1.7,2]


esquerda, meio, direita = st.columns([1.1,1.1,0.3], gap='large')
with meio:
    sempre, muitas_vezes, as_vezes, poucas_vezes, nunca, nao_possui = st.columns(6, gap='large')
    sempre.write('sempre')
    muitas_vezes.write('muitas vezes')
    as_vezes.write('às vezes')
    poucas_vezes.write('poucas vezes')
    nunca.write('nunca')


with st.container():
    st.markdown("""
    <style>
    [role=radiogroup]{
        gap: 5rem;
    }
    </style>
    """,unsafe_allow_html=True)
    cheiro = create_radio(phrase='sinto cheiros e/ou odores no ambiente', large=True, two_columns_width=width_choosen, selection=opt, use_list_selection=True, key='cheirosfortes')
    fadiga = create_radio(phrase='sensação de fadiga e/ou sonolência', large=True, two_columns_width=width_choosen, selection=opt, use_list_selection=True, key='fadiga')
    ressecamento = create_radio(phrase='sensação de ressecamento nos olhos, nariz e/ou mãos', large=True, two_columns_width=width_choosen, selection=opt, use_list_selection=True, key='ressecamento')
    alergia = create_radio(phrase='irritações na pele e/ou alergias', large=True, two_columns_width=width_choosen, selection=opt, use_list_selection=True, key='alergias')

st.title('')
st.title('')
st.title('')
st.title('')
st.title('Considerando todos os aspectos,')
st.subheader('qual o seu nível de satisfação com a qualidade do ar interno na sua estação de trabalho?')
st.title('')

my_width = [1,0.5,0.4,1.5,1]
qualidadedoar = create_radio(divide=True, five_columns_width=my_width,min=1, max=5, extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)')

qualidadedoar_ruim = False
if qualidadedoar:
    if qualidadedoar <= 2:
        qualidadedoar_ruim = True
        st.title('')
        st.title('')
        st.title('')
        st.title('')
        st.title("Temos uma nota baixa para a qualidade do ar...")
        st.subheader('Então, para termos certeza, por favor indique os motivos pelos quais você está insatisfeito(a).')
        st.info('Você pode selecionar mais de um, se aplicável.', icon='ℹ️')
        st.title('')
        cheiroscheckbox = st.checkbox('cheiros e odores', key='cheiroscheckbox')
        abafadocheckbox = st.checkbox('ambiente abafado', key='abafadocheckbox')
        arsecocheckbox = st.checkbox('ar interno muito seco', key='arsecocheckbox')
        arumidocheckbox = st.checkbox('ar interno muito úmido', key='arumidocheckbox')
        poeiracheckbox = st.checkbox('há poeira que causa irritação ou alergias', key='poeiracheckbox')
        alergiascheckbox = st.checkbox('há produtos que causam irritação ou alergias', key='alergiascheckbox')
        outros = st.checkbox('outro, por favor especifique:', key='outros')
        if outros:
            entrada = st.text_input(label='no label', label_visibility='hidden',value=None, key='entrybox', placeholder='Descreva aqui', max_chars=150)

st.title('')
if next_page_button('Próximo'):
    message = 'Erro: '
    ok = True
    arinterno = [cheiro, fadiga, ressecamento, alergia, qualidadedoar]
    if None in arinterno:
        ok = False
        message += '|Perguntas não respondidas'
    if qualidadedoar_ruim:
        if outros:
            if entrada == None:
                ok = False
                message += '|Caixa de texto vazia'
    if ok:
        st.session_state['PeR']['q3a - sinto cheiros e/ou odores no ambiente'] = cheiro
        st.session_state['PeR']['q3a - sensação de fadiga e/ou sonolência'] = fadiga
        st.session_state['PeR']['q3a - sensação de ressecamento nos olhos, nariz e/ou mãos'] = ressecamento
        st.session_state['PeR']['q3a - irritações na pele e/ou alergias'] = alergia
        st.session_state['PeR']['q3a - nível de satisfação com o ar interno'] = qualidadedoar
        st.session_state['PeR']['q3a - insatifação por cheiros e odores'] = None
        st.session_state['PeR']['q3a - insatifação por ambiente abafado'] = None
        st.session_state['PeR']['q3a - insatifação por ar interno muito seco'] =  None
        st.session_state['PeR']['q3a - insatifação por ar interno muito úmido'] = None
        st.session_state['PeR']['q3a - insatifação por haver poeira que causa irritação ou alergias'] = None
        st.session_state['PeR']['q3a - insatifação por haver produtos que causam irritação ou alergias'] = None
        st.session_state['PeR']['q3a - outros motivos'] = None
        if qualidadedoar_ruim:
            st.session_state['PeR']['q3a - insatifação por cheiros e odores'] = cheiroscheckbox
            st.session_state['PeR']['q3a - insatifação por ambiente abafado'] = abafadocheckbox
            st.session_state['PeR']['q3a - insatifação por ar interno muito seco'] =  arsecocheckbox
            st.session_state['PeR']['q3a - insatifação por ar interno muito úmido'] = arumidocheckbox
            st.session_state['PeR']['q3a - insatifação por haver poeira que causa irritação ou alergias'] = poeiracheckbox
            st.session_state['PeR']['q3a - insatifação por haver produtos que causam irritação ou alergias'] = alergiascheckbox
            if outros:
                st.session_state['PeR']['q3a - outros motivos'] = entrada
        st.session_state['hierarquia'] += 1
        switch_page('q4')
    else:
        st.error(message)

footer()