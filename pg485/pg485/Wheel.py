
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Wheel(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.myparent = parent
	
	def InitializeComponent(self):
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._radioButton9 = System.Windows.Forms.RadioButton()
		self._radioButton8 = System.Windows.Forms.RadioButton()
		self._radioButton7 = System.Windows.Forms.RadioButton()
		self._radioButton6 = System.Windows.Forms.RadioButton()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.Color.LimeGreen
		self._groupBox2.Controls.Add(self._radioButton9)
		self._groupBox2.Controls.Add(self._radioButton8)
		self._groupBox2.Controls.Add(self._radioButton7)
		self._groupBox2.Controls.Add(self._radioButton6)
		self._groupBox2.Location = System.Drawing.Point(12, 12)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(239, 150)
		self._groupBox2.TabIndex = 2
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Wheel sets:"
		# 
		# radioButton9
		# 
		self._radioButton9.Location = System.Drawing.Point(7, 113)
		self._radioButton9.Name = "radioButton9"
		self._radioButton9.Size = System.Drawing.Size(104, 24)
		self._radioButton9.TabIndex = 3
		self._radioButton9.TabStop = True
		self._radioButton9.Text = "61mm $28"
		self._radioButton9.UseVisualStyleBackColor = True
		# 
		# radioButton8
		# 
		self._radioButton8.Location = System.Drawing.Point(7, 82)
		self._radioButton8.Name = "radioButton8"
		self._radioButton8.Size = System.Drawing.Size(104, 24)
		self._radioButton8.TabIndex = 2
		self._radioButton8.TabStop = True
		self._radioButton8.Text = "58mm $24"
		self._radioButton8.UseVisualStyleBackColor = True
		# 
		# radioButton7
		# 
		self._radioButton7.Location = System.Drawing.Point(7, 51)
		self._radioButton7.Name = "radioButton7"
		self._radioButton7.Size = System.Drawing.Size(104, 24)
		self._radioButton7.TabIndex = 1
		self._radioButton7.TabStop = True
		self._radioButton7.Text = "55mm $22"
		self._radioButton7.UseVisualStyleBackColor = True
		# 
		# radioButton6
		# 
		self._radioButton6.Location = System.Drawing.Point(7, 20)
		self._radioButton6.Name = "radioButton6"
		self._radioButton6.Size = System.Drawing.Size(104, 24)
		self._radioButton6.TabIndex = 0
		self._radioButton6.TabStop = True
		self._radioButton6.Text = "51mm $20"
		self._radioButton6.UseVisualStyleBackColor = True
		# 
		# Wheel
		# 
		self.BackColor = System.Drawing.Color.PaleGreen
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._groupBox2)
		self.Name = "Wheel"
		self.Text = "Wheel"
		self.FormClosing += self.WheelFormClosing
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)


	def WheelFormClosing(self, sender, e):
		self.myparent.Show()