﻿import System.Drawing
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
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter Text:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(13, 61)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Duplicates:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label2.Click += self.Label2Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 98)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(260, 64)
		self._button1.TabIndex = 2
		self._button1.Text = "Print"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightSkyBlue
		self._label3.Location = System.Drawing.Point(76, 61)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 3
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label3.Click += self.Label3Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(12, 185)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(260, 64)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(76, 15)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 6
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "ProgStr1"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label3.Text = ""
		myStr = self._textBox1.Text.lower()
		for lcv in range(len(myStr)):
			for lcv2 in range(lcv+1, len(myStr)):
				ltr1 = myStr[lcv]
				ltr2 = myStr[lcv2]
				if ltr1 == ltr2:
					self._label3.Text += ltr2 + " "

	def Label3Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._label3.Text = ""
		self._textBox1.Text = ""