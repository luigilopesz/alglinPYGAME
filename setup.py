from setuptools import setup, find_packages

setup(
    name="alglinPYGAME",
    version="0.1.0",
    packages=find_packages(),  # Encontrar automaticamente todos os pacotes
    install_requires=[
        'pygame',
        'numpy',
    ],
    package_data={
        'alglinPYGAME': ['assets/**/*.png']
    },
    entry_points={
        "console_scripts": [
            "alglinPYGAME=alglinPYGAME.main:main",  # Certifique-se de que este caminho esteja correto
        ],
    },
    author="Luigi Lopes",
    author_email="luigilopes09@gmail.com",
    description="Jogo de Algebra Linear",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/luigilopesz/alglinPYGAME",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
