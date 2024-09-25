from configurate import *

create_top('Ao solicitar algum ajuste e/ou alteração nos sistemas a seguir a fim de atender à sua preferência,', use_line=False, use_progress=True, progress_percentage=85)

st.subheader('qual o seu nível de satisfação com a velocidade e a eficiência da resposta à sua solicitação?')

my_width = [1.5,0.1,0.4,0.6,0.5]
st.title('')
esquerda, meio, direita = st.columns([0.2,1,0.2])
with direita:
    st.caption('**nunca solicitei ajustes**')
    st.write('')
    st.write('')
    clima_checkbox = st.checkbox('no label', label_visibility='hidden', key='clima_checkbox')
with esquerda:
    st.title('')
    st.write('')
    st.write('')
    st.markdown('**1.aquecimento e/ou resfriamento**')
with meio:
    st.title('')
    if clima_checkbox:
        clima = create_radio(desabilitado=True, extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='clima', min=1, max=5, five_columns_width=my_width)
    else:
        clima = create_radio(extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='clima', min=1, max=5, five_columns_width=my_width)
esquerda, direita = st.columns([1.2,0.2])
esquerda.info('por exemplo, elevar ou reduzir a temperatura do sistema de climatização', icon='ℹ️')


esquerda, meio, direita = st.columns([0.2,1,0.2])
with direita:
    st.title('')
    ventilacao_checkbox = st.checkbox('no label', label_visibility='hidden', key='ventilacao_checkbox')
with esquerda:
    st.title('')
    st.markdown('**2.ventilação**')
with meio:
    if ventilacao_checkbox:
        ventilacao = create_radio(desabilitado=True, extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='ventilacao', min=1, max=5, five_columns_width=my_width)
    else:
        ventilacao = create_radio(extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='ventilacao', min=1, max=5, five_columns_width=my_width)
esquerda, direita = st.columns([1.2,0.2])
esquerda.info('por exemplo, aumentar ou reduzir a velocidade e/ou direção do ar', icon='ℹ️')


esquerda, meio, direita = st.columns([0.2,1,0.2])
with direita:
    st.title('')
    iluminacao_checkbox = st.checkbox('no label', label_visibility='hidden', key='iluminacao_checkbox')
with esquerda:
    st.title('')
    st.markdown('**3.iluminação**')
with meio:
    if iluminacao_checkbox:
        iluminacao = create_radio(desabilitado=True, extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='iluminacao', min=1, max=5, five_columns_width=my_width)
    else:
        iluminacao = create_radio(extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='iluminacao', min=1, max=5, five_columns_width=my_width)
esquerda, direita = st.columns([1.2,0.2])
esquerda.info('por exemplo, trocar, acender ou apagar lâmpadas; abrir ou fechar elementos de sombreamento', icon='ℹ️')

st.title('')
st.title('')
esquerda, direita = st.columns(2, gap='large')
esquerda.subheader('Você gostaria de compartilhar alguma ocasião em que foi necessário algum ajuste dos sistemas do edifício com o objetivo de melhorar a sua satisfação com a sua estação de trabalho?')
entrada_solicitacao = direita.text_area(label='no label', label_visibility='hidden',value=None, key='entrybox_5', placeholder='Deixe sua mensagem aqui (não obrigatório)', max_chars=250)

st.title("")
if next_page_button('Próximo'):
    ok = True
    if not clima:
        if not clima_checkbox:
            ok = False
    if not ventilacao:
        if not ventilacao_checkbox:
            ok = False
    if not iluminacao:
        if not iluminacao_checkbox:
            ok = False
    if ok:
        st.session_state['PeR']['sp - velocidade de resposta à solicitação de aquecimento e/ou resfriamento'] = 'Não possui'
        st.session_state['PeR']['sp - velocidade de resposta à solicitação de controle de ventilação'] = 'Não possui'
        st.session_state['PeR']['sp - velocidade de resposta à solicitação de alteração de iluminação'] = 'Não possui'

        if not clima_checkbox:
            st.session_state['PeR']['sp - velocidade de resposta à solicitação de aquecimento e/ou resfriamento'] = clima
        if not ventilacao_checkbox:
            st.session_state['PeR']['sp - velocidade de resposta à solicitação de controle de ventilação'] = ventilacao
        if not iluminacao_checkbox:
            st.session_state['PeR']['sp - velocidade de resposta à solicitação de alteração de iluminação'] = iluminacao

        st.session_state['PeR']['sp - comentários'] = entrada_solicitacao
        switch_page('q6')
    else:
        st.error('Responda **todas** as perguntas para prosseguir')

footer()