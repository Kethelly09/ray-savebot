
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
         "Ola Me envie o link do vídeo e eu o baixarei para você.🎬"
      
        Divirta-se 🥰
      
        — Bot criado com @GenesisCreatorBot
    )

def main():
    if not TOKEN:
        print("TOKEN não encontrado!")
        return

    print("BOT INICIANDO...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("BOT RODANDO...")
    app.run_polling()

if __name__ == "__main__":
    main()
