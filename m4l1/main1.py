import discord
import os
import uuid
from discord.ext import commands
from model1 import get_class 
intents = discord.Intents.default()
intents.message_content = True  # necessário para ler mensagens

bot = commands.Bot(command_prefix='$', intents=intents)

# Cria a pasta 'save' se não existir
if not os.path.exists('save'):
    os.makedirs('save')

@bot.event
async def on_ready():
    print(f'✅ Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá, eu sou o {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def enviar(ctx):
    # Verifica se há arquivos anexados
    if not ctx.message.attachments:
        await ctx.send("❌ Nenhuma imagem foi enviada! Anexe uma imagem junto com o comando.")
        return

    # Pega o primeiro anexo
    anexo = ctx.message.attachments[0]
    nome_original = anexo.filename
    
    # Gera nome único para não sobrescrever arquivos
    extensao = os.path.splitext(nome_original)[1]  # pega .png, .jpg...
    nome_unico = f"{uuid.uuid4()}{extensao}"  # ex: a1b2c3...png
    
    caminho_salvar = f"save/{nome_unico}"
    
    # Salva o arquivo
    await anexo.save(caminho_salvar)
    
    await ctx.send(
        f"✅ Imagem recebida!\n"
        f"Nome original: {nome_original}\n"
        f"Arquivo salvo como: {nome_unico}\n"
        f"URL: {anexo.url}"
    )

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")

bot.run("token")