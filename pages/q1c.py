from configurate import *

create_top(big_text_title='Onde você passa mais tempo?', subtitle='Em um dia típico de trabalho, com que frequência você estima que utilize...', use_line=True, use_progress=True, progress_percentage=25)
st.info('Já sabemos como é o layout da sua estação de trabalho e a sua proximidade com as aberturas. Agora precisamos saber o tempo que você costuma utilizar cada um desses ambientes.', icon='ℹ️')
st.markdown("""
    <style>
    [role=radiogroup]{
        gap: 5rem;
    }
    </style>
    """,unsafe_allow_html=True)


esquerda, meio, direita = st.columns([1.05,1.1,0.4], gap='large')
with meio:
    sempre, muitas_vezes, as_vezes, poucas_vezes, nunca, nao_possui = st.columns(6, gap='large')
    sempre.write('sempre')
    muitas_vezes.write('muitas vezes')
    as_vezes.write('às vezes')
    poucas_vezes.write('poucas vezes')
    nunca.write('nunca')
    nao_possui.write('não possui')


opcoes = ['sempre', 'muitas vezes', 'às vezes', 'poucas vezes', 'nunca', 'não possui']

estacaodetrabalho = create_radio(large=True, phrase='sua estação de trabalho?', use_list_selection=True, selection=opcoes, two_columns_width=[1.5,2], key='estacaotrab')
estacaodetrabalhorotativa = create_radio(large=True, phrase='estações de trabalho rotativas e/ou não-fixas?', use_list_selection=True, selection=opcoes, two_columns_width=[1.5,2], key='estacaorotativa')
areagrupo = create_radio(large=True, phrase='áreas específicas para desenvolver atividades em grupo e/ou dinâmicas?', use_list_selection=True, selection=opcoes, two_columns_width=[1.5,2], key='areagrupo')
individual = create_radio(large=True, phrase='áreas específicas para desenvolver atividades individuais e/ou focadas?', use_list_selection=True, selection=opcoes, two_columns_width=[1.5,2], key='individual') 
conferencia = create_radio(large=True, phrase='salas de conferência e/ou reunião?', use_list_selection=True, selection=opcoes, two_columns_width=[1.5,2], key='conf')
fora = create_radio(large=True, phrase='fica fora do escritório, em atividades externas?', use_list_selection=True, selection=opcoes, two_columns_width=[1.5,2], key='fora')

st.title('')
if next_page_button('Próximo'):
    options = [estacaodetrabalho, estacaodetrabalhorotativa, areagrupo, individual, conferencia, fora]
    if None in options:
        st.error('Responda **todas** as questões para prosseguir') 
    else:
        st.session_state['PeR']['q1c - estação de trabalho'] = estacaodetrabalho
        st.session_state['PeR']['q1c - estações de trabalho rotativas'] = estacaodetrabalhorotativa
        st.session_state['PeR']['q1c - áreas para atividades em grupo'] = areagrupo
        st.session_state['PeR']['q1c - áreas para atividades focadas ou individuais'] =  individual
        st.session_state['PeR']['q1c - salas comerciais ou de reunião'] = conferencia
        st.session_state['PeR']['q1c - atividades externas ou fica fora do escritório'] = fora
        switch_page('q2')

footer()