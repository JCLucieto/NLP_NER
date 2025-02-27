#==========================
#  Aplicação Streamlit
#==========================

# Imports
import streamlit as st
import spacy
from spacy_streamlit import visualize_ner

# Titulo
st.title('Reconhecimento de Entidades Nomeadas (NER)')

# Localização do Modelo NER
caminho_modelo = './modelo'
modelo = spacy.load(caminho_modelo)

# Colorindo os rótulos
rotulos = list(modelo.get_pipe('ner').labels)
cores = {
    'B-JURISPRUDENCIA': '#F0F8FF',
    'B-LEGISLACAO': '#FA8072',
    'B-LOCAL': '#98FB98',
    'B-ORGANIZACAO': '#DDA0DD',
    'B-PESSOA': '#F0E68C',
    'B-TEMPO': '#FFB6C1',
    'I-JURISPRUDENCIA': '#F0F8FF',
    'I-LEGISLACAO': '#FA8072',
    'I-LOCAL': '#98FB98',
    'I-ORGANIZACAO': '#DDA0DD',
    'I-PESSOA': '#F0E68C',
    'I-TEMPO': '#FFB6C1',
    'LOC': '#D3D3D3',
    'MISC': '#D3D3D3',
    'ORG': '#D3D3D3',
    'PER': '#D3D3D3'
}
opcoes = {'ents': rotulos, 'colors': cores}

# Solicita a escolha da opção para digitar um texto ou carregar um arquivo
escolha = st.radio(label='Escolha uma Opção:', options=['Digitar um Texto', 'Enviar um Arquivo'])

# Variável para receber o texto
texto = ''

# Trata a escolha do usuário

if escolha == 'Digitar um Texto':
    # Exibe o campo de texto logo após a escolha
    texto = st.text_area('Insira o texto:')
    # Exibe o botão "Enviar Texto" logo após o campo de texto
    if st.button('Enviar Texto') and texto:
        # Processamento do Texto (Aplicação do modelo)
        doc = modelo(texto)
        visualize_ner(
            doc,
            labels=rotulos,
            displacy_options=opcoes,
            title='Reconhecimento de Entidades Nomeadas'
        )

elif escolha == 'Enviar um Arquivo':
    arquivo = st.file_uploader('Faça o upload do arquivo (somente .txt):', type='txt')
    if arquivo is not None:
        texto = arquivo.read().decode('utf-8')
        # Processamento do Texto (Aplicação do modelo)
        doc = modelo(texto)
        visualize_ner(
            doc,
            labels=rotulos,
            displacy_options=opcoes,
            title='Reconhecimento de Entidades Nomeadas'
        )
