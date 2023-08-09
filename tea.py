import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


TOKEN = "vk1.a.hEEDGvZeT662vl6cm84AG7Pp-DlAnUnBfuN9GniNo0v1CldwaUG64n_mFk_uueI4BjNEDJAObcDr4yXHOev-t28jDCmhjXwC6tTPfyS46xYBwzvSp6O9GCSHfpQEHblDUQkWQ0q2vJqaJQquMoMEoZuTbGMRKOesntWUsAwJcpRoA8k12wZzUTY7Rqr6eCGBP8YI1uwJDOXlJCbpHDPu1w"

vk_session = vk_api.VkApi(token=TOKEN)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def send_some_msg(id, msg):
    vk_session.method("messages.send", {"user_id": id, "message":msg, "random_id":0})



for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text
            id = event.user_id
            send_some_msg(id, msg)



