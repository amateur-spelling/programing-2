
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Student(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._label7 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._groupBox3.SuspendLayout()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Olive
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(199, 287)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(166, 78)
		self._button2.TabIndex = 8
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Olive
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(25, 287)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(166, 78)
		self._button1.TabIndex = 7
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
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
		self._groupBox3.Location = System.Drawing.Point(25, 122)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(340, 159)
		self._groupBox3.TabIndex = 5
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Total Cost"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.LightGreen
		self._label7.Location = System.Drawing.Point(80, 120)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(173, 23)
		self._label7.TabIndex = 5
		self._label7.Text = "label7"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightGreen
		self._label6.Location = System.Drawing.Point(80, 73)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(173, 23)
		self._label6.TabIndex = 4
		self._label6.Text = "label6"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightGreen
		self._label5.Location = System.Drawing.Point(80, 30)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(173, 23)
		self._label5.TabIndex = 3
		self._label5.Text = "label5"
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
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.LimeGreen
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(25, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(340, 94)
		self._groupBox1.TabIndex = 4
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "How many tickets?"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(247, 59)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(87, 20)
		self._textBox1.TabIndex = 1
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
		# Student
		# 
		self.BackColor = System.Drawing.Color.OliveDrab
		self.ClientSize = System.Drawing.Size(386, 392)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox1)
		self.Name = "Student"
		self.Text = "Student"
		self._groupBox3.ResumeLayout(False)
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)

