from configurate import *

def reset_var(var):
    var = None

create_top(use_line=False, use_progress=True, progress_percentage=80)
st.info('Estamos quase acabando! Precisamos apenas dos últimos detalhes', icon='ℹ️')
st.title('Qual é o seu nível de satisfação com a disponibilidade de controle')
st.subheader('dos itens a seguir para adaptação da sua estação de trabalho de forma a atender às suas preferências?')
my_width = [1.5,0.5,0.4,0.6,0.5]
st.title('')
esquerda, direita = st.columns([1,0.2])

with direita:
    st.caption('meu escritório não possui')
    st.write('')
    st.write('')
    arcondicionado_checkbox = st.checkbox('no label', label_visibility='hidden', key='arcondicionado_checkbox')
    st.title('')
    ventiladores_checkbox = st.checkbox('no label', label_visibility='hidden', key='ventiladores_checkbox')
    st.title('')
    janelas_checkbox = st.checkbox('no label', label_visibility='hidden', key='janelas_checkbox')
    st.title('')
    cortinas_checkbox = st.checkbox('no label', label_visibility='hidden', key='cortinas_checkbox')
    st.title('')
    luzes_checkbox = st.checkbox('no label', label_visibility='hidden', key='luzes_checkbox')
with esquerda:
    st.title('')
    if arcondicionado_checkbox:
        arcondicionado = create_radio(desabilitado=True, phrase='ar-condicionado e/ou aquecedores', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='controlearcondicionado', min=1, max=5, five_columns_width=my_width)
    else:
        arcondicionado = create_radio(phrase='ar-condicionado e/ou aquecedores', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='controlearcondicionado', min=1, max=5, five_columns_width=my_width)
    if ventiladores_checkbox:
        ventiladores = create_radio(desabilitado=True, phrase='ventiladores', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='controleventiladores', min=1, max=5, five_columns_width=my_width)
    else:
        ventiladores = create_radio(phrase='ventiladores', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='controleventiladores', min=1, max=5, five_columns_width=my_width)
    if janelas_checkbox:
        janelas = create_radio(desabilitado=True, phrase='abrir ou fechar janelas', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='controlejanelas', min=1, max=5, five_columns_width=my_width)
    else:
        janelas = create_radio(phrase='abrir ou fechar janelas', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='controlejanelas', min=1, max=5, five_columns_width=my_width)
    if cortinas_checkbox:
        cortinas = create_radio(desabilitado=True, phrase='abrir ou fechar cortinas', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='controlecortinas', min=1, max=5, five_columns_width=my_width)
    else:
        cortinas = create_radio(phrase='abrir ou fechar cortinas', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='controlecortinas', min=1, max=5, five_columns_width=my_width)
    if luzes_checkbox:
        luzes = create_radio(desabilitado=True, phrase='acender ou apagar as luzes', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='controleluzes', min=1, max=5, five_columns_width=my_width)
    else:
        luzes = create_radio(phrase='acender ou apagar as luzes', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', divide=True, key='controleluzes', min=1, max=5, five_columns_width=my_width)

st.title('')
if next_page_button('Próximo'):
    ok = True
    if not arcondicionado:
        if not arcondicionado_checkbox:
            ok = False
    if not ventiladores:
        if not ventiladores_checkbox:
            ok = False
    if not janelas:
        if not janelas_checkbox:
            ok = False
    if not cortinas:
        if not cortinas_checkbox:
            ok = False
    if not luzes:
        if not luzes_checkbox:
            ok = False
    if ok:
        st.session_state['PeR']['cp - controle de ar-condicionado e aquecedores'] = 'Não possui'
        st.session_state['PeR']['cp - controle de ventiladores'] = 'Não possui'
        st.session_state['PeR']['cp - controle de janelas'] = 'Não possui'
        st.session_state['PeR']['cp - controle de cortinas'] = 'Não possui'
        st.session_state['PeR']['cp - controle de luzes'] = 'Não possui'

        if not arcondicionado_checkbox:
            st.session_state['PeR']['cp - controle de ar-condicionado e aquecedores'] = arcondicionado
        if not ventiladores_checkbox:
            st.session_state['PeR']['cp - controle de ventiladores'] = ventiladores
        if not janelas_checkbox:
            st.session_state['PeR']['cp - controle de janelas'] = janelas
        if not cortinas_checkbox:
            st.session_state['PeR']['cp - controle de cortinas'] = cortinas
        if not luzes_checkbox:
            st.session_state['PeR']['cp - controle de luzes'] = luzes
            
        switch_page('sp')
    else:
        st.error('Responda **todas** as perguntas')

footer()