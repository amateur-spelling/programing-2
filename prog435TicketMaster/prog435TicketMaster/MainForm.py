import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(313, 227)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Selcet the Type of Ticket Sales"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(7, 32)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(139, 41)
		self._label1.TabIndex = 0
		self._label1.Text = """Select General Sales for all ticket sales to the General Public
"""
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(7, 122)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(139, 36)
		self._label2.TabIndex = 1
		self._label2.Text = "Select Student Sales for all ticket sales to Students"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(337, 252)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "prog435TicketMaster"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)

