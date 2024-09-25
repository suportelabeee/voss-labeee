import streamlit as st
st.set_page_config(layout='wide',initial_sidebar_state='collapsed', page_title=f"Sobre nós - VOSS", page_icon = '👩‍💻')
from configurate import *

initialize_page()

st.markdown("""## Sobre a VOSS | About VOSS 

**PT/BR**
A pesquisa VOSS (*Virtual Occupant Suvey System*) foi desenvolvida pelos pesquisadores do [LabEEE](https://labeee.ufsc.br/) [Zac Milioli](https://www.linkedin.com/in/zac-milioli/) e [Luiza de Castro](https://www.linkedin.com/in/arq-luiza-de-castro/), sob coordenação de [Renata De Vecchi](http://lattes.cnpq.br/0594650510499319) e [Roberto Lamberts](http://lattes.cnpq.br/0755959610406012).

Clique aqui para acessar o [repositório](https://github.com/Zac-Milioli/qai-st-labeee) do aplicativo.

**EN**
The *Virtual Occupant Survey System* (VOSS) has been developed by researchers from the Laboratory of Energy Efficiency in Building (LabEEE) at Federal University of Santa Catarina.

Click here to access the app [repository](https://github.com/Zac-Milioli/qai-st-labeee).

## Publicações | Publications

- (ARTIGO ENTAC 2024: em processo de publicação).

- CASTRO, Luiza; DE VECCHI, Renata; LAMBERTS, Roberto. Design process for an occupant survey system to assess satisfaction with indoor environmental quality. **Building Research and Information**, p. 1-19, 2024. Disponível em: https://doi.org/10.1080/09613218.2024.2374343.

- CASTRO, Luiza Tavares de. **User satisfaction evaluation of indoor environmental quality for office buildings.** 129 f. Dissertação (Mestrado) - Curso de Arquitetura e Urbanismo, Centro Tecnológico, Universidade Federal de Santa Catarina, Florianópolis, 2022. Disponível em: https://labeee.ufsc.br/index.php/pt-br/node/1098.""")