import telebot

CHAVE_API = "6015295818:AAF1LD2xwQtVns9Jjyf87sK9NKukh7wWXag"
bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands="Frontend1")
def responder(mensagem):
    text = """"
Front-end é a parte de um sistema, aplicativo ou site que interage diretamente com o usuário. É a camada responsável por exibir e renderizar o conteúdo visualmente, incluindo o design, a interface do usuário e a interação através de elementos como botões, menus, formulários, entre outros. Em resumo, o front-end é a parte visível e interativa de uma aplicação web.
    """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands="Frontend2")
def responder(mensagem):
    text = """"
Para começar a estudar front-end, você deve aprender HTML, CSS e JavaScript. O HTML é a linguagem de marcação que estrutura o conteúdo da página, o CSS é utilizado para estilizar e dar aparência ao conteúdo, e o JavaScript é responsável pela interatividade e dinamismo na página. Essas são as bases fundamentais para iniciar seus estudos em front-end.        
    """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands="Frontend3")
def responder(mensagem):
    text = """"
React: Um framework JavaScript de código aberto mantido pelo Facebook. É amplamente utilizado para a construção de interfaces de usuário interativas e reativas.
Angular: Um framework TypeScript mantido pelo Google. Ele permite a criação de aplicativos web escaláveis e complexos, com recursos avançados.
Vue.js: Um framework JavaScript progressivo e de fácil aprendizado. É conhecido por sua simplicidade e flexibilidade, permitindo criar desde pequenos componentes até aplicativos de página única (SPA).
Bootstrap: Uma biblioteca CSS que oferece um conjunto de estilos pré-definidos e componentes reutilizáveis. É utilizado para criar interfaces responsivas e bem estruturadas rapidamente.

Esses são apenas alguns exemplos de frameworks populares no desenvolvimento front-end. É importante lembrar que o cenário de tecnologias pode evoluir rapidamente, então fique atento às tendências e às necessidades do mercado ao escolher quais frameworks aprender.
    """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands="Backend1")
def responder(mensagem):
    text = """"
Backend é a parte do sistema de software que lida com a lógica de negócios, processamento de dados e armazenamento. É responsável por tudo o que acontece nos bastidores de um aplicativo, sem ser visível para o usuário final.    
    """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands="Backend2")
def responder(mensagem):
    text = """"
Para começar a estudar Backend, você precisa aprender uma linguagem de programação popular, como Python, Java ou Node.js. Em seguida, familiarize-se com frameworks e bibliotecas relevantes, como Django, Spring ou Express.js. Aprenda também sobre bancos de dados, APIs e serviços web, fundamentos da web, arquitetura de software, versionamento de código e segurança. Esteja ciente de que a aprendizagem contínua é essencial nessa área.    
    """
    bot.send_message(mensagem.chat.id, text)


@bot.message_handler(commands="Backend3")
def responder(mensagem):
    text = """"
Python: Django e Flask.
Java: Spring Boot e Play Framework.
JavaScript/Node.js: Express.js e Koa.js.
Ruby: Ruby on Rails.
PHP: Laravel e Symfony.

A escolha do framework dependerá da linguagem que você estiver usando e das necessidades do projeto. Lembre-se de que compreender os conceitos fundamentais do desenvolvimento Backend é fundamental, independentemente do framework escolhido.
    """
    bot.send_message(mensagem.chat.id, text)


def verificar(mensagem):
    return True


@bot.message_handler(commands="Frontend")
def responder(mensagem):
    text = """"
    Escolha uma opção para continuar (Clique no item):
    
/Frontend1 O que quer dizer Front-end ?
/Frontend2 O que eu devo aprender para começar a estudar Front-end?
/Frontend3 Quais Frameworks devo saber para evoluir no Front-end?

Clique em alguma das 3 opções, qualquer ação diferente, não ira funcionar!
    """
    bot.reply_to(mensagem, text)

@bot.message_handler(commands="Backend")
def responder(mensagem):
    text = """"
Escolha uma opção para continuar (Clique no item):
    
/Backend1 O que quer dizer Backend ?
/Backend2 O que eu devo aprender para começar a estudar Backend?
/Backend3 Quais Frameworks devo saber para evoluir no Backend?
    
Clique em alguma das 3 opções, qualquer ação diferente, não ira funcionar!
    """
    bot.reply_to(mensagem, text)

@bot.message_handler(func=verificar)
def responder(mensagem):
    text = """"
Escolha uma opção para continuar (Clique no item):
Você gostaria de saber mais sobre Frontend ou Backend?

/Frontend
/Backend
    
Clique em alguma das 2 opções, qualquer ação diferente, não ira funcionar!
    """
    bot.reply_to(mensagem, text)

bot.polling()
