from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 관리자 텔레그램 ID 리스트 (본인 ID로 변경하세요)
ADMINS = [8069493255]

# /start 명령어 핸들러 함수
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("
안녕하세요, 오리엔 인베스트 입니다. 원활하고 빠른 상담을 진행을 위해 아래 항목 기재 부탁드립니다. 

항목1 기존회원/신규회원 
항목2 이름 
항목3 연락처
항목3 생년월일 
항목4 문의내용")

# 사용자가 보낸 메시지를 관리자들에게 전달하고, 사용자에게 접수 완료 메시지 보내기
async def forward_to_admins(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message

    # 관리자가 보낸 메시지는 무시
    if user.id in ADMINS:
        return

    forward_text = f"📩 사용자 @{user.username or user.first_name} (ID: {user.id}) 님이 보낸 메시지:\n{message.text}"

    # 관리자에게 메시지 전달
    for admin_id in ADMINS:
        try:
            await context.bot.send_message(chat_id=admin_id, text=forward_text)
        except Exception as e:
            print(f"관리자 {admin_id}에게 메시지 전달 실패: {e}")

    # 사용자에게 접수 완료 메시지 전송
    await update.message.reply_text("접수 되었습니다, 문의내용 파악 후 신속하게 상담사 연결 도와 드리겠습니다. 잠시만 기다려 주세요.")

if __name__ == '__main__':
    TOKEN = "8135523315:AAF4UQ9NuSKIkhWj7Hb7nXKv0QGyqWpiWQg"

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.User(user_id=ADMINS)), forward_to_admins))

    print("봇이 실행 중입니다...")
    app.run_polling()


