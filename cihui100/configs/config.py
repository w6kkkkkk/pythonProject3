import pymysql

#学生账号
# NAME_PSW = {'username':'zdh5','password':'zzzzhujingjing123'}
# NAME_PSW = {'username':'老师1','password':'123456'}

url1 = 'http://tomcat4.kouyu100.com/dc100p'
NAME_PSW = {'username':'zdh2','password':'zzzzhujingjing123'}
NAME_PSW_teacher = {'username':'zdht','password':'123456'}

NAME_PSW1 = {'username':'卢佳音','password':'123456'}
NAME_PSW2 = {'username':'张潇尹','password':'123456'}
NAME_PSW3 = {'username':'金志洋','password':'123456'}
NAME_PSW4 = {'username':'刘锦瑞','password':'123456'}
NAME_PSW5 = {'username':'杨亮','password':'123456'}

#数据库
class py_mysql():
    #线上库
    # db = pymysql.connect(
    #     host='rm-bp18or1ukeb1y70d4jo.mysql.rds.aliyuncs.com',
    #     port=3306,
    #     user='testgroup',
    #     password='ZtYCyKaWNO0S',
    #     database='kouyu100_dctj',
    #     charset='utf8'
    # )
    db = pymysql.connect(
        host='rm-bp1rngw0n26j0smjj7o.mysql.rds.aliyuncs.com',
        port=3306,
        user='testgroup',
        password='ZtYCyKaWNO0S',
        database='kouyu100_dctj',
        charset='utf8'
    )
    def mysql(self,sql=None):

        cursor = py_mysql.db.cursor()
        cursor.execute(sql)
        data=cursor.fetchone()

        #data1=cursor.fetchall()
        print(data)
        #print(data1)
        # cursor.close()

        return data

    def mysql1(self,sql=None):

        cursor = py_mysql.db.cursor()
        cursor.execute(sql)
        data1=cursor.fetchall()

        return data1