from configurate import *

create_top(big_text_title='Sua resposta foi registrada com sucesso.', subtitle='Agradecemos a sua participação na pesquisa.', img_url=r'static/fim.png', use_line=False, use_progress=True, progress_percentage=100)

if not st.session_state.get("registered"):
    with st.spinner("Registrando suas respostas, aguarde..."): 
        register_answer()
        send_thanks_email(st.session_state['email'])
        st.session_state['registered'] = True

cols = st.columns([1,2,2])
if cols[0].button("Sair", use_container_width=True):
    st.session_state['PeR'] = None
    switch_page('QAI')

footer()