"""
    连接数据库
"""
import pymysql
from common.ReadConfigFile import ReadConfig


class MysqlOpe(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host=ReadConfig().get_ip,
            port=ReadConfig().get_mysql_port,
            user=ReadConfig().get_mysql_user,
            passwd=ReadConfig().get_mysql_passwd,
            db=ReadConfig().get_mysql_database,
            charset=ReadConfig().get_mysql_charset
        )
        self.cursor = self.conn.cursor()

    # 增/改/删
    def mysql_ope_other(self, other_sql):
        try:
            self.cursor.execute(other_sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            self.mysql_ope_close()

    # 查
    def mysql_ope_select(self, select_sql):
        self.cursor.execute(select_sql)
        result = self.cursor.fetchall()
        self.mysql_ope_close()
        return result

    # 关闭数据库
    def mysql_ope_close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    sql = "select * from dept"
    MysqlOpe().mysql_ope_select(sql)
