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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.YellowGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(188, 9)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(138, 89)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.YellowGreen
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(188, 133)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(138, 89)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.YellowGreen
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(188, 262)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(138, 89)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(332, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(138, 89)
		self._label1.TabIndex = 7
		self._label1.Text = "Subtotal"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(332, 133)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(138, 89)
		self._label2.TabIndex = 8
		self._label2.Text = "Tax"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(332, 265)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(138, 89)
		self._label3.TabIndex = 9
		self._label3.Text = "Total"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.LimeGreen
		self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(13, 13)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(154, 61)
		self._button4.TabIndex = 10
		self._button4.Text = "Miscellaneous"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.Color.LimeGreen
		self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(12, 92)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(155, 63)
		self._button5.TabIndex = 11
		self._button5.Text = "Wheel"
		self._button5.UseVisualStyleBackColor = False
		# 
		# button6
		# 
		self._button6.BackColor = System.Drawing.Color.LimeGreen
		self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(12, 172)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(155, 73)
		self._button6.TabIndex = 12
		self._button6.Text = "Truck"
		self._button6.UseVisualStyleBackColor = False
		# 
		# button7
		# 
		self._button7.BackColor = System.Drawing.Color.LimeGreen
		self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(12, 262)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(155, 75)
		self._button7.TabIndex = 13
		self._button7.Text = "Deck"
		self._button7.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.PaleGreen
		self.ClientSize = System.Drawing.Size(504, 363)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "pg485"
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		pass

	def Button4Click(self, sender, e):
		pass