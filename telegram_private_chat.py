import os
import sys
from check_mx import divide_line

def read_file(file_name:str) -> str | None:
    text = None
    try:
        line = divide_line()
        with open(file_name, 'r') as file:
            text = file.read().strip()
        print(
                f'\nТекст файла {file_name}\n'
                f'{line}\n'
                f'{text}\n'
                f'{line}'
            )
    except Exception as err:
        print(f'Error: {err}')

    return text

def main():
    params = sys.argv
    if len(params) == 2 and '.txt' in params[1]:
        if os.path.exists(params[1].strip()):
            file_name = params[1].strip()
            print(f'Файл {file_name} обнаружен')
            read_file(file_name=file_name)
        else:
            print(f'Файл {params[1].strip()} не обнаружен')
        
    else:
        print(
                f'Пример использования\n'
                f'python3 telegram_private_chat.py text.txt'
                )

if __name__ == '__main__':
    main()
