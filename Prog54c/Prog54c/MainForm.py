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
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(352, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(125, 32)
		self._button1.TabIndex = 0
		self._button1.Text = "Calulate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(352, 50)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(125, 35)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(352, 92)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(125, 34)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.CadetBlue
		self._label1.Location = System.Drawing.Point(12, 68)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(152, 56)
		self._label1.TabIndex = 3
		self._label1.Text = "label1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.CadetBlue
		self._label2.Location = System.Drawing.Point(178, 69)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(154, 55)
		self._label2.TabIndex = 4
		self._label2.Text = "label2"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(128, 24)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 5
		self._textBox1.Text = "3.712"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(489, 138)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Var1 = float(self._textBox1.Text)
		Pi = 3.14159
		
		Area = round((Var1**2) * Pi,3)
		Dim = round((Var1 * 2) * Pi,3)
		
		self._label1.Text = str(Area)
		self._label2.Text = str(Dim)