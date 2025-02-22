﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Green
		self._button3.Location = System.Drawing.Point(172, 12)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(196, 80)
		self._button3.TabIndex = 2
		self._button3.Text = "Calulate"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.ForestGreen
		self._label1.Location = System.Drawing.Point(12, 132)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "label1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.ForestGreen
		self._label2.Location = System.Drawing.Point(12, 183)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "label2"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.LimeGreen
		self._textBox1.Location = System.Drawing.Point(12, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.LimeGreen
		self._textBox2.Location = System.Drawing.Point(12, 38)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 6
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.LimeGreen
		self._textBox3.Location = System.Drawing.Point(12, 64)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 7
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.Color.LimeGreen
		self._textBox4.Location = System.Drawing.Point(12, 90)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 8
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.Green
		self._button4.Location = System.Drawing.Point(172, 183)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(196, 80)
		self._button4.TabIndex = 9
		self._button4.Text = "Exit"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.Color.Green
		self._button5.Location = System.Drawing.Point(172, 98)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(196, 80)
		self._button5.TabIndex = 10
		self._button5.Text = "Clear"
		self._button5.UseVisualStyleBackColor = False
		self._button5.Click += self.Button5Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkGreen
		self.ClientSize = System.Drawing.Size(379, 275)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Name = "MainForm"
		self.Text = "prog 54b"
		self.ResumeLayout(False)
		self.PerformLayout()

		
	def Label2Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		
		Var1 = int(self._textBox1.Text)
		Var2 = int(self._textBox2.Text)
		Var3 = int(self._textBox3.Text)
		Var4 = int(self._textBox4.Text)
		
		
		Sum = float(Var1) + float(Var2) + float(Var3) + float(Var4)
		Ave = float(Sum/4)
		
		self._label1.Text = str(Sum)
		
		self._label2.Text = str(Ave)

	def Button5Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._label1.Text = ""
		self._label2.Text = ""

	def Button4Click(self, sender, e):
		Application.Exit()