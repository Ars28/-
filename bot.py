import telebot
from telebot import types
from telegram import *
import sqlite3

counter = 0
secCounter = 0

def addProject(a,b,c,d,e,f):
    connection = sqlite3.connect('Slaves.db')
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?)",(a,b,c,d,e,f))
    connection.commit()
    connection.close()

def deleteProject(a):
    connection = sqlite3.connect('Slaves.db')
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM projects WHERE project_id = ?",(a,))
    connection.commit()
    connection.close()

def updateProject(a,b,c,d,e):
    connection = sqlite3.connect('Slaves.db')
    cursor = connection.cursor()
    cursor.execute(f"UPDATE projects SET name=?, idea=?, needed_skills=?, information=? WHERE project_id=?",(a,b,c,d,e))
    connection.commit()
    connection.close()

def showProject(mes):
    connection = sqlite3.connect('Slaves.db')
    cursor = connection.cursor()
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton("Меню")
    markup.add(btn1)
    cursor.execute("SELECT active FROM projects")
    x = cursor.fetchone()
    if x[0] == 1:
        cursor.execute("SELECT name, idea, information, needed_skills FROM projects")
        listOfProjects = cursor.fetchall()
        l = ''
        for i in listOfProjects:
            for j in i:
                l = l + str(j) + '\n'
                l += '\n'
            l = l[:-1] + 'Статус:🟢Активно'
        listOfProjects = l
    else:
        cursor.execute("SELECT name, idea, information, needed_skills FROM projects")
        listOfProjects = cursor.fetchall()
        l = ''
        for i in listOfProjects:
            for j in i:
                l = l + str(j) + '\n'
                l += '\n'
            l = l[:-1] + 'Статус:🔴Неактивно'
        listOfProjects = l
    connection.commit()
    connection.close()
    bot.send_message(mes.chat.id, text=str(listOfProjects), reply_markup=markup)

def changeStatus(a):
    connection = sqlite3.connect('Slaves.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT active FROM projects WHERE project_id = {int(a)}")
    x = cursor.fetchone()
    print(x)
    if x[0] == 1:
        cursor.execute(f"UPDATE projects SET active = 0 WHERE project_id = {int(a)}")
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton("Меню")
        markup.add(btn1)
        bot.send_message(a, text="Теперь ваше заявление неактивно", reply_markup=markup)
    else:
        cursor.execute(f"UPDATE projects SET active = 1 WHERE project_id = {int(a)}")
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton("Меню")
        markup.add(btn1)
        bot.send_message(a, text="Теперь ваше заявление активно", reply_markup=markup)
    connection.commit()
    connection.close()

def addEmployee(a,b,c,d,e,f):
    connection = sqlite3.connect('Slaves.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)",(a,b,c,d,e,f))
    connection.commit()
    connection.close()

def deleteEmployee(a):
    connection = sqlite3.connect('Slaves.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = ?",(a,))
    connection.commit()
    connection.close()

def updateEmployee(a,b,c,d,e,f):
    connection = sqlite3.connect('Slaves.db')
    cursor = connection.cursor()
    cursor.execute(f"UPDATE projects SET phone=?, mail=?, telegram=?, information=?, skills=? WHERE user_id=?",(a,b,c,d,e,f))
    connection.commit()
    connection.close()

def showEmployee(mes):
    connection = sqlite3.connect('Slaves.db')
    cursor = connection.cursor()
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton("Меню")
    markup.add(btn1)
    cursor.execute("SELECT phone, mail, telegram, information, skills FROM users")
    listOfEmployee = cursor.fetchall()
    l = ''
    for i in listOfEmployee:
        for j in i:
            l = l + str(j) + '\n'
            l += '\n'
    listOfEmployee = l[:-1]
    connection.commit()
    connection.close()
    bot.send_message(mes.chat.id, text=str(listOfEmployee), reply_markup=markup)

BotToken = '6701532409:AAG7NaySQo1zX941ZvX-VXrq1cRzZ98AQsc'
bot = telebot.TeleBot(BotToken, parse_mode='HTML')

def pInf(mes):
    global information
    information = mes.text
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton("Завершить")
    btn2=types.KeyboardButton("Меню")
    markup.add(btn1, btn2)
    bot.send_message(mes.chat.id, text='Нажмите "Завершить", чтобы сохранить данные', reply_markup=markup)

def pIdea(mes):
    global idea
    idea = mes.text
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton("Далее")
    btn2=types.KeyboardButton("Меню")
    markup.add(btn1, btn2)
    bot.send_message(mes.chat.id, text='Нажмите "Далее", чтобы продолжить', reply_markup=markup)

def pName(mes):
    global name
    name = mes.text
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton("Далее")
    btn2=types.KeyboardButton("Меню")
    markup.add(btn1, btn2)
    bot.send_message(mes.chat.id, text='Нажмите "Далее", чтобы продолжить', reply_markup=markup)

def setPhone(mes):
    global phone
    phone = mes.text
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton("Продолжить")
    btn2=types.KeyboardButton("Меню")
    markup.add(btn1, btn2)
    bot.send_message(mes.chat.id, text='Продолжить?', reply_markup=markup)

def setMail(mes):
    global mail
    mail = mes.text
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton("Сохранить")
    btn2=types.KeyboardButton("Меню")
    markup.add(btn1, btn2)
    bot.send_message(mes.chat.id, text='Сохранить этот адрес электронной почты?', reply_markup=markup)

def setTel(mes):
    global tel
    tel = mes.text
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types.KeyboardButton("Сохранить")
    btn2=types.KeyboardButton("Меню")
    markup.add(btn1, btn2)
    bot.send_message(mes.chat.id, text='Сохранить этот ник?', reply_markup=markup)

ni2 = ''
def m(t):
    global ni2
    ni2 = str(t.text)
    pmarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1=types.KeyboardButton('Подтвердить')
    pmarkup.add(b1)
    bot.send_message(t.chat.id, text='Подтвердить внесение информации?', reply_markup=pmarkup)

ni1 = None
ni3 = []
def skillsCounter(t):
    global ni3
    if t.text != 'Закончить':
        ni3.append(str(t.text))
    pmarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1=types.KeyboardButton('Добавить ещё')
    b2=types.KeyboardButton('Закончить')
    pmarkup.add(b1, b2)
    bot.send_message(t.chat.id, text='Добавить ещё навыки?', reply_markup=pmarkup)

pSkills = []
def missSkillsCounter(t):
    global pSkills
    if t.text != 'Закончить':
        pSkills.append(str(t.text))
    pmarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1=types.KeyboardButton('Добавить ещё')
    b2=types.KeyboardButton('Закончить')
    pmarkup.add(b1, b2)
    bot.send_message(t.chat.id, text='Добавить ещё навыки?', reply_markup=pmarkup)

@bot.message_handler(commands=['start'])
def send_welcome(message):
   markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
   btn1=types.KeyboardButton('Стартапы МАИ')
   btn2=types.KeyboardButton('Для стартаперов')
   btn3=types.KeyboardButton('Для соискателей')
   markup.add(btn1, btn2, btn3)
   bot.reply_to(message, "Приветствую! Я - Ваш помощник для реализации проектов на территории МАИ. Что Вас интересует?".format(message.from_user), reply_markup=markup)



@bot.message_handler(content_types=['text'])
def rep(message):
    global ni2, ni3, pSkills, secCounter, updater, employeeUpdater
    if message.text == 'Стартапы МАИ':
        global counter
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton("3D-моделирование")
        btn2=types.KeyboardButton("Энергетика, теплотехника и управление")
        btn3=types.KeyboardButton("Бизнес-аналитика (BI-разработчик)")
        btn4=types.KeyboardButton("Data-scientist")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Вот все стартапы, организуемые непосредственно Московским Авиационным Институтом'.format(message.from_user), reply_markup = markup)
    elif message.text == 'Для стартаперов':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton("Добавить свой стартап в базу")
        btn2=types.KeyboardButton("Редактировать свой стартап")
        btn3=types.KeyboardButton("Удалить свой стартап")
        btn4=types.KeyboardButton("Соискатели, ищущие новые стартапы")
        btn5=types.KeyboardButton("Изменить статус")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, 'Здесь Вы можете проверить, находятся ли студенты с нужными вам навыками в поиске новых проектов или добавть свой проект в базу данных, чтобы новые соискатели могли с Вами контактировать. Вы также можете моенять статус вашего заявления, в случае, если вы больше не ищете новых сотрудников, или, наоборот, Вам снова нужны новые люди в команду'.format(message.from_user), reply_markup = markup)
    elif message.text == 'Для соискателей':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton("Стартапы, нуждающиеся в новых кадрах")
        btn2=types.KeyboardButton("Добавить себя в список соискателей")
        btn3=types.KeyboardButton("Редактировать свою информацию")
        btn4=types.KeyboardButton("Удалить свою информацию")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Вы можете посмотреть список существующих стартапов, либо добавить себя в список соискателей, ищущих новые проекты. Так новые команды смогут контактировать с вами на начальном этапе, чтобы вместе работать над инновационными проектами'.format(message.from_user), reply_markup = markup)
    elif message.text == '3D-моделирование':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton("Меню")
        markup.add(btn1)
        bot.send_message(message.chat.id, '🖥 <a href="https://my.mai.ru/job/583/">3D-моделирование</a> и проект "VR/AR разработка".\nЕсли тебя заинтересовало направление, читай требования и оставляй свой отклик на <a href="https://my.mai.ru/job/">Цифровой кадровой платформе</a>. По всем вопросам можно обратиться к Анастасии в личные сообщения телеграмма @npv29'.format(message.from_user), reply_markup = markup)
    elif message.text == 'Энергетика, теплотехника и управление':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton("Меню")
        markup.add(btn1)
        bot.send_message(message.chat.id, text='🖲 <a href="https://my.mai.ru/job/574/">Энергетика, теплотехника и проектное управление</a> в проект "Криогенная энергетика".\nЕсли тебя заинтересовало направление, читай требования и оставляй свой отклик на <a href="https://my.mai.ru/job/">Цифровой кадровой платформе</a>. По всем вопросам можно обратиться к Анастасии в личные сообщения телеграмма @npv29', reply_markup = markup)
    elif message.text == 'Бизнес-аналитика (BI-разработчик)':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton("Меню")
        markup.add(btn1)
        bot.send_message(message.chat.id, text='⭐️ <a href="https://my.mai.ru/cabinet/vacancy/582/">Бизнес-аналитика (BI-разработчик)</a> в проект "Создание систем предиктивного обслуживания".\nЕсли тебя заинтересовало направление, читай требования и оставляй свой отклик на <a href="https://my.mai.ru/job/">Цифровой кадровой платформе</a>. По всем вопросам можно обратиться к Анастасии в личные сообщения телеграмма @npv29', reply_markup = markup)
    elif message.text == 'Data-scientist':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton("Меню")
        markup.add(btn1)
        bot.send_message(message.chat.id, text='🗂 <a href="https://my.mai.ru/job/584/">Data-scientist</a> в проект "VR/AR разработка".\nЕсли тебя заинтересовало направление, читай требования и оставляй свой отклик на <a href="https://my.mai.ru/job/">Цифровой кадровой платформе</a>. По всем вопросам можно обратиться к Анастасии в личные сообщения телеграмма @npv29', reply_markup = markup)
    elif message.text == 'Удалить свой стартап':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1=types.KeyboardButton('Удалить')
        b2=types.KeyboardButton('Меню')
        markup.add(b1, b2)
        m2 = bot.send_message(message.chat.id,'Вы действительно хотите удалить свой стартап из нашей базы данных? Если нет, нажмите кномпку "меню"', reply_markup=markup)
    elif message.text == 'Удалить':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1=types.KeyboardButton('Меню')
        markup.add(b1)
        m2 = bot.send_message(message.chat.id,'Данные успешно удалены', reply_markup=markup)
        deleteProject(int(message.chat.id))
    elif message.text == 'Удалить свою информацию':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1=types.KeyboardButton('Убрать')
        b2=types.KeyboardButton('Меню')
        markup.add(b1, b2)
        m2 = bot.send_message(message.chat.id,'Вы действительно хотите убрать свои данные из нашей базы? Если нет, нажмите кномпку "меню"', reply_markup=markup)
    elif message.text == 'Убрать':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1=types.KeyboardButton('Меню')
        markup.add(b1)
        m2 = bot.send_message(message.chat.id,'Данные успешно удалены', reply_markup=markup)
        deleteEmployee(int(message.chat.id))
    elif message.text == 'Стартапы, нуждающиеся в новых кадрах':
        try:
            showProject(message)
        except:
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1=types.KeyboardButton("Меню")
            markup.add(btn1)
            bot.send_message(message.chat.id, text='К сожалению, в нашу базу не добавили ни одного проекта :(', reply_markup=markup)
    elif message.text == 'Добавить себя в список соискателей' or (message.text == 'Добавить ещё' and counter == 0) or message.text == 'Редактировать свою информацию':
        if message.text == 'Редактировать свою информацию':
            employeeUpdater = 1
        else:
            employeeUpdater = 0
        skillsMarkup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1=types.KeyboardButton('Программирование')
        b2=types.KeyboardButton('Дизайн')
        b3=types.KeyboardButton('Аналитика')
        b4=types.KeyboardButton('Маркетинг')
        b5=types.KeyboardButton('Менеджмент')
        b6=types.KeyboardButton('Закончить')
        skillsMarkup.add(b1, b2, b3, b4, b5, b6)
        m2 = bot.send_message(message.chat.id,'Выберите навыки которыми владеете', reply_markup=skillsMarkup)
        bot.register_next_step_handler(m2, skillsCounter)
    elif message.text == 'Закончить' and counter == 0:
        m3 = bot.send_message(message.chat.id, 'Укажте полный номер вашего телефона', reply_markup=None)
        bot.register_next_step_handler(m3, setPhone)
    elif message.text == 'Продолжить':
        m4 = bot.send_message(message.chat.id, 'Укажите свою электронную почту', reply_markup=None)
        bot.register_next_step_handler(m4, setMail)
    elif message.text == 'Сохранить' and secCounter == 0:
        m5 = bot.send_message(message.chat.id, 'Укажите свой ник в телеграм (@petiya_petiachkin)', reply_markup=None)
        bot.register_next_step_handler(m5, setTel)
        secCounter = 1
    elif message.text == 'Сохранить' and secCounter == 1:
        m1 = bot.send_message(message.chat.id,'Пожалуйста, расскажите о себе', reply_markup=None)
        bot.register_next_step_handler(m1, m)
        u = ''
        for i in ni3:
            u = u + str(i) + '\n'
        ni3 = u
        ni2 = str(ni2)
    elif message.text == 'Подтвердить':
        try:
            ni1 = message.chat.id
            ni2 = str(ni2)
            if employeeUpdater:
                updateEmployee(phone, mail, tel, ni2, ni3, message.chat.id)
            else:
                addEmployee(ni1, phone, mail, tel, ni2, ni3)
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1=types.KeyboardButton("Меню")
            markup.add(btn1)
            bot.send_message(message.chat.id, text='Данные сохранены', reply_markup=markup)
            ni2 = ''
            ni3 = []
        except:
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1=types.KeyboardButton("Меню")
            markup.add(btn1)
            bot.send_message(message.chat.id, text='А вы уже зарегистрированы', reply_markup=markup)
    elif message.text == 'Соискатели, ищущие новые стартапы':
        try:
            showEmployee(message)
        except:
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1=types.KeyboardButton("Меню")
            markup.add(btn1)
            bot.send_message(message.chat.id, text='К сожалению, сейчас нет активных соискателей :(', reply_markup=markup)
    elif message.text == 'Добавить свой стартап в базу' or message.text == 'Редактировать свой стартап':
        counter = 0
        updater = 0
        if message.text == 'Редактировать свой стартап':
            updater = 1
        global prId
        prId = message.chat.id
        m6 = bot.send_message(message.chat.id, text='Введите название Вашего проекта')
        bot.register_next_step_handler(m6, pName)
    elif message.text == 'Далее' and counter == 0:
        counter = 1
        m7 = bot.send_message(message.chat.id, text='Опишите идею Вашего проекта')
        bot.register_next_step_handler(m7, pIdea)
    elif message.text == 'Далее' and counter == 1 or (message.text == 'Добавить ещё' and counter == 2):
        counter = 2
        skillsMarkup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1=types.KeyboardButton('Программирование')
        b2=types.KeyboardButton('Дизайн')
        b3=types.KeyboardButton('Аналитика')
        b4=types.KeyboardButton('Маркетинг')
        b5=types.KeyboardButton('Менеджмент')
        b6=types.KeyboardButton('Закончить')
        skillsMarkup.add(b1, b2, b3, b4, b5, b6)
        m8 = bot.send_message(message.chat.id, text='Укажите ключевые навыки, необходимые для завершения проекта, которых нет в вашей команде', reply_markup=skillsMarkup)
        bot.register_next_step_handler(m8, missSkillsCounter)
    elif message.text == 'Закончить' and counter == 2:
        counter = 3
        m9 = bot.send_message(message.chat.id, text='Как и с кем нужно связаться, чтобы попасть к вам в команду?')
        bot.register_next_step_handler(m9, pInf)
    elif message.text == 'Завершить' and counter == 3:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton("Меню")
        markup.add(btn1)
        k = ''
        for i in pSkills:
            k = k + str(i) + '\n'
        pSkills = k
        if updater:
            updateProject(name, idea, pSkills, information, message.chat.id)
        else:
            addProject(prId, name, idea, pSkills, information, 1)
        bot.send_message(message.chat.id, text='Данные сохранены', reply_markup=markup)
        updater = 0
        counter = 0
    elif message.text == 'Изменить статус':
        changeStatus(message.chat.id)
    elif message.text == 'Меню':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton('Стартапы МАИ')
        btn2=types.KeyboardButton('Для стартаперов')
        btn3=types.KeyboardButton('Для соискателей')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text='Что-то ещё?', reply_markup = markup)


bot.infinity_polling()