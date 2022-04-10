# Отправка сообщения с нужными параметрами.

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import main_token

tokenApiVk = vk_api.VkApi(token = main_token)

def cmd(user, text, atach, stick, keyboy):
    try:
        tokenApiVk.method('messages.send', {'user_id': user,
                                    'message': text,
                                    'random_id': 0,
                                    'attachment': atach,
                                    'sticker_id': stick,
                                    'keyboard': keyboy})
        return 0
    except:
        return 1
