import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Salmon
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(162, 238)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.OrangeRed
		self._button1.ForeColor = System.Drawing.Color.Indigo
		self._button1.Location = System.Drawing.Point(182, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(90, 43)
		self._button1.TabIndex = 1
		self._button1.Text = "Print"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.OrangeRed
		self._button2.ForeColor = System.Drawing.Color.Indigo
		self._button2.Location = System.Drawing.Point(182, 62)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(90, 43)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.OrangeRed
		self._button3.ForeColor = System.Drawing.Color.Indigo
		self._button3.Location = System.Drawing.Point(181, 111)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(90, 43)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Tomato
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Lang122b"
		self.ResumeLayout(False)


	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button1Click(self, sender, e):
		self._listBox1.Items.Clear()
		for lcv in range(0,41,1):
			line = lcv * 4.00
			self._listBox1.Items.Add(str(lcv) + "\t" + str(line))			
		

	def Button3Click(self, sender, e):
		Application.Exit()