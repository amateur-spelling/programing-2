using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Progpay
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        const int intMAX_EMPLOYEES = 5;
        const decimal decHOURLY_PAY_RATE = 6.0m;
        private void button1_Click(object sender, EventArgs e)
        {
            // calc & display gross pay earned by employees
            int[] intHours = new int[intMAX_EMPLOYEES];


        }
    }
}
