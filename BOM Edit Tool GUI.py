# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 17:26:42 2018

@author: 59505
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLineEdit,QLabel, QTextEdit, QFileDialog
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300,300,1200,800)
        self.setWindowTitle('BOM Edit Tool')
        
        self.lb1 = QLabel('BOM Edit Tool',self)     
        self.lb1.move(600,50)
        self.lb2 = QLabel('旧BOM',self)
        self.lb2.move(100,200)
        self.lb3 = QLabel('新BOM',self)
        self.lb3.move(100,400)        
        self.lb4 = QLabel('Copyright © 2019 - 3019 Elias Shi. All Rights Reserved.',self)
        self.lb4.move(650,750)
        
        
        
        
        
        startbt = QPushButton('开始',self)
        startbt.move(200,700)
        qbtn = QPushButton('退出', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.move(400,700)
        
        
        self.bt3 = QPushButton('打开文件',self)
        self.bt3.move(1000,200)
        self.bt4 = QPushButton('打开文件',self)
        self.bt4.move(1000,400)
        
        
        self.tx1 = QTextEdit(self)
        self.tx1.setGeometry(200,200,750,50)
        self.tx2 = QTextEdit(self)
        self.tx2.setGeometry(200,400,750,50)
        
        
        '''
        self.bt3.clicked.connect(self.openfile)
        self.bt3.clicked.connect(self.openfile)
        
    def openfile(self):
        fname = QFileDialog.getOpenFileName(self,'打开文件','./')
        #self.tx1.setText(fname)
       ''' 
        
                     
        
    
        
        self.show()  
  
        
        
if __name__ == '__main__':
    app=0
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    