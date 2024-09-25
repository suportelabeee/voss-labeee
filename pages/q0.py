from configurate import *

create_top(big_text_title='Pesquisa de clima organizacional', img_url=r'static/Q0.png', use_line=False, use_progress=True, progress_percentage=5)

st.markdown("""
    <style>
    [role=radiogroup]{
        gap: 1rem;
    }
    </style>
    """,unsafe_allow_html=True)

st.subheader('Como você classifica a sua satisfação com as condições físicas')
st.subheader('(temperatura, qualidade do ar interno, iluminação e acústica)')
st.subheader('do seu ambiente de trabalho para a realização das suas atividades?')

valor = create_radio(phrase='Em uma escala de 0 a 10', large=True, min=0, max=10)
esquerda, direita, vazio = st.columns([1.09,1.25,0.9])
with direita:
    zero, um, dois, três, quatro, cinco, seis, sete, oito, nove, dez = st.columns(11)
    zero.write('0')
    um.write('1')
    dois.write('2')
    três.write('3')
    quatro.write('4')
    cinco.write('5')
    seis.write('6')
    sete.write('7')
    oito.write('8')
    nove.write('9')
    dez.write('10')

st.title('')
if next_page_button('Próxima página'):
    if valor == None:
        st.error('Responda para prosseguir')
    else:
        st.session_state['PeR']['q0'] = valor
        if valor <= 6:
            switch_page('introq1_insat')
        else:
            switch_page('introq1_sat')

footer()