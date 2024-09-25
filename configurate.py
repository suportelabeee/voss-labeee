from __future__ import annotations
## IMPORTED FUTURE FOR ST_PAGES HIDE PAGES
import streamlit as st 
import smtplib
import email.message
from random import randint
import json
import requests
from streamlit_gsheets import GSheetsConnection
import gspread
from google.oauth2.service_account import Credentials
from time import sleep
from datetime import datetime

# ---------------VARIÁVEIS---------------

project = "VOSS"
placeholder_img = r'static/placeholder.png'
st.session_state['auth'] = False

credentials = json.loads(st.secrets['CREDENTIALS'])
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(credentials, scopes=scopes)
client = gspread.authorize(creds)

sheet_id = st.secrets['SHEET_ID']

workbook = client.open_by_key(sheet_id)
worksheet_build = workbook.worksheet('build')
worksheet_user = workbook.worksheet('user')

support_mail = "escritorios.qai.bot@gmail.com"

password = st.secrets['PASSWORD']

authorization_list = st.secrets["AUTH_LIST"]

injection = st.secrets['INJECTION']

# ---------------------------------------


def initialize_page():
    st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
        [data-testid="stToolbarActions"] {
            display: none
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True,)
    

def create_top(big_text_title: str = None, subtitle: str = None, subtitle2: str = None, subsubtitle: str = None, img_url: str = None, use_line: bool = True, use_progress: bool = False, progress_percentage:int = 0, use_image: bool = True):
    st.set_page_config(
    page_title=f'{project}',
    page_icon = '🖥️',
    layout='wide',
    initial_sidebar_state='collapsed'
    )
    st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
    [data-testid="stToolbarActions"] {
        display: none
    }
    [data-testid="stHeader"] {
        display: none;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""",
    unsafe_allow_html=True,)
    if use_image:
        _,col,_ = st.columns([5,1,5])
        col.image(r'static/voss-03.png', width=100, use_column_width=True)
    with st.container():
        esquerda, meio, direita = st.columns(3)
        if use_progress:
            meio.progress(progress_percentage)

    with st.container():
        esquerda, direita = st.columns(2, gap='medium')
        if big_text_title:
            esquerda.title(big_text_title)
        if subtitle:
            esquerda.subheader(subtitle)
        if subtitle2:
            esquerda.subheader(subtitle2)
        if subsubtitle:
            esquerda.write(subsubtitle)
        if img_url:
            direita.image(img_url, width=600)
    if use_line:
        st.markdown('---')


def footer():
    st.title('')
    col1, _, col2, col3 = st.columns(4)
    col1.image(r'static/lab_banner.png', width=300)
    col2.markdown(f"[SOBRE NÓS](https://voss-labeee.streamlit.app/SobreNos)")
    col3.markdown(f"[SUPORTE](mailto:{support_mail})")


def get_build_info_by_id(id_: int):
    conn = st.connection("gsheets", type=GSheetsConnection, ttl=0)
    sql = f'SELECT * FROM build WHERE "id" = {id_}'
    response = conn.query(sql)
    if response.empty:
        return None, "ERROR"
    return response, "OK"


def register_answer():
    worksheet_user.append_row([st.session_state['edificio']] + [st.session_state['email']] + [st.session_state['tempo']] + list(st.session_state['PeR'].values()))


def place_left_subtitle(text: str):
    esquerda, direita = st.columns([3,1])
    esquerda.markdown(f'**{text}**')


def next_page_button(name: str, phrase: str = None, aviso: str = None):
    esquerda, direita = st.columns([4,1])
    if phrase:
        esquerda.subheader(phrase)
    if aviso:
        esquerda.info(aviso)
    direita.write('')
    botao = direita.button(label=name)
    return botao


def centered_button(name: str):
    esquerda, meio, direita = st.columns([1.5,1,1])
    botao = meio.button(name)
    return botao


def create_radio(name: str = None, phrase:str = None, extreme_left:str = None, extreme_right:str = None, min:int = 0, max:int = 10, divide:bool = False, key = None, show_values:bool = False, large:bool = False, five_columns_width:list = [1,0.5,0.4,0.6,1], two_columns_width:list = [1,2], selection:list = None, use_list_selection:bool = False, desabilitado: bool = False):
    if use_list_selection:
        opt = selection
    else:
        opt = range(min, max+1)
    if large:
        esquerda, direita = st.columns(two_columns_width)
        if phrase:
            esquerda.title('')
            esquerda.write(phrase)
        if name:
            if show_values:
                valor = direita.radio(label=name, options=opt, horizontal=True, index=None, key=key)
            else:
                valor = direita.radio(label=name, options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
        else:
            if show_values:
                valor = direita.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, index=None, key=key)
            else:
                valor = direita.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
    elif divide:
        esquerda, vazio, meioesquerda, meio, meiodireita = st.columns(five_columns_width)
        if phrase:
            esquerda.title('')
            esquerda.write(phrase)
        if extreme_left:
            meioesquerda.title('')
            meioesquerda.caption(extreme_left)
        if extreme_right:
            meiodireita.title('')
            meiodireita.caption(extreme_right)
        if name:
            if show_values:
                valor = meio.radio(label=name, options=opt, horizontal=True, index=None, key=key)
            else:
                valor = meio.radio(label=name, options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
        else:
            if show_values:
                valor = meio.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, index=None, key=key)
            else:
                if desabilitado:
                    valor = meio.radio(disabled=True, label='No name', label_visibility='hidden', options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
                else:
                    valor = meio.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
    else:
        if name:
            if show_values:
                valor = st.radio(label=name, options=opt, horizontal=True, index=None, key=key)
            else:
                valor = st.radio(label=name, options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
        else:
            if show_values:
                valor = st.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, index=None, key=key)
            else:
                valor = st.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
    return valor


def nested_radio(name: str = None, text_left:str = None, text_right:str = None, min:int = 0, max:int = 10, key = None, show_values:bool = False, columns_width:list = [0.2,0.6,0.6], selection:list = None, use_list_selection:bool = False):
    esquerda, meio, direita = st.columns(columns_width)
    if use_list_selection:
        opt = selection
    else:
        opt = range(min, max+1)
    if text_left:
        esquerda.write('')
        esquerda.write('')
        esquerda.caption(text_left)
    if text_right:
        direita.write('')
        direita.write('')
        direita.caption(text_right)
    if name:
        if show_values:
            valor = meio.radio(label=name, options=opt, horizontal=True, index=None, key=key)
        else:
            valor = meio.radio(label=name, options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
    else:
        if show_values:
            valor = meio.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, index=None, key=key)
        else:
            valor = meio.radio(label='No name', label_visibility='hidden', options=opt, horizontal=True, format_func=(lambda x: ''), index=None, key=key)
    return valor


def mail_auth_code(mail_person:str):
    auth_code = authorization_list[randint(0, len(authorization_list)-1)]
    corpo_email = f"""
    <p>Seu código de verificação para o questionário é<p>
    <h1><strong>{auth_code}</strong></h1>
    <br>
    <hr>
    <p>Esta é uma mensagem automática, não é necessário respondê-la.</p><br><br>
    <a href="https://labeee.ufsc.br/pt-br/en-welcome"><img src="https://labeee.ufsc.br/sites/default/files/labeee_final_completo_maior.png" width="400" /></a>"""
    msg = email.message.Message() 
    msg['Subject'] = f'CÓDIGO DE VERIFICAÇÃO - {project}, LabEEE'
    msg['From'] = 'escritorios.qai.bot@gmail.com'
    msg['To'] = mail_person
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    return auth_code


def send_thanks_email(mail_person:str):
    corpo_email = f"""
    <h2>A equipe {project} agradece pela participação na pesquisa!</h2>
    <br>
    <hr>
    <p>Esta é uma mensagem automática, não é necessário respondê-la.</p><br><br>
    <a href="https://labeee.ufsc.br/pt-br/en-welcome"><img src="https://labeee.ufsc.br/sites/default/files/labeee_final_completo_maior.png" width="400" /></a>"""
    msg = email.message.Message()
    msg['Subject'] = f'CONFIRMAÇÃO DE PARTICIPAÇÃO - {project}, LabEEE'
    msg['From'] = 'escritorios.qai.bot@gmail.com'
    msg['To'] = mail_person
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))


### IMPORTS FROM EXTERNAL MODULES
## STREAMLIT_EXTRAS --> switch page button
def switch_page(page_name: str):
    """
    Switch page programmatically in a multipage app

    Args:
        page_name (str): Target page name
    """
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")

    page_name = standardize_name(page_name)

    pages = get_pages("streamlit_app.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")


## ST_PAGES --> hide pages
import json
from dataclasses import dataclass
from pathlib import Path
from time import sleep

import toml

try:
    from streamlit import _gather_metrics  # type: ignore
except ImportError:

    def _gather_metrics(name, func, *args, **kwargs):
        return func


import streamlit as st
from streamlit import runtime
from streamlit.commands.page_config import get_random_emoji
from streamlit.errors import StreamlitAPIException
from streamlit.watcher import LocalSourcesWatcher

try:
    from streamlit.runtime.scriptrunner import get_script_run_ctx
except ImportError:
    from streamlit.scriptrunner.script_run_context import (  # type: ignore
        get_script_run_ctx,
    )

from streamlit.source_util import _on_pages_changed, get_pages

try:
    from streamlit.source_util import page_icon_and_name
except ImportError:
    from streamlit.source_util import page_name_and_icon  # type: ignore

    def page_icon_and_name(script_path: Path) -> tuple[str, str]:
        icon, name = page_name_and_icon(script_path)
        return name, icon


try:
    from streamlit import cache_resource
except ImportError:
    from streamlit import experimental_singleton as cache_resource

from streamlit.util import calc_md5

def _get_page_hiding_code(pages_to_hide: list[str]) -> str:
    styling = ""
    current_pages = get_pages("")
    section_hidden = False
    for idx, val in enumerate(current_pages.values()):
        page_name = val.get("page_name")
        if val.get("is_section"):
            # Set whole section as hidden
            section_hidden = page_name in pages_to_hide
        elif not val.get("in_section"):
            # Reset whole section hiding if we hit a page thats not in a section
            section_hidden = False
        if page_name in pages_to_hide or section_hidden:
            styling += f"""
                div[data-testid=\"stSidebarNav\"] li:nth-child({idx + 1}) {{
                    display: none;
                }}
            """

    styling = f"""
        <style>
            {styling}
        </style>
    """

    return styling


def _hide_pages(hidden_pages: list[str]):
    """
    For an app that wants to dynmically hide specific pages from the navigation bar.
    Note - this simply uses CSS to hide the menu item, it does not remove the page
    If using this with any security / permissions in mind,
    you also need to block the hidden page from executing
    """

    styling = _get_page_hiding_code(hidden_pages)

    st.write(
        styling,
        unsafe_allow_html=True,
    )


hide_pages = _gather_metrics("st_pages.hide_pages", _hide_pages)
