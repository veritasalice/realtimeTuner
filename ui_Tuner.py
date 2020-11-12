# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tuner.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/img/music.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnGetFile = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGetFile.sizePolicy().hasHeightForWidth())
        self.btnGetFile.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/104.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGetFile.setIcon(icon1)
        self.btnGetFile.setObjectName("btnGetFile")
        self.horizontalLayout_2.addWidget(self.btnGetFile)
        self.editOutputFile = QtWidgets.QLineEdit(self.centralwidget)
        self.editOutputFile.setObjectName("editOutputFile")
        self.horizontalLayout_2.addWidget(self.editOutputFile)
        self.LabPassTime = QtWidgets.QLabel(self.centralwidget)
        self.LabPassTime.setMinimumSize(QtCore.QSize(100, 0))
        self.LabPassTime.setObjectName("LabPassTime")
        self.horizontalLayout_2.addWidget(self.LabPassTime)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        # self.label.setStyleSheet("QLabel{color:rgb(255,255,255)}")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pitchname = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pitchname.sizePolicy().hasHeightForWidth())
        self.pitchname.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        self.pitchname.setFont(font)
        self.pitchname.setTextFormat(QtCore.Qt.PlainText)
        self.pitchname.setAlignment(QtCore.Qt.AlignCenter)
        self.pitchname.setObjectName("pitchname")
        self.horizontalLayout_3.addWidget(self.pitchname)
        self.theorical = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theorical.sizePolicy().hasHeightForWidth())
        self.theorical.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.theorical.setFont(font)
        self.theorical.setTextFormat(QtCore.Qt.PlainText)
        self.theorical.setAlignment(QtCore.Qt.AlignCenter)
        self.theorical.setObjectName("theorical")
        self.horizontalLayout_3.addWidget(self.theorical)
        self.measurement = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measurement.sizePolicy().hasHeightForWidth())
        self.measurement.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        self.measurement.setFont(font)
        self.measurement.setTextFormat(QtCore.Qt.PlainText)
        self.measurement.setAlignment(QtCore.Qt.AlignCenter)
        self.measurement.setObjectName("measurement")
        self.horizontalLayout_3.addWidget(self.measurement)
        self.errorvalue = QtWidgets.QLabel(self.centralwidget)
        self.errorvalue.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorvalue.sizePolicy().hasHeightForWidth())
        self.errorvalue.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        self.errorvalue.setFont(font)
        self.errorvalue.setTextFormat(QtCore.Qt.PlainText)
        self.errorvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.errorvalue.setObjectName("errorvalue")
        self.horizontalLayout_3.addWidget(self.errorvalue)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.c1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c1.sizePolicy().hasHeightForWidth())
        self.c1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.c1.setFont(font)
        self.c1.setObjectName("c1")
        self.verticalLayout_3.addWidget(self.c1)
        op = QtWidgets.QGraphicsOpacityEffect()  # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        op.setOpacity(0.8)
        self.c1.setGraphicsEffect(op)

        self.d1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d1.sizePolicy().hasHeightForWidth())
        self.d1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.d1.setFont(font)
        self.d1.setObjectName("d1")
        self.verticalLayout_3.addWidget(self.d1)
        op = QtWidgets.QGraphicsOpacityEffect()  # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        op.setOpacity(0.8)
        self.d1.setGraphicsEffect(op)

        self.e1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.e1.sizePolicy().hasHeightForWidth())
        self.e1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.e1.setFont(font)
        self.e1.setObjectName("e1")
        self.verticalLayout_3.addWidget(self.e1)
        op = QtWidgets.QGraphicsOpacityEffect()  # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        op.setOpacity(0.8)
        self.e1.setGraphicsEffect(op)

        self.f1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f1.sizePolicy().hasHeightForWidth())
        self.f1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.f1.setFont(font)
        self.f1.setObjectName("f1")
        self.verticalLayout_3.addWidget(self.f1)
        op = QtWidgets.QGraphicsOpacityEffect()  # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        op.setOpacity(0.8)
        self.f1.setGraphicsEffect(op)

        self.g1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g1.sizePolicy().hasHeightForWidth())
        self.g1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.g1.setFont(font)
        self.g1.setObjectName("g1")
        self.verticalLayout_3.addWidget(self.g1)
        op = QtWidgets.QGraphicsOpacityEffect()  # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        op.setOpacity(0.8)
        self.g1.setGraphicsEffect(op)

        self.a1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a1.sizePolicy().hasHeightForWidth())
        self.a1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.a1.setFont(font)
        self.a1.setObjectName("a1")
        self.verticalLayout_3.addWidget(self.a1)
        op = QtWidgets.QGraphicsOpacityEffect()  # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        op.setOpacity(0.8)
        self.a1.setGraphicsEffect(op)

        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b1.sizePolicy().hasHeightForWidth())
        self.b1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.verticalLayout_3.addWidget(self.b1)
        op = QtWidgets.QGraphicsOpacityEffect()  # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        op.setOpacity(0.8)
        self.b1.setGraphicsEffect(op)

        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.c1m = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c1m.sizePolicy().hasHeightForWidth())
        self.c1m.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.c1m.setFont(font)
        self.c1m.setText("")
        self.c1m.setTextFormat(QtCore.Qt.RichText)
        self.c1m.setAlignment(QtCore.Qt.AlignCenter)
        self.c1m.setObjectName("c1m")
        self.verticalLayout_5.addWidget(self.c1m)
        self.d1m = QtWidgets.QLabel(self.centralwidget)
        self.d1m.setText("")
        self.d1m.setTextFormat(QtCore.Qt.AutoText)
        self.d1m.setAlignment(QtCore.Qt.AlignCenter)
        self.d1m.setObjectName("d1m")
        self.verticalLayout_5.addWidget(self.d1m)
        self.e1m = QtWidgets.QLabel(self.centralwidget)
        self.e1m.setText("")
        self.e1m.setAlignment(QtCore.Qt.AlignCenter)
        self.e1m.setObjectName("e1m")
        self.verticalLayout_5.addWidget(self.e1m)
        self.f1m = QtWidgets.QLabel(self.centralwidget)
        self.f1m.setText("")
        self.f1m.setAlignment(QtCore.Qt.AlignCenter)
        self.f1m.setObjectName("f1m")
        self.verticalLayout_5.addWidget(self.f1m)
        self.g1m = QtWidgets.QLabel(self.centralwidget)
        self.g1m.setText("")
        self.g1m.setAlignment(QtCore.Qt.AlignCenter)
        self.g1m.setObjectName("g1m")
        self.verticalLayout_5.addWidget(self.g1m)
        self.a1m = QtWidgets.QLabel(self.centralwidget)
        self.a1m.setText("")
        self.a1m.setAlignment(QtCore.Qt.AlignCenter)
        self.a1m.setObjectName("a1m")
        self.verticalLayout_5.addWidget(self.a1m)
        self.b1m = QtWidgets.QLabel(self.centralwidget)
        self.b1m.setText("")
        self.b1m.setAlignment(QtCore.Qt.AlignCenter)
        self.b1m.setObjectName("b1m")
        self.verticalLayout_5.addWidget(self.b1m)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.c1e = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c1e.sizePolicy().hasHeightForWidth())
        self.c1e.setSizePolicy(sizePolicy)
        self.c1e.setText("")
        self.c1e.setTextFormat(QtCore.Qt.RichText)
        self.c1e.setAlignment(QtCore.Qt.AlignCenter)
        self.c1e.setObjectName("c1e")
        self.verticalLayout_6.addWidget(self.c1e)
        self.d1e = QtWidgets.QLabel(self.centralwidget)
        self.d1e.setText("")
        self.d1e.setTextFormat(QtCore.Qt.AutoText)
        self.d1e.setAlignment(QtCore.Qt.AlignCenter)
        self.d1e.setObjectName("d1e")
        self.verticalLayout_6.addWidget(self.d1e)
        self.e1e = QtWidgets.QLabel(self.centralwidget)
        self.e1e.setText("")
        self.e1e.setAlignment(QtCore.Qt.AlignCenter)
        self.e1e.setObjectName("e1e")
        self.verticalLayout_6.addWidget(self.e1e)
        self.f1e = QtWidgets.QLabel(self.centralwidget)
        self.f1e.setText("")
        self.f1e.setAlignment(QtCore.Qt.AlignCenter)
        self.f1e.setObjectName("f1e")
        self.verticalLayout_6.addWidget(self.f1e)
        self.g1e = QtWidgets.QLabel(self.centralwidget)
        self.g1e.setText("")
        self.g1e.setAlignment(QtCore.Qt.AlignCenter)
        self.g1e.setObjectName("g1e")
        self.verticalLayout_6.addWidget(self.g1e)
        self.a1e = QtWidgets.QLabel(self.centralwidget)
        self.a1e.setText("")
        self.a1e.setAlignment(QtCore.Qt.AlignCenter)
        self.a1e.setObjectName("a1e")
        self.verticalLayout_6.addWidget(self.a1e)
        self.b1e = QtWidgets.QLabel(self.centralwidget)
        self.b1e.setText("")
        self.b1e.setAlignment(QtCore.Qt.AlignCenter)
        self.b1e.setObjectName("b1e")
        self.verticalLayout_6.addWidget(self.b1e)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.comboDevices = QtWidgets.QComboBox(self.centralwidget)
        self.comboDevices.setObjectName("comboDevices")
        self.horizontalLayout_4.addWidget(self.comboDevices)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.comboCodec = QtWidgets.QComboBox(self.centralwidget)
        self.comboCodec.setObjectName("comboCodec")
        self.horizontalLayout_4.addWidget(self.comboCodec)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.comboSampleRate = QtWidgets.QComboBox(self.centralwidget)
        self.comboSampleRate.setObjectName("comboSampleRate")
        self.horizontalLayout_4.addWidget(self.comboSampleRate)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.comboChannels = QtWidgets.QComboBox(self.centralwidget)
        self.comboChannels.setObjectName("comboChannels")
        self.horizontalLayout_4.addWidget(self.comboChannels)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(5, 8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainToolBar.sizePolicy().hasHeightForWidth())
        self.mainToolBar.setSizePolicy(sizePolicy)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.actRecord = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("data/img/icons8-record.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actRecord.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.actRecord.setFont(font)
        self.actRecord.setVisible(True)
        self.actRecord.setObjectName("actRecord")
        self.actStop = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("data/img/icons8-stop (1).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actStop.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.actStop.setFont(font)
        self.actStop.setObjectName("actStop")
        self.actQuit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("data/img/button_cancel.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actQuit.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.actQuit.setFont(font)
        self.actQuit.setObjectName("actQuit")
        self.mainToolBar.addAction(self.actRecord)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actStop)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actQuit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.c1, self.d1)
        MainWindow.setTabOrder(self.d1, self.e1)
        MainWindow.setTabOrder(self.e1, self.f1)
        MainWindow.setTabOrder(self.f1, self.g1)
        MainWindow.setTabOrder(self.g1, self.a1)
        MainWindow.setTabOrder(self.a1, self.b1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnGetFile.setText(_translate("MainWindow", "录音输出文件"))
        self.LabPassTime.setText(_translate("MainWindow", "已录时间："))
        self.label.setText(_translate("MainWindow", "乐音基频频率在线检测"))
        self.pitchname.setText(_translate("MainWindow", "音名"))
        self.theorical.setText(_translate("MainWindow", "理论值(Hz)"))
        self.measurement.setText(_translate("MainWindow", "实测值(Hz)"))
        self.errorvalue.setText(_translate("MainWindow", "误差(%)"))
        self.c1.setText(_translate("MainWindow", "c1"))
        self.d1.setText(_translate("MainWindow", "d1"))
        self.e1.setText(_translate("MainWindow", "e1"))
        self.f1.setText(_translate("MainWindow", "f1"))
        self.g1.setText(_translate("MainWindow", "g1"))
        self.a1.setText(_translate("MainWindow", "a1"))
        self.b1.setText(_translate("MainWindow", "b1"))
        self.label_4.setText(_translate("MainWindow", "261.626"))
        self.label_5.setText(_translate("MainWindow", "293.665"))
        self.label_7.setText(_translate("MainWindow", "329.628"))
        self.label_9.setText(_translate("MainWindow", "349.228"))
        self.label_8.setText(_translate("MainWindow", "391.995"))
        self.label_6.setText(_translate("MainWindow", "440.000"))
        self.label_10.setText(_translate("MainWindow", "493.883"))
        self.label_2.setText(_translate("MainWindow", "输入设备"))
        self.label_11.setText(_translate("MainWindow", "音频编码"))
        self.label_3.setText(_translate("MainWindow", "采样率"))
        self.label_12.setText(_translate("MainWindow", "通道数"))
        self.mainToolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actRecord.setText(_translate("MainWindow", "录音"))
        self.actStop.setText(_translate("MainWindow", "停止"))
        self.actQuit.setText(_translate("MainWindow", "退出"))

# import res_rc
