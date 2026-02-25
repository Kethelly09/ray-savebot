import os
import yt_dlp
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! 👋\n\n"
        "Me envie um link de vídeo que eu faço o download para você 🎬\n\n"
        "Bot criado com @GenesisCreatorBot"
    )

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    await update.message.reply_text("Baixando vídeo... ⏳")

    ydl_opts = {
        "format": "mp4",
        "outtmpl": "video.%(ext)s",
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        with open("video.mp4", "rb") as video:
            await update.message.reply_video(video)

        os.remove("video.mp4")

    except Exception as e:
        await update.message.reply_text("Erro ao baixar o vídeo 😢")

def main():
    if not TOKEN:
        print("TOKEN não encontrado!")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))

    print("BOT RODANDO...")
    app.run_polling()

if __name__ == "__main__":
    main()
