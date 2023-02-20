from subprocess import Popen, PIPE

# main tasks
# check disk free space
# check os start time
# check sql backup exist
# send logs to owner
# create excel list from database data

def check_config_file_exist():
    pass

def check_disk_free_space():
    pass

def check_os_start_time():
    with Popen(['systeminfo'], stdout=PIPE) as proc:
        a = proc.stdout.readlines()
    
    for _ in a:
        s = _.decode('UTF-8').strip()
        if s.startswith('System Boot Time') or s.startswith('Время загрузки системы'):
            print(s)

def check_sql_backup_exist():
    pass

if __name__ == '__main__':
    pass