
from public.read_config import ReadConfig

MySQL_conf = {
    'host': ReadConfig().get_ip,
    'port':30006,
    'database': 'xxx',
    'user': 'root',
    'password': 'xxx',
    'charset': 'utf8'
}

