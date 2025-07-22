#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: E310 WBFM Host Flowgraph
# Author: Ettus Research
# Description: Demo application of streaming proessed data from E310
# Generated: Tue Dec 12 08:27:31 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
import xmlrpclib


class e310_fm_rx_zmq__host(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "E310 WBFM Host Flowgraph")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("E310 WBFM Host Flowgraph")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "e310_fm_rx_zmq__host")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.server_address = server_address = "192.168.10.2"
        self.samp_rate = samp_rate = 48000
        self.rx_gain = rx_gain = 50
        self.freq = freq = 98.5e6
        self.audio_gain = audio_gain = 0.5

        ##################################################
        # Blocks
        ##################################################
        self._audio_gain_range = Range(0, 1, 0.1, 0.5, 100)
        self._audio_gain_win = RangeWidget(self._audio_gain_range, self.set_audio_gain, 'Audio Gain', "counter_slider", float)
        self.top_layout.addWidget(self._audio_gain_win)
        self.zeromq_pull_source_0_0_0 = zeromq.pull_source(gr.sizeof_float, 1024, "tcp://"+server_address+":9999", 100, False, -1)
        self.zeromq_pull_source_0 = zeromq.pull_source(gr.sizeof_float, 1, "tcp://"+server_address+":9997", 100, False, -1)
        self.xmlrpc_client0 = xmlrpclib.Server('http://192.168.10.2:30000')
        self.xmlrpc_client = xmlrpclib.Server('http://192.168.10.2:30000')
        self._rx_gain_range = Range(0, 70, 1, 50, 200)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, 'RF Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_gain_win, 1,0,1,2)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            1024,
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-60, 50)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_win)
        self._freq_range = Range(88e6, 108e6, 100e3, 98.5e6, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'Frequency (Hz)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_win, 0,0,1,2)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((audio_gain, ))
        self.audio_sink_0 = audio.sink(samp_rate, '', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.zeromq_pull_source_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.zeromq_pull_source_0_0_0, 0), (self.qtgui_vector_sink_f_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "e310_fm_rx_zmq__host")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_server_address(self):
        return self.server_address

    def set_server_address(self, server_address):
        self.server_address = server_address

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.xmlrpc_client0.set_rx_gain(self.rx_gain)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.xmlrpc_client.set_freq(self.freq)

    def get_audio_gain(self):
        return self.audio_gain

    def set_audio_gain(self, audio_gain):
        self.audio_gain = audio_gain
        self.blocks_multiply_const_vxx_0_0.set_k((self.audio_gain, ))


def main(top_block_cls=e310_fm_rx_zmq__host, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
