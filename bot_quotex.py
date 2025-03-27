import telebot
import time
import requests
import random

# Configurações do Bot
TOKEN = "7880857109:AAG7Oe3fKo48MI9OgNSkYyJ2yt6g-w-oMAQ" 

CHAT_ID = "7268477518"

bot = telebot.TeleBot(TOKEN)

# Lista de ativos monitorados
ATIVOS = ["EUR/USD", "GBP/USD", "ARS/USD", "COP/USD", "NDZ/USD", "CAD/USD", 
          "CAD/EUR", "INR/USD", "AUD/USD", "Bitcoin/USD", "TRY/USD"]

# Variáveis de controle
sinais_enviados = 0
limite_perda_diaria = 3
perdas = 0

# Função para buscar preços (simulação)
def buscar_preco(ativo):
    return random.uniform(1.0, 2.0)  # Simulação de cotação

# Função para verificar padrões de velas e cruzamento de médias
def analisar_mercado(ativo):
    rsi = random.randint(20, 80)  # Simula um RSI aleatório
    media_curta = random.uniform(1.0, 2.0)
    media_longa = random.uniform(1.0, 2.0)

    # Estratégia de entrada (simulação)
    if rsi < 30 and media_curta > media_longa:
        return f"📢 *Sinal de COMPRA* em {ativo}\n📉 RSI: {rsi}\n📊 Médias móveis cruzaram para alta!"
    elif rsi > 70 and media_curta < media_longa:
        return f"📢 *Sinal de VENDA* em {ativo}\n📈 RSI: {rsi}\n📊 Médias móveis cruzaram para baixa!"
    return None

# Função para enviar sinais no Telegram
def enviar_sinal():
    global sinais_enviados, perdas

    if perdas >= limite_perda_diaria:
        bot.send_message(CHAT_ID, "⚠️ *Limite de perdas atingido! Parando os sinais por hoje.*")
        return

    ativo = random.choice(ATIVOS)
    sinal = analisar_mercado(ativo)

    if sinal:
        sinais_enviados += 1
        bot.send_message(CHAT_ID, sinal, parse_mode="Markdown")

        # Simulação de resultado (50% de chance de ganhar/perder)
        resultado = random.choice(["win", "loss"])
        if resultado == "loss":
            perdas += 1
            bot.send_message(CHAT_ID, f"❌ Perda no {ativo}. Iniciando Martingale!")

            # Martingale 1 nível (dobrando a entrada)
            martingale_sinal = analisar_mercado(ativo)
            if martingale_sinal:
                bot.send_message(CHAT_ID, f"🎲 *Martingale:* {martingale_sinal}", parse_mode="Markdown")
                resultado = random.choice(["win", "loss"])
                if resultado == "loss":
                    perdas += 1  # Conta mais uma perda

# Loop principal (envia sinais a cada 5 minutos)
while True:
    enviar_sinal()
    time.sleep(300)  # Espera 5 minutos antes do próximo sinal