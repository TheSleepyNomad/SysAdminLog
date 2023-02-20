from subprocess import Popen, PIPE
from shutil import disk_usage
from app.config.config import GB

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
        s = _.decode('UTF-8').strip()
        if s.startswith('System Boot Time') or s.startswith('Время загрузки системы'):
            print(s)

