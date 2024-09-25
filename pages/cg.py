from configurate import *

create_top(big_text_title='Considerando todos os aspectos,', use_line=False, use_progress=True, progress_percentage=75)

st.subheader('por favor indique o seu nível de satisfação com o conforto em geral da sua estação de trabalho.')

st.title('')
confortogeral = create_radio(divide=True, min=1, max=5, extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', key='confortogeral')

st.title('')
st.title('')
st.title('')
esquerda, direita = st.columns(2, gap='large')
esquerda.subheader('Por favor sinta-se à vontade para adicionar comentários que você possa ter a respeito da qualidade ambiental interna da sua estação de trabalho.')
entrada_confortogeral = direita.text_area(label='no label', label_visibility='hidden',value=None, key='entrybox_4', placeholder='Deixe sua mensagem aqui (não obrigatório)', max_chars=250)

st.title('')
if next_page_button('Próximo'):
    if None in [confortogeral]:
        st.error('Responda a questão para continuar')
    else:
        st.session_state['PeR']['cg - nível de satisfação com o conforto geral da estação de trabalho'] = confortogeral
        st.session_state['PeR']['cg - comentários'] = entrada_confortogeral
        switch_page('cp')

footer()