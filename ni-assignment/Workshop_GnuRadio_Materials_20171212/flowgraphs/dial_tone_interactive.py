#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Dial Tone Interactive GUI
# Author: Ettus Research
# Description: Interactive Dial Tone Example
# Generated: Wed Aug 30 20:17:21 2017
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
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys


class dial_tone_interactive(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Dial Tone Interactive GUI")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Dial Tone Interactive GUI")
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

        self.settings = Qt.QSettings("GNU Radio", "dial_tone_interactive")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.r4 = r4 = 941
        self.r3 = r3 = 852
        self.r2 = r2 = 770
        self.r1 = r1 = 697
        self.dial_tone2 = dial_tone2 = 440
        self.dial_tone1 = dial_tone1 = 350
        self.c3 = c3 = 1477
        self.c2 = c2 = 1336
        self.c1 = c1 = 1209
        self.btn_zero = btn_zero = 0
        self.btn_two = btn_two = 0
        self.btn_three = btn_three = 0
        self.btn_star = btn_star = 0
        self.btn_six = btn_six = 0
        self.btn_seven = btn_seven = 0
        self.btn_pound = btn_pound = 0
        self.btn_one = btn_one = 0
        self.btn_nine = btn_nine = 0
        self.btn_four = btn_four = 0
        self.btn_five = btn_five = 0
        self.btn_eight = btn_eight = 0
        self.samp_rate = samp_rate = 32000
        self.noise = noise = 0.005
        self.freq2 = freq2 = c1 if btn_one or btn_four or btn_seven or btn_star else c2 if btn_two or btn_five or btn_eight or btn_zero else c3 if btn_three or btn_six or btn_nine or btn_pound else dial_tone2
        self.freq1 = freq1 = r1 if btn_one or btn_two or btn_three else r2 if btn_four or btn_five or btn_six ==1 else r3 if btn_seven or btn_eight or btn_nine else r4 if btn_star or btn_zero or btn_pound else dial_tone1
        self.ampl = ampl = .4

        ##################################################
        # Blocks
        ##################################################
        self._noise_range = Range(0, .2, .001, 0.005, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, 'Noise Amplitude', "counter_slider", float)
        self.top_grid_layout.addWidget(self._noise_win, 0, 3, 1, 3)
        self._ampl_range = Range(0, .5, .001, .4, 200)
        self._ampl_win = RangeWidget(self._ampl_range, self.set_ampl, 'Volume', "counter_slider", float)
        self.top_grid_layout.addWidget(self._ampl_win, 0, 0, 1, 3)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/10, #bw
        	"", #name
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
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not False)
        
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 1, 0, 1, 6)
        self.low_pass_filter_0 = filter.fir_filter_fff(10, firdes.low_pass(
        	1, samp_rate, 2e3, 1200, firdes.WIN_HAMMING, 6.76))
        _btn_zero_push_button = Qt.QPushButton('0')
        self._btn_zero_choices = {'Pressed': 1, 'Released': 0}
        _btn_zero_push_button.pressed.connect(lambda: self.set_btn_zero(self._btn_zero_choices['Pressed']))
        _btn_zero_push_button.released.connect(lambda: self.set_btn_zero(self._btn_zero_choices['Released']))
        self.top_grid_layout.addWidget(_btn_zero_push_button, 5, 2, 1, 2)
        _btn_two_push_button = Qt.QPushButton('2')
        self._btn_two_choices = {'Pressed': 1, 'Released': 0}
        _btn_two_push_button.pressed.connect(lambda: self.set_btn_two(self._btn_two_choices['Pressed']))
        _btn_two_push_button.released.connect(lambda: self.set_btn_two(self._btn_two_choices['Released']))
        self.top_grid_layout.addWidget(_btn_two_push_button, 2, 2, 1, 2)
        _btn_three_push_button = Qt.QPushButton('3')
        self._btn_three_choices = {'Pressed': 1, 'Released': 0}
        _btn_three_push_button.pressed.connect(lambda: self.set_btn_three(self._btn_three_choices['Pressed']))
        _btn_three_push_button.released.connect(lambda: self.set_btn_three(self._btn_three_choices['Released']))
        self.top_grid_layout.addWidget(_btn_three_push_button, 2, 4, 1, 2)
        _btn_star_push_button = Qt.QPushButton('*')
        self._btn_star_choices = {'Pressed': 1, 'Released': 0}
        _btn_star_push_button.pressed.connect(lambda: self.set_btn_star(self._btn_star_choices['Pressed']))
        _btn_star_push_button.released.connect(lambda: self.set_btn_star(self._btn_star_choices['Released']))
        self.top_grid_layout.addWidget(_btn_star_push_button, 5, 0, 1, 2)
        _btn_six_push_button = Qt.QPushButton('6')
        self._btn_six_choices = {'Pressed': 1, 'Released': 0}
        _btn_six_push_button.pressed.connect(lambda: self.set_btn_six(self._btn_six_choices['Pressed']))
        _btn_six_push_button.released.connect(lambda: self.set_btn_six(self._btn_six_choices['Released']))
        self.top_grid_layout.addWidget(_btn_six_push_button, 3, 4, 1, 2)
        _btn_seven_push_button = Qt.QPushButton('7')
        self._btn_seven_choices = {'Pressed': 1, 'Released': 0}
        _btn_seven_push_button.pressed.connect(lambda: self.set_btn_seven(self._btn_seven_choices['Pressed']))
        _btn_seven_push_button.released.connect(lambda: self.set_btn_seven(self._btn_seven_choices['Released']))
        self.top_grid_layout.addWidget(_btn_seven_push_button, 4, 0, 1, 2)
        _btn_pound_push_button = Qt.QPushButton('#')
        self._btn_pound_choices = {'Pressed': 1, 'Released': 0}
        _btn_pound_push_button.pressed.connect(lambda: self.set_btn_pound(self._btn_pound_choices['Pressed']))
        _btn_pound_push_button.released.connect(lambda: self.set_btn_pound(self._btn_pound_choices['Released']))
        self.top_grid_layout.addWidget(_btn_pound_push_button, 5, 4, 1, 2)
        _btn_one_push_button = Qt.QPushButton('1')
        self._btn_one_choices = {'Pressed': 1, 'Released': 0}
        _btn_one_push_button.pressed.connect(lambda: self.set_btn_one(self._btn_one_choices['Pressed']))
        _btn_one_push_button.released.connect(lambda: self.set_btn_one(self._btn_one_choices['Released']))
        self.top_grid_layout.addWidget(_btn_one_push_button, 2, 0, 1, 2)
        _btn_nine_push_button = Qt.QPushButton('9')
        self._btn_nine_choices = {'Pressed': 1, 'Released': 0}
        _btn_nine_push_button.pressed.connect(lambda: self.set_btn_nine(self._btn_nine_choices['Pressed']))
        _btn_nine_push_button.released.connect(lambda: self.set_btn_nine(self._btn_nine_choices['Released']))
        self.top_grid_layout.addWidget(_btn_nine_push_button, 4, 4, 1, 2)
        _btn_four_push_button = Qt.QPushButton('4')
        self._btn_four_choices = {'Pressed': 1, 'Released': 0}
        _btn_four_push_button.pressed.connect(lambda: self.set_btn_four(self._btn_four_choices['Pressed']))
        _btn_four_push_button.released.connect(lambda: self.set_btn_four(self._btn_four_choices['Released']))
        self.top_grid_layout.addWidget(_btn_four_push_button, 3, 0, 1, 2)
        _btn_five_push_button = Qt.QPushButton('5')
        self._btn_five_choices = {'Pressed': 1, 'Released': 0}
        _btn_five_push_button.pressed.connect(lambda: self.set_btn_five(self._btn_five_choices['Pressed']))
        _btn_five_push_button.released.connect(lambda: self.set_btn_five(self._btn_five_choices['Released']))
        self.top_grid_layout.addWidget(_btn_five_push_button, 3, 2, 1, 2)
        _btn_eight_push_button = Qt.QPushButton('8')
        self._btn_eight_choices = {'Pressed': 1, 'Released': 0}
        _btn_eight_push_button.pressed.connect(lambda: self.set_btn_eight(self._btn_eight_choices['Pressed']))
        _btn_eight_push_button.released.connect(lambda: self.set_btn_eight(self._btn_eight_choices['Released']))
        self.top_grid_layout.addWidget(_btn_eight_push_button, 4, 2, 1, 2)
        self.blocks_add_xx = blocks.add_vff(1)
        self.audio_sink = audio.sink(32000, '', True)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq2, ampl, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, freq1, ampl, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise, -42)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx, 2))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx, 0))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx, 1))    
        self.connect((self.blocks_add_xx, 0), (self.audio_sink, 0))    
        self.connect((self.blocks_add_xx, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "dial_tone_interactive")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_r4(self):
        return self.r4

    def set_r4(self, r4):
        self.r4 = r4
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_r3(self):
        return self.r3

    def set_r3(self, r3):
        self.r3 = r3
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_r2(self):
        return self.r2

    def set_r2(self, r2):
        self.r2 = r2
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_r1(self):
        return self.r1

    def set_r1(self, r1):
        self.r1 = r1
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_dial_tone2(self):
        return self.dial_tone2

    def set_dial_tone2(self, dial_tone2):
        self.dial_tone2 = dial_tone2
        self.set_freq2(self.c1 if self.btn_one or self.btn_four or self.btn_seven or self.btn_star else self.c2 if self.btn_two or self.btn_five or self.btn_eight or self.btn_zero else self.c3 if self.btn_three or self.btn_six or self.btn_nine or self.btn_pound else self.dial_tone2)

    def get_dial_tone1(self):
        return self.dial_tone1

    def set_dial_tone1(self, dial_tone1):
        self.dial_tone1 = dial_tone1
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_c3(self):
        return self.c3

    def set_c3(self, c3):
        self.c3 = c3
        self.set_freq2(self.c1 if self.btn_one or self.btn_four or self.btn_seven or self.btn_star else self.c2 if self.btn_two or self.btn_five or self.btn_eight or self.btn_zero else self.c3 if self.btn_three or self.btn_six or self.btn_nine or self.btn_pound else self.dial_tone2)

    def get_c2(self):
        return self.c2

    def set_c2(self, c2):
        self.c2 = c2
        self.set_freq2(self.c1 if self.btn_one or self.btn_four or self.btn_seven or self.btn_star else self.c2 if self.btn_two or self.btn_five or self.btn_eight or self.btn_zero else self.c3 if self.btn_three or self.btn_six or self.btn_nine or self.btn_pound else self.dial_tone2)

    def get_c1(self):
        return self.c1

    def set_c1(self, c1):
        self.c1 = c1
        self.set_freq2(self.c1 if self.btn_one or self.btn_four or self.btn_seven or self.btn_star else self.c2 if self.btn_two or self.btn_five or self.btn_eight or self.btn_zero else self.c3 if self.btn_three or self.btn_six or self.btn_nine or self.btn_pound else self.dial_tone2)

    def get_btn_zero(self):
        return self.btn_zero

    def set_btn_zero(self, btn_zero):
        self.btn_zero = btn_zero
        self.set_freq2(self.c1 if self.btn_one or self.btn_four or self.btn_seven or self.btn_star else self.c2 if self.btn_two or self.btn_five or self.btn_eight or self.btn_zero else self.c3 if self.btn_three or self.btn_six or self.btn_nine or self.btn_pound else self.dial_tone2)
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_btn_two(self):
        return self.btn_two

    def set_btn_two(self, btn_two):
        self.btn_two = btn_two
        self.set_freq2(self.c1 if self.btn_one or self.btn_four or self.btn_seven or self.btn_star else self.c2 if self.btn_two or self.btn_five or self.btn_eight or self.btn_zero else self.c3 if self.btn_three or self.btn_six or self.btn_nine or self.btn_pound else self.dial_tone2)
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_btn_three(self):
        return self.btn_three

    def set_btn_three(self, btn_three):
        self.btn_three = btn_three
        self.set_freq2(self.c1 if self.btn_one or self.btn_four or self.btn_seven or self.btn_star else self.c2 if self.btn_two or self.btn_five or self.btn_eight or self.btn_zero else self.c3 if self.btn_three or self.btn_six or self.btn_nine or self.btn_pound else self.dial_tone2)
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_btn_star(self):
        return self.btn_star

    def set_btn_star(self, btn_star):
        self.btn_star = btn_star
        self.set_freq2(self.c1 if self.btn_one or self.btn_four or self.btn_seven or self.btn_star else self.c2 if self.btn_two or self.btn_five or self.btn_eight or self.btn_zero else self.c3 if self.btn_three or self.btn_six or self.btn_nine or self.btn_pound else self.dial_tone2)
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_btn_six(self):
        return self.btn_six

    def set_btn_six(self, btn_six):
        self.btn_six = btn_six
        self.set_freq2(self.c1 if self.btn_one or self.btn_four or self.btn_seven or self.btn_star else self.c2 if self.btn_two or self.btn_five or self.btn_eight or self.btn_zero else self.c3 if self.btn_three or self.btn_six or self.btn_nine or self.btn_pound else self.dial_tone2)
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_btn_seven(self):
        return self.btn_seven

    def set_btn_seven(self, btn_seven):
        self.btn_seven = btn_seven
        self.set_freq2(self.c1 if self.btn_one or self.btn_four or self.btn_seven or self.btn_star else self.c2 if self.btn_two or self.btn_five or self.btn_eight or self.btn_zero else self.c3 if self.btn_three or self.btn_six or self.btn_nine or self.btn_pound else self.dial_tone2)
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_btn_pound(self):
        return self.btn_pound

    def set_btn_pound(self, btn_pound):
        self.btn_pound = btn_pound
        self.set_freq2(self.c1 if self.btn_one or self.btn_four or self.btn_seven or self.btn_star else self.c2 if self.btn_two or self.btn_five or self.btn_eight or self.btn_zero else self.c3 if self.btn_three or self.btn_six or self.btn_nine or self.btn_pound else self.dial_tone2)
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_btn_one(self):
        return self.btn_one

    def set_btn_one(self, btn_one):
        self.btn_one = btn_one
        self.set_freq2(self.c1 if self.btn_one or self.btn_four or self.btn_seven or self.btn_star else self.c2 if self.btn_two or self.btn_five or self.btn_eight or self.btn_zero else self.c3 if self.btn_three or self.btn_six or self.btn_nine or self.btn_pound else self.dial_tone2)
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_btn_nine(self):
        return self.btn_nine

    def set_btn_nine(self, btn_nine):
        self.btn_nine = btn_nine
        self.set_freq2(self.c1 if self.btn_one or self.btn_four or self.btn_seven or self.btn_star else self.c2 if self.btn_two or self.btn_five or self.btn_eight or self.btn_zero else self.c3 if self.btn_three or self.btn_six or self.btn_nine or self.btn_pound else self.dial_tone2)
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_btn_four(self):
        return self.btn_four

    def set_btn_four(self, btn_four):
        self.btn_four = btn_four
        self.set_freq2(self.c1 if self.btn_one or self.btn_four or self.btn_seven or self.btn_star else self.c2 if self.btn_two or self.btn_five or self.btn_eight or self.btn_zero else self.c3 if self.btn_three or self.btn_six or self.btn_nine or self.btn_pound else self.dial_tone2)
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_btn_five(self):
        return self.btn_five

    def set_btn_five(self, btn_five):
        self.btn_five = btn_five
        self.set_freq2(self.c1 if self.btn_one or self.btn_four or self.btn_seven or self.btn_star else self.c2 if self.btn_two or self.btn_five or self.btn_eight or self.btn_zero else self.c3 if self.btn_three or self.btn_six or self.btn_nine or self.btn_pound else self.dial_tone2)
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_btn_eight(self):
        return self.btn_eight

    def set_btn_eight(self, btn_eight):
        self.btn_eight = btn_eight
        self.set_freq2(self.c1 if self.btn_one or self.btn_four or self.btn_seven or self.btn_star else self.c2 if self.btn_two or self.btn_five or self.btn_eight or self.btn_zero else self.c3 if self.btn_three or self.btn_six or self.btn_nine or self.btn_pound else self.dial_tone2)
        self.set_freq1(self.r1 if self.btn_one or self.btn_two or self.btn_three else self.r2 if self.btn_four or self.btn_five or self.btn_six ==1 else self.r3 if self.btn_seven or self.btn_eight or self.btn_nine else self.r4 if self.btn_star or self.btn_zero or self.btn_pound else self.dial_tone1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/10)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 2e3, 1200, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.analog_noise_source_x_0.set_amplitude(self.noise)

    def get_freq2(self):
        return self.freq2

    def set_freq2(self, freq2):
        self.freq2 = freq2
        self.analog_sig_source_x_1.set_frequency(self.freq2)

    def get_freq1(self):
        return self.freq1

    def set_freq1(self, freq1):
        self.freq1 = freq1
        self.analog_sig_source_x_0.set_frequency(self.freq1)

    def get_ampl(self):
        return self.ampl

    def set_ampl(self, ampl):
        self.ampl = ampl
        self.analog_sig_source_x_1.set_amplitude(self.ampl)
        self.analog_sig_source_x_0.set_amplitude(self.ampl)


def main(top_block_cls=dial_tone_interactive, options=None):

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
