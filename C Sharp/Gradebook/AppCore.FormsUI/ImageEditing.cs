using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace AppCore.FormsUI
{
    public partial class ImageEditing : Form
    {
        public ImageEditing()
        {
            InitializeComponent();
        }

        private void BrightenImage_Click(object sender, EventArgs e)
        {
            ImageBrightening formBrighten = new ImageBrightening();
            //formBrighten.Show();

            if(formBrighten.ShowDialog() == DialogResult.OK)
            {
                int brightness = (formBrighten.brightnessValue);
                MessageBox.Show(brightness.ToString());

            }
        }
    }
}
