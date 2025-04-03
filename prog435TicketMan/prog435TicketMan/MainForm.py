import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.LimeGreen
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Controls.Add(self._button2)
		self._groupBox1.Controls.Add(self._button1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(307, 229)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Select ticket sale type"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(175, 19)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(116, 64)
		self._button1.TabIndex = 0
		self._button1.Text = "&General Sales"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightGreen
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(175, 146)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(116, 64)
		self._button2.TabIndex = 1
		self._button2.Text = "&Student Sales"
		self._button2.UseVisualStyleBackColor = False
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.ForestGreen
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.Desktop
		self._label1.Location = System.Drawing.Point(7, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(162, 63)
		self._label1.TabIndex = 2
		self._label1.Text = "select General Sales for all ticket sales to the general public"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.ForestGreen
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.SystemColors.Desktop
		self._label2.Location = System.Drawing.Point(7, 146)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(162, 64)
		self._label2.TabIndex = 3
		self._label2.Text = "Select Student Sales for all ticket sales to students"
		self._label2.Click += self.Label2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightGreen
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(242, 271)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(126, 49)
		self._button3.TabIndex = 1
		self._button3.Text = "E&xit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.OliveDrab
		self.ClientSize = System.Drawing.Size(396, 332)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "prog435TicketMan"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		Application.Exit()

	def Label2Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		general = General(self)
		General = show()
		self = Hide()