from configurate import * 

create_top(big_text_title='Parece que encontramos um ponto crítico com a acústica...', img_url=r'static/Q5a.png', use_progress=True, progress_percentage=65)

img_width = 200

if st.session_state.get('janela') == 1:
    existe_janela = True
else:
    existe_janela = False

st.subheader('Em sua estação de trabalho, como você descreve ou classifica os itens a seguir?')
st.title('')
esquerda, meio, direita = st.columns([0.5,1,1.5])
width_select = [0.2,0.5,1]
left = 'incomoda'
right = 'não incomoda'

esquerda.title('')
esquerda.markdown('**ruídos gerados por colegas:**')
meio.title('')
meio.write('conversas que consigo entender tudo que é dito')
meio.subheader('')
meio.write('conversas de fundo, que não consigo entender o que é dito')
meio.subheader('')
meio.write('teclados, passos, abertura e fechamento de gavetas, etc.')
with direita:
    ruidos_colegas_1 = nested_radio(text_left=left, text_right=right, key='ruidos_colegas_1', min=1, max=5, columns_width=width_select)
    ruidos_colegas_2 = nested_radio(text_left=left, text_right=right, key='ruidos_colegas_2', min=1, max=5, columns_width=width_select)
    ruidos_colegas_3 = nested_radio(text_left=left, text_right=right, key='ruidos_colegas_3', min=1, max=5, columns_width=width_select)
meio.title('')
direita.title('')
esquerda.write('')
esquerda.write('')
esquerda.write('')
esquerda.write('')
esquerda.title('')
esquerda.title('')
esquerda.title('')
esquerda.title('') 
esquerda.markdown('**ruídos gerados pelo edifício:**')
meio.title('')
meio.write('ar-condicionado')
meio.subheader('')
meio.write('outros equipamentos')
meio.subheader('')
meio.write('telefones tocando')
with direita:
    ruidos_edificio_1 = nested_radio(text_left=left, text_right=right, key='ruidos_edificio_1', min=1, max=5, columns_width=width_select)
    ruidos_edificio_2 = nested_radio(text_left=left, text_right=right, key='ruidos_edificio_2', min=1, max=5, columns_width=width_select)
    ruidos_edificio_3 = nested_radio(text_left=left, text_right=right, key='ruidos_edificio_3', min=1, max=5, columns_width=width_select)
meio.write('')
meio.write('')
meio.write('')
direita.write('')
direita.write('')
direita.write('')
esquerda.write('')
esquerda.write('')
esquerda.write('')
esquerda.write('')
esquerda.title('')
esquerda.title('')
esquerda.title('')
esquerda.title('')
esquerda.markdown('**ruídos gerados pelo entorno:**')
meio.title('')
meio.write('barulho externo, vindo da rua')
with direita:
    ruido_externo = nested_radio(text_left=left, text_right=right, key='barulho_externo', min=1, max=5, columns_width=width_select)

if existe_janela:
    st.title('')
    st.title('')
    st.title('')
    st.title('Sobre os controles existentes no seu ambiente de trabalho')
    st.subheader('Como você classifica o nível de controle que você possui sobre ruídos externos?')
    st.info('As ilustrações abaixo podem auxiliá-lo(a) a diferenciar os tipos de controle', icon='ℹ️')
    st.title('')
    classificacoes, esquerda, meioesquerda, meiodireita, direita = st.columns([0.5,1,1,1,1])
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')

    classificacoes.markdown('**nenhum controle:**')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.write('')
    classificacoes.write('')
    classificacoes.write('')
    classificacoes.write('')
    esquerda.image(r'static/nenhumcontrolejanela1.png', width=img_width)
    nenhumcontrolejanela1 = esquerda.checkbox(label='as janelas não são operáveis e estão sempre fechadas', key='ruido_nenhumcontrolejanela1')
    meioesquerda.image(r'static/nenhumcontrolejanela2.png', width=img_width)
    nenhumcontrolejanela2 = meioesquerda.checkbox(label='as janelas são operáveis, porém a política da empresa não permite que sejam abertas', key='ruido_nenhumcontrolejanela2')
    meiodireita.image(r'static/nenhumcontrolejanela3.png', width=img_width)
    nenhumcontrolejanela3 = meiodireita.checkbox(label='a decisão de abrir ou fechar as janelas não é minha', key='ruido_nenhumcontrolejanela3')
    meioesquerda.title('')
    esquerda.title('')

    classificacoes.markdown('**algum controle:**')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.write('')
    classificacoes.write('')
    classificacoes.write('')
    esquerda.image(r'static/opiniaogeral.png', width=img_width)
    algumcontrolejanela = esquerda.checkbox(label='todos os colegas dão sua opinião e chegamos a um acordo', key='ruido_opiniaogeraljanela')

    esquerda.title('')

    classificacoes.markdown('**controle total:**')
    esquerda.image(r'static/controletotaljanela.png', width=img_width)
    controletotaljanela = esquerda.checkbox(label='abro e fecho a janela mais próxima à minha estação de trabalho sempre que me sinto desconfortável com ruídos externos', key='ruido_controletotaljanela')

st.title('')
st.title('')
st.title('')
st.title('Considerando todos os aspectos,')
st.subheader('qual o seu nível de satisfação com a acústica da sua estação de trabalho?')
st.title('')
width_large = [1,1,0.4,0.6,1]
satisfacao_ruidos = create_radio(divide=True, min=1, max=5, key='satsifacaoruidos', extreme_left='insatisfeito(a)', extreme_right='satisfeito(a)', five_columns_width=width_large)

insatisfacao_ruidos = False
if satisfacao_ruidos:
    if satisfacao_ruidos <= 2:
        insatisfacao_ruidos = True
        st.title('')
        st.title('')
        st.title('')
        st.title('Temos uma nota baixa para o ambiente acústico...')
        st.subheader('Então, para termos certeza, por favor indique os motivos pelos quais você está insatisfeito(a) com os ruídos em geral.')
        st.info('Você pode selecionar mais de um, se aplicável.', icon='ℹ️')
        st.title('')
        ruidos_checkbox1 = st.checkbox('as conversas dos colegas me incomodam', key='ruidos_checkbox1')
        ruidos_checkbox2 = st.checkbox('o barulho do ar-condicionado me incomoda', key='ruidos_checkbox2')
        ruidos_checkbox3 = st.checkbox('o barulho de outros equipamentos me incomoda', key='ruidos_checkbox3')
        ruidos_checkbox4 = st.checkbox('o barulho de telefones tocando me incomoda', key='ruidos_checkbox4')
        ruidos_checkbox5 = st.checkbox('o barulho externo, vindo da rua, me incomoda', key='ruidos_checkbox5')
        ruidos_checkbox6 = st.checkbox('não há um local adequado para ter uma conversa privada com colegas', key='ruidos_checkbox6')
        ruidos_checkbox7 = st.checkbox('não há um local adequado para fazer um telefonema ou chamada de vídeo', key='ruidos_checkbox7')
        outros = st.checkbox('outro, por favor especifique:', key='outros_3')
        if outros:
            entrada = st.text_input(label='no label', label_visibility='hidden',value=None, key='entrybox_3', placeholder='Descreva aqui', max_chars=150)



st.title('')
if next_page_button('Próximo'):
    message = 'Erro: '
    siga = True
    if existe_janela:
        controlejanela = {'as janelas não são operáveis e estão sempre fechadas':nenhumcontrolejanela1, 'as janelas são operáveis, porém a política da empresa não permite que sejam abertas':nenhumcontrolejanela2, 'a decisão de abrir ou fechar as janelas não é minha':nenhumcontrolejanela3, 'todos os colegas dão sua opinião e chegamos a um acordo':algumcontrolejanela, 'abro e fecho a janela mais próxima sempre que me sinto desconfortável com os ruídos externos':controletotaljanela}
        verdadeiros_controlejanela = [chave for chave, valor in controlejanela.items() if valor]
        if len(verdadeiros_controlejanela) != 1:
            siga = False
            message += '|Escolha **uma** opção de nível de controle de janelas'
    ruidos_opcoes = [ruidos_colegas_1, ruidos_colegas_2, ruidos_colegas_3, ruidos_edificio_1, ruidos_edificio_2, ruidos_edificio_3, ruido_externo]
    if None in ruidos_opcoes:
        siga = False
        message += '|Responda **todas** as questões de ruídos no ambiente de trabalho'
    if insatisfacao_ruidos:
        if outros:
            if not entrada:
                siga = False
                message += '|Caixa de texto vazia'
    if siga:
        st.session_state['PeR']['q5a - conversas que consigo entener tudo que é dito'] = ruidos_colegas_1 
        st.session_state['PeR']['q5a - conversas de fundo, que não consigo entender o que é dito'] = ruidos_colegas_2
        st.session_state['PeR']['q5a - teclados, passos, abertura e fechamento de gavetas, etc'] = ruidos_colegas_3
        st.session_state['PeR']['q5a - ar-condicionado'] = ruidos_edificio_1
        st.session_state['PeR']['q5a - outros equipamentos'] = ruidos_edificio_2
        st.session_state['PeR']['q5a - telefones tocando'] = ruidos_edificio_3
        st.session_state['PeR']['q5a - barulho externo, vindo da rua'] = ruido_externo
        st.session_state['PeR']['q5a - qual seu nível de satisfação com a privacidade acústica da sua estação de trabalho'] = satisfacao_ruidos
        
        # não obrigatórios
        st.session_state['PeR']['q5a - controle de janela'] = None
        st.session_state['PeR']['q5a - as conversas dos colegas me incomodam'] = None
        st.session_state['PeR']['q5a - o barulho do ar-condicionado me incomoda'] = None
        st.session_state['PeR']['q5a - o barulho de outros equipamentos me incomoda'] = None
        st.session_state['PeR']['q5a - o barulho de telefones tocando me incomoda'] = None
        st.session_state['PeR']['q5a - o barulho externo, vindo da rua, me incomoda'] = None
        st.session_state['PeR']['q5a - não há um local adequado para ter uma conversa privada com colegas'] = None
        st.session_state['PeR']['q5a - não há um local adequado para fazer um telefonema ou chamada de vídeo'] = None
        st.session_state['PeR']['q5a - outros motivos'] = None
        
        if existe_janela:
            st.session_state['PeR']['q5a - controle de janela'] = verdadeiros_controlejanela[0]
        if insatisfacao_ruidos:
            st.session_state['PeR']['q5a - as conversas dos colegas me incomodam'] = ruidos_checkbox1
            st.session_state['PeR']['q5a - o barulho do ar-condicionado me incomoda'] = ruidos_checkbox2
            st.session_state['PeR']['q5a - o barulho de outros equipamentos me incomoda'] = ruidos_checkbox3
            st.session_state['PeR']['q5a - o barulho de telefones tocando me incomoda'] = ruidos_checkbox4
            st.session_state['PeR']['q5a - o barulho externo, vindo da rua, me incomoda'] = ruidos_checkbox5
            st.session_state['PeR']['q5a - não há um local adequado para ter uma conversa privada com colegas'] = ruidos_checkbox6
            st.session_state['PeR']['q5a - não há um local adequado para fazer um telefonema ou chamada de vídeo'] = ruidos_checkbox7
            if outros:
                st.session_state['PeR']['q5a - outros motivos'] = entrada
        if st.session_state.get('hierarquia') >= 2:
            switch_page('hi')
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
            switch_page('cg')
    else:
        st.error(message)

footer()