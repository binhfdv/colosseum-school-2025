#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FRS Transceiver
# Author: Ettus Research
# Description: Transmit and Receive demo for FRS 
# Generated: Wed Aug 30 21:49:34 2017
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
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import sip
import sys
import time


class frs_transceiver(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "FRS Transceiver")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("FRS Transceiver")
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

        self.settings = Qt.QSettings("GNU Radio", "frs_transceiver")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.xlate_bw = xlate_bw = 12.5e3
        self.samp_rate = samp_rate = 1e6
        self.bb_rate = bb_rate = 25e3
        self.xlate_freq = xlate_freq = 200e3
        self.tx_gain = tx_gain = 30
        self.transmit = transmit = 0
        self.taps = taps = firdes.low_pass(1.0, samp_rate, xlate_bw/2, 1000)
        self.sql_lev = sql_lev = -60
        self.speaker_audio_rate = speaker_audio_rate = 48000
        self.rx_gain = rx_gain = 0
        self.micvol = micvol = 2
        self.mic_audio_rate = mic_audio_rate = 48000
        self.freq = freq = 467.5875e6
        self.decimation = decimation = int(samp_rate / bb_rate)
        self.ctcss_freq = ctcss_freq = 0
        self.ctcss = ctcss = False
        self.af_gain = af_gain = 1

        ##################################################
        # Blocks
        ##################################################
        self._tx_gain_range = Range(0, 70, 1, 30, 200)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, 'TX Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_gain_win, 1,3,1,3)
        _transmit_push_button = Qt.QPushButton('TX')
        self._transmit_choices = {'Pressed': 1, 'Released': 0}
        _transmit_push_button.pressed.connect(lambda: self.set_transmit(self._transmit_choices['Pressed']))
        _transmit_push_button.released.connect(lambda: self.set_transmit(self._transmit_choices['Released']))
        self.top_grid_layout.addWidget(_transmit_push_button, 3,5,1,1)
        self._sql_lev_range = Range(-100, 100, 1, -60, 200)
        self._sql_lev_win = RangeWidget(self._sql_lev_range, self.set_sql_lev, 'Squelch', "counter_slider", float)
        self.top_grid_layout.addWidget(self._sql_lev_win, 3,1,1,2)
        self._micvol_range = Range(0, 10, .1, 2, 200)
        self._micvol_win = RangeWidget(self._micvol_range, self.set_micvol, 'Mic', "counter_slider", float)
        self.top_grid_layout.addWidget(self._micvol_win, 2,3,1,3)
        self._freq_options = [462.5625e6, 462.5875e6, 462.6125e6, 462.6375e6, 462.6625e6, 462.6875e6, 462.7125e6, 467.5625e6, 467.5875e6, 467.6125e6, 467.6375e6, 467.6625e6, 467.6875e6, 467.7125e6]
        self._freq_labels = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
        self._freq_tool_bar = Qt.QToolBar(self)
        self._freq_tool_bar.addWidget(Qt.QLabel('Channel'+": "))
        self._freq_combo_box = Qt.QComboBox()
        self._freq_tool_bar.addWidget(self._freq_combo_box)
        for label in self._freq_labels: self._freq_combo_box.addItem(label)
        self._freq_callback = lambda i: Qt.QMetaObject.invokeMethod(self._freq_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._freq_options.index(i)))
        self._freq_callback(self.freq)
        self._freq_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_freq(self._freq_options[i]))
        self.top_grid_layout.addWidget(self._freq_tool_bar, 3,0,1,1)
        self._ctcss_freq_options = [0, 67.0,  71.9,  74.4,  77.0,  79.7,  82.5,  85.4,  88.5,  91.5,  94.8, 97.4, 100.0, 103.5, 107.2, 110.9, 114.8, 118.8, 123.0, 127.3, 131.8, 136.5, 141.3, 146.2, 151.4, 156.7, 162.2, 167.9, 173.8, 179.9, 186.2, 192.8, 203.5, 210.7, 218.1, 225.7, 233.6, 241.8, 250.3]
        self._ctcss_freq_labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38"]
        self._ctcss_freq_tool_bar = Qt.QToolBar(self)
        self._ctcss_freq_tool_bar.addWidget(Qt.QLabel('CTCSS'+": "))
        self._ctcss_freq_combo_box = Qt.QComboBox()
        self._ctcss_freq_tool_bar.addWidget(self._ctcss_freq_combo_box)
        for label in self._ctcss_freq_labels: self._ctcss_freq_combo_box.addItem(label)
        self._ctcss_freq_callback = lambda i: Qt.QMetaObject.invokeMethod(self._ctcss_freq_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._ctcss_freq_options.index(i)))
        self._ctcss_freq_callback(self.ctcss_freq)
        self._ctcss_freq_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_ctcss_freq(self._ctcss_freq_options[i]))
        self.top_grid_layout.addWidget(self._ctcss_freq_tool_bar, 3,3,1,2)
        _ctcss_check_box = Qt.QCheckBox('CTCSS')
        self._ctcss_choices = {True: True, False: False}
        self._ctcss_choices_inv = dict((v,k) for k,v in self._ctcss_choices.iteritems())
        self._ctcss_callback = lambda i: Qt.QMetaObject.invokeMethod(_ctcss_check_box, "setChecked", Qt.Q_ARG("bool", self._ctcss_choices_inv[i]))
        self._ctcss_callback(self.ctcss)
        _ctcss_check_box.stateChanged.connect(lambda i: self.set_ctcss(self._ctcss_choices[bool(i)]))
        self.top_grid_layout.addWidget(_ctcss_check_box, 3,4,1,1)
        self._af_gain_range = Range(0, 5, 1, 1, 200)
        self._af_gain_win = RangeWidget(self._af_gain_range, self.set_af_gain, 'Volume', "counter_slider", float)
        self.top_grid_layout.addWidget(self._af_gain_win, 2,0,1,3)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "type=b200")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(freq-200e3, 0)
        self.uhd_usrp_source_0.set_gain(tx_gain, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "type=b200")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(freq, 0)
        self.uhd_usrp_sink_0.set_gain(tx_gain, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0.set_bandwidth(1e6, 0)
        self._rx_gain_range = Range(0, 70, 1, 0, 200)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, 'RX Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_gain_win, 1,0,1,3)
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_fff(
                interpolation=speaker_audio_rate/1000,
                decimation=25,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=25,
                decimation=mic_audio_rate/1000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(samp_rate/25e3),
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	samp_rate, #bw
        	"Spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
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
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,6)
        self.nbfm_normal = analog.nbfm_rx(
        	audio_rate=25000,
        	quad_rate=25000,
        	tau=75e-6,
        	max_dev=5e3,
          )
        self.gr_multiply_const_vxx_1 = blocks.multiply_const_vff((0.0 if transmit else af_gain, ))
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(decimation, (taps), xlate_freq, samp_rate)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/demouser/ettus_workshop/sources/harvard.wav', True)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((micvol, ))
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blks2_selector_0_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=1,
        	num_outputs=2,
        	input_index=0,
        	output_index=transmit,
        )
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=0 if ctcss else 1,
        	output_index=0,
        )
        self.audio_sink_0 = audio.sink(speaker_audio_rate, "", True)
        self.analog_simple_squelch_cc_0 = analog.simple_squelch_cc(sql_lev, 1e-4)
        self.analog_sig_source_x_0 = analog.sig_source_f(25e3, analog.GR_COS_WAVE, ctcss_freq if ctcss else 0, .375, 0)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=25000,
        	quad_rate=25000,
        	tau=75e-6,
        	max_dev=5e3,
        	fh=-1.0,
                )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_tx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.analog_simple_squelch_cc_0, 0), (self.nbfm_normal, 0))    
        self.connect((self.blks2_selector_0, 0), (self.analog_nbfm_tx_0, 0))    
        self.connect((self.blks2_selector_0_0, 0), (self.blocks_null_sink_1, 0))    
        self.connect((self.blks2_selector_0_0, 1), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blks2_selector_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_simple_squelch_cc_0, 0))    
        self.connect((self.gr_multiply_const_vxx_1, 0), (self.audio_sink_0, 0))    
        self.connect((self.nbfm_normal, 0), (self.rational_resampler_xxx_1_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blks2_selector_0_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.blks2_selector_0, 1))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.gr_multiply_const_vxx_1, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "frs_transceiver")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_xlate_bw(self):
        return self.xlate_bw

    def set_xlate_bw(self, xlate_bw):
        self.xlate_bw = xlate_bw
        self.set_taps(firdes.low_pass(1.0, self.samp_rate, self.xlate_bw/2, 1000))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_taps(firdes.low_pass(1.0, self.samp_rate, self.xlate_bw/2, 1000))
        self.set_decimation(int(self.samp_rate / self.bb_rate))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq, self.samp_rate)

    def get_bb_rate(self):
        return self.bb_rate

    def set_bb_rate(self, bb_rate):
        self.bb_rate = bb_rate
        self.set_decimation(int(self.samp_rate / self.bb_rate))

    def get_xlate_freq(self):
        return self.xlate_freq

    def set_xlate_freq(self, xlate_freq):
        self.xlate_freq = xlate_freq
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.xlate_freq)

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_source_0.set_gain(self.tx_gain, 0)
        	
        self.uhd_usrp_sink_0.set_gain(self.tx_gain, 0)
        	

    def get_transmit(self):
        return self.transmit

    def set_transmit(self, transmit):
        self.transmit = transmit
        self.gr_multiply_const_vxx_1.set_k((0.0 if self.transmit else self.af_gain, ))
        self.blks2_selector_0_0.set_output_index(int(self.transmit))

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.taps))

    def get_sql_lev(self):
        return self.sql_lev

    def set_sql_lev(self, sql_lev):
        self.sql_lev = sql_lev
        self.analog_simple_squelch_cc_0.set_threshold(self.sql_lev)

    def get_speaker_audio_rate(self):
        return self.speaker_audio_rate

    def set_speaker_audio_rate(self, speaker_audio_rate):
        self.speaker_audio_rate = speaker_audio_rate

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain

    def get_micvol(self):
        return self.micvol

    def set_micvol(self, micvol):
        self.micvol = micvol
        self.blocks_multiply_const_vxx_0.set_k((self.micvol, ))

    def get_mic_audio_rate(self):
        return self.mic_audio_rate

    def set_mic_audio_rate(self, mic_audio_rate):
        self.mic_audio_rate = mic_audio_rate

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_callback(self.freq)
        self.uhd_usrp_source_0.set_center_freq(self.freq-200e3, 0)
        self.uhd_usrp_sink_0.set_center_freq(self.freq, 0)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq, self.samp_rate)

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation

    def get_ctcss_freq(self):
        return self.ctcss_freq

    def set_ctcss_freq(self, ctcss_freq):
        self.ctcss_freq = ctcss_freq
        self._ctcss_freq_callback(self.ctcss_freq)
        self.analog_sig_source_x_0.set_frequency(self.ctcss_freq if self.ctcss else 0)

    def get_ctcss(self):
        return self.ctcss

    def set_ctcss(self, ctcss):
        self.ctcss = ctcss
        self._ctcss_callback(self.ctcss)
        self.blks2_selector_0.set_input_index(int(0 if self.ctcss else 1))
        self.analog_sig_source_x_0.set_frequency(self.ctcss_freq if self.ctcss else 0)

    def get_af_gain(self):
        return self.af_gain

    def set_af_gain(self, af_gain):
        self.af_gain = af_gain
        self.gr_multiply_const_vxx_1.set_k((0.0 if self.transmit else self.af_gain, ))


def main(top_block_cls=frs_transceiver, options=None):

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
