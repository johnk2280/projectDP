from PyQt5 import QtSql, QtWidgets
import pandas as pd


class MyDB:
    def __init__(self):
        self.create_connection()
        self.select_builders()

    def create_connection(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('../create_db/projectDP.db')
        self.db.open()

        if not self.db.isOpen():
            return f'Connection not established.'

        print(self.db.tables())

    def select_builders(self):
        query = QtSql.QSqlQuery()
        query.exec_('SELECT * FROM builders')
        lst = []
        if query.isActive():
            query.first()
            while query.isValid():
                lst.append(str(query.value('id')) + ': ' + query.value('title') + ': ' + str(query.value('inn')))
                query.next()

            for el in lst:
                print(el)

        self.db.close()

        print(query)


mydb = MyDB()
# mydb.create_connection()
# mydb.select_builders()
