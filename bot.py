from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start 명령어 핸들러 함수
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("안녕하세요! 상담봇입니다. 무엇을 도와드릴까요?")

if __name__ == '__main__':
    # 봇 토큰 입력 (자신의 봇 토큰으로 바꿔주세요)
    TOKEN = "8135523315:AAF4UQ9NuSKIkhWj7Hb7nXKv0QGyqWpiWQg"

    # Application 객체 생성
    app = ApplicationBuilder().token(TOKEN).build()

    # 명령어 핸들러 등록
    app.add_handler(CommandHandler("start", start))

    # 봇 실행 (비동기)
    print("봇이 실행 중입니다...")
    app.run_polling()
