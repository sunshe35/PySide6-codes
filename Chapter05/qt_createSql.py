from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRecord, QSqlQuery
import sys
import random
import os
os.chdir(os.path.dirname(__file__))

def createRelationalTables():

    query = QSqlQuery()

    query.exec('drop table student2')
    query.exec("create table student2(id int primary key, name varchar(20), sex int, subject int, score float )")

    id = 0
    for name in ['张三','李四','王五','赵六']:
        sex = id %2
        print(sex)
        for subject in range(3):
            id += 1
            score = random.randint(70,100)
            query.exec(f"insert into student2 values({id}, '{name}', {sex}, {subject}, {score})")

    query.exec('drop table sex')
    query.exec("create table sex(id int, name varchar(20))")
    query.exec("insert into sex values(1, '男')")
    query.exec("insert into sex values(0, '女')")

    query.exec('drop table subject')
    query.exec("create table subject(id int, name varchar(20))")
    query.exec("insert into subject values(0, '计算机科学与技术')")
    query.exec("insert into subject values(1, '生物工程')")
    query.exec("insert into subject values(2, '物理学')")


def createDataPandas():
    import pandas as pd
    import random
    import sqlite3

    _list = []
    id = 0
    for name in ['张三', '李四', '王五', '赵六']:
        for namePlus in range(1,9):
            for subject in ['语文', '数学', '外语', '综合']:
                for sex in ['男','女']:
                    name2 = name+str(namePlus)
                    id+=1
                    age = random.randint(20,30)
                    score = round(random.random() * 40 + 60,2)
                    if score >= 80:
                        describe = f'{name2}的{subject}成绩是：优秀'
                    else:
                        describe = f'{name2}的{subject}成绩是：良好'
                    _list.append([id,name2,subject,sex,age,score,describe])
    df = pd.DataFrame(_list, columns=['id','name','subject','sex','age','score','describe'])
    df.set_index('id',inplace=True)

    connect = sqlite3.connect('.\db\database.db')
    df.to_sql('student',connect, if_exists='replace')
    return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./db/database.db')
    # db.setDatabaseName(':memory:')
    if db.open() is not True:
        QMessageBox.critical(QWidget(), "警告", "数据连接失败，程序即将退出")
        exit()

    createDataPandas()
    createRelationalTables()
