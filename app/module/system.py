from subprocess import Popen, PIPE
from shutil import disk_usage

def check_disk_free_space():
    with Popen(['fsutil', 'fsinfo', 'drives'], stdout=PIPE) as proc:
        a = proc.stdout.read().decode('UTF-8').strip()
        print(a)
        print(round(disk_usage(a[8:]).free / (1024 * 1024 * 1024),2))

def check_os_start_time():
    with Popen(['systeminfo'], stdout=PIPE) as proc:
        a = proc.stdout.readlines()
    
    for _ in a:
        s = _.decode('UTF-8').strip()
        if s.startswith('System Boot Time') or s.startswith('Время загрузки системы'):
            print(s)


check_disk_free_space()