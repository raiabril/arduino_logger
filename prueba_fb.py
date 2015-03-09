# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep 12 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import os
from numpy import arange, sin, pi
import matplotlib

# comment out the following to use wx rather than wxagg
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

###########################################################################
## Class MyFrame1
###########################################################################
class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        
class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem1 )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem3 )
		
		self.m_menu1.AppendSeparator()
		
		self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_EXIT, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem4 )
		
		self.m_menubar1.Append( self.m_menu1, u"File" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		general = wx.BoxSizer( wx.HORIZONTAL )
		
		plot = wx.BoxSizer( wx.VERTICAL )
		
		self.panel_plot = CanvasPanel(self)
		plot.Add( self.panel_plot, 1, wx.EXPAND |wx.ALL, 5 )
		
		general.Add( plot, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Arduino Logger! by Rai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Fichero", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		bSizer5.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		self.m_dirPicker2 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer5.Add( self.m_dirPicker2, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Parametros", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer5.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Numero de muestras", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer14.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Frecuencia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer14.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		bSizer13.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		bSizer5.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Go!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button1, 0, wx.ALL, 5 )
		
		general.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		self.SetSizer( general )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
		# Events.
                self.Bind(wx.EVT_MENU, self.OnExit, self.m_menuItem4)
                self.Bind(wx.EVT_BUTTON, self.OnGo, self.m_button1)
	
	def __del__( self ):
		pass
		
        def OnExit(self,e):
            self.Close(True)  # Close the frame.
            
        def OnGo(self,e):
            print 'Click'
            self.panel_plot.draw()
            self.panel_plot.canvas.draw()
            self.panel_plot.canvas.Refresh()
            self.Show()

	

if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = MyFrame1(parent = None)
	frame.Show()
	app.MainLoop()
	
	