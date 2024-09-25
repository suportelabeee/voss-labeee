from configurate import *

create_top(big_text_title='Você pode escolher diariamente a sua estação de trabalho -', subtitle='queremos saber um pouco mais sobre isso.', use_progress=True, progress_percentage=21)

st.subheader('Quais dos fatores a seguir são mais importantes na escolha da sua estação de trabalho?')

confortotermico = create_radio(phrase='Conforto térmico', extreme_left='pouco importante', extreme_right='muito importante', min=1, max=5, key='ct', divide=True)
qualidadedoar = create_radio(phrase='Qualidade do ar', extreme_left='pouco importante', extreme_right='muito importante', min=1, max=5, key='qa', divide=True)
confortovisual = create_radio(phrase='Conforto visual', extreme_left='pouco importante', extreme_right='muito importante', min=1, max=5, key='cv', divide=True)
confortoacustico = create_radio(phrase='Privacidade visual', extreme_left='pouco importante', extreme_right='muito importante', min=1, max=5, key='ca', divide=True)
privacidadevisual = create_radio(phrase='Privacidade acústica', extreme_left='pouco importante', extreme_right='muito importante', min=1, max=5, key='pv', divide=True)
privacidadeacustica = create_radio(phrase='Conforto térmico', extreme_left='pouco importante', extreme_right='muito importante', min=1, max=5, key='pa', divide=True)
estarproximodecolegas = create_radio(phrase='Estar próximo à colegas e equipe de trabalho mesmo que não esteja totalmente confortável', extreme_left='pouco importante', extreme_right='muito importante', min=1, max=5, key='equipe', divide=True)

st.title('')
st.title('')
st.title('Considerando todos os aspectos,')
place_left_subtitle('com que frequência você tende a buscar ambientes e/ou estações de trabalho baseando-se nas suas preferências pessoais?')

aspectos = create_radio(divide=True, extreme_left='Nunca', extreme_right='Sempre', min=0, max=4, show_values=False, key='aspectos')

st.title('')

options = [confortotermico, qualidadedoar, confortovisual, confortoacustico, privacidadevisual, privacidadeacustica, estarproximodecolegas, aspectos]
if next_page_button(name='Próximo'):
    if None in options:
        st.error('Responda **todas** as questões para prosseguir')
    else:
        st.session_state['PeR']['c0 - conforto térmico'] = confortotermico
        st.session_state['PeR']['c0 - qualidade do ar'] = qualidadedoar
        st.session_state['PeR']['c0 - conforto visual'] = confortovisual
        st.session_state['PeR']['c0 - conforto acústico'] = confortoacustico
        st.session_state['PeR']['c0 - privacidade visual'] = privacidadevisual
        st.session_state['PeR']['c0 - privacidade acústica'] = privacidadeacustica
        st.session_state['PeR']['c0 - proximidade de colegas'] = estarproximodecolegas
        st.session_state['PeR']['c0 - aspectos'] = aspectos
        switch_page('q1b')

footer()