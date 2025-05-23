﻿import System.Drawing
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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Chocolate
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 102)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(109, 68)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Chocolate
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(127, 102)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(109, 68)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Chocolate
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(242, 102)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(109, 68)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Peru
		self._textBox1.Location = System.Drawing.Point(172, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(179, 20)
		self._textBox1.TabIndex = 3
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.SaddleBrown
		self._label1.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label1.Location = System.Drawing.Point(12, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(109, 20)
		self._label1.TabIndex = 4
		self._label1.Text = "Pizza Diameter"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.SaddleBrown
		self._label2.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label2.Location = System.Drawing.Point(12, 60)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(109, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Cost to Make"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Peru
		self._label3.Location = System.Drawing.Point(172, 60)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(179, 20)
		self._label3.TabIndex = 6
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SandyBrown
		self.ClientSize = System.Drawing.Size(365, 184)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "LP3-2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		sum = 0.0
		diameter = float(self._textBox1.Text)
		
		sum = round(0.75 + 1.00 + 0.05 * diameter * diameter, 2)
		self._label3.Text = str(sum)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label3.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit