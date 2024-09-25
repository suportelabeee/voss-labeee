from configurate import *

create_top(big_text_title='Conforto Térmico', subtitle='Com relação ao ambiente térmico da sua estação de trabalho, você costuma sentir algum dos itens a seguir?', use_progress=True, progress_percentage=30)

st.markdown("""
    <style>
    [role=radiogroup]{
        gap: 5rem;
    }
    </style>
    """,unsafe_allow_html=True)


esquerda, meio, direita = st.columns([1.1,1.1,0.3], gap='large')
with meio:
    sempre, muitas_vezes, as_vezes, poucas_vezes, nunca, nao_possui = st.columns(6, gap='large')
    sempre.write('sempre')
    muitas_vezes.write('muitas vezes')
    as_vezes.write('às vezes')
    poucas_vezes.write('poucas vezes')
    nunca.write('nunca')

opcoes = ['sempre', 'muitas vezes', 'às vezes', 'poucas vezes', 'nunca']
choose_width = [1.7,2]

calor = create_radio(phrase='sinto desconforto pelo calor', selection=opcoes, use_list_selection=True, large=True, key='calor', two_columns_width=choose_width)
frio = create_radio(phrase='sinto desconforto pelo frio', selection=opcoes, use_list_selection=True, large=True, key='frio', two_columns_width=choose_width)
mvento = create_radio(phrase='sinto desconforto porque há muito vento', selection=opcoes, use_list_selection=True, large=True, key='mvento', two_columns_width=choose_width)
pvento = create_radio(phrase='sinto desconforto porque há pouco vento', selection=opcoes, use_list_selection=True, large=True, key='pvento', two_columns_width=choose_width)
sol = create_radio(phrase='o sol direto me atrapalha', selection=opcoes, use_list_selection=True, large=True, key='sol', two_columns_width=choose_width)
superficie = create_radio(phrase='há superfícies próximas (pisos, paredes, etc) muito quentes ou muito frias', selection=opcoes, use_list_selection=True, large=True, key='super', two_columns_width=choose_width)
corpo = create_radio(phrase='sinto desconforto por frio ou calor em alguma parte específica do corpo (mãos, pés, pescoço, cabeça, etc)', selection=opcoes, use_list_selection=True, large=True, key='corpo', two_columns_width=choose_width)

st.title('')
if next_page_button('Próximo'):
    options = [calor, frio, mvento, pvento, sol, superficie, corpo]
    if None in options:
        st.error('Responda **todas** as questões para continuar')
    else:
        st.session_state['PeR']['q2 - desconforto pelo calor'] = calor
        st.session_state['PeR']['q2 - desconforto pelo frio'] =frio
        st.session_state['PeR']['q2 - desconforto por excesso de vento'] = mvento
        st.session_state['PeR']['q2 - desconforto por falta de vento'] = pvento
        st.session_state['PeR']['q2 - desconforto por sol direto'] = sol
        st.session_state['PeR']['q2 - desconforto com temperatura de superfícies próximas'] = superficie
        st.session_state['PeR']['q2 - desconforto por frio ou calor em partes específicas do corpo'] = corpo
        if ('sempre' in options) or ('muitas vezes' in options) or ('às vezes' in options): 
            switch_page('q2a')
        else:
            st.session_state['PeR']['q2a - satisfacao em meses quentes'] = None
            st.session_state['PeR']['q2a - satisfacao em meses frios'] = None
            st.session_state['PeR']['q2a - ambiente térmico em meses quentes - temperatura'] = None
            st.session_state['PeR']['q2a - ambiente térmico em meses frios - temperatura'] = None
            st.session_state['PeR']['q2a - movimento do ar em meses quentes - ventilação'] = None
            st.session_state['PeR']['q2a - movimento do ar em meses frios - ventilação'] = None
            st.session_state['PeR']['q2a - ambiente térmico em meses quentes - conforto'] = None
            st.session_state['PeR']['q2a - ambiente  térmico em meses frios - conforto'] = None
            st.session_state['PeR']['q2a - ar-condicionado'] = None
            st.session_state['PeR']['q2a - aquecedores'] = None
            st.session_state['PeR']['q2a - ventilador de teto e/ou parede'] = None
            st.session_state['PeR']['q2a - ventilador portátil, de mesa e/ou individual'] = None
            st.session_state['PeR']['q2a - controle de janela'] = None
            st.session_state['PeR']['q2a - controle de ar-condicionado'] = None
            st.session_state['PeR']['q2a - controle de ventiladores'] = None
            st.session_state['PeR']['q2a - sinto desconforto por calor em meses quentes'] = None 
            st.session_state['PeR']['q2a - sinto desconforto por frio em meses quentes'] = None
            st.session_state['PeR']['q2a - sinto desconforto porque há muito vento em meses quentes'] = None
            st.session_state['PeR']['q2a - sinto desconforto porque há pouco vento em meses quentes'] = None
            st.session_state['PeR']['q2a - o sol direto me atrapalha em meses quentes'] = None
            st.session_state['PeR']['q2a - sinto desconforto devido à corrente de ar gerada pelo ar-condicionado em meses quentes'] = None 
            st.session_state['PeR']['q2a - sinto desconforto por não poder controlar a temperatura do ar-condicionado de acordo com a minha preferência em meses quentes'] = None
            st.session_state['PeR']['q2a - sinto desconforto devido à corrente de ar gerada pelo(s) ventialdor(es) em meses quentes'] = None
            st.session_state['PeR']['q2a - sinto desconforto devido à corrente de ar proveniente da(s) janela(s) em meses quentes'] = None
            st.session_state['PeR']['q2a - sinto desconforto por não poder abrir ou fechar as janelas de acordo com a minha preferência em meses quentes'] = None
            st.session_state['PeR']['q2a - há superfícies próximas (pisos, paredes, equipamentos etc) muito quentes ou muito frias em meses quentes'] = None
            st.session_state['PeR']['q2a - sinto desconforto por frio ou calor em alguma parte específica do corpo (mãos, pés, pescoço, cabeça, etc) em meses quentes'] = None
            st.session_state['PeR']['q2a - outros motivos de desconforto em meses quentes'] = None
            st.session_state['PeR']['q2a - sinto desconforto por calor em meses frios'] = None 
            st.session_state['PeR']['q2a - sinto desconforto por frio em meses frios'] = None
            st.session_state['PeR']['q2a - sinto desconforto porque há muito vento em meses frios'] = None
            st.session_state['PeR']['q2a - sinto desconforto porque há pouco vento em meses frios'] = None
            st.session_state['PeR']['q2a - o sol direto me atrapalha em meses frios'] = None
            st.session_state['PeR']['q2a - sinto desconforto devido à corrente de ar gerada pelo ar-condicionado em meses frios'] = None 
            st.session_state['PeR']['q2a - sinto desconforto por não poder controlar a temperatura do ar-condicionado de acordo com a minha preferência em meses frios'] = None
            st.session_state['PeR']['q2a - sinto desconforto devido à corrente de ar gerada pelo(s) ventialdor(es) em meses frios'] = None
            st.session_state['PeR']['q2a - sinto desconforto devido à corrente de ar proveniente da(s) janela(s) em meses frios'] = None 
            st.session_state['PeR']['q2a - sinto desconforto por não poder abrir ou fechar as janelas de acordo com a minha preferência em meses frios'] = None
            st.session_state['PeR']['q2a - há superfícies próximas (pisos, paredes, equipamentos etc) muito quentes ou muito frias em meses frios'] = None
            st.session_state['PeR']['q2a - sinto desconforto por frio ou calor em alguma parte específica do corpo (mãos, pés, pescoço, cabeça, etc) em meses frios'] = None
            st.session_state['PeR']['q2a - outros motivos de desconforto em meses frios'] = None
            switch_page('q3')

footer()