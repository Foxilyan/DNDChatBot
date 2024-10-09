from copy import deepcopy
import json


empty_sheet = {
    'bio': {
        'имя': None
    },
    'статы': {
        'сила': None,
        'ловкость': None,
        'телосложение': None,
        'интеллект': None,
        'мудрость': None,
        'харизма': None
    },
    'спасброски': {
        'спас сила': None,
        'спас ловкость': None,
        'спас телосложение': None,
        'спас интеллект': None,
        'спас мудрость': None,
        'спас харизма': None
    },
    'скиллы': {
        'акробатика': None,
        'расследование': None,
        'атлетика': None,
        'восприятие': None,
        'выживание': None,
        'выступление': None,
        'запугивание': None,
        'история': None,
        'ловкость рук': None,
        'магия': None,
        'медицина': None,
        'обман': None,
        'природа': None,
        'проницательность': None,
        'религия': None,
        'скрытность': None,
        'убеждение': None,
        'уход за животными': None
    }
}


def start_register(message, bot):
    sheet = deepcopy(empty_sheet)
    bot.send_message(message.chat.id, 'Введите имя персонажа')
    bot.register_next_step_handler(message, set_name, sheet, bot)


def set_name(message, sheet, bot):
    name = message.text
    sheet['bio']['имя'] = name
    set_stats(message, sheet, bot)


def set_stats(message, sheet, bot):
    for stats in sheet:
        for stat in sheet[stats]:
            if sheet[stats][stat] is None:
                bot.send_message(message.chat.id, f'Введите значение {stat}')
                bot.register_next_step_handler(message, set_stat, stat, stats, sheet, bot)
                return
    bot.send_message(message.chat.id, str(sheet))
    bot.send_message(message.chat.id, str(empty_sheet))
    with open(f'../Characters/{sheet['bio']['имя']}.json', 'w') as file:
        json.dump(sheet, file, indent=4)


def set_stat(message, stat, stats, sheet, bot):
    try:
        sheet[stats][stat] = int(message.text)
        set_stats(message, sheet, bot)
    except BaseException:
        bot.send_message(message.chat.id, 'Дебил, давай нормально')
        bot.register_next_step_handler(message, set_stat, stat, stats, sheet, bot)