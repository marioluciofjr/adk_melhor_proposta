# adk_melhor_proposta
Repositório que ajuda na precificação de serviços, utilizando agentes inteligentes de IA generativa.

![license - MIT](https://img.shields.io/badge/license-MIT-green)
[![site - prazocerto.me](https://img.shields.io/badge/site-prazocerto.me-230023)](https://prazocerto.me)
[![linkedin - @marioluciofjr](https://img.shields.io/badge/linkedin-marioluciofjr-blue)](https://linkedin.com/in/marioluciofjr)

## Índice

* [Introdução](#introdução)
* [Estrutura do projeto](#estrutura-do-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Requisitos](#requisitos)
* [Como obter a API KEY no Google AI Studio](#como-obter-a-api-key-no-google-ai-studio)
* [Como executar](#como-executar)
* [Links úteis](#links-úteis)
* [Contribuições](#contribuições)
* [Licença](#licença)
* [Contato](#contato)

## Introdução

Este projeto integra múltiplos agentes inteligentes para aprimorar negociações e precificação de projetos. Através de métodos inovadores, como o acarv e a abordagem ZOPA, a ferramenta auxilia usuários a estabelecer orçamentos precisos, combinando informações de custos essenciais e operacionais. Os agentes interagem de forma sequencial e coordenada, proporcionando recepção calorosa, cálculos assertivos, estratégias de negociação e orientações para manter o equilíbrio emocional. O modelo generativo utilizado nos testes foi o `gemini-2.0-flash`.

## Estrutura do projeto

A ideia deste projeto de multiagentes surgiu a partir da aula de MCP e A2A, do professor Sandeco Macedo. Fui sugerir um conteúdo para o canal dele no YouTube e ele perguntou se eu não conseguiria fazer esse projeto de precificação. Utilizei um fluxo de agentes simples com a arquitetura do [ADK (Agent Development Kit)](https://google.github.io/adk-docs/), do Google. É apenas um projeto para fins didáticos, de modo que sirva para estudar um pouco mais sobre o desenvolvimento de agentes inteligentes.

Logo abaixo, confira a breve descrição de cada agente desse fluxo.

### boas_vindas
Descrição: Dá as boas-vindas à pessoa usuária após o gatilho "Olá".
O que faz: Recepciona a pessoa com empatia, educadamente e faz perguntas iniciais para conhecer melhor seus interesses e profissão.
Como pode ajudar a pessoa usuária: Cria um ambiente amigável e acolhedor, facilitando a continuidade da interação e ajustando a conversa conforme as necessidades do usuário.

### precifica
**Descrição**: Responsável por precificar o projeto após o agente de boas-vindas.
**O que faz**: Recolhe informações financeiras e operacionais da pessoa usuária, armazena os dados em variáveis e utiliza a ferramenta “acarv”, que utiliza o [método da Ana Carvalho RP](https://www.linkedin.com/posts/anacarvalhorp_precifica%C3%A7%C3%A3o-activity-7237086282177249283-y-Wm?utm_source=share&utm_medium=member_desktop&rcm=ACoAACHvXJYBKyTyP1ggw536I9ZWCnCwD7LTax0) como premissa para calcular o orçamento ideal.
**Como pode ajudar a pessoa usuária**: Auxilia na definição de um valor justo e competitivo para o projeto, garantindo rapidez, segurança e confiança na negociação.

### zopa
**Descrição**: Identifica a melhor zona de possível acordo (ZOPA) após a precificação do projeto.
**O que faz**: Analisa o valor indicado e o contexto da negociação para sugerir a melhor estratégia de ajuste de preço.
**Como pode ajudar a pessoa usuária**: Oferece orientações sobre negociação, ajudando a encontrar um equilíbrio onde ambas as partes possam chegar a um acordo satisfatório.

### relaxa
**Descrição**: Fornece dicas para reduzir a insegurança durante a negociação final, ativado após a análise do ZOPA.
**O que faz**: Acalma a pessoa, oferece conselhos de produtividade e técnicas para manter o equilíbrio emocional, baseados em estudo sobre saúde mental e produtividade.
**Como pode ajudar a pessoa usuária**: Promove bem-estar e segurança, reduzindo o estresse e ajudando a pessoa a negociar com mais confiança e clareza.

### melhor_proposta
**Descrição**: Organiza e coordena a sequência de todos os agentes, aguardando o comando "next" para avançar na conversa.
**O que faz**: Gerencia o fluxo de interação, garantindo que os agentes "boas_vindas", "precifica", "zopa" e "relaxa" atuem na ordem planejada.
**Como pode ajudar a pessoa usuária**: Assegura uma experiência integrada e ordenada, permitindo uma transição suave entre etapas da negociação e facilitando a compreensão do processo como um todo.

> [!TIP]
> Want to better understand this repository, but you don't speak Portuguese? Check out this complete tutorial:
> [Tutorial - adk_melhor_proposta](https://code2tutorial.com/tutorial/dd5c621b-9835-49a0-b06a-d7d053d00b61/index.md)
>
> Talk to a generative AI about this project:
> [Talk to GitHub - adk_perfis_ia](https://talktogithub.com/marioluciofjr/adk_melhor_proposta)

## Tecnologias utilizadas

<div>
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/63e3b960-3dc5-48fc-a300-b3104430235f" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/31ed57e7-f4b7-4d86-9373-668a38f8db17" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/0324b2d2-c9f4-4c2e-ba62-703a7f346de6" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/76e7aca0-5321-4238-9742-164c20af5b4a" />&nbsp;&nbsp;&nbsp    
</div><br><br>

* ADK (Agent Development Kit);
* Visual Studio Code
* Google AI Studio
* Gemini
* Python

## Requisitos

Para utilizar este projeto, você precisa de:

- **Conta Google**: para acessar o Google AI Studio
- **Chave de API do Google AI Studio (Gemini API)**: instruções para obtenção abaixo
- **IDE**: para realizar o projeto escolhi o VS Code, mas pode ser outra da sua preferência (Cursor, Windsurf etc.)
- **UV**: instalador rápido de pacotes python

## Como obter a API KEY no Google AI Studio

Para utilizar este código, você precisará de uma chave de API do Google Gemini:

1. Acesse o [Google AI Studio](https://ai.dev/app/apikey)
2. Faça login com sua conta Google
3. Clique no botão "Criar chave de API"
4. Aceite os termos de serviço, se solicitado
5. Copie a chave gerada e guarde-a em local seguro

> [!IMPORTANT]
> Atualmente, o Google AI Studio oferece um uso gratuito da API para testes. Sobre demais detalhes da API do Gemini, leia a [documentação oficial](https://ai.google.dev/gemini-api/docs/pricing?hl=pt-br#:~:text=O%20uso%20do%20Google%20AI,em%20todos%20os%20pa%C3%ADses%20dispon%C3%ADveis). Caso você não queira utilizar o Gemini, pesquise como obter a API KEY do modelo generativo de sua preferência.

## Como executar

1. Instale o VS Code se ainda não tiver em sua máquina (confira o link na seção [`Links úteis`](#links-úteis));
2. No cabeçalho deste repositório, clique no botão `<> Code`, que fica do lado de `Add file`. Escolha a opção 'Download ZIP';
3. Descompacte o arquivo na sua máquina na pasta de sua preferência;
4. Abra o VSCode e ache a sua pasta com o atalho `CTRL + O` (File > Open Folder);
5. Abra o terminal com o atalho `CTRL + J`;
6. Caso ainda não tenha o uv instalado, faça isso com o comando:
   ```powershell
   pip install uv
   ```
7. Crie o ambiente virtual com o comando:
   ```powershell
   uv venv
   ```
8. Ative o ambiente virtual com o comando (no Windows):
   ```powershell
   .venv\Scripts\activate
   ```
9. Coloque a api_key, que pegou no Google AI Studio, no seu arquivo `.env`:
    ```env
    GOOGLE_API_KEY=sua_api_key
    ```
10. Volte ao terminal e digite o comando:
    ```powershell
    adk web
    ```
11. Aparecerá essa informação no seu terminal. Basta clicar em `CTRL`e depois no link que aparece em `http://localhost:8000`:
    
    ![Image](https://github.com/user-attachments/assets/5ec45cbd-38f8-4e67-b1fc-286b509141f9)

12. Logo em seguida abrirá uma aba no seu navegador que tem essa interface:

    ![Image](https://github.com/user-attachments/assets/b5d2bfa7-e368-4436-97c7-f6ead8f29457)

13. Para começar, basta digitar em `Type a message`:
    ```prompt
    Olá
    ```
    Depois você pode chamar cada agente com o gatilho `next`. Se tiver dúvidas, assista o tutorial:

    [`TUTORIAL EM VÍDEO`](https://docs.google.com/videos/d/1q7s01JzJZKa2p871g3J0GVrqz09vzK0xuHU7tPOtMKs/edit?usp=sharing)

## Links úteis

* [Documentação oficial do ADK (Agent Development Kit)](https://google.github.io/adk-docs/) - Tudo que você precisa saber sobre o ADK do Google;
* [Como instalar o VSCode](https://code.visualstudio.com/download) - Link direto para download (retorne para a seção [`Como executar`](#como-executar))
* [O que são agentes de IA?](https://www.ibm.com/br-pt/think/topics/ai-agents) - Explicação da IBM sobre agentes inteligentes de IA;
* [6 segredos do GitHub Copilot no VSCode](https://youtu.be/FaR6tQ1VMnc?si=vvtBvtGKnhNmline) - vídeo do canal `Código Fonte TV`sobre o GitHub Copilot no VSCode, com explicação bem didática a respeito do assunto;
* [O que é uma API?](https://www.alura.com.br/artigos/api) - Guia da Alura sobre APIs;
* [venv — Criação de ambientes virtuais](https://docs.python.org/pt-br/3/library/venv.html) - Explicação completa de como funcionam os venvs
* [Features do UV](https://docs.astral.sh/uv/getting-started/features/) - algumas funcionalidades para utilizar o uv no terminal da melhor maneira;
* [MCP e A2A](https://physia.com.br/mcp/) - link de compra do livro do professor Sandeco;
* [Agentes de IA poderosos com o Google ADK](https://www.youtube.com/watch?v=NkIZgBvA6G4&list=PLbmt8d_ueDMWHIv-HgdM532MLFSju6W2D&ab_channel=Sandeco) - playlist de vídeos do canal Sandeco sobre o framework ADK.

## Contribuições

Contribuições são bem-vindas! Se você tem ideias para melhorar este projeto, sinta-se à vontade para fazer um fork do repositório.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](https://github.com/marioluciofjr/adk_melhor_proposta/blob/main/LICENSE) para detalhes.

## Contato
    
Mário Lúcio - Prazo Certo®
<div>  	
  <a href="https://www.linkedin.com/in/marioluciofjr" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> 
  <a href = "mailto:marioluciofjr@gmail.com" target="_blank"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <a href="https://prazocerto.me/contato" target="_blank"><img src="https://img.shields.io/badge/prazocerto.me/contato-230023?style=for-the-badge&logo=wordpress&logoColor=white"></a>
</div> 

