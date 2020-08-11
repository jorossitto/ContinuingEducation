using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AppCore.FormsUI
{
    //double[,] problemTwoMatrix = new double[,] { {1,3.2}, {2, 6.4 }


    public partial class NeuralNetworkForm : Form
    {
        public NeuralNetworkForm()
        {
            InitializeComponent();
        }

        private void Training_Click(object sender, EventArgs e)
        {
            //ProblemOne();
            IList<double> problemTwoX = new List<double>() { 1, 2, 3, 4, 5, 6 };
            IList<double> problemTwoY = new List<double>() { 3.2, 6.4, 10.5, 17.7, 28.1, 38.5 };
        }

        private void ProblemOne()
        {
            double w = 0.1;
            double b = 0.4;
            double x = 0;
            for (int j = 0; j < 1000; j++)
            {
                for (int i = 1; i < 10; i++)
                {
                    x = i;
                    double newW = newWeight(x, w, b);
                    double newb = newBias(x, w, b);
                    w = newW;
                    b = newb;
                }
            }
            MessageBox.Show("w = " + w.ToString() + " b =" + b.ToString());
        }

        double newWeight(double x, double w, double b)
        {
            // compute output
            double a = w * x + b;
            double y = 0.3 * x + 2;
            double gradw = -1 * (y - a) * x;
            w = w - 0.01 * gradw;
            return w;
        }
        double newBias(double x, double w, double b)
        {
            // compute output
            double a = w * x + b;
            double y = 0.3 * x + 2;
            double gradb = -1 * (y - a) * 1;
            b = b - 0.01 * gradb;
            return b;
        }


    }
}
