# -*- coding: gbk -*-
#Boa:Frame:Frame1

import wx
import threading
from baidu import get_rank

class MyThread(threading.Thread):
    def __init__(self, s):
        threading.Thread.__init__(self)
        self.s = s

    def run(self):
        data = self.s.textCtrl1.GetValue().encode("gbk")
        lines = data.split("\n")
        self.s.gauge1.SetRange(len(lines))
        self.s.gauge1.SetValue(0)
        for line in lines:
            try:
                self.s.gauge1.SetValue(self.s.gauge1.GetValue() + 1)
                line = line.strip()
                if not line:
                    continue
                keyword, website = line.split()
                rank = get_rank(keyword, website)
                s = "%s,%s,%s\n"%(keyword, website, rank)
                open("data.csv", "a").write(s)
            except:
                wx.MessageBox(line + "  此行数据有误！")
            
        self.s.isrun = False
        wx.MessageBox("完成! 请查看输出文件 data.csv")



def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1GAUGE1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(5)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(637, 354), size=wx.Size(874, 540),
              style=wx.DEFAULT_FRAME_STYLE,
              title='贵仁医疗网络服务有限公司（百度/360快速排名,见效后付费。联系QQ：10855513）')
        self.SetClientSize(wx.Size(858, 502))
        self.SetBackgroundColour(wx.Colour(253, 234, 213))
        self.SetToolTipString('')

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(24, 16), size=wx.Size(800, 424),
              style=wx.TE_MULTILINE, value='')

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label='\xbf\xaa\xca\xbc\xb2\xc9\xbc\xaf', name='button1',
              parent=self, pos=wx.Point(24, 456), size=wx.Size(96, 32),
              style=0)
        self.button1.SetToolTipString('')
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label='',
              name='staticText1', parent=self, pos=wx.Point(32, 32),
              size=wx.Size(0, 14), style=0)
        self.staticText1.SetToolTipString('')

        self.gauge1 = wx.Gauge(id=wxID_FRAME1GAUGE1, name='gauge1', parent=self,
              pos=wx.Point(128, 456), range=100, size=wx.Size(696, 32),
              style=wx.GA_HORIZONTAL)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.isrun = False

    def OnButton1Button(self, event): 
        if not self.isrun:
            self.isrun = True
            t = MyThread(self)
            t.start()
        else:
            wx.MessageBox("正在进行采集 请稍候..")
        event.Skip()
