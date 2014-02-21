# -*- coding: gbk -*-
#Boa:Frame:Frame1

import wx
from baidu import get_rank

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
              title='\xb0\xd9\xb6\xc8\xc5\xc5\xc3\xfb')
        self.SetClientSize(wx.Size(858, 502))
        self.SetBackgroundColour(wx.Colour(253, 234, 213))
        self.SetToolTipString('')

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(24, 16), size=wx.Size(800, 424),
              style=wx.TE_MULTILINE, value='')
        self.textCtrl1.SetToolTipString('\xca\xe4\xc8\xeb\xd2\xaa\xb2\xc9\xbc\xaf\xb5\xc4\xca\xfd\xbe\xdd \xb9\xd8\xbc\xfc\xd7\xd6\xd3\xeb\xcd\xf8\xd6\xb7\xbc\xe4\xd2\xd4 \xa1\xb0,\xa1\xb1 \xb7\xd6\xb8\xf4\n\xc8\xe7\xa3\xba\nabc,abc.go.com\nbbb,www.ycdbk.com')

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

    def OnButton1Button(self, event):
        data = self.textCtrl1.GetValue().encode("gbk")
        lines = data.split("\n")
        self.gauge1.SetRange(len(lines))
        self.gauge1.SetValue(0)
        for line in lines:
            try:
                self.gauge1.SetValue(self.gauge1.GetValue() + 1)
                keyword, website = line.split(",")
                rank = get_rank(keyword, website)
                s = "%s,%s,%s\n"%(keyword, website, rank)
                open("data.csv", "a").write(s)
            except:
                wx.MessageBox(line + "  此行数据有误！")
            
        wx.MessageBox("完成! 请查看输出文件 data.csv")
        event.Skip()
