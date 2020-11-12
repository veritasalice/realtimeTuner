# -*- coding: utf-8 -*-
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QFileDialog
# from PyQt5.uic import loadUi
from PyQt5.QtMultimedia import (QMediaPlayer, QAudioRecorder, QAudioProbe, QMultimedia,
                                QMediaContent, QMediaRecorder, QAudioEncoderSettings)
from PyQt5.QtCore import QUrl, pyqtSlot, pyqtSignal
import sys
import os
from ui_Tuner import Ui_MainWindow
import librosa
from scipy import optimize
import numpy as np


class Tuner(QMainWindow):

    def __init__(self, parent=None):
        super(Tuner, self).__init__(parent)
        # 从文件中加载UI定义
        # self.ui = loadUi('Tuner.ui')  #pyqt5
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面

        # # 播放标准音
        self.mediaPlayer = QMediaPlayer(self)
        self.ui.c1.clicked.connect(self.playaudioc)
        self.ui.d1.clicked.connect(self.playaudiod)
        self.ui.e1.clicked.connect(self.playaudioe)
        self.ui.f1.clicked.connect(self.playaudiof)
        self.ui.g1.clicked.connect(self.playaudiog)
        self.ui.a1.clicked.connect(self.playaudioa)
        self.ui.b1.clicked.connect(self.playaudiob)

        # 录音
        self.fileName = ""
        self.recorder = QAudioRecorder(self)
        self.recorder.stateChanged.connect(self.do_stateChanged)
        self.recorder.durationChanged.connect(self.do_durationChanged)

        self.probe = QAudioProbe(self)  # 探测器
        self.probe.setSource(self.recorder)
        # self.probe.audioBufferProbed.connect(self.do_processBuffer)

        if self.recorder.defaultAudioInput() == "":  # str类型
            return  # 无音频录入设备

        for device in self.recorder.audioInputs():
            self.ui.comboDevices.addItem(device)  # 音频录入设备列表

        for codecName in self.recorder.supportedAudioCodecs():
            self.ui.comboCodec.addItem(codecName)  # 支持的音频编码

        sampleList, isContinuous = self.recorder.supportedAudioSampleRates()
        # isContinuous 是否支持连续的采样率，与C++不一样
        for i in range(len(sampleList)):
            self.ui.comboSampleRate.addItem("%d" % sampleList[i])  # 支持的采样率

        ##  channels
        self.ui.comboChannels.addItem("1")
        self.ui.comboChannels.addItem("2")
        self.ui.comboChannels.addItem("4")

        ##  ==============自定义功能函数============

    def __setRecordParams(self):  ##设置音频输入参数
        selectedFile = self.ui.editOutputFile.text().strip()
        if (selectedFile == ""):
            QMessageBox.critical(self, "错误", "请先设置录音输出文件")
            return False

        if os.path.exists(selectedFile):
            os.remove(selectedFile)  # 删除已有文件
        ##         QMessageBox.critical(self,"错误","录音输出文件被占用，无法删除")
        ##         return False

        recordFile = QUrl.fromLocalFile(selectedFile)
        self.recorder.setOutputLocation(recordFile)  # 设置输出文件

        recordDevice = self.ui.comboDevices.currentText()
        self.recorder.setAudioInput(recordDevice)  # 设置录入设备

        settings = QAudioEncoderSettings()  # 音频编码设置
        settings.setCodec(self.ui.comboCodec.currentText())  # 编码

        sampRate = int(self.ui.comboSampleRate.currentText())
        settings.setSampleRate(sampRate)  # 采样率

        channelCount = int(self.ui.comboChannels.currentText())
        settings.setChannelCount(channelCount)  # 通道数

        settings.setEncodingMode(QMultimedia.ConstantBitRateEncoding)  # 固定比特率

        self.recorder.setAudioSettings(settings)  # 音频设置
        return True

    def pitch_estimation(self, wavpath):
        if os.path.exists(wavpath):
            y, sr = librosa.load(wavpath)
            f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('B3'),
                                                         fmax=librosa.note_to_hz('C5'))
            f0 = f0[~np.isnan(f0)]
            times = librosa.times_like(f0)
            level = optimize.curve_fit(lambda x, b: b, times, np.nan_to_num(f0))[0]
            pitch = np.around(level[0], decimals=3).astype(float)
        return pitch
        ##  ==========由connectSlotsByName() 自动连接的槽函数==================

    @pyqtSlot()
    def on_btnGetFile_clicked(self):  ##"录音输出文件"按钮
        curPath = os.getcwd()  # 获取系统当前目录
        dlgTitle = "选择输出文件"
        filt = "wav文件(*.wav)"
        self.fileName, flt, = QFileDialog.getSaveFileName(self, dlgTitle, curPath, filt)
        if (self.fileName != ""):
            self.ui.editOutputFile.setText(self.fileName)

    @pyqtSlot()  ##开始录音
    def on_actRecord_triggered(self):
        success = True
        if (self.recorder.state() == QMediaRecorder.StoppedState):  # 已停止，重新设置
            success = self.__setRecordParams()  # 设置录音参数
        if success:
            self.recorder.record()

    @pyqtSlot()  ##退出
    def on_actQuit_triggered(self):
        sys.exit(app.exec_())

    # @pyqtSlot()  ##暂停
    # def on_actPause_triggered(self):
    #     self.recorder.pause()

    @pyqtSlot()  ##停止
    def on_actStop_triggered(self):
        self.recorder.stop()
        # 录完立马分析并显示Hz
        name = self.fileName.split('/')[-1][:-4]  # 存储的文件名 无.wav
        # func = lambda x, b: b
        if name == 'c1':
            # if os.path.exists(self.fileName):
            #     y, sr = librosa.load(self.fileName)
            #     f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C4'),
            #                                                  fmax=librosa.note_to_hz('C5'))
            #     f0 = f0[~np.isnan(f0)]
            #     times = librosa.times_like(f0)
            #     level = optimize.curve_fit(lambda x, b: b, times, np.nan_to_num(f0))[0]
            #     pitch = np.around(level[0], decimals=3).astype(float)
            pitch = self.pitch_estimation(self.fileName)
            self.ui.c1m.setStyleSheet("color:rgb(10,10,10,255);"
                                      "font-size:32px;"
                                      "font-weight:600;"
                                      "font-family:Times New Roman;")
            self.ui.c1m.setText(str(pitch))
            F0 = 261.626
            err = np.around(np.abs(pitch - F0) / F0, decimals=4)*100
            self.ui.c1e.setStyleSheet("color:rgb(10,10,10,255);"
                                      "font-size:32px;"
                                      "font-weight:600;"
                                      "font-family:Times New Roman;")
            self.ui.c1e.setText(str(err))
        elif name == 'd1':
            pitch = self.pitch_estimation(self.fileName)
            self.ui.d1m.setStyleSheet("color:rgb(10,10,10,255);"
                                      "font-size:32px;"
                                      "font-weight:600;"
                                      "font-family:Times New Roman;")
            self.ui.d1m.setText(str(pitch))
            F0 = 293.665
            err = np.around(np.abs(pitch - F0) / F0, decimals=4)*100
            self.ui.d1e.setStyleSheet("color:rgb(10,10,10,255);"
                                      "font-size:32px;"
                                      "font-weight:600;"
                                      "font-family:Times New Roman;")
            self.ui.d1e.setText(str(err))
        elif name == 'e1':
            pitch = self.pitch_estimation(self.fileName)
            self.ui.e1m.setStyleSheet("color:rgb(10,10,10,255);"
                                      "font-size:32px;"
                                      "font-weight:600;"
                                      "font-family:Times New Roman;")
            self.ui.e1m.setText(str(pitch))
            F0 = 329.628
            err = np.around(np.abs(pitch - F0) / F0, decimals=4)*100
            self.ui.e1e.setStyleSheet("color:rgb(10,10,10,255);"
                                      "font-size:32px;"
                                      "font-weight:600;"
                                      "font-family:Times New Roman;")
            self.ui.e1e.setText(str(err))
        elif name == 'f1':
            pitch = self.pitch_estimation(self.fileName)
            self.ui.f1m.setStyleSheet("color:rgb(10,10,10,255);"
                                      "font-size:32px;"
                                      "font-weight:600;"
                                      "font-family:Times New Roman;")
            self.ui.f1m.setText(str(pitch))
            F0 = 349.228
            err = np.around(np.abs(pitch - F0) / F0, decimals=4)*100
            self.ui.f1e.setStyleSheet("color:rgb(10,10,10,255);"
                                      "font-size:32px;"
                                      "font-weight:600;"
                                      "font-family:Times New Roman;")
            self.ui.f1e.setText(str(err))
        elif name == 'g1':
            pitch = self.pitch_estimation(self.fileName)
            self.ui.g1m.setStyleSheet("color:rgb(10,10,10,255);"
                                      "font-size:32px;"
                                      "font-weight:600;"
                                      "font-family:Times New Roman;")
            self.ui.g1m.setText(str(pitch))
            F0 = 391.995
            err = np.around(np.abs(pitch - F0) / F0, decimals=4)*100
            self.ui.g1e.setStyleSheet("color:rgb(10,10,10,255);"
                                      "font-size:32px;"
                                      "font-weight:600;"
                                      "font-family:Times New Roman;")
            self.ui.g1e.setText(str(err))
        elif name == 'a1':
            pitch = self.pitch_estimation(self.fileName)
            self.ui.a1m.setStyleSheet("color:rgb(10,10,10,255);"
                                      "font-size:32px;"
                                      "font-weight:600;"
                                      "font-family:Times New Roman;")
            self.ui.a1m.setText(str(pitch))
            F0 = 440.000
            err = np.around(np.abs(pitch - F0) / F0, decimals=4)*100
            self.ui.a1e.setStyleSheet("color:rgb(10,10,10,255);"
                                      "font-size:32px;"
                                      "font-weight:600;"
                                      "font-family:Times New Roman;")
            self.ui.a1e.setText(str(err))
        elif name == 'b1':
            pitch = self.pitch_estimation(self.fileName)
            self.ui.b1m.setStyleSheet("color:rgb(10,10,10,255);"
                                      "font-size:32px;"
                                      "font-weight:600;"
                                      "font-family:Times New Roman;")
            self.ui.b1m.setText(str(pitch))
            F0 = 493.883
            err = np.around(np.abs(pitch - F0) / F0, decimals=4)*100
            self.ui.b1e.setStyleSheet("color:rgb(10,10,10,255);"
                                      "font-size:32px;"
                                      "font-weight:600;"
                                      "font-family:Times New Roman;")
            self.ui.b1e.setText(str(err))
        else:
            QMessageBox.critical(self, "文件名错误", "请输入c1-b1中的音名")


    ##  =============自定义槽函数===============================
    def do_stateChanged(self, state):  ##状态变化
        isRecording = (state == QMediaRecorder.RecordingState)  # 正在录制
        self.ui.actRecord.setEnabled(not isRecording)
        # self.ui.actPause.setEnabled(isRecording)
        self.ui.actStop.setEnabled(isRecording)

        isStoped = (state == QMediaRecorder.StoppedState)  # 已停止
        self.ui.btnGetFile.setEnabled(isStoped)
        self.ui.editOutputFile.setEnabled(isStoped)



    def do_durationChanged(self, duration):  ##持续时间长度变化
        self.ui.LabPassTime.setText("已录制 %d 秒" % (duration / 1000))

    #   ============================================================================
    @pyqtSlot()
    def playaudioc(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("data/standard/C4.wav")))
        self.mediaPlayer.play()

    @pyqtSlot()
    def playaudiod(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("data/standard/D4.wav")))
        self.mediaPlayer.play()

    @pyqtSlot()
    def playaudioe(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("data/standard/E4.wav")))
        self.mediaPlayer.play()

    @pyqtSlot()
    def playaudiof(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("data/standard/F4.wav")))
        self.mediaPlayer.play()

    @pyqtSlot()
    def playaudiog(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("data/standard/G4.wav")))
        self.mediaPlayer.play()

    @pyqtSlot()
    def playaudioa(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("data/standard/A4.wav")))
        self.mediaPlayer.play()

    @pyqtSlot()
    def playaudiob(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("data/standard/B4.wav")))
        self.mediaPlayer.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Tuner()
    window.setStyleSheet("#MainWindow{border-image:url(data/img/earphone1.jpg)}")  # 这里使用相对路径，也可以使用绝对路径
    window.showFullScreen()
    # window.show()
    sys.exit(app.exec_())
