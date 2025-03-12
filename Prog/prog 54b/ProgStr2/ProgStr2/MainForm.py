import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 10)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter Word1:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(13, 83)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Duplicates:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label2.Click += self.Label2Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 121)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(260, 64)
		self._button1.TabIndex = 2
		self._button1.Text = "Print"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.OliveDrab
		self._label3.ForeColor = System.Drawing.Color.WhiteSmoke
		self._label3.Location = System.Drawing.Point(85, 83)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 3
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label3.Click += self.Label3Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(12, 205)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(260, 64)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Olive
		self._textBox1.ForeColor = System.Drawing.Color.WhiteSmoke
		self._textBox1.Location = System.Drawing.Point(85, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 6
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Olive
		self._textBox2.ForeColor = System.Drawing.Color.WhiteSmoke
		self._textBox2.Location = System.Drawing.Point(85, 48)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 8
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(13, 46)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Enter Word2:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkKhaki
		self.ClientSize = System.Drawing.Size(284, 276)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "ProgStr2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label3.Text = ""
		word1 = self._textBox1.Text.lower()
		word2 = self._textBox2.Text.lower()
		
		if len(word1) != len(word2):
			self._label3.Text = "False"
			return
		else:
			for lcv in range(len(word1)):
				c = word1[lcv]
				index = word2.find(c)
				if index == -1:
					self._label3.Text = "False"
				else:
					word2 = word2[0:index] + word2[index+1:]
		self._label3.Text = str(len(word2) == 0)

	def Label3Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._label3.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""

	def Label1Click(self, sender, e):
		pass