import asyncio
import importlib
import os
from threading import Thread

from flask import Flask
from pyrogram import idle

from Extractor.modules import ALL_MODULES

# =========================
# WEB SERVER FOR KOYEB
# =========================

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is Running Successfully!"

def run_web():
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

# Background me web server start
Thread(target=run_web).start()

# =========================
# BOT
# =========================

loop = asyncio.get_event_loop()

async def sumit_boot():

    for all_module in ALL_MODULES:
        importlib.import_module("Extractor.modules." + all_module)

    print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")

    await idle()

    print("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")

if __name__ == "__main__":
    loop.run_until_complete(sumit_boot())
