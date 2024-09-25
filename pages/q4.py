from configurate import *

create_top(big_text_title='Conforto visual', use_progress=True, progress_percentage=50)

st.subheader('Com relação ao conforto visual na sua estação de trabalho, você costuma sentir algum dos itens a seguir?')

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

opt = ['sempre', 'muitas vezes', 'às vezes', 'poucas vezes', 'nunca']
choosen_width = [1.7,2]

claro = create_radio(large=True, phrase='sinto desconforto com o ambiente muito claro (muito iluminado)', selection=opt, use_list_selection=True, key='claro', two_columns_width=choosen_width)
escuro = create_radio(large=True, phrase='sinto desconforto com o ambiente muito escuro (pouco iluminado)', selection=opt, use_list_selection=True, key='escuro', two_columns_width=choosen_width)
ofuscamento = create_radio(large=True, phrase='sinto desconforto com o ofuscamento', selection=opt, use_list_selection=True, key='ofuscamento', two_columns_width=choosen_width)
reflexos = create_radio(large=True, phrase='sinto desconforto com os reflexos na tela do meu computador', selection=opt, use_list_selection=True, key='reflexos', two_columns_width=choosen_width)
luzes = create_radio(large=True, phrase='sinto desconforto com luzes piscando', selection=opt, use_list_selection=True, key='luzes', two_columns_width=choosen_width)
objetos = create_radio(large=True, phrase='sinto desconforto pois não consigo diferenciar objetos (alto e/ou baixo contraste)', selection=opt, use_list_selection=True, key='objetos', two_columns_width=choosen_width)

st.title('')
if next_page_button('Próximo'):
    respostas = [claro, escuro, ofuscamento, reflexos, luzes, objetos]
    if None in respostas:
        st.error('Responda **todas** as questões para prosseguir')
    else:
        st.session_state['PeR']['q4 - sinto desconforto com o ambiente muito claro (muito iluminado)'] = claro
        st.session_state['PeR']['q4 - sinto desconforto com o ambiente muito escuro (pouco iluminado)'] = escuro
        st.session_state['PeR']['q4 - sinto desconforto com o ofuscamento'] = ofuscamento
        st.session_state['PeR']['q4 - sinto desconforto com os reflexos na tela do meu computador'] = reflexos
        st.session_state['PeR']['q4 - sinto desconforto com luzes piscando'] = luzes
        st.session_state['PeR']['q4 - sinto desconforto pois não consigo diferenciar objetos (alto e/ou baixo contraste)'] = objetos
        if ('sempre' in respostas) or ('muitas vezes' in respostas) or ('às vezes' in respostas): 
            switch_page('q4a')
        else:
            st.session_state['PeR']['q4a - a disponibilidade de iluminação artificial (lâmpadas e luminárias)?'] = None
            st.session_state['PeR']['q4a - a ocorrência de ofuscamento gerado pela iluminação artificial?'] = None
            st.session_state['PeR']['q4a - a disponibilidade de iluminação natural (luz do sol e o céu) durante o verão e/ou meses quentes'] = None
            st.session_state['PeR']['q4a - a disponibilidade de iluminação natural (luz do sol e o céu) durante o inverno e/ou meses frios'] = None
            st.session_state['PeR']['q4a - a disponibilidade de iluminação natural (luz do sol e o céu) no período da manhã'] = None
            st.session_state['PeR']['q4a - a disponibilidade de iluminação natural (luz do sol e o céu) no período da tarde'] = None
            st.session_state['PeR']['q4a - a ocorrência de ofuscamento gerado pela iluminação natural durante o verão e/ou meses quentes'] = None
            st.session_state['PeR']['q4a - a ocorrência de ofuscamento gerado pela iluminação natural durante o inverno e/ou meses frios'] = None
            st.session_state['PeR']['q4a - a ocorrência de ofuscamento gerado pela iluminação natural no período da manhã'] = None
            st.session_state['PeR']['q4a - a ocorrência de ofuscamento gerado pela iluminação natural no período da tarde'] = None
            st.session_state['PeR']['q4a - nível de controle sobre iluminação artificial'] = None
            st.session_state['PeR']['q4a - nível de satisfação com privacidade visual'] = None
            st.session_state['PeR']['q4a - nível de satisfação com ambiente luminoso'] = None
            
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
            switch_page('q5')

footer()