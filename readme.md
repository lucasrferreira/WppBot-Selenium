![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/ribeiroferreiralucas/WppScrapper?style=flat-square)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ribeiroferreiralucas/wppscrapper/CI?style=flat-square)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/ribeiroferreiralucas/wppscrapper/selenium?style=flat-square)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/ribeiroferreiralucas/wppscrapper/flask?style=flat-square)
![Docker Image Version (latest semver)](https://img.shields.io/docker/v/ribeiroferreiralucas/wppscrapper?sort=semver&style=flat-square)
![GitHub issues](https://img.shields.io/github/issues-raw/ribeiroferreiralucas/wppscrapper?style=flat-square)

# WppScrapper

O WppScrapper é um projeto de uma aplicação que se propõe a permitir que qualquer pessoa, especialmente jornalistas e pesquisadores, sejam capazes de coletar e extrair dados das trocas de mensagens do WhatsApp.

O projeto nasce do trabalho de conclusão de curso de [ribeiroferreiralucas](https://github.com/ribeiroferreiralucas) e [wilsonoliveira](https://github.com/wilsonoliveira) motivados pelo crescente uso do WhatsApp como ferramenta de organização social, consumo e divulgação de noticias e agitação social.

Link para o TCC: LINK AQUI ;)

## Getting Started 

### Pré-requisitos
 - Python3 >= 3.14
 - Pip3
 - geckodriver == 0.26
 - Firefox == 60
 
#### Instalando e configurando o geckodriver
- Windows
	- Faça download do drive correspondente ao seu sistema operacional: https://github.com/mozilla/geckodriver/releases
	- Extraia
	- Win: Posicione o arquivo `geckodriver` onde desejar e adicione o caminho até ele na variável de ambiente `PATH`.
- Lunux: (Ref: https://askubuntu.com/a/871077)
	- Faça download do drive correspondente ao seu sistema operacional: https://github.com/mozilla/geckodriver/releases
	- `tar -xvzf geckodriver*` (Extração do arquivo baixado)
	- `chmod +x geckodriver`
	- `export PATH=$PATH:/[path-to-extracted-file]/.`
- OSX:
	- `brew install geckodriver`
### Installing

#### Rodando em ambiente local
- Baixe ou Clone esse projeto para o seu dispositivo.
- Tenha certeza que todos os pré-requisitos estão instalados corretamente em sua máquina.
 - Abra o terminal no projeto e crie um `virtual environment`
	 - $ `python3 -m venv venv`
- Ative o `environment`
	- $ `. venv/bin/activate`
 - Instale as dependências usando pip
	 - $ `pip3 install -r requirements.txt`

 - Agora basta rodar a aplicação:
	 - $ `python back.py`
	 - A aplicação irá ficar exposta no endpoint: http://127.0.0.1:5000/

#### Rodando em docker local clonando o projeto
ref: http://containertutorials.com/docker-compose/flask-simple-app.html
- Baixe ou Clone esse projeto para o seu dispositivo.
- Certifique-se de ter o docker propriamente instalado.
- $ `docker build -t wppscrapper:latest .`
- $ `docker run -d -p 5000:5000 wppscrapper`

<!-- #### Rodando em docker local usando uma imagem pronta
ref: http://containertutorials.com/docker-compose/flask-simple-app.html
- Baixe ou Clone esse projeto para o seu dispositivo.
- Certifique-se de ter o docker propriamente instalado.
- $ `docker build -t wppscrapper:latest .`
- $ `docker run -d -p 5000:5000 flask-sample-one` -->

## O Projeto
O principal objetivo do projeto é desenvolver uma aplicação de fácil uso para que diferentes perfis de pessoas consigam extrair informações úteis do aplicativo de troca de mensagens WhatsApp.

 ### Funcionalidades desejadas
 
 - [ ] Autenticar uma conta do WhatsApp através da aplicação
 - [ ] Listar todos os grupos dessa conta de WhatsApp
 - [ ] Permitir ao usuário requisitar que a aplicação inicie a coleta de mensagens
 - [ ] Permitir ao usuário requisitar que a aplicação pause a coleta de mensagens
 - [ ] Permitir ao usuário que baixe todas as mensagens coletadas em diferentes formatos
	 - [ ] csv
	 - [ ] json
 - [ ] A aplicação deverá rodar num ambiente docker de fácil instalação local
 - [ ] A aplicação deverá rodar num ambiente docker de fácil instalação remota (Azure; AWS, Google Cloud...)

## Feito com

* [Flask](https://palletsprojects.com/p/flask/) - The web framework used


<!---
## Deployment

Add additional notes about how to deploy this on a live system

 ## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 
-->

## Autores

* **Lucas Ribeiro Ferreira**  - [ribeiroferreiralucas](https://github.com/ribeiroferreiralucas)
* **Wilson Oliveira**  - [wilsonoliveira](https://github.com/wilsonoliveira)

Veja a lista de [contribuidores](https://github.com/your/project/contributors) que participam desse projeto.
