import wx

from myframe import MyFrame


class MyApp(wx.App):

    def OnInit(self):
        """."""
        self.frame1 = MyFrame(None, 'Checksum (CRC32, JSON)')
        self.frame1.CenterOnScreen()
        self.frame1.Show()

        return True


def main():
    app = MyApp()
    app.MainLoop()


if __name__ == "__main__":
    main()
