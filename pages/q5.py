from configurate import *

create_top(big_text_title='Conforto acústico', use_progress=True, progress_percentage=60)

st.subheader('Com relação ao conforto acústico na sua estação de trabalho, você costuma sentir algum dos itens a seguir?')

list_selection = ['sempre', 'muitas vezes', 'às vezes', 'poucas vezes', 'nunca']
choosen_width = [1.7,2]

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

conversacolegas = create_radio(large=True, use_list_selection=True, selection=list_selection, phrase='sinto desconforto com conversas dos colegas', key='conversacolegas', two_columns_width=choosen_width)
ruidoequipamentos = create_radio(large=True, use_list_selection=True, selection=list_selection, phrase='sinto desconforto com ruídos de equipamentos', key='ruidoequipamentos', two_columns_width=choosen_width)
barulhoexterno = create_radio(large=True, use_list_selection=True, selection=list_selection, phrase='sinto desconforto com o barulho externo, vindo da rua', key='barulhoexterno', two_columns_width=choosen_width)

st.title('')
if next_page_button('Próximo'):
    q5_quest = [conversacolegas, ruidoequipamentos, barulhoexterno]
    if None in q5_quest:
        st.error('Responda **todas** as questões pra prosseguir')
    else:
        st.session_state['PeR']['q5 - sinto desconforto com conversas dos colegas'] = conversacolegas
        st.session_state['PeR']['q5 - sinto desconforto com ruídos de equipamentos'] = ruidoequipamentos
        st.session_state['PeR']['q5 - sinto desconforto com o barulho externo, vindo da rua'] = barulhoexterno
        if ('sempre' in q5_quest) or ('muitas vezes' in q5_quest) or ('às vezes' in q5_quest): 
            switch_page('q5a')
        else:
            st.session_state['PeR']['q5a - conversas que consigo entener tudo que é dito'] = None 
            st.session_state['PeR']['q5a - conversas de fundo, que não consigo entender o que é dito'] = None
            st.session_state['PeR']['q5a - teclados, passos, abertura e fechamento de gavetas, etc'] = None
            st.session_state['PeR']['q5a - ar-condicionado'] = None
            st.session_state['PeR']['q5a - outros equipamentos'] = None
            st.session_state['PeR']['q5a - telefones tocando'] = None
            st.session_state['PeR']['q5a - barulho externo, vindo da rua'] = None
            st.session_state['PeR']['q5a - qual seu nível de satisfação com a acústica da sua estação de trabalho'] = None
            st.session_state['PeR']['q5a - controle de janela'] = None
            st.session_state['PeR']['q5a - as conversas dos colegas me incomodam'] = None
            st.session_state['PeR']['q5a - o barulho do ar-condicionado me incomoda'] = None
            st.session_state['PeR']['q5a - o barulho de outros equipamentos me incomoda'] = None
            st.session_state['PeR']['q5a - o barulho de telefones tocando me incomoda'] = None
            st.session_state['PeR']['q5a - o barulho externo, vindo da rua, me incomoda'] = None
            st.session_state['PeR']['q5a - não há um local adequado para ter uma conversa privada com colegas'] = None
            st.session_state['PeR']['q5a - não há um local adequado para fazer um telefonema ou chamada de vídeo'] = None
            st.session_state['PeR']['q5a - outros motivos'] = None
            if st.session_state.get('hierarquia') >= 2:
                switch_page('hi')
            elif st.session_state.get('hierarquia') == 1:
                st.session_state['PeR']['hi - conforto térmico'] = None
                st.session_state['PeR']['hi - qualidade do ar'] = None
                st.session_state['PeR']['hi - conforto visual'] = None
                st.session_state['PeR']['hi - conforto acústico'] = None
                st.session_state['PeR']['hi - ambientes específicos para atividades diferenciadas'] = None
                st.session_state['PeR']['hi - proximidade e/ou acesso a vistas externas'] = None
                st.session_state['PeR']['hi - privacidade visual'] = None
                st.session_state['PeR']['hi - privacidade acústica'] = None
                st.session_state['PeR']['hi - estar próximo à colegas e equipe de trabalho mesmo que não esteja totalmente confortável'] = None
                switch_page('cg')
            else:
                st.session_state['PeR']['hi - conforto térmico'] = None
                st.session_state['PeR']['hi - qualidade do ar'] = None
                st.session_state['PeR']['hi - conforto visual'] = None
                st.session_state['PeR']['hi - conforto acústico'] = None
                st.session_state['PeR']['hi - ambientes específicos para atividades diferenciadas'] = None
                st.session_state['PeR']['hi - proximidade e/ou acesso a vistas externas'] = None
                st.session_state['PeR']['hi - privacidade visual'] = None
                st.session_state['PeR']['hi - privacidade acústica'] = None
                st.session_state['PeR']['hi - estar próximo à colegas e equipe de trabalho mesmo que não esteja totalmente confortável'] = None
                st.session_state['PeR']['cg - nível de satisfação com o conforto geral da estação de trabalho'] = None
                st.session_state['PeR']['cg - comentários'] = None
                st.session_state['PeR']['cp - controle de ar-condicionado e aquecedores'] = None
                st.session_state['PeR']['cp - controle de ventiladores'] = None
                st.session_state['PeR']['cp - controle de janelas'] = None
                st.session_state['PeR']['cp - controle de cortinas'] = None
                st.session_state['PeR']['cp - controle de luzes'] = None
                st.session_state['PeR']['sp - velocidade de resposta à solicitação de aquecimento e/ou resfriamento'] = None
                st.session_state['PeR']['sp - velocidade de resposta à solicitação de controle de ventilação'] = None
                st.session_state['PeR']['sp - velocidade de resposta à solicitação de alteração de iluminação'] = None
                st.session_state['PeR']['sp - comentários'] = None
                switch_page('q6')

footer()