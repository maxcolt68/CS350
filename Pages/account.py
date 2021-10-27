import wx


class Account(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.Back_Button = wx.Button(parent=self, label="Back", pos=(0, 0), size=(50, 50))
        self.Back_Button.Bind(wx.EVT_BUTTON, parent.setPrevious)

        self.Home_button = wx.Button(parent=self, label="Home", pos=(350, 0), size=(80, 50))
        self.Home_button.Bind(wx.EVT_BUTTON, parent.setHomepage)

        self.box = wx.StaticBox(parent=self, pos=(50, 50), size=(400, 200))

        self.Sign_in = wx.Button(parent=self, label="Sign in", pos=(350, 90), size=(80, 50))
        self.Sign_in.Bind(wx.EVT_BUTTON, self.Sign_in_example)

        self.Account_name = wx.StaticText(parent=self, pos=(100, 90), size=(150, 20))
        self.Account_age = wx.StaticText(parent=self, pos=(100, 110), size=(150, 20))
        self.Account_available = wx.StaticText(parent=self, pos=(100, 160), size=(150, 70))

        self.ingredients_list = wx.TextCtrl(parent=self, pos=(60, 60), size=(200, 100), style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.ingredients_list.Show()

        self.tools_list = wx.TextCtrl(parent=self, pos=(280, 60), size=(200, 50), style=wx.TE_READONLY | wx.TE_MULTILINE)
        self.tools_list.Show()

        self.ingredient_add = wx.Button(parent=self, label="Add", pos=(0, 0), size=(50, 50))
        self.ingredient_box = wx.TextCtrl(parent=self, pos=(0, 0), size=(50, 50))
        self.ingredient_del = wx.Button(parent=self, label="Del", pos=(0, 0), size=(50, 50))

        self.tool_add = wx.Button(parent=self, label="Add", pos=(0, 0), size=(50, 50))
        self.tool_del = wx.Button(parent=self, label="Del", pos=(0, 0), size=(50, 50))

        self.update_user()
        # there is supposed to be a way to render panels inside panels, but I couldnt get it to work, might be worth looking at again
        # self.pantry = pn.Pantry(self, True)
        #
        # self.self_sizer = wx.BoxSizer()
        # self.pantry_sizer = wx.BoxSizer()
        #
        # self.pantry_sizer.Add(self.pantry, 1, wx.ALL | wx.EXPAND, 20)
        # self.self_sizer.Add(self.pantry_sizer, 1, wx.ALL | wx.EXPAND, 20)
        #
        # self.SetSizer(self.self_sizer)


    # one of the most important UI functions, this is where the window resize gets handled
    def resize_main(self, event=None):
        size = self.GetSize()
        self.Home_button.SetPosition((size[0]-80, 0))

        self.ingredients_list.SetPosition((50, 260))
        self.ingredients_list.SetSize(int(size[0]/2)-40, size[1]-330)
        self.tools_list.SetPosition((int(size[0]/2)+20, 260))
        self.tools_list.SetSize(int(size[0]/2)-40, size[1] - 330)
        self.ingredient_add.SetPosition((int(size[0] * .25) - 70, size[1] - 60))
        self.ingredient_del.SetPosition((int(size[0] * .25) + 80, size[1] - 60))
        self.tool_add.SetPosition((int(size[0] * .70) - 70, size[1] - 60))
        self.tool_del.SetPosition((int(size[0] * .70) + 80, size[1] - 60))
        self.ingredient_box.SetPosition((int(size[0] * .25) - 20, size[1] - 60))
        self.ingredient_box.SetSize(100, 50)

    # updates the fields with user data if it is available
    def update_user(self):
        self.Account_name.SetLabel("Name: {}".format(self.parent.user.username))
        self.Account_age.SetLabel("Account age: {}".format(self.parent.user.account_age))
        self.Account_available.SetLabel("Permissions: \n{}".format(self.parent.user.permissions))
        self.tools_list.SetValue(self.parent.user.tools)
        self.ingredients_list.SetValue(self.parent.user.pantry)

    # to be replaced by real function, this is for demo purposes only
    def Sign_in_example(self, event):
        self.parent.setSignin()
        self.update_user()



