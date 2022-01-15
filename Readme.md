# Projeto para adicionar e-mails na lista de "Emails Bloqueados" ou "Emails Liberados" da Locaweb

**SEJA BEM-VINDO A ESTE REPOSITÓRIO!!!**
------------

Note que este é o meu primeiro projeto em Python e o primeiro compartilhado no GitHub. Cada dia que passa eu aprendo um pouco mais sobre o Python e assim irei melhorando o código do programa.

### Introdução

Atualmente, aqui na empresa, nós utilizamos o provedor de e-mails Locaweb devido ao bom custo/benefício. Em contrapartida ao seu bom custo/benefício, ele fica um pouco a desejar em alguns aspectos, como por exemplo, nós não termos uma opção que facilite a adição de diversos e-mails/domínios de uma única vez na lista de "Emails Bloqueados" ou "Emails Liberados".

Infelizmente, nós acabamos recebendo muitos spams todos os dias e, como mencionado, não existe uma maneira rápida e fácil de adicionar diversos e-mails/domínios para serem bloqueados, evitando assim o recebimento de e-mails que são indesejados, ou liberados, para garantir que e-mails importantes não caiam na caixa de spam. A única forma disponível é a apresentada pela ajuda online do próprio site da Locaweb. Ela pode ser acessada [neste link](https://ajuda.locaweb.com.br/wiki/criar-enderecos-liberados-e-bloqueados-email-locaweb/ "neste link").

### Motivação

A motivação para iniciar o desenvolvimento desse projeto foi mais pessoal do que profissional. Eu estava cansado de procurar e-mails importantes e ter que garimpar entre tantos outros e-mails com conteúdos não solicitados e que não possuiam nenhuma função prática para o meu trabalho ou para a minha vida, os chamados e-mails spams. Mas, confesso que está sendo uma oportunidade de aprender algo novo. Como, por exemplo, a linguagem Python, Markdown, Git e Github. Assuntos que eu ainda não tinha tido uma real motivação e necessidade de botar a mão na massa e aprender.

Como a plataforma da Locaweb não me permite adicionar uma lista de e-mail, nós temos que adicionar manualmente um por um. Por conta disso, eu decidi pesquisar, estudar e criar esse projeto com o Python para que nós possamos pegar um arquivo TXT com uma lista de e-mail/domínios e adicionar diretamente e de forma automatizada na aba de "Emails Bloqueados"/"Emails Liberados" da Locaweb.

### Descrição do projeto

Em primeiro lugar vou explicar como é realizada a adição manual dos e-mails/domínios no servidor da Locaweb:

1. Faça o login em seu e-mail;
2. Clique sobre o seu nome e selecione "Configurações";

 ![Configuração](https://ajuda.locaweb.com.br/files/2018/05/config_filtro_web_novo.jpg "Configuração")

3. Do lado esquerdo do navegador clique em "Filtros e Regras";
4. Emails Bloqueados ou Emails Liberados;

 ![Emails Bloqueados](https://ajuda.locaweb.com.br/files/2020/06/emails_bloqueados-01.png "Emails Bloqueados")

 ![Emails Liberados](https://ajuda.locaweb.com.br/files/2020/06/emails_liberados-02.png "Emails Liberados")

5. Inserir no campo o e-mail, ou o domínio que deseja bloquear, ou liberar;
6. Clique no botão "Adicionar";
7. Ao fim da inserção dos e-mails/domínios, clique no botão "Salvar".