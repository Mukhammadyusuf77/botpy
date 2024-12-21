from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

# Bot token
BOT_TOKEN = "7797887530:AAFvnxm_5sfewQtu_yxtRtHXMnmoSJTzMqM"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Language choices
languages = {
    "uz": "🇺🇿 O'zbek",
    "ru": "🇷🇺 Русский",
    "en": "🇬🇧 English"
}

# Lessons content
lessons = {
    "uz": [
        "1. Koreys tiliga kirish\n\nMaqsad: Tarix, madaniyat va alifbo (한글 - Hangul) haqida bilib olish.\n- Hangul tarixi (Qirol Sejong loyihasi).\n- Asosiy xususiyatlari: Gap tuzilishi (SOV – Sub'yekt, Ob'yekt, Fe'l).\n- Nega koreys tilini o'rganish kerak?\n\nMashq: Koreyscha salomlashishlarni yodlang:\n안녕하세요 (annyeonghaseyo) — Salom (rasmiy).\n안녕 (annyeong) — Salom (norasmiy).",
        "2. Hangul alifbosi: Unli tovushlar\n\nMaqsad: Asosiy unli tovushlarni o'rganish.\n- Asosiy unlilar: ㅏ, ㅓ, ㅗ, ㅜ, ㅡ, ㅣ.\n- Qo'shma unlilar: ㅑ, ㅕ, ㅛ, ㅠ, ㅐ, ㅔ.\n- Har bir tovushning to'g'ri talaffuzi.\n\nMashq: Unli tovushlar bilan bo'g'inlarni yozing va o'qing: 아, 어, 오, 우.",
        "3. Hangul alifbosi: Undosh tovushlar\n\nMaqsad: Undosh tovushlarni o'qish va yozishni o'rganish.\n- Asosiy undoshlar: ㄱ, ㄴ, ㄷ, ㄹ, ㅁ, ㅂ, ㅅ, ㅇ, ㅈ, ㅎ.\n- Yumshoq tovushlar talaffuzi (masalan, ㅇ).\n- Qo'shma undoshlar: ㅋ, ㅌ, ㅍ, ㅊ.\n\nMashq: Bo'g'inlar tuzing: 가, 나, 다, 마, 바, 사.",
        "4. Unli va undoshlarni birlashtirish\n\nMaqsad: Unli va undosh tovushlarni qanday birlashtirishni o'rganing.\n- Misollar: 가, 너, 도, 루, 무.\n- Bo'g'inlarni shakllantirish qoidalari.\n\nMashq: So'zlarni o'qib yozing: 하나 (bir), 나라 (mamlakat), 사람 (odam).",
        "5. Salomlashish va xayrlashish\n\nMaqsad: Salomlashish uchun asosiy iboralarni o'zlashtirish.\n- 안녕하세요 (annyeonghaseyo) — Salom.\n- 안녕히 가세요 (annyeonghi gaseyo) — Xayr (ular ketayotgan bo'lsa).\n- 안녕히 계세요 (annyeonghi gyeseyo) — Xayr (siz ketayotgan bo'lsangiz).\n\nMashq: Qisqa dialoglarni amalda bajaring."
    ],
    "ru": [
        "1. Введение в корейский язык\n\nЦель: Узнать об истории, культуре и алфавите (한글 - Хангыль).\n- История Хангыля (проект короля Седжона).\n- Основные особенности: Структура предложения (SOV – Подлежащее, Дополнение, Сказуемое).\n- Почему стоит учить корейский язык?\n\nПрактика: Запомните корейские приветствия:\n안녕하세요 (annyeonghaseyo) — Здравствуйте (официально).\n안녕 (annyeong) — Привет (неофициально).",
        "2. Алфавит Хангыль: Гласные\n\nЦель: Освоить основные гласные звуки.\n- Основные гласные: ㅏ, ㅓ, ㅗ, ㅜ, ㅡ, ㅣ.\n- Составные гласные: ㅑ, ㅕ, ㅛ, ㅠ, ㅐ, ㅔ.\n- Правильное произношение каждого звука.\n\nПрактика: Напишите и прочитайте слоги с гласными: 아, 어, 오, 우.",
        "3. Алфавит Хангыль: Согласные\n\nЦель: Научиться читать и писать согласные.\n- Основные согласные: ㄱ, ㄴ, ㄷ, ㄹ, ㅁ, ㅂ, ㅅ, ㅇ, ㅈ, ㅎ.\n- Произношение мягких звуков (например, ㅇ).\n- Удвоенные согласные: ㅋ, ㅌ, ㅍ, ㅊ.\n\nПрактика: Составьте слоги: 가, 나, 다, 마, 바, 사.",
        "4. Сочетание гласных и согласных\n\nЦель: Научиться сочетать гласные и согласные.\n- Примеры: 가, 너, 도, 루, 무.\n- Правила формирования слогов.\n\nПрактика: Прочитайте и напишите слова: 하나 (один), 나라 (страна), 사람 (человек).",
        "5. Приветствия и прощания\n\nЦель: Освоить основные фразы для приветствий.\n- 안녕하세요 (annyeonghaseyo) — Здравствуйте.\n- 안녕히 가세요 (annyeonghi gaseyo) — До свидания (если человек уходит).\n- 안녕히 계세요 (annyeonghi gyeseyo) — До свидания (если вы уходите).\n\nПрактика: Разыграйте короткие диалоги."
    ],
    "en": [
        "1. Introduction to Korean\n\nGoal: Learn about the history, culture, and alphabet (한글 – Hangul).\n- History of Hangul (King Sejong’s project).\n- Key features: Sentence structure (SOV – Subject, Object, Verb).\n- Why learn Korean?\n\nPractice: Memorize Korean greetings:\n안녕하세요 (annyeonghaseyo) — Hello (formal).\n안녕 (annyeong) — Hi (informal).",
        "2. Hangul Alphabet: Vowels\n\nGoal: Master the basic vowel sounds.\n- Basic vowels: ㅏ, ㅓ, ㅗ, ㅜ, ㅡ, ㅣ.\n- Compound vowels: ㅑ, ㅕ, ㅛ, ㅠ, ㅐ, ㅔ.\n- Correct pronunciation of each sound.\n\nPractice: Write and read syllables with vowels: 아, 어, 오, 우.",
        "3. Hangul Alphabet: Consonants\n\nGoal: Learn to read and write consonants.\n- Basic consonants: ㄱ, ㄴ, ㄷ, ㄹ, ㅁ, ㅂ, ㅅ, ㅇ, ㅈ, ㅎ.\n- Pronunciation of soft sounds (e.g., ㅇ).\n- Double consonants: ㅋ, ㅌ, ㅍ, ㅊ.\n\nPractice: Build syllables: 가, 나, 다, 마, 바, 사.",
        "4. Combining Vowels and Consonants\n\nGoal: Learn how to combine vowels and consonants.\n- Examples: 가, 너, 도, 루, 무.\n- Rules for forming syllables.\n\nPractice: Read and write words: 하나 (one), 나라 (country), 사람 (person).",
        "5. Greetings and Farewells\n\nGoal: Master basic phrases for greetings.\n- 안녕하세요 (annyeonghaseyo) — Hello.\n- 안녕히 가세요 (annyeonghi gaseyo) — Goodbye (if they are leaving).\n- 안녕히 계세요 (annyeonghi gyeseyo) — Goodbye (if you are leaving).\n\nPractice: Act out short dialogues."
    ]
}

# Greetings
greetings = {
    "uz": "Assalomu alaykum! Koreys tilini o'rganishni boshlashga tayyormisiz? Tilni tanlang:",
    "ru": "Здравствуйте! Готовы начать изучение корейского языка? Выберите язык:",
    "en": "Hello! Are you ready to start learning Korean? Choose a language:"
}

# User preferences storage
user_preferences = {}

# Start command handler
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    lang_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for lang_code, lang_name in languages.items():
        lang_keyboard.add(KeyboardButton(lang_name))
    await message.answer("Please choose your language / Tanlang / Выберите язык:", reply_markup=lang_keyboard)

# Language selection handler
@dp.message_handler(lambda message: message.text in languages.values())
async def select_language(message: types.Message):
    user_id = message.from_user.id
    for lang_code, lang_name in languages.items():
        if message.text == lang_name:
            user_preferences[user_id] = lang_code
            break
    lesson_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(1, 6):
        lesson_keyboard.add(KeyboardButton(f"Lesson {i}"))
    lang = user_preferences[user_id]
    await message.answer(greetings[lang], reply_markup=lesson_keyboard)

# Lesson selection handler
@dp.message_handler(lambda message: message.text.startswith("Lesson"))
async def select_lesson(message: types.Message):
    try:
        user_id = message.from_user.id
        lang = user_preferences.get(user_id, "en")
        lesson_number = int(message.text.split()[1]) - 1
        await message.answer(lessons[lang][lesson_number])
        if lesson_number == 4:
            await message.answer("Visit our website for more lessons: [yourwebsite.com](http://yourwebsite.com)", parse_mode="Markdown")
    except (IndexError, ValueError):
        await message.answer("Invalid lesson selection.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
