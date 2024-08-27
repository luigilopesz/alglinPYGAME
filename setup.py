from setuptools import setup, find_packages

setup(
    name="alglinPYGAME",  # Nome do pacote
    version="0.1.0",  # Versão do pacote
    packages=find_packages(),  # Encontrar automaticamente todos os pacotes
    install_requires=[  # Dependências
        # Liste aqui outras bibliotecas que seu pacote precisa
    ],
    package_data={
        '': ['assets/**/*.png']  # Inclui todos os arquivos .png dentro do diretório 'img' de todos os pacotes
    },
    entry_points={
        "console_scripts": [
            "alglinPYGAME=alglinPYGAME.Main:Main",  # Se quiser criar um comando de terminal
        ],
    },
    author="Luigi Lopes",  # Seu nome
    author_email="luigilopes09@gmail.com",  # Seu email
    description='''
    # alglinPYGAME

jogo do Luigi 

Ao iniciar o jogo, responda a pergunta corretamente e ganhe um poder especial!!!

o poder especial é um tiro teleguiado (somente 1)

O objetivo do jogo é matar todos os aliens.

Voce possui 10 tiros normais ( +1 teleguiado se acertar a pergunta )

BOA SORTE !!!
''',
    long_description=open("README.md").read(),  # Descrição longa (usualmente do README)
    long_description_content_type="text/markdown",
    url="https://github.com/luigilopesz/alglinPYGAME",  # URL do seu repositório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versão mínima do Python
)