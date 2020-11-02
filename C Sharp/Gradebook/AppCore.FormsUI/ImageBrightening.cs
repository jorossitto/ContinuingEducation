using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace AppCore.FormsUI
{
    public partial class ImageBrightening : Form
    {
        public int brightnessValue;
        public ImageBrightening()
        {
            InitializeComponent();
        }

        private void Submit_Click(object sender, EventArgs e)
        {
            brightnessValue = int.Parse(brightnessTxt.Text);
        }

        public void brightnessTxt_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
