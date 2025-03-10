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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Goldenrod
		self._button1.Location = System.Drawing.Point(169, 12)
		self._button1.Name = "button1"
		self._button1.RightToLeft = System.Windows.Forms.RightToLeft.No
		self._button1.Size = System.Drawing.Size(103, 70)
		self._button1.TabIndex = 0
		self._button1.Text = "Print"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Goldenrod
		self._button2.Location = System.Drawing.Point(169, 88)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(103, 70)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Goldenrod
		self._button3.Location = System.Drawing.Point(169, 164)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(103, 70)
		self._button3.TabIndex = 1
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(12, 25)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(138, 20)
		self._textBox1.TabIndex = 2
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Goldenrod
		self._label1.Location = System.Drawing.Point(12, 52)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(151, 182)
		self._label1.TabIndex = 3
		self._label1.Text = "label1"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Orange
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Stringinterview3"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		string = self._textBox1.Text
		retur = ""
		perchance = 0
		check = 0
		lcv = 0	
		while lcv <= len(string)-1:
			if string[check] == string[lcv]:
				perchance += 1
			lcv += 1
			if perchance > 1:
				check += 1 
				lcv = 0
				perchance = 0
			else: 
				retur = string[check]
				self._label1.Text = retur
	
			
			
	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label1.Text = ""