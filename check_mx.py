import csv
import dns.resolver
import os
import sys
import shutil

def divide_line() -> str:
    len_line = shutil.get_terminal_size().columns
    line = '-'*len_line
    return line

def check_mx(domain:str) -> str:
    status = None
    
    try:
        request = dns.resolver.resolve(domain, 'MX')
        resolve = str(request[0].exchange)
        status = 'Домен валиден'
    except Exception as err:
        if 'The DNS query name does not exist:' in str(err):
            status = 'Домен отсутствует'
        else:
            print(f'Error: {err}')

    return status

def processing_source_base(base:str) -> None:
    line = divide_line()
    list_domain = set()

    with open(base, 'r') as file:
        number_domain = 0
        for row in csv.DictReader(file):
            email = row.get('Email')
            domain = None
            if '@' in email and '.' in email.split('@')[1]:domain = email.split('@')[1]
            
            if domain != None and domain not in list_domain:
                list_domain.add(domain)
                number_domain+=1
                status = check_mx(domain=domain) 
           
                print(
                        f'{line}\n'
                        f'[{number_domain}] {email}\t{domain}\n'
                        f'STATUS:\t{status}'
                        )

def main():
    params = sys.argv
    if len(params) == 2 and '.csv' in params[1]:
        file_name = params[1].strip()
        print(f'Имя файла: {file_name}')
        if os.path.exists(file_name):
            processing_source_base(base=file_name)
        else:
            print(f'Файл {file_name} отсутствует!')
    else:
        sys.exit(
                f'Пример использования:\n'
                f'python3 check_mx.py emails.csv'
                )

if __name__ == '__main__':
    main()
