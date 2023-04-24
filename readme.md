<a name="readme-top"></a>


[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Base Script Selenium</h3>

  <p align="center">
    Um script simples para a base de aplicações em Selenium!
    <br />
    <a href="https://selenium-python.readthedocs.io"><strong>Selenium Docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">Exemplo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Reportar Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Conteudo</summary>
  <ol>
    <li>
      <a href="#Sobre-o-projeto">Sobre o Projeto</a>
    </li>
    <li>
      <a href="#Guia-de-Inicialização">Guia de Inicialização</a>
      <ul>
        <li><a href="#Requisitos">Requisitos</a></li>
        <li><a href="#Instalação">Instalação</a></li>
      </ul>
    </li>
    <li>
      <a href="#Como-usar">Como Usar</a>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## Sobre o projeto

Esse script usa uma ferramenta chamada `Selenium` para controlar o navegador `Google Chrome`. 
O objetivo do script é acessar um site específico e mantê-lo aberto.

* Para isso, o script começa desabilitando algumas mensagens no console. Em seguida, ele define onde está o programa que controla o Chrome (chamado de ChromeDriver).

* O script cria um objeto com algumas opções que o navegador deve usar, como se estivesse sendo usado por uma pessoa. Depois disso, ele adiciona uma opção que evita que o site perceba que o navegador está sendo controlado.

Com tudo isso configurado, o script abre o navegador, acessa o site desejado e mantém ele aberto.

### Linguagem do Codigo

Este e um codigo bastente simples que utiliza o Python como linguagem principal.

* [![Python][Python.py]][Python-url]


<!-- GETTING STARTED -->
## Guia de Inicialização

Esse é um guia simples para voce poder iniciar seu script.

### Requisitos

* Python 3 instalado
* Biblioteca Selenium instalada
* Google Chrome instalado
* ChromeDriver instalado

### Instalação

1. Instale o Python 3 (caso não tenha instalado): [Python](https://www.python.org/downloads/)
2. Instale a biblioteca Selenium executando o seguinte comando no terminal: 
   ```sh
   pip install selenium
   ```
3. Baixe e instale o Google Chrome: [Google Chrome](https://www.google.com/intl/pt-BR/chrome/)
4. Baixe o ChromeDriver compatível com a versão do seu Google Chrome: [Chrome Driver](chromedriver.chromium.org/home)
5. Descompacte o arquivo baixado e mova o arquivo 'chromedriver' para uma pasta de sua preferência.
6. Altere a variável driver_path no script para apontar para o caminho onde o arquivo 'chromedriver' foi salvo.


<!-- USAGE EXAMPLES -->
## Como Usar

1. Abra um terminal na pasta onde o script está salvo.
2. Execute o comando: python nome_do_script.py
3. O script irá abrir o Google Chrome, acessar o site https://bot.sannysoft.com e manter o navegador aberto.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/Dixavado/Base-Selenium/forks
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/Dixavado/Base-Selenium/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/Dixavado/Base-Selenium/issues
[Python.py]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org