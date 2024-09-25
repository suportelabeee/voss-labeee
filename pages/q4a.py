from configurate import *

img_width = 200
create_top(big_text_title='Opa, encontramos um problema com o conforto visual...', img_url=r'static/Q4a.png', use_progress=True, progress_percentage=55)

if st.session_state.get('janela') == 1:
    existe_janela = True
else:
    existe_janela = False

st.subheader('Na sua estação de trabalho, como você descreve ou classifica...')
st.title('')
esquerda, meio, direita = st.columns(3)
with meio:
    iluminacaoartificial = nested_radio(text_left='baixa', text_right='alta', min=1, max=5, key='disponibilidadedeluzartificial')
    ofuscamentoluzartificial = nested_radio(text_left='recorrente', text_right='inexistente', min=1, max=5, key='ofuscamentoporluzartificial')
with esquerda:
    st.write('')
    st.write('')
    st.write('a disponibilidade de iluminação artificial (lâmpadas e luminárias)?')
    st.write('')
    st.write('')
    st.write('a ocorrência de ofuscamento gerado pela iluminação artificial?')

st.title('')
st.title('')
esquerda, meio, direita = st.columns(3)
esquerda.title('')
esquerda.write('a disponibilidade de iluminação natural (luz do sol e o céu)?')
with meio:
    disp_verao_luznatural = nested_radio(key='disp_verao_luznatural', text_left='baixa', text_right='alta', name='durante o verão e/ou meses quentes',min=1, max=5)
    st.title('')
    disp_manha_luznatural = nested_radio(key='disp_manha_luznatural', text_left='baixa', text_right='alta', name='no período da manhã',min=1, max=5)
    st.title('')
    st.title('')
with direita:
    disp_inverno_luznatural = nested_radio(key='disp_inverno_luznatural', text_left='baixa', text_right='alta', name='durante o inverno e/ou meses frios',min=1, max=5)
    st.title('')
    disp_tarde_luznatural = nested_radio(key='disp_tarde_luznatural', text_left='baixa', text_right='alta', name='no período da tarde',min=1, max=5)
    st.title('')
    st.title('')

esquerda.title('')
esquerda.title('')
esquerda.title('')
esquerda.title('')
esquerda.title('')
esquerda.write('')
esquerda.write('a ocorrência de ofuscamento gerado pela iluminação natural?')
with meio:
    ofuscamento_verao_luznarutal = nested_radio(key='ofuscamento_verao_luznarutal', text_left='recorrente', text_right='inexistente', name='durante o verão e/ou meses quentes',min=1, max=5)
    st.title('')
    ofuscamento_manha_luznarutal = nested_radio(key='ofuscamento_manha_luznarutal', text_left='recorrente', text_right='inexistente', name='no período da manhã',min=1, max=5)
with direita:
    ofuscamento_inverno_luznarutal = nested_radio(key='ofuscamento_inverno_luznarutal', text_left='recorrente', text_right='inexistente', name='durante o inverno e/ou meses frios',min=1, max=5)
    st.title('')
    ofuscamento_tarde_luznarutal = nested_radio(key='ofuscamento_tarde_luznarutal', text_left='recorrente', text_right='inexistente', name='no período da tarde',min=1, max=5)

st.title('')
st.title('')
st.title('')
st.title('Sobre os controles existentes no seu ambiente de trabalho')
st.subheader('Como você classifica o nível de controle que você possui sobre a iluminação artificial?')
st.info('As ilustrações abaixo podem auxiliá-lo(a) a diferenciar os tipos de controle', icon='ℹ️')
st.title('')
classificacoes, esquerda, meio, direita = st.columns([0.5,1,1,1])
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
esquerda.image(r'static/nenhumcontroleartificial1.png', width=img_width)
nenhumcontroleartificial1 = esquerda.checkbox(label='os interruptores não estão localizados na sala', key='nenhumcontroleartificial1')
meio.image(r'static/nenhumcontroleartificial2.png', width=img_width)
nenhumcontroleartificial2 = meio.checkbox(label='as luminárias são acionadas por um único interruptor (todas acesas ou todas apagadas)', key='nenhumcontroleartificial2')
direita.image(r'static/nenhumcontroleartificial3.png', width=img_width)
nenhumcontroleartificial3 = direita.checkbox(label='a decisão de acender ou apagar as luzes não é minha', key='nenhumcontroleartificial3')
meio.title('')
meio.write('')
esquerda.title('')
direita.title('')
direita.title('')

classificacoes.markdown('**algum controle:**')
classificacoes.title('')
classificacoes.title('')
classificacoes.title('')
classificacoes.title('')
classificacoes.title('')
classificacoes.write('')
classificacoes.write('')
classificacoes.write('')
esquerda.image(placeholder_img, width=img_width)
algumcontroleartificial1 = esquerda.checkbox(label='todos os colegas dão sua opinião e chegamos a um acordo', key='algumcontroleartificial1')
meio.image(r'static/algumcontroleartificial2.png', width=img_width)
algumcontroleartificial2 = meio.checkbox(label='todos os colegas dão sua opinião e chegamos a um acordo', key='algumcontroleartificial2')
direita.image(r'static/opiniaogeral.png', width=img_width)
algumcontroleartificial3 = direita.checkbox(label='todos os colegas dão sua opinião e chegamos a um acordo', key='algumcontroleartificial3')
esquerda.title('')
meio.title('')
direita.title('')

classificacoes.markdown('**controle total:**')
esquerda.image(r'static/controletotalartificial.png', width=img_width)
controletotalartificial = esquerda.checkbox(label='acendo ou apago as luzes sempre que me sinto desconfortável com a iluminação artificial', key='controletotalartificial')

if existe_janela:
    st.title('')
    st.title('')
    st.title('')
    st.subheader('Como você classifica o nível de controle que você possui sobre a iluminação natural?')
    st.info('As ilustrações abaixo podem auxiliá-lo(a) a diferenciar os tipos de controle', icon='ℹ️')
    st.title('')
    classificacoes, esquerda, meio, direita = st.columns([0.5,1,1,1])
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
    esquerda.image(r'static/nenhumcontrolenatural1.png', width=img_width)
    nenhumcontrolenatural1 = esquerda.checkbox(label='não existem elementos de sombreamento (cortinas ou persianas) para controle da iluminação natural', key='nenhumcontrolenatural1')
    meio.image(r'static/nenhumcontrolenatural2.png', width=img_width)
    nenhumcontrolenatural2 = meio.checkbox(label='a decisão de abrir ou fechar as cortinas não é minha', key='nenhumcontrolenatural2')
    meio.title('')
    esquerda.title('')

    classificacoes.markdown('**algum controle:**')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.title('')
    classificacoes.write('')
    classificacoes.write('')
    esquerda.image(r'static/opiniaogeral.png', width=img_width)
    algumcontrolenatural1 = esquerda.checkbox(label='todos os colegas dão sua opinião e chegamos a um acordo', key='algumcontrolenatural1')
    esquerda.title('')
    meio.title('')
    meio.title('')
    meio.title('')
    meio.title('')
    meio.title('')
    meio.title('')
    meio.title('')
    meio.write('')
    meio.write('')

    classificacoes.markdown('**controle total:**')
    esquerda.image(r'static/controletotalnatural1.png', width=img_width)
    controletotalnarutal1 = esquerda.checkbox(label='abro e fecho a cortina mais próxima à minha estação de trabalho sempre que me sinto desconfortável com a iluminação natural', key='controletotalnarutal1')
    meio.image(r'static/controletotalnatural2.png', width=img_width)
    controletotalnarutal2 = meio.checkbox(label='abro e fecho a cortina mais próxima à minha estação de trabalho sempre que me sinto desconfortável com o sol direto', key='controletotalnarutal2')


st.title('')
st.title('')
st.title('')
st.title('Como você descreve ou classifica')
st.subheader('a sua estação de trabalho com relação a privacidade visual (não ser visto por outros)?')
st.title('')
privacidadevisual = create_radio(divide=True, extreme_left='insatisfatória', extreme_right='satisfatória', min=1, max=5, key='satisfacaoprivacidadevisual')

st.title('')
st.title('')
st.title('')
st.title('Considerando todos os aspectos,')
st.subheader('qual o seu nível de satisfação com o ambiente luminoso na sua estação de trabalho?')
st.title('')
satisfacaocomambienteluminoso = create_radio(divide=True, extreme_left='insatisfatória', extreme_right='satisfatória', min=1, max=5, key='satisfacaocomambienteluminoso')

insatisfeito_luminoso = False
if satisfacaocomambienteluminoso:
    if satisfacaocomambienteluminoso <= 2:
        insatisfeito_luminoso = True
        st.title('')
        st.title('')
        st.title('')
        st.title('Temos uma nota baixa para o ambiente luminoso...')
        st.subheader('Então, para termos certeza, por favor indique os motivos pelos quais você está insatisfeito(a) com a iluminação em geral.')
        st.info('Você pode selecionar mais de um, se aplicável.', icon='ℹ️')
        st.title('')
        luminosocheckbox = st.checkbox('sinto desconforto com o ambiente muito claro (muito iluminado)', key='cheiroscheckbox')
        escurocheckbox = st.checkbox('sinto desconforto com o ambiente muito escuro (pouco iluminado)', key='escurocheckbox')
        ofuscamentolampadacheckbox = st.checkbox('sinto desconforto com o ofuscamento gerado por lâmpadas e luminárias', key='ofuscamentolampadacheckbox')
        ofuscamentosolcheckbox = st.checkbox('sinto desconforto com o ofuscamento gerado pela luz do sol e do céu', key='ofuscamentosolcheckbox')
        reflexoscheckbox = st.checkbox('sinto desconforto com a iluminação que gera reflexos na tela do meu computador', key='reflexoscheckbox')
        luzespiscandocheckbox = st.checkbox('sinto desconforto com luzes piscando', key='luzespiscandocheckbox')
        objetoscheckbox = st.checkbox('sinto desconforto pois não consigo diferenciar objetos (alto e/ou baixo contraste)', key='objetoscheckbox')
        if existe_janela:
            if nenhumcontrolenatural1 or nenhumcontrolenatural2 or algumcontrolenatural1:
                brisescheckbox = st.checkbox('sinto desconforto por não poder controlar os elementos de sombreamento (cortinas ou brises)', key='brisescheckbox')
        if nenhumcontroleartificial1 or nenhumcontroleartificial2 or nenhumcontroleartificial3 or algumcontroleartificial1 or algumcontroleartificial2 or algumcontroleartificial3:
            acionarlampadacheckbox = st.checkbox('sinto desconforto por não poder controlar o acionamento das lâmpadas e luminárias', key='acionarlampadacheckbox')
        outros = st.checkbox('outro, por favor especifique:', key='outros_2')
        if outros:
            entrada = st.text_input(label='no label', label_visibility='hidden',value=None, key='entrybox_2', placeholder='Descreva aqui', max_chars=150)

st.title('')
if next_page_button('Próximo'):
    message = 'Erro: '
    ok = True
    sec1 = [iluminacaoartificial, ofuscamentoluzartificial]
    if None in sec1:
        ok = False
        message += '|Faltou resposta para disponibilidade e ofuscamento de luz artificial'
    sec2 = [disp_verao_luznatural, disp_manha_luznatural, disp_inverno_luznatural, disp_tarde_luznatural, ofuscamento_verao_luznarutal, ofuscamento_manha_luznarutal, ofuscamento_inverno_luznarutal, ofuscamento_tarde_luznarutal]
    if None in sec2:
        ok = False
        message += '|Faltou resposta para disponibilidade e ofuscamento de luz natural'
    artificialluz = {'os interruptores não estão localizados na sala': nenhumcontroleartificial1, 'as luminárias são acionadas por um único interruptor (todas acesas ou todas apagadas)': nenhumcontroleartificial2, 'a decisão de acender ou apagar as luzes não é minha': nenhumcontroleartificial3, 'os interruptores estão muito afastados da minha estação de trabalho': algumcontroleartificial1, 'posso optar por acender as luminárias de acordo com a luz natural disponível': algumcontroleartificial2, 'todos os colegas dão sua opinião e chegamos a um acordo': algumcontroleartificial3, 'acendo ou apago as luzes sempre que me sinto desconfortável com a iluminação artificial': controletotalartificial}
    verdadeirosartificial = [chave for chave, valor in artificialluz.items() if valor]
    if len(verdadeirosartificial) != 1:
        ok = False
        message += '|Responda **uma** alternativa para o nível de controle sobre luz artificial'
    if existe_janela:
        naturalluz = {'não existem elementos de sombreamento (cortinas ou persianas) para controle da iluminação natural': nenhumcontrolenatural1, 'a decisão de abrir ou fechar as cortinas não é minha': nenhumcontrolenatural2, 'todos os colegas dão sua opinião e chegamos a um acordo': algumcontrolenatural1, 'abro e fecho a cortina mais próxima à minha estação de trabalho sempre que me sinto desconfortável com a iluminação natural': controletotalnarutal1, 'abro e fecho a cortina mais próxima à minha estação de trabalho sempre que me sinto desconfortável com o sol direto': controletotalnarutal2}
        verdadeirosnatural = [chave for chave, valor in naturalluz.items() if valor]
        if len(verdadeirosnatural) != 1:
            ok = False
            message += '|Responda **uma** alternativa para o nível de controle sobre luz natural'
    if not privacidadevisual:
        ok = False
        message += '|Responda alguma aternativa sobre classificação de privacidade visual'
    if not satisfacaocomambienteluminoso:
        ok = False
        message += '|Responda alguma aternativa sobre seu nível de satisfação com ambiente luminoso'
    if insatisfeito_luminoso:
        if outros:
            if not entrada:
                ok = False
                message += '|Caixa de texto não preenchida'
    if ok:
        st.session_state['PeR']['q4a - a disponibilidade de iluminação artificial (lâmpadas e luminárias)?'] = sec1[0]
        st.session_state['PeR']['q4a - a ocorrência de ofuscamento gerado pela iluminação artificial?'] = sec1[1]
        st.session_state['PeR']['q4a - a disponibilidade de iluminação natural (luz do sol e o céu) durante o verão e/ou meses quentes'] = sec2[0]
        st.session_state['PeR']['q4a - a disponibilidade de iluminação natural (luz do sol e o céu) durante o inverno e/ou meses frios'] = sec2[2]
        st.session_state['PeR']['q4a - a disponibilidade de iluminação natural (luz do sol e o céu) no período da manhã'] = sec2[1]
        st.session_state['PeR']['q4a - a disponibilidade de iluminação natural (luz do sol e o céu) no período da tarde'] = sec2[3]
        st.session_state['PeR']['q4a - a ocorrência de ofuscamento gerado pela iluminação natural durante o verão e/ou meses quentes'] = sec2[4]
        st.session_state['PeR']['q4a - a ocorrência de ofuscamento gerado pela iluminação natural durante o inverno e/ou meses frios'] = sec2[6]
        st.session_state['PeR']['q4a - a ocorrência de ofuscamento gerado pela iluminação natural no período da manhã'] = sec2[5]
        st.session_state['PeR']['q4a - a ocorrência de ofuscamento gerado pela iluminação natural no período da tarde'] = sec2[7]
        st.session_state['PeR']['q4a - nível de controle sobre iluminação artificial'] = verdadeirosartificial[0]
        st.session_state['PeR']['q4a - nível de satisfação com privacidade visual'] = privacidadevisual
        st.session_state['PeR']['q4a - nível de satisfação com ambiente luminoso'] = satisfacaocomambienteluminoso

        # não obrigatórios
        st.session_state['PeR']['q4a - nível de controle sobre iluminação natural'] = None
        st.session_state['PeR']['q4a - sinto desconforto com o ambiente muito claro (muito iluminado)'] = None
        st.session_state['PeR']['q4a - sinto desconforto com o ambiente muito escuro (pouco iluminado)'] = None
        st.session_state['PeR']['q4a - sinto desconforto com o ofuscamento gerado por lâmpadas e luminárias'] = None
        st.session_state['PeR']['q4a - sinto desconforto com o ofuscamento gerado pela luz do sol e do céu'] = None
        st.session_state['PeR']['q4a - sinto desconforto com a iluminação que gera reflexos na tela do meu computador'] = None
        st.session_state['PeR']['q4a - sinto desconforto com luzes piscando'] = None
        st.session_state['PeR']['q4a - sinto desconforto pois não consigo diferenciar objetos (alto e/ou baixo contraste)'] = None
        st.session_state['PeR']['q4a - sinto desconforto por não poder controlar os elementos de sombreamento (cortinas ou brises)'] = None
        st.session_state['PeR']['q4a - sinto desconforto por não poder controlar o acionamento das lâmpadas e luminárias'] = None
        st.session_state['PeR']['q4a - outros motivos'] = None

        if existe_janela:
            st.session_state['PeR']['q4a - nível de controle sobre iluminação natural'] = verdadeirosnatural[0]
        if insatisfeito_luminoso:
            st.session_state['PeR']['q4a - sinto desconforto com o ambiente muito claro (muito iluminado)'] = luminosocheckbox
            st.session_state['PeR']['q4a - sinto desconforto com o ambiente muito escuro (pouco iluminado)'] = escurocheckbox
            st.session_state['PeR']['q4a - sinto desconforto com o ofuscamento gerado por lâmpadas e luminárias'] = ofuscamentolampadacheckbox
            st.session_state['PeR']['q4a - sinto desconforto com o ofuscamento gerado pela luz do sol e do céu'] = ofuscamentosolcheckbox
            st.session_state['PeR']['q4a - sinto desconforto com a iluminação que gera reflexos na tela do meu computador'] = reflexoscheckbox
            st.session_state['PeR']['q4a - sinto desconforto com luzes piscando'] = luzespiscandocheckbox
            st.session_state['PeR']['q4a - sinto desconforto pois não consigo diferenciar objetos (alto e/ou baixo contraste)'] = objetoscheckbox
            if existe_janela:
                if nenhumcontrolenatural1 or nenhumcontrolenatural2 or algumcontrolenatural1:
                    st.session_state['PeR']['q4a - sinto desconforto por não poder controlar os elementos de sombreamento (cortinas ou brises)'] = brisescheckbox
            if nenhumcontroleartificial1 or nenhumcontroleartificial2 or nenhumcontroleartificial3 or algumcontroleartificial1 or algumcontroleartificial2 or algumcontroleartificial3:
                st.session_state['PeR']['q4a - sinto desconforto por não poder controlar o acionamento das lâmpadas e luminárias'] = acionarlampadacheckbox
            if outros:
                st.session_state['PeR']['q4a - outros motivos'] = entrada
        st.session_state['hierarquia'] += 1
        switch_page('q5')
    else:
        st.error(message)

footer()