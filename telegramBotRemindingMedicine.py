from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

about = """
أفوجين دواء يحتوي على مادة المينوكسيديل كمادة فعالة، يستخدم للرجال والنساء لعلاج الصلع وتساقط الشعر.يستخدم بخاخ أفوجين مباشرة على فروة الرأس بالطريقة التالية
1-	تجفيف الشعر وفروة الرأس جيداً قبل الاستخدام.
2-	رش بخاخ أفوجين على فروة الرأس 8-10 مرات، مرتين يومياً، ثم تدليك فروة الرأس جيداً لتوزيع الدواء.
3-	ترك الدواء ليجف على فروة الرأس، مع مراعاة عدم استخدام مجففات الشعر والسشوار، لأن الحرارة قد تقلل من مفعول محلول أفوجين.
4-	لأفضل النتائج يجب استعمال بخاخ أفوجين لمدة 4 شهور على الأقل.
ملاحظة
يجب ترك محلول أفوجين على الشعر لمدة لا تقل عن ساعتين إلى أربع ساعات، ليأخذ الدواء مفعوله في تحفيز نمو الشعر

"""
# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = '6446026854:AAEBkymSDRnisrFmCOnvBwu3y2zojh8xl_8'

def send_reminder(context: CallbackContext):
    chat_id = context.job.context
    context.bot.send_message(chat_id=chat_id, text="وقت أخذ العلاج")

def start(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
   
    context.bot.send_message(chat_id=user_id, text="""
أهلا بك عزيزي المشترك 
نتمنى لك رحلة علاجية ميسرة وأن لايريك الله مكروها

                          """)

    context.bot.send_message(chat_id=user_id, text= """

بوت التذكير من تكامل هو احدى مشاريع مسار الطب الرقمي (طلاب)، 
جاءت فكرة التطبيق بعد دراسة لمشكلة نسيان أخذ العلاجات اللازمة من قبل كثير من الناس مما أسهم في تدهور صحتهم وزيادة الأمراض والمشاكل التي يعانون منها،
سيكون هذا البوت رفيقك في التذكير الى حين انتهاء المدة العلاجية
راجين من الله دوام الصحة والعافية عليكم 

تم انشاء هذا البوت بواسطة الطلاب:
حسين أستاد.
علي الكاظم.
سعود الشويرد.

واشراف:
المهندس التقني: إبراهيم محمد النبهان.
الأستاذ: قاسم عبدالعزيز الخليفة.
          
                                                    
                                                    """)
    
    context.bot.send_message(chat_id=user_id, text="انت الان مشترك في خدمة التذكير بالعلاج")

    context.bot.send_message(chat_id=user_id, text="للاطلاع على معلومات العلاج  /info")

def info(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    context.bot.send_message(chat_id=user_id, text= about)



    # Schedule the reminder
    job = context.job_queue.run_repeating(send_reminder, interval=60, context=user_id)
    context.chat_data['job'] = job
    

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Handler for the /start command
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("info", info))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
