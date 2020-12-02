import vk_api
import requests
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

session = requests.Session()
token = '38b60dcff0e7f2091a4d36c4ef30655cad47036013860f7104977b7ed6daeff142ee245ed702dfe3404b3'
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
# try:
#     vk_session.auth(token_only=True)
#     print(vk_session.api_version)
# except vk_api.AuthError as error_msg:
#     print(error_msg)

longpoll = VkBotLongPoll(vk_session, 116472426)
vk = vk_session.get_api()
print(vk_session.api_version)
for event in longpoll.listen():
    print("new event")
    if event.type == VkBotEventType.MESSAGE_NEW and event.object['text']:
    # Слушаем longpoll, если пришло сообщение то:
        if event.object['text'] == 'ты сука?' or event.object['text'] == 'ты чо':  # Если написали заданную фразу
            if event.from_user:  # Если написали в ЛС
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    message='слыш ты чо бля',
                    random_id=random.randint(0, 999999999999999)
                )
            elif event.from_chat:  # Если написали в Беседе
                vk.messages.send(  # Отправляем собщение
                    chat_id=event.chat_id,
                    message='а может ты сука',
                    random_id=random.randint(0, 999999999999999)
                )
