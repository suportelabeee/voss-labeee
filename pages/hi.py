from configurate import *

create_top(big_text_title='Considerando a atual configuração física do seu escritório,', use_line=False, use_progress=True, progress_percentage=70)

st.subheader('você poderia indicar a importância dos fatores a seguir na realização das suas atividades de trabalho diárias?')
left = 'pouco importante'
right = 'muito importante'

st.title('')
with st.form('hierarquia de importância'):
    selecao = [1,2,3,4,5,6,7,8,9]
    while len(selecao) >= 1:
        indice_sorteado = randint(0,len(selecao)-1)
        valor_sorteado = selecao[indice_sorteado]
        if valor_sorteado == 1:
            fat1 = create_radio(phrase='conforto térmico', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat1')
            selecao.pop(indice_sorteado)
        elif valor_sorteado == 2:
            fat2 = create_radio(phrase='qualidade do ar', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat2')
            selecao.pop(indice_sorteado)
        elif valor_sorteado == 3:
            fat3 = create_radio(phrase='conforto visual', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat3')
            selecao.pop(indice_sorteado)
        elif valor_sorteado == 4:
            fat4 = create_radio(phrase='conforto acústico', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat4')
            selecao.pop(indice_sorteado)
        elif valor_sorteado == 5:
            fat5 = create_radio(phrase='ambientes específicos para atividades diferenciadas', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat5')
            selecao.pop(indice_sorteado)
        elif valor_sorteado == 6:
            fat6 = create_radio(phrase='proximidade e/ou acesso a vistas externas', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat6')
            selecao.pop(indice_sorteado)
        elif valor_sorteado == 7:
            fat7 = create_radio(phrase='privacidade visual', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat7')
            selecao.pop(indice_sorteado)
        elif valor_sorteado == 8:
            fat8 = create_radio(phrase='privacidade acústica', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat8')
            selecao.pop(indice_sorteado)
        elif valor_sorteado == 9:
            fat9 = create_radio(phrase='estar próximo à colegas e equipe de trabalho mesmo que não esteja totalmente confortável', divide=True, extreme_left=left, extreme_right=right, min=1, max=5, key='fat9')
            selecao.pop(indice_sorteado)
    st.title('')
    st.title('')
    esquerda, direita = st.columns([2,0.5])
    with direita:
        seguir = st.form_submit_button('Próximo')
    st.title('')
    st.title('')
    if seguir:
        questoes = [fat1, fat2, fat3, fat4, fat5, fat6, fat7, fat8, fat9]
        if None in questoes:
            st.error('Responda **todas** as questões para prosseguir')
        else:
            st.session_state['PeR']['hi - conforto térmico'] = fat1 
            st.session_state['PeR']['hi - qualidade do ar'] = fat2
            st.session_state['PeR']['hi - conforto visual'] = fat3
            st.session_state['PeR']['hi - conforto acústico'] = fat4
            st.session_state['PeR']['hi - ambientes específicos para atividades diferenciadas'] = fat5
            st.session_state['PeR']['hi - proximidade e/ou acesso a vistas externas'] = fat6
            st.session_state['PeR']['hi - privacidade visual'] = fat7
            st.session_state['PeR']['hi - privacidade acústica'] = fat8
            st.session_state['PeR']['hi - estar próximo à colegas e equipe de trabalho mesmo que não esteja totalmente confortável'] = fat9
            switch_page('cg')

footer()