from configurate import *

create_top(big_text_title=f'{st.session_state["PeR"]["q0"]} é uma ótima avaliação!', use_line=False,subtitle='Aparentemente, não há problemas com a estrutura do seu ambiente de trabalho :)', img_url=r'static/Q1sat.png', use_progress=True, progress_percentage=10)

st.title('')
if next_page_button(name='Combinado', phrase='Vamos apenas fazer algumas perguntas para ter certeza que está tudo bem, ok?'):
    switch_page('q1a')

footer()