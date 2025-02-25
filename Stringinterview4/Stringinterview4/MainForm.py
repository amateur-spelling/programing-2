import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.OrangeRed
		self._button1.Location = System.Drawing.Point(130, 21)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(106, 71)
		self._button1.TabIndex = 0
		self._button1.Text = "Print"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.OrangeRed
		self._button2.Location = System.Drawing.Point(130, 98)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(106, 72)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.OrangeRed
		self._button3.Location = System.Drawing.Point(130, 176)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(106, 77)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Tomato
		self._label1.Location = System.Drawing.Point(2, 68)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(122, 185)
		self._label1.TabIndex = 3
		self._label1.Text = "label1"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(13, 21)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self.ClientSize = System.Drawing.Size(248, 265)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Stringinterview4"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		string = self._textBox1.Text
		lcv = len(string) - 1
		baring = ""
		while lcv > 0:
			baring += string[lcv]
			lcv -= 1
		baring += string[0]
		self._label1.Text = baring

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label1.Text = ""
		

	def Button3Click(self, sender, e):
		Application.Exit()