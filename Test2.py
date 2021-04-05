import mysql.connector
import jinja2

connect_args = {"host": "127.0.0.1", "port": 3306, "user": "root", "password": "malloc"}
db1 = mysql.connector.connect(**connect_args)
result = db1.cmd_query("""select * from company.customers""")
result