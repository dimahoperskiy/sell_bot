import vk_api
import time

while True:
    try:
        def auth_handler():
            key = input("Enter authentication code: ")
            remember_device = True
            return key, remember_device

        def main():
            login, password = '', ''
            vk_session = vk_api.VkApi(login, password, auth_handler=auth_handler)
            try:
                vk_session.auth()
                vk = vk_session.get_api()
                print(vk.wall.post(owner_id='-141601326',
                                   message='Продам бота, который будет постить ваше объявление в эту (или другую) '
                                           'группу каждые 30 (или не 30) минут. Лс',
                                   attachments=['photo164563385_457257393']))
                time.sleep(1800)
            except vk_api.AuthError as error_msg:
                print(error_msg)
                return


        if __name__ == '__main__':
            main()
    except Exception as E:
        time.sleep(1)
