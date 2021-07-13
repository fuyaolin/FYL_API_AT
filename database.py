
from public.read_config import ReadConfig

MySQL_conf = {
    'host': ReadConfig().get_ip,
    'port':30006,
    'database': 'AnyRobot',
    'user': 'root',
    'password': 'eisoo.com',
    'charset': 'utf8'
}

