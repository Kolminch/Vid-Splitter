import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import video_splitter as vs
import settings

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("%s started the bot", user.first_name.title())
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def split(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Download file.
    file_id = update.message.video.file_id
    new_file = await context.bot.get_file(file_id)
    video_name = await new_file.download_to_drive("vid/video.mp4")
    logger.info("Saved %s ", video_name)

    # split
    split_videos = vs.split(str(video_name))
    
    for v in split_videos:
        await context.bot.send_video(chat_id=update.effective_chat.id, video=v)
    
    # Remove files to reuse folder    
    vs.remove(split_videos)
    vs.remove([str(video_name)])
    logger.info("Removed %s and split videos", video_name)
    

if __name__ == '__main__':
    print(settings.BOT_TOKEN)
    application = ApplicationBuilder().token(settings.BOT_TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    video_handler = MessageHandler(filters.VIDEO, split)
    application.add_handler(start_handler)
    application.add_handler(video_handler)
    
    application.run_polling()