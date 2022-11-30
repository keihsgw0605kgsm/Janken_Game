#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import random
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
  
# Create an PyQT4 application object.
a = QApplication(sys.argv)
  
# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget()

# Set window size.
w.resize(540, 400)

# Set window title
w.setWindowTitle("じゃんけんゲーム")
 
# Text
labelA = QLabel(w)
labelB = QLabel(w)
labelA.setText("じゃーんけん")
labelA.move(0, 30)
labelA.setAlignment(Qt.AlignHCenter)
#label.resize(label.sizeHint())
labelA.resize(540,300)


def show_fig(path: str):
    pixmap = QPixmap(path)
    pixmap_resized = pixmap.scaled(200, 300, Qt.KeepAspectRatio)
    labelB.setPixmap(pixmap_resized)
    #labelB.setAlignment(Qt.AlignHCenter)
    labelB.move(160, 80)

 
def on_click(num):
    comHand = random.randint(0,2)
    if comHand == 0:
        str = "グー"
        show_fig("figs/gu.png")
    elif comHand == 1:
        str = "チョキ"
        show_fig("figs/choki.png")
    else:
        str = "パー"
        show_fig("figs/pa.png")
 
    if comHand == num:
        result = "あいこ"
    elif ( (comHand == 0 and num == 2) or (comHand == 1 and num == 0) or (comHand == 2 and num == 1) ):
       result = "あなたの勝ち"
    else:
        result = "あなたの負け"
 
    labelA.setText("ぽんっ！{0}\n{1}！".format(str,result))
 
# button1
btn1 = QPushButton('グー', w)
btn1.clicked.connect(lambda: on_click(0))
btn1.resize(100,50)
btn1.move(40, 300)
 
# button2
btn2 = QPushButton('チョキ', w)
btn2.clicked.connect((lambda: on_click(1)))
btn2.resize(100,50)
btn2.move(220, 300)
 
# button3
btn3 = QPushButton('パー', w)
btn3.clicked.connect((lambda: on_click(2)))
btn3.resize(100,50)
btn3.move(400, 300)
 
show_fig("figs/janken.png")

# Show window
w.show()
  
sys.exit(a.exec_())