import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import mysql.connector
import pandas as pd
import openpyxl


from_class = uic.loadUiType("editor.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__() # 부모클래스 생성자 실행
        self.setupUi(self)
        self.setWindowTitle("SQL MAKER!")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.btnConnect.clicked.connect(self.connectDB)
        self.btnSee.clicked.connect(self.SeeTable)
        self.btnTable.clicked.connect(self.showTable)
        self.btnMkTable.clicked.connect(self.tableOpenFile)
        self.make_it.clicked.connect(self.make_table)
        self.btnDel.clicked.connect(self.del_table)
        self.btnInsert.clicked.connect(self.insert_data)
        self.progressBar.valueChanged.connect(self.printValue)

    
    
    def printValue(self):
        pass
    

    def insert_data(self):
        items = []
        for result_iterator in self.result:
            items.append(result_iterator[0])

        item, ok = QInputDialog.getItem(self, 'QInputDialog - insert data',
                                            'table:', items, 0, False)

        if ok and item:
            stra = item
        
        name = QFileDialog.getOpenFileName(self)[0]
        if name[-3:] == "csv":
            try:
                df = pd.DataFrame(pd.read_csv(name))
            except:
                df = pd.DataFrame(pd.read_csv(name, encoding='EUC-KR'))
            
        
        elif name[-4:] == "xlsx":
            try:
                df = pd.DataFrame(pd.read_excel(name))
            except:
                df = pd.DataFrame(pd.read_excel(name, encoding='EUC-KR'))

        df = df.fillna(0)
        x_count = df.shape[1]
        sql2 = "insert into " + stra + " values ("
        for i in range(x_count):
            sql2 = sql2 + " %s"
            if(i != x_count -1):
                sql2 = sql2 + ", "
        sql2 = sql2 + " );"    

        
        count = 0
        cal = 1
        max = 100


        for i, row in df.iterrows():
            self.cursor.execute(sql2, tuple(row))
            self.local.commit()
            count += 1
            if count >= len(df)/max * cal:
                self.progressBar.setValue(cal)
                cal += 1;

        self.progressBar.setValue(100)

        while (self.show_table.rowCount() > 0):
           self.show_table.removeRow(0)

        self.cursor.execute(" show columns from " + stra)

        columns_list = []
        result = self.cursor.fetchall()
        for row in result:
            row[0].replace("(", "")
            row[0].replace("'", "")
            columns_list.append(row[0])
    

        self.show_table.setColumnCount(len(columns_list))
        self.show_table.setHorizontalHeaderLabels(each for each in columns_list)

        self.cursor.execute("select *  from " + stra)

        result1 = self.cursor.fetchall()
        for i in range(len(result1)):
            row = self.show_table.rowCount()
            self.show_table.insertRow(row)
            for j in range(len(columns_list)):
                self.show_table.setItem(row, j, QTableWidgetItem(str(result1[i][j])))

        

        


        


    def del_table(self):
        items = []
        for result_iterator in self.result:
            items.append(result_iterator[0])

        item, ok = QInputDialog.getItem(self, 'QInputDialog - table',
                                            'table:', items, 0, False)

        if ok and item:
            stra = item

        sql2 = "drop table " + stra
        self.cursor.execute(sql2)
        self.SeeTable()
        
        while (self.show_table.rowCount() > 0):
           self.show_table.removeRow(0)

        

        


        

    def make_table(self):
        self.cursor.execute(self.sql)
        #self.state_line_2.setText(" )
        self.textEdit.setText("success make table!! name : " + self.table_name)
        self.SeeTable()

        self.cursor.execute(" show columns from " + self.table_name)

        columns_list = []
        result = self.cursor.fetchall()
        for row in result:
            row[0].replace("(", "")
            row[0].replace("'", "")
            columns_list.append(row[0])
    

        self.show_table.setColumnCount(len(columns_list))
        self.show_table.setHorizontalHeaderLabels(each for each in columns_list)

        self.cursor.execute("select *  from " + self.table_name)

        result1 = self.cursor.fetchall()
        for i in range(len(result1)):
            row = self.show_table.rowCount()
            self.show_table.insertRow(row)
            for j in range(len(columns_list)):
                self.show_table.setItem(row, j, QTableWidgetItem(str(result1[i][j])))



    def tableOpenFile(self):
        name = QFileDialog.getOpenFileName(self)[0]
        if name[-3:] == "csv":
            try:
                df = pd.DataFrame(pd.read_csv(name))
            except:
                df = pd.DataFrame(pd.read_csv(name, encoding='EUC-KR'))
            
        
        elif name[-4:] == "xlsx":
            try:
                df = pd.DataFrame(pd.read_excel(name))
            except:
                df = pd.DataFrame(pd.read_excel(name, encoding='EUC-KR'))

        df_list = df.columns.values.tolist()
        text, ok = QInputDialog.getText(self, 'make table', 'table name :')
        if ok and text:
            self.table_name = text

        table_type_list = []
        df_type = pd.DataFrame(
                        {'int' : ['1'],
                         'float' : ['1.0'],
                         'date' : ['2022-11-07'],
                         'object' : ["string"]
                       }) 
        df_type = df_type.astype({'int':'int'})
        df_type = df_type.astype({'float':'float'})

        for each in range(len(df_list)):
            for i in range(len(df_type)):
                if df[df_list[each]].dtype == df_type['int'].dtype:
                    table_type_list.append("int")
                elif df[df_list[each]].dtype == df_type['float'].dtype:
                    table_type_list.append("float")
                elif df[df_list[each]].dtype == df_type['object'].dtype:
                    table_type_list.append("varchar(100)")
        
        self.sql = "create table " + self.table_name + "\n" + \
                "("

        for i in range(len(df_list)):
                    self.sql = self.sql +" `" + df_list[i] + "` " + table_type_list[i]
                    if(i != len(df_list)-1):
                        self.sql = self.sql + "," + "\n"
        self.sql = self.sql + " );"

        self.textEdit.setText("check sql code \n\n" + self.sql)



    def connectDB(self):
        print("연결")
        try:
            fun_local = mysql.connector.connect(
            host = self.Uhost_line.text(),
            port = 3306,
            user = self.Uname_line.text(),
            password = self.Upassword_line.text(),
            database = self.Udatabase_line.text()
            )
            
            self.state_line.setText("YES!")
            self.local = fun_local #self 쓰면 클래스내에서 사용가능
            self.cursor = fun_local.cursor(buffered=True)
            self.SeeTable()
            

        except:
            self.state_line.setText("NO!")
    
    def SeeTable(self):
        sql_sea = "show tables"
        self.cursor.execute(sql_sea)
        self.result = self.cursor.fetchall()
        while (self.tableWidget.rowCount() > 0):
           self.tableWidget.removeRow(0)
        for result_iterator in self.result:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(result_iterator[0]))
        

    def showTable(self):
        items = []
        for result_iterator in self.result:
            items.append(result_iterator[0])

        item, ok = QInputDialog.getItem(self, 'QInputDialog - table',
                                            'table:', items, 0, False)

        if ok and item:
            stra = item
            self.se_ta.setText(item)

        while (self.show_table.rowCount() > 0):
           self.show_table.removeRow(0)

        # select * from table
        self.cursor.execute(" show columns from " + stra)

        columns_list = []
        result = self.cursor.fetchall()
        for row in result:
            row[0].replace("(", "")
            row[0].replace("'", "")
            columns_list.append(row[0])
    

        self.show_table.setColumnCount(len(columns_list))
        self.show_table.setHorizontalHeaderLabels(each for each in columns_list)

        self.cursor.execute("select *  from " + stra)

        result1 = self.cursor.fetchall()
        for i in range(len(result1)):
            row = self.show_table.rowCount()
            self.show_table.insertRow(row)
            for j in range(len(columns_list)):
                self.show_table.setItem(row, j, QTableWidgetItem(str(result1[i][j])))

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myWindows = WindowClass()
    
    myWindows.show()
    
    sys.exit(app.exec_())
