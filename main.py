import telebot

CHAVE_API = "6015295818:AAF1LD2xwQtVns9Jjyf87sK9NKukh7wWXag"


def verificar(mensagem):
    if mensagem.text == "Olá":
        return True
    else:
        return False
@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem, "Olá aqui é o Bot criado por Gabriel Bernardo")


bot = telebot.TeleBot(CHAVE_API)