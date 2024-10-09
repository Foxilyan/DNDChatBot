from Administrator import Seeker

def associate_char_and_player(message, bot, associations):
    character = Seeker.get_character(Seeker.get_name_from_command(message), bot)
    if character is not None:
        associations[message.from_user.id] = character
        bot.send_message(message.chat.id, f'Игрок {message.from_user.first_name} играет как {character['bio']['имя']}')
        bot.send_message(message.chat.id, str(associations))
        return
    bot.send_message(message.chat.id, 'Персонаж не найден')