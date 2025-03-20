import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._lblMessage = System.Windows.Forms.Label()
		self._menufile1 = System.Windows.Forms.MenuStrip()
		self._mnuFile = System.Windows.Forms.ToolStripMenuItem()
		self._mnuExit = System.Windows.Forms.ToolStripMenuItem()
		self._mnuColor = System.Windows.Forms.ToolStripMenuItem()
		self._mnuRed = System.Windows.Forms.ToolStripMenuItem()
		self._mnuGreen = System.Windows.Forms.ToolStripMenuItem()
		self._mnuBlue = System.Windows.Forms.ToolStripMenuItem()
		self._mnuBlack = System.Windows.Forms.ToolStripMenuItem()
		self._toolStripMenuItem1 = System.Windows.Forms.ToolStripSeparator()
		self._mnuVisible = System.Windows.Forms.ToolStripMenuItem()
		self._mnuHelp = System.Windows.Forms.ToolStripMenuItem()
		self._mnuAbout = System.Windows.Forms.ToolStripMenuItem()
		self._menufile1.SuspendLayout()
		self.SuspendLayout()
		# 
		# lblMessage
		# 
		self._lblMessage.Location = System.Drawing.Point(25, 85)
		self._lblMessage.Name = "lblMessage"
		self._lblMessage.Size = System.Drawing.Size(178, 67)
		self._lblMessage.TabIndex = 0
		self._lblMessage.Text = "Hello World!"
		self._lblMessage.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# menufile1
		# 
		self._menufile1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._mnuFile,
			self._mnuColor,
			self._mnuHelp]))
		self._menufile1.Location = System.Drawing.Point(0, 0)
		self._menufile1.Name = "menufile1"
		self._menufile1.Size = System.Drawing.Size(281, 24)
		self._menufile1.TabIndex = 1
		self._menufile1.Text = "menuStrip1"
		# 
		# mnuFile
		# 
		self._mnuFile.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._mnuExit]))
		self._mnuFile.Name = "mnuFile"
		self._mnuFile.Size = System.Drawing.Size(37, 20)
		self._mnuFile.Text = "&File"
		# 
		# mnuExit
		# 
		self._mnuExit.Name = "mnuExit"
		self._mnuExit.Size = System.Drawing.Size(152, 22)
		self._mnuExit.Text = "&Exit"
		self._mnuExit.Click += self.MnuExitClick
		# 
		# mnuColor
		# 
		self._mnuColor.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._mnuRed,
			self._mnuGreen,
			self._mnuBlue,
			self._mnuBlack,
			self._toolStripMenuItem1,
			self._mnuVisible]))
		self._mnuColor.Name = "mnuColor"
		self._mnuColor.Size = System.Drawing.Size(48, 20)
		self._mnuColor.Text = "&Color"
		# 
		# mnuRed
		# 
		self._mnuRed.Name = "mnuRed"
		self._mnuRed.Size = System.Drawing.Size(152, 22)
		self._mnuRed.Text = "&Red"
		self._mnuRed.Click += self.MnuRedClick
		# 
		# mnuGreen
		# 
		self._mnuGreen.Name = "mnuGreen"
		self._mnuGreen.Size = System.Drawing.Size(152, 22)
		self._mnuGreen.Text = "&Green"
		self._mnuGreen.Click += self.MnuGreenClick
		# 
		# mnuBlue
		# 
		self._mnuBlue.Name = "mnuBlue"
		self._mnuBlue.Size = System.Drawing.Size(152, 22)
		self._mnuBlue.Text = "&Blue"
		self._mnuBlue.Click += self.MnuBlueClick
		# 
		# mnuBlack
		# 
		self._mnuBlack.Name = "mnuBlack"
		self._mnuBlack.Size = System.Drawing.Size(152, 22)
		self._mnuBlack.Text = "Blac&k"
		self._mnuBlack.Click += self.MnuBlackClick
		# 
		# toolStripMenuItem1
		# 
		self._toolStripMenuItem1.Name = "toolStripMenuItem1"
		self._toolStripMenuItem1.Size = System.Drawing.Size(149, 6)
		# 
		# mnuVisible
		# 
		self._mnuVisible.CheckOnClick = True
		self._mnuVisible.Name = "mnuVisible"
		self._mnuVisible.Size = System.Drawing.Size(152, 22)
		self._mnuVisible.Text = "Visible"
		self._mnuVisible.Click += self.VisableToolStripMenuItemClick
		# 
		# mnuHelp
		# 
		self._mnuHelp.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._mnuAbout]))
		self._mnuHelp.Name = "mnuHelp"
		self._mnuHelp.Size = System.Drawing.Size(44, 20)
		self._mnuHelp.Text = "&Help"
		# 
		# mnuAbout
		# 
		self._mnuAbout.Name = "mnuAbout"
		self._mnuAbout.Size = System.Drawing.Size(152, 22)
		self._mnuAbout.Text = "&About"
		self._mnuAbout.Click += self.MnuAboutClick
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(281, 243)
		self.Controls.Add(self._lblMessage)
		self.Controls.Add(self._menufile1)
		self.MainMenuStrip = self._menufile1
		self.Name = "MainForm"
		self.Text = "prog447MenuDemo"
		self._menufile1.ResumeLayout(False)
		self._menufile1.PerformLayout()
		self.ResumeLayout(False)
		self.PerformLayout()


	def VisableToolStripMenuItemClick(self, sender, e):
		if self.mnuVisible.Checked == True:
			self._lblMessage.Visible = True
		else:
			self._lblMessage.Visible = False

	def MnuExitClick(self, sender, e):
		Application.Exit()

	def MnuRedClick(self, sender, e):
		self._lblMessage.ForeColor = Color.Red

	def MnuGreenClick(self, sender, e):
		self._lblMessage.ForeColor = Color.Green

	def MnuBlueClick(self, sender, e):
		self._lblMessage.ForeColor = Color.Blue

	def MnuBlackClick(self, sender, e):
		self._lblMessage.ForeColor = Color.Black

	def MnuAboutClick(self, sender, e):
		MessageBox.Show("Menu System Demo\n"    
					"Designed for Starting Out "  
					"with Windows From Applications",
					"About Menu Demo")