import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

class robloxid(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
           command_prefix='<',
           intents=intents
        )
        self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f'{self.user} foi inicializado!')
bot = robloxid()

@bot.tree.command(name='olá',description='Diga olá!')
async def ola(interaction:discord.Interaction):
   await interaction.response.send_message(f'Olá, {interaction.user.mention}! Acabamos de se conhecer?',ephemeral=True)

@bot.tree.command(name='adição',description='Adiciona dois fatores da adição.')
@app_commands.describe(
     n1='Primeiro fator a ser adicionado.',
     n2='Segundo fator a ser adicionado.'
)
async def adicao(interaction:discord.Interaction,n1:int,n2:int):
   await interaction.response.send_message(f'A adição de {n1} e {n2} tem o resultado de {n1 + n2}.',ephemeral=True)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1383549555072831618)
    if channel:
        embed = discord.Embed(
            title=f'Bem-vindo(a), {member.mention}!',
            description='Leia as <#1383549485782929438> e divirta-se!',
            color=discord.Color.green()
        )
        await channel.send(embed=embed,delete_after=5)

@bot.tree.command(name="set_regras", description="Envia as regras do servidor organizadas por categoria")
@commands.has_permissions(administrator=True)
async def set_regras(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📜 Regras do Servidor",
        color=discord.Color.orange()
    )

    # 🧑‍🤝‍🧑 Convivência
    embed.add_field(
        name="🧑‍🤝‍🧑 Convivência",
        value=(
            "**1. Respeito acima de tudo:** Ofensas, discriminação e brigas não serão toleradas.\n"
            "**2. Nome e avatar apropriados:** Nada ofensivo, sexual ou provocativo.\n"
            "**3. Siga as orientações da staff:** Obedeça e respeite a moderação."
        ),
        inline=False
    )

    # 🛡️ Segurança
    embed.add_field(
        name="🛡️ Segurança",
        value=(
            "**4. Sem conteúdo impróprio:** NSFW, gore ou conteúdo ilegal resultará em ban.\n"
            "**5. Proibido uso de cheats/hacks:** Seja em jogos ou bots, resultará em punição.\n"
            "**6. Denuncie comportamentos suspeitos:** Ajude a staff a manter o servidor seguro."
        ),
        inline=False
    )

    # 📢 Comunicação
    embed.add_field(
        name="📢 Comunicação",
        value=(
            "**7. Nada de spam ou flood:** Mensagens repetidas ou exageradas não são permitidas.\n"
            "**8. Proibida autopromoção:** Não divulgue servidores, canais ou redes sem permissão."
        ),
        inline=False
    )

    # 🛠️ Organização
    embed.add_field(
        name="🛠️ Organização",
        value=(
            "**9. Use os canais corretamente:** Respeite a função de cada canal.\n"
            "**10. Não peça cargos ou vantagens:** Isso inclui cargos, itens ou permissões especiais."
        ),
        inline=False
    )

    embed.set_footer(text="O descumprimento dessas regras pode levar a punições como mute, kick ou banimento.")

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="regra", description="Veja a explicação de uma regra específica")
@app_commands.describe(numero="Número da regra (1 a 10)")
async def regra(interaction: discord.Interaction, numero: int):
    regras = {
        1: "🧑‍🤝‍🧑 **Regra 1 - Respeito acima de tudo:**\nNão toleramos ofensas, xingamentos, racismo ou preconceito de qualquer tipo.",
        2: "🧑‍🤝‍🧑 **Regra 2 - Nome e avatar apropriados:**\nEvite nomes/avatares ofensivos, provocativos ou com teor sexual.",
        3: "🧑‍🤝‍🧑 **Regra 3 - Respeite a staff:**\nA equipe está aqui para manter a ordem. Obedeça e não provoque.",
        4: "🛡️ **Regra 4 - Sem conteúdo impróprio:**\nNada de NSFW, gore ou qualquer coisa ilegal.",
        5: "🛡️ **Regra 5 - Proibido uso de cheats/hacks:**\nCheats em jogos ou no servidor resultam em ban imediato.",
        6: "🛡️ **Regra 6 - Denuncie comportamentos suspeitos:**\nUse o canal correto ou chame a staff.",
        7: "📢 **Regra 7 - Nada de spam ou flood:**\nMensagens repetitivas, caps lock excessivo ou emojis em excesso serão removidos.",
        8: "📢 **Regra 8 - Sem autopromoção:**\nProibido divulgar links de servidores, canais, redes sociais sem permissão.",
        9: "🛠️ **Regra 9 - Use os canais corretamente:**\nCada canal tem sua função. Exemplo: memes no #memes, dúvidas no #ajuda.",
        10: "🛠️ **Regra 10 - Não peça cargos ou vantagens:**\nCargos são conquistados. Pedir cargos ou vantagens atrapalha a equipe."
    }

    regra_texto = regras.get(numero)

    if not regra_texto:
        await interaction.response.send_message("❌ Regra inválida. Escolha um número de 1 a 10.", ephemeral=True)
        return

    embed = discord.Embed(
        title=f"📘 Regra {numero}",
        description=regra_texto,
        color=discord.Color.blue()
    )

    await interaction.response.send_message(embed=embed, ephemeral=True)

bot.run(TOKEN)
