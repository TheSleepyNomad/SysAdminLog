from subprocess import Popen, PIPE
from shutil import disk_usage
from app.config.config import GB
from datetime import datetime, time

def check_disk_free_space():
    # send command in cmd
    with Popen(['fsutil', 'fsinfo', 'drives'], stdout=PIPE) as proc:
        cmd_result = proc.stdout.read().decode('UTF-8').strip()
        # get all computer drivers
        disk_list = []
        for disk in cmd_result[8:].split(' '):
            disk_list.append(disk)
        # generate dict of disk
        disk_dict = {disk: round(disk_usage(disk).free / GB, 2) for disk in disk_list}
        for disk, space in disk_dict.items():
            if space <= 100:
                print(f'Отправляем лог, что на диске {disk} осталось {space} Gb свободного пространства')

def check_os_start_time():
    with Popen(['systeminfo'], stdout=PIPE) as proc:
        a = proc.stdout.readlines()
    
    for _ in a:
        cmd_result = _.decode('UTF-8').strip()
        if cmd_result.startswith('System Boot Time') or cmd_result.startswith('Время загрузки системы'):
            _sep_str = cmd_result[17:-2].strip().split(' ')
            date_str = f'{_sep_str[0][:-1]} {_sep_str[1]}'
            date_from_cmd = datetime.strptime(date_str, '%m/%d/%Y %H:%M:%S')
            current_date = datetime.now()
            if date_from_cmd.date() == current_date.date() and date_from_cmd.time() < current_date.time():
                print('Все хорошо!')
            else:
                print(f'Последний раз компьютер перезагружался {date_from_cmd.date()}')

