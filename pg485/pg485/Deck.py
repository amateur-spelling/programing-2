
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Deck(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.myparent = parent
	
	def InitializeComponent(self):
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._radioButton12 = System.Windows.Forms.RadioButton()
		self._radioButton11 = System.Windows.Forms.RadioButton()
		self._radioButton10 = System.Windows.Forms.RadioButton()
		self._groupBox3.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox3
		# 
		self._groupBox3.BackColor = System.Drawing.Color.LimeGreen
		self._groupBox3.Controls.Add(self._radioButton12)
		self._groupBox3.Controls.Add(self._radioButton11)
		self._groupBox3.Controls.Add(self._radioButton10)
		self._groupBox3.Location = System.Drawing.Point(12, 12)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(238, 119)
		self._groupBox3.TabIndex = 3
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Deck:"
		# 
		# radioButton12
		# 
		self._radioButton12.Location = System.Drawing.Point(7, 82)
		self._radioButton12.Name = "radioButton12"
		self._radioButton12.Size = System.Drawing.Size(158, 24)
		self._radioButton12.TabIndex = 6
		self._radioButton12.TabStop = True
		self._radioButton12.Text = "The Street King         $50"
		self._radioButton12.UseVisualStyleBackColor = True
		# 
		# radioButton11
		# 
		self._radioButton11.Location = System.Drawing.Point(7, 51)
		self._radioButton11.Name = "radioButton11"
		self._radioButton11.Size = System.Drawing.Size(158, 24)
		self._radioButton11.TabIndex = 5
		self._radioButton11.TabStop = True
		self._radioButton11.Text = "The Dictator of Grind $45"
		self._radioButton11.UseVisualStyleBackColor = True
		# 
		# radioButton10
		# 
		self._radioButton10.Location = System.Drawing.Point(6, 20)
		self._radioButton10.Name = "radioButton10"
		self._radioButton10.Size = System.Drawing.Size(159, 24)
		self._radioButton10.TabIndex = 4
		self._radioButton10.TabStop = True
		self._radioButton10.Text = "The Master Thrasher $60"
		self._radioButton10.UseVisualStyleBackColor = True
		# 
		# Deck
		# 
		self.BackColor = System.Drawing.Color.PaleGreen
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._groupBox3)
		self.Name = "Deck"
		self.Text = "Deck"
		self.FormClosing += self.DeckFormClosing
		self._groupBox3.ResumeLayout(False)
		self.ResumeLayout(False)


	def DeckFormClosing(self, sender, e):
		self.myparent.Show()