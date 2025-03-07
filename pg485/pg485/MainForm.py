import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.stotal = 0
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._radioButton12 = System.Windows.Forms.RadioButton()
		self._radioButton11 = System.Windows.Forms.RadioButton()
		self._radioButton10 = System.Windows.Forms.RadioButton()
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._radioButton15 = System.Windows.Forms.RadioButton()
		self._radioButton14 = System.Windows.Forms.RadioButton()
		self._radioButton13 = System.Windows.Forms.RadioButton()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._radioButton9 = System.Windows.Forms.RadioButton()
		self._radioButton8 = System.Windows.Forms.RadioButton()
		self._radioButton7 = System.Windows.Forms.RadioButton()
		self._radioButton6 = System.Windows.Forms.RadioButton()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._radioButton5 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._groupBox3.SuspendLayout()
		self._groupBox4.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.YellowGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(482, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(138, 89)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.YellowGreen
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(482, 137)
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
		self._button3.Location = System.Drawing.Point(482, 266)
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
		self._label1.Location = System.Drawing.Point(626, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(138, 89)
		self._label1.TabIndex = 7
		self._label1.Text = "Subtotal"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(626, 137)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(138, 89)
		self._label2.TabIndex = 8
		self._label2.Text = "Tax"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(626, 269)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(138, 89)
		self._label3.TabIndex = 9
		self._label3.Text = "Total"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# groupBox3
		# 
		self._groupBox3.BackColor = System.Drawing.Color.LimeGreen
		self._groupBox3.Controls.Add(self._radioButton12)
		self._groupBox3.Controls.Add(self._radioButton11)
		self._groupBox3.Controls.Add(self._radioButton10)
		self._groupBox3.Location = System.Drawing.Point(272, 13)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(204, 119)
		self._groupBox3.TabIndex = 10
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
		# groupBox4
		# 
		self._groupBox4.BackColor = System.Drawing.Color.LimeGreen
		self._groupBox4.Controls.Add(self._radioButton15)
		self._groupBox4.Controls.Add(self._radioButton14)
		self._groupBox4.Controls.Add(self._radioButton13)
		self._groupBox4.Location = System.Drawing.Point(272, 205)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(204, 119)
		self._groupBox4.TabIndex = 11
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
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.Color.LimeGreen
		self._groupBox2.Controls.Add(self._radioButton9)
		self._groupBox2.Controls.Add(self._radioButton8)
		self._groupBox2.Controls.Add(self._radioButton7)
		self._groupBox2.Controls.Add(self._radioButton6)
		self._groupBox2.Location = System.Drawing.Point(12, 205)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(239, 150)
		self._groupBox2.TabIndex = 12
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
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.LimeGreen
		self._groupBox1.Controls.Add(self._radioButton5)
		self._groupBox1.Controls.Add(self._radioButton4)
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(239, 182)
		self._groupBox1.TabIndex = 13
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Miscellaneous:"
		# 
		# radioButton5
		# 
		self._radioButton5.Location = System.Drawing.Point(7, 144)
		self._radioButton5.Name = "radioButton5"
		self._radioButton5.Size = System.Drawing.Size(104, 24)
		self._radioButton5.TabIndex = 4
		self._radioButton5.TabStop = True
		self._radioButton5.Text = "Assembly    $10"
		self._radioButton5.UseVisualStyleBackColor = True
		# 
		# radioButton4
		# 
		self._radioButton4.Location = System.Drawing.Point(7, 113)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(182, 24)
		self._radioButton4.TabIndex = 3
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "Nut/Bolt kit $3"
		self._radioButton4.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(7, 82)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Rising pads $2"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(7, 51)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Bearing       $30"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(7, 20)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Grip tape     $10"
		self._radioButton1.UseVisualStyleBackColor = True
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		self._radioButton1.Click += self.RadioButton1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.PaleGreen
		self.ClientSize = System.Drawing.Size(782, 448)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox4)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "pg485"
		self._groupBox3.ResumeLayout(False)
		self._groupBox4.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button3Click(self, sender, e):
		pass

	def Button4Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		total = 0
		tax = 0
		
		self._label1.Text == str(self.stotal)

	def RadioButton1CheckedChanged(self, sender, e):
		self.stotal += 5

	def RadioButton1Click(self, sender, e):
		pass