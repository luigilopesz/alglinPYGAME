from setuptools import setup, find_packages

setup(
    name="alglinPYGAME",  # Nome do pacote
    version="0.1.0",  # Versão do pacote
    packages=find_packages(include=['alglinPYGAME', 'alglinPYGAME.*']),  # Encontrar automaticamente todos os pacotes
    install_requires=[  # Dependências
        'pygame',  # Adicione dependências como pygame aqui
        'numpy',   # Adicione numpy ou outras bibliotecas que você usa
    ],
    package_data={
        'alglinPYGAME': ['assets/**/*.png']  # Inclui todos os arquivos .png dentro da pasta 'assets'
    },
    entry_points={
        "console_scripts": [
            "alglinPYGAME=alglinPYGAME.main:main",  # Corrigido o caminho do entry point
        ],
    },
    author="Luigi Lopes",  # Seu nome
    author_email="luigilopes09@gmail.com",  # Seu email
    description="Jogo de Algebra Linear",
    long_description=open("README.md").read(),  # Descrição longa (usualmente do README)
    long_description_content_type="text/markdown",
    url="https://github.com/luigilopesz/alglinPYGAME",  # URL do seu repositório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versão mínima do Python
)
