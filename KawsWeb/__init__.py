# 用pymysql代替mysqldb 原因：python3不支持mysqldb
import pymysql
pymysql.install_as_MySQLdb()
