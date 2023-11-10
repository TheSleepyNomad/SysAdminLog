import subprocess
from locale import getlocale
from json import dumps
from datetime import datetime
import re


def get_os_language() -> str:
    """
    Определяет язык операционной системы и возвращает команду для cmd
    """

    if getlocale()[0] == 'English_United States':
        cmd_command = 'systeminfo | find "System Boot Time"'
    else:
        cmd_command = 'systeminfo | find "Время загрузки системы"'

    return cmd_command


def get_system_boot_time(command: str) -> datetime:
    result = subprocess.Popen(command, 
                              shell=True, 
                              stdout=subprocess.PIPE, 
                              encoding='utf-8', 
                              creationflags=subprocess.CREATE_NEW_CONSOLE)
    
    date = ''
    for data in result.stdout:
        date = data

    date_from_systeminfo = re.search('\d{1,2}/\d{1,2}/\d{4}', date).group(0)
    datetime_from_systeminfo = datetime.strptime(date_from_systeminfo, '%m/%d/%Y')

    return datetime_from_systeminfo


def compare_dates(date: datetime) -> str:
    current_date = datetime.date(datetime.now())

    if date == datetime.date(datetime.now()):
        return f'Перезагрузка была: Текущая дата {current_date.strftime("%d/%m/%Y")}, а дата последней перезагрузки {date.strftime("%d/%m/%Y")}'
    else:
        return f'Перезагрузки не было: Текущая дата {current_date.strftime("%d/%m/%Y")}, а дата последней перезагрузки {date.strftime("%d/%m/%Y")}'


def create_json_log(msg: str):
    with open('server_status_date.json', 'w', encoding='utf-8') as file:
        file.write(dumps({'name': 'server status', 'msg': msg}))


def check_server_restart():
    cmd = get_os_language()
    date = get_system_boot_time(cmd)
    msg = compare_dates(date)
    create_json_log(msg)


check_server_restart()
