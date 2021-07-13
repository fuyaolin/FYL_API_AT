"""
    连接数据库
"""
import pymysql
from public.read_config import ReadConfig

class Mysql_Ope():
    def __init__(self):
        pass

    # 连接数据库
    def mysql_ope_connection(self):
        self.conn = pymysql.connect(
            host=ReadConfig().get_ip,
            port=ReadConfig().get_mysql_port,
            user=ReadConfig().get_mysql_user,
            passwd=ReadConfig().get_mysql_passwd,
            db=ReadConfig().get_mysql_database,
            charset=ReadConfig().get_mysql_charset
        )

    # 查询数据库
    def mysql_ope_select(self, select_sql):
        self.mysql_ope_connection()
        self.cursor = self.conn.cursor()
        self.cursor.execute(select_sql)
        self.cursor.fetchone()
        self.mysql_ope_close()

    # 关闭数据库
    def mysql_ope_close(self):
        self.cursor.close()
        self.conn.close()
