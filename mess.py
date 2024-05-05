import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7057532692:AAHwUixvbpFE5Zu3mcDAWIXAlkzIhvbQcvo'
offset = -2
counter = 0

def send_message(chat_id, text):
    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}')

def send_sticker(chat_id, sticker_id):
    requests.get(f'{API_URL}{BOT_TOKEN}/sendSticker?chat_id={chat_id}&sticker={sticker_id}')

def send_photo(chat_id, photo_id):
    requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={photo_id}')

def send_audio(chat_id, audio_id):
    requests.get(f'{API_URL}{BOT_TOKEN}/sendAudio?chat_id={chat_id}&audio={audio_id}')

def send_video(chat_id, video_id):
    requests.get(f'{API_URL}{BOT_TOKEN}/sendVideo?chat_id={chat_id}&video={video_id}')

def send_document(chat_id, document_id):
    requests.get(f'{API_URL}{BOT_TOKEN}/sendDocument?chat_id={chat_id}&document={document_id}')

def send_animation(chat_id, animation_id):
    requests.get(f'{API_URL}{BOT_TOKEN}/sendAnimation?chat_id={chat_id}&animation={animation_id}')

while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']

            if 'sticker' in result['message']:
                sticker_id = result['message']['sticker']['file_id']
                send_message(chat_id, 'Стикер!')

            if 'audio' in result['message']:
                audio_id = result['message']['audio']['file_id']
                send_message(chat_id, 'Музыка!')

            if 'video' in result['message']:
                video_id = result['message']['video']['file_id']
                send_message(chat_id, 'Видео!')

            if 'document' in result['message']:
                document_id = result['message']['document']['file_id']
                send_message(chat_id, 'Документ!')

            if 'animation' in result['message']:
                animation_id = result['message']['animation']['file_id']
                send_message(chat_id, 'Анимация!')

            if 'voice' in result['message']:
                voice_id = result['message']['voice']['file_id']
                send_message(chat_id, 'Не люблю слушать голосовые)!')

            if 'text' in result['message']:
                send_message(chat_id, 'Классное сообщение, жаль читать не умею!')

            if 'text' in result['message']:
                text = result['message']['text']
                if '😊' in text or '😃' in text or '😄' in text:
                    send_message(chat_id, 'Улыбнулся! :)')

            if 'video_note' in result['message']:
                video_id = result['message']['video_note']['file_id']
                send_message(chat_id, 'Видеосообщение, прикольно')

            if 'photo' in result['message']:
                photo_sizes = result['message']['photo']
                photo_file_id = photo_sizes[-1]['file_id']
                send_message(chat_id, 'Фото огонь!')

            time.sleep(1)
            counter += 1