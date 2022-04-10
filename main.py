import vk_api
import requests
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.longpoll import VkLongPoll, VkEventType
from config import main_token, questions, bot_id
from methods import sender, actionDB
from keyboards import *
import json
import time

CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app')
tokenApiVk = vk_api.VkApi(token = main_token)
vk_session = tokenApiVk.get_api()
longpoll = VkBotLongPoll(tokenApiVk, bot_id) # Авторизация токена.

users = dict()

def main():
    for event in longpoll.listen(): # Обработчик для личных сообщений бота.
        if event.type == VkBotEventType.MESSAGE_NEW:

            message_text = event.object['message']['text'].lower()
            user_id = event.object['message']['from_id']

            if message_text == 'привет':
                sender.cmd(user_id, 'Привет вездекодерам!', None, None, clean)
                sender.cmd(user_id, questions[0], None, None, k1)

            if message_text in ['нравится', 'не нравится'] and users.get(user_id) != None:
                id = users[user_id]
                if message_text == 'нравится':
                    vote = 1
                    sender.cmd(user_id, 'Записал! (👍)', None, None, None)
                else:
                    vote = 0
                    sender.cmd(user_id, 'Записал! (👎)', None, None, None)
                actionDB.vote(user_id, id, vote)

            if message_text == 'мем' or message_text in ['нравится', 'не нравится'] and users.get(user_id) != None:
                result = actionDB.getPhoto(user_id)
                while result[0] in result[2]:
                    result = actionDB.getPhoto(user_id)

                sender.cmd(user_id, 'Вот твой мем:', result[1], None, first)

                if users.get(user_id) is None: users[user_id] = result[0]
                else: users[user_id] = result[0]


            elif message_text == 'статистика':
                result = actionDB.getData(user_id)
                message = f'Статистика.\nКоличество лайков: {result[0].count(1)}\nКоличество дизлайков: {result[0].count(0)}\n\nПоказаны самые популярные мемы:'
                sender.cmd(user_id, message, ",".join(result[1]), None, None)

        elif event.type == VkBotEventType.MESSAGE_EVENT:

            user_id = event.object.user_id
            new_payload = event.object.payload

            if new_payload.get('type') == '1':
                answer = new_payload.get('answer')
                sender.cmd(user_id, f"Записал ваш ответ: {answer}", None, None, clean)
                sender.cmd(user_id, questions[1], None, None, k2)

            elif new_payload.get('type') == '2':
                answer = new_payload.get('answer')
                sender.cmd(user_id, f"Записал ваш ответ: {answer}", None, None, clean)
                sender.cmd(user_id, questions[2], None, None, k3)

            elif new_payload.get('type') == '3':
                answer = new_payload.get('answer')
                sender.cmd(user_id, f"Записал ваш ответ: {answer}", None, None, clean)
                sender.cmd(user_id, questions[3], None, None, k4)

            elif new_payload.get('type') == '4':
                answer = new_payload.get('answer')
                sender.cmd(user_id, f"Записал ваш ответ: {answer}", None, None, clean)
                sender.cmd(user_id, questions[4], None, None, k5)

            elif new_payload.get('type') == '5':
                answer = new_payload.get('answer')
                sender.cmd(user_id, f"Записал ваш ответ: {answer}", None, None, clean)
                sender.cmd(user_id, questions[5], None, None, k6)

            elif new_payload.get('type') == '6':
                answer = new_payload.get('answer')
                sender.cmd(user_id, 'Я запомнил))', None, None, clean)
                sender.cmd(user_id, questions[6], None, None, k7)

            elif new_payload.get('type') == '7':
                answer = new_payload.get('answer')
                sender.cmd(user_id, f"Записал ваш ответ: {answer}", None, None, clean)
                sender.cmd(user_id, questions[7], None, None, k8)

            elif new_payload.get('type') == '8':
                tokenApiVk.method('messages.sendMessageEventAnswer', {
                    'event_id': event.object.event_id,
                    'user_id': user_id,
                    'peer_id': event.object.peer_id,
                    'event_data': json.dumps({
                        "type": "show_snackbar",
                        "text": "Спасибо за прохождение нашего допроса!"
                    })
                }
                                      )


def handlerExcept():
    if __name__ == '__main__':
        try:
            main()
        except requests.exceptions.ConnectionError:
            time.sleep(2)
            handlerExcept()
        except requests.exceptions.ReadTimeout:
            time.sleep(2)
            handlerExcept()
if __name__ == '__main__':
    handlerExcept()
