
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Truck(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.myparent = parent
	
	def InitializeComponent(self):
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._radioButton15 = System.Windows.Forms.RadioButton()
		self._radioButton14 = System.Windows.Forms.RadioButton()
		self._radioButton13 = System.Windows.Forms.RadioButton()
		self._groupBox4.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox4
		# 
		self._groupBox4.BackColor = System.Drawing.Color.LimeGreen
		self._groupBox4.Controls.Add(self._radioButton15)
		self._groupBox4.Controls.Add(self._radioButton14)
		self._groupBox4.Controls.Add(self._radioButton13)
		self._groupBox4.Location = System.Drawing.Point(12, 12)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(186, 119)
		self._groupBox4.TabIndex = 4
		self._groupBox4.TabStop = False
		self._groupBox4.Text = "Truck assemblies:"
		# 
		# radioButton15
		# 
		self._radioButton15.Location = System.Drawing.Point(7, 81)
		self._radioButton15.Name = "radioButton15"
		self._radioButton15.Size = System.Drawing.Size(104, 24)
		self._radioButton15.TabIndex = 2
		self._radioButton15.TabStop = True
		self._radioButton15.Text = "8.5 axle   $45"
		self._radioButton15.UseVisualStyleBackColor = True
		# 
		# radioButton14
		# 
		self._radioButton14.Location = System.Drawing.Point(7, 50)
		self._radioButton14.Name = "radioButton14"
		self._radioButton14.Size = System.Drawing.Size(104, 24)
		self._radioButton14.TabIndex = 1
		self._radioButton14.TabStop = True
		self._radioButton14.Text = "8.0 axle   $40"
		self._radioButton14.UseVisualStyleBackColor = True
		# 
		# radioButton13
		# 
		self._radioButton13.Location = System.Drawing.Point(7, 19)
		self._radioButton13.Name = "radioButton13"
		self._radioButton13.Size = System.Drawing.Size(104, 24)
		self._radioButton13.TabIndex = 0
		self._radioButton13.TabStop = True
		self._radioButton13.Text = "7.75 axle $35"
		self._radioButton13.UseVisualStyleBackColor = True
		# 
		# Truck
		# 
		self.BackColor = System.Drawing.Color.PaleGreen
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._groupBox4)
		self.Name = "Truck"
		self.Text = "Truck"
		self.FormClosing += self.TruckFormClosing
		self._groupBox4.ResumeLayout(False)
		self.ResumeLayout(False)


	def TruckFormClosing(self, sender, e):
		self.myparent.Show()