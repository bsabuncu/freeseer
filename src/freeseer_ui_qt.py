# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'freeseer_ui_qt.ui'
#
# Created: Tue Feb  9 20:58:33 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_FreeseerMainWindow(object):
    def setupUi(self, FreeseerMainWindow):
        FreeseerMainWindow.setObjectName("FreeseerMainWindow")
        FreeseerMainWindow.resize(463, 509)
        self.centralwidget = QtGui.QWidget(FreeseerMainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.main = QtGui.QWidget()
        self.main.setObjectName("main")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.main)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.recordButton = QtGui.QPushButton(self.main)
        self.recordButton.setCheckable(True)
        self.recordButton.setObjectName("recordButton")
        self.verticalLayout_2.addWidget(self.recordButton)
        self.optionsLayout = QtGui.QVBoxLayout()
        self.optionsLayout.setObjectName("optionsLayout")
        self.deviceOptionsLayout = QtGui.QHBoxLayout()
        self.deviceOptionsLayout.setObjectName("deviceOptionsLayout")
        self.deviceLabel = QtGui.QLabel(self.main)
        self.deviceLabel.setMaximumSize(QtCore.QSize(40, 16777215))
        self.deviceLabel.setObjectName("deviceLabel")
        self.deviceOptionsLayout.addWidget(self.deviceLabel)
        self.videoDeviceList = QtGui.QComboBox(self.main)
        self.videoDeviceList.setObjectName("videoDeviceList")
        self.deviceOptionsLayout.addWidget(self.videoDeviceList)
        self.videoSourceList = QtGui.QComboBox(self.main)
        self.videoSourceList.setObjectName("videoSourceList")
        self.deviceOptionsLayout.addWidget(self.videoSourceList)
        self.audioSourceList = QtGui.QComboBox(self.main)
        self.audioSourceList.setObjectName("audioSourceList")
        self.deviceOptionsLayout.addWidget(self.audioSourceList)
        self.optionsLayout.addLayout(self.deviceOptionsLayout)
        self.talkListLayout = QtGui.QHBoxLayout()
        self.talkListLayout.setObjectName("talkListLayout")
        self.talkLabel = QtGui.QLabel(self.main)
        self.talkLabel.setMaximumSize(QtCore.QSize(40, 24))
        self.talkLabel.setObjectName("talkLabel")
        self.talkListLayout.addWidget(self.talkLabel)
        self.talkList = QtGui.QComboBox(self.main)
        self.talkList.setObjectName("talkList")
        self.talkListLayout.addWidget(self.talkList)
        self.optionsLayout.addLayout(self.talkListLayout)
        self.verticalLayout_2.addLayout(self.optionsLayout)
        self.feedbackLayout = QtGui.QHBoxLayout()
        self.feedbackLayout.setObjectName("feedbackLayout")
        self.previewWidget = QtGui.QWidget(self.main)
        self.previewWidget.setObjectName("previewWidget")
        self.feedbackLayout.addWidget(self.previewWidget)
        self.audioFeedbackSlider = QtGui.QSlider(self.main)
        self.audioFeedbackSlider.setOrientation(QtCore.Qt.Vertical)
        self.audioFeedbackSlider.setObjectName("audioFeedbackSlider")
        self.feedbackLayout.addWidget(self.audioFeedbackSlider)
        self.verticalLayout_2.addLayout(self.feedbackLayout)
        self.tabWidget.addTab(self.main, "")
        self.editTalksPage = QtGui.QWidget()
        self.editTalksPage.setObjectName("editTalksPage")
        self.verticalLayout = QtGui.QVBoxLayout(self.editTalksPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.talkLineEdit = QtGui.QLineEdit(self.editTalksPage)
        self.talkLineEdit.setObjectName("talkLineEdit")
        self.verticalLayout.addWidget(self.talkLineEdit)
        self.editActionslayout = QtGui.QHBoxLayout()
        self.editActionslayout.setObjectName("editActionslayout")
        self.addTalkButton = QtGui.QPushButton(self.editTalksPage)
        self.addTalkButton.setObjectName("addTalkButton")
        self.editActionslayout.addWidget(self.addTalkButton)
        self.removeTalkButton = QtGui.QPushButton(self.editTalksPage)
        self.removeTalkButton.setObjectName("removeTalkButton")
        self.editActionslayout.addWidget(self.removeTalkButton)
        self.saveTalkButton = QtGui.QPushButton(self.editTalksPage)
        self.saveTalkButton.setObjectName("saveTalkButton")
        self.editActionslayout.addWidget(self.saveTalkButton)
        self.verticalLayout.addLayout(self.editActionslayout)
        self.editTalkList = QtGui.QListWidget(self.editTalksPage)
        self.editTalkList.setObjectName("editTalkList")
        self.verticalLayout.addWidget(self.editTalkList)
        self.tabWidget.addTab(self.editTalksPage, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)
        FreeseerMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FreeseerMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 463, 20))
        self.menubar.setObjectName("menubar")
        self.menuFreeseer = QtGui.QMenu(self.menubar)
        self.menuFreeseer.setObjectName("menuFreeseer")
        FreeseerMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FreeseerMainWindow)
        self.statusbar.setObjectName("statusbar")
        FreeseerMainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(FreeseerMainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFreeseer.addAction(self.actionExit)
        self.menubar.addAction(self.menuFreeseer.menuAction())

        self.retranslateUi(FreeseerMainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FreeseerMainWindow)

    def retranslateUi(self, FreeseerMainWindow):
        FreeseerMainWindow.setWindowTitle(QtGui.QApplication.translate("FreeseerMainWindow", "freeseer - video studio in a backpack", None, QtGui.QApplication.UnicodeUTF8))
        self.recordButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Record", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceLabel.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Device:", None, QtGui.QApplication.UnicodeUTF8))
        self.talkLabel.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Talk:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), QtGui.QApplication.translate("FreeseerMainWindow", "main", None, QtGui.QApplication.UnicodeUTF8))
        self.addTalkButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "add", None, QtGui.QApplication.UnicodeUTF8))
        self.removeTalkButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "remove", None, QtGui.QApplication.UnicodeUTF8))
        self.saveTalkButton.setText(QtGui.QApplication.translate("FreeseerMainWindow", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.editTalksPage), QtGui.QApplication.translate("FreeseerMainWindow", "edit talks", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFreeseer.setTitle(QtGui.QApplication.translate("FreeseerMainWindow", "freeseer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("FreeseerMainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

