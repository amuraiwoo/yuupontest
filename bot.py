import discord
from discord import app_commands
import asyncio
import os
from flask import Flask
from threading import Thread

# ===== keep-alive 用 =====
app_flask = Flask(__name__)

@app_flask.route("/")
def home():
    return "OK"

def run_flask():
    app_flask.run(host="0.0.0.0", port=10000)

Thread(target=run_flask).start()
# ========================

SEND_COUNT = 50
SEND_INTERVAL = 1.5

class App(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.none())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

bot = App()

@bot.tree.command(
    name="yuupon",
    description="ゆうぽんのアプリ"
)
async def yuupon(interaction: discord.Interaction):
    await interaction.response.send_message("# 障害者たちを倒す！正義のひーろーゆうぽん様参上！")

    for i in range(SEND_COUNT):
        await asyncio.sleep(SEND_INTERVAL)
        await interaction.followup.send(f"# @everyoneゆうぽん様万歳wwwwww🤣 🤣 🤣 🤣 🤣 🤣 🤣 🤣 🤣 こんなクソ鯖徹底的に潰してやるわwwwwww何も出来ない特別支援学級のみんなーwwwwwwwwwwwww障害者のみんなwwwwwwwひっひっひwwwゆうぽん万歳！！🤓🤓🤓🤓お前らこの鯖入れよ！ゆうぽん万歳早く入れよ！w🤓🤓🤓🤓この文章読んで画面の前で赤面になってる君！悔しいもんな！悔しいよな！でもお前ら何もできないもんなwww何も言い返せないもんな！www無能な管理人はもっと対策施策でもしたらどうだ？あ、できないからこうなってるんだ！！！‪🤣‬‪🤣‬‪🤣‬‪🤣‬‪🤣https://discord.gg/erRwpctpeN {i+1}")

bot.run(os.getenv("TOKEN"))

