
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class General(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.LimeGreen
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(340, 94)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "How many tickets?"
		# 
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.Color.LimeGreen
		self._groupBox2.Controls.Add(self._radioButton3)
		self._groupBox2.Controls.Add(self._radioButton2)
		self._groupBox2.Controls.Add(self._radioButton1)
		self._groupBox2.Location = System.Drawing.Point(13, 114)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(161, 159)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Section"
		# 
		# groupBox3
		# 
		self._groupBox3.BackColor = System.Drawing.Color.LimeGreen
		self._groupBox3.Controls.Add(self._label7)
		self._groupBox3.Controls.Add(self._label6)
		self._groupBox3.Controls.Add(self._label5)
		self._groupBox3.Controls.Add(self._label4)
		self._groupBox3.Controls.Add(self._label3)
		self._groupBox3.Controls.Add(self._label2)
		self._groupBox3.Location = System.Drawing.Point(180, 114)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(173, 159)
		self._groupBox3.TabIndex = 0
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Total Cost"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(141, 59)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 20)
		self._label1.TabIndex = 0
		self._label1.Text = """Number of tickets:
"""
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(247, 59)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(87, 20)
		self._textBox1.TabIndex = 1
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(6, 30)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Section A"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(6, 72)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Section B"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(6, 120)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Section C"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.ForestGreen
		self._label2.Location = System.Drawing.Point(7, 30)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(67, 23)
		self._label2.TabIndex = 0
		self._label2.Text = "Tickets:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.ForestGreen
		self._label3.Location = System.Drawing.Point(7, 73)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(67, 23)
		self._label3.TabIndex = 1
		self._label3.Text = "Tax:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.ForestGreen
		self._label4.Location = System.Drawing.Point(7, 120)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(67, 23)
		self._label4.TabIndex = 2
		self._label4.Text = "Total:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightGreen
		self._label5.Location = System.Drawing.Point(80, 30)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(87, 23)
		self._label5.TabIndex = 3
		self._label5.Text = "label5"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightGreen
		self._label6.Location = System.Drawing.Point(80, 73)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(87, 23)
		self._label6.TabIndex = 4
		self._label6.Text = "label6"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.LightGreen
		self._label7.Location = System.Drawing.Point(80, 120)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(87, 23)
		self._label7.TabIndex = 5
		self._label7.Text = "label7"
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(39, 288)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(113, 50)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(208, 288)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(118, 50)
		self._button2.TabIndex = 3
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		# 
		# General
		# 
		self.BackColor = System.Drawing.Color.OliveDrab
		self.ClientSize = System.Drawing.Size(365, 350)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "General"
		self.Text = "General"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		numtick = 0
		tickcost = 0.0
		saletax = 0.0
		total = 0.0
		
		numtick = textBox1.Text
		