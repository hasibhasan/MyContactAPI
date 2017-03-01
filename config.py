# DATABASE SETTINGS
pg_db_username = 'postgres'
pg_db_password = ''
pg_db_name = 'flask-angularjs-api'
pg_db_hostname = 'localhost'

# MYSQL
mysql_db_username = 'root'
mysql_db_password = ''
mysql_db_name = 'test'
mysql_db_hostname = 'localhost'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# PostgreSQL
# Comment the below string if you are using MySQL or MariaDB
"""SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER=pg_db_username,
                                                                                        DB_PASS=pg_db_password,
                                                                                        DB_ADDR=pg_db_hostname,
                                                                                        DB_NAME=pg_db_name)"""

# MySQL
# Uncomment the below string if you are using MySQL or MariaDB
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER=mysql_db_username,
                                                                                        DB_PASS=mysql_db_password,
                                                                                        DB_ADDR=mysql_db_hostname,
                                                                                        DB_NAME=mysql_db_name)
