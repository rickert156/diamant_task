import os
import sys
import telegram
from config import TOKEN_BOT, CHAT_ID
from check_mx import divide_line

def send_text(message_text:str):
    bot = telegram.Bot(token=TOKEN_BOT)
    bot.send_message(chat_id=CHAT_ID, text=message_text)

def read_file(file_name:str) -> str | None:
    text = None
    try:
        with open(file_name, 'r') as file:
            text = file.read().strip()
    except Exception as err:
        print(f'Error: {err}')

    return text

def main():
    line = divide_line()
    params = sys.argv
    if len(params) == 2 and '.txt' in params[1]:
        if os.path.exists(params[1].strip()):
            file_name = params[1].strip()
            print(f'Файл {file_name} обнаружен')
            text = read_file(file_name=file_name)
            print(
                    f'\nТекст файла {file_name}\n'
                    f'{line}\n'
                    f'{text}\n'
                    f'{line}'
            )
            send_text(message_text=text)
        else:
            print(f'Файл {params[1].strip()} не обнаружен')
        
    else:
        print(
                f'Пример использования\n'
                f'python3 telegram_private_chat.py text.txt'
                )

if __name__ == '__main__':
    main()
