from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from settings import TELEGRAM_TOKEN
import structlog

logger = structlog.get_logger()

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = f'Hello {update.effective_user.first_name}'
    logger.debug(msg)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    return await hello(update=update, context=context)


if __name__ == "__main__":
    
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hello", hello))

    app.run_polling()