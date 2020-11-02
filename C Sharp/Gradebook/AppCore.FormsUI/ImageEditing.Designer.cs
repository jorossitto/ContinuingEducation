namespace AppCore.FormsUI
{
    partial class ImageEditing
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.BrightenImage = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // BrightenImage
            // 
            this.BrightenImage.Location = new System.Drawing.Point(56, 396);
            this.BrightenImage.Name = "BrightenImage";
            this.BrightenImage.Size = new System.Drawing.Size(123, 23);
            this.BrightenImage.TabIndex = 0;
            this.BrightenImage.Text = "Brighten Image";
            this.BrightenImage.UseVisualStyleBackColor = true;
            this.BrightenImage.Click += new System.EventHandler(this.BrightenImage_Click);
            // 
            // ImageEditing
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.BrightenImage);
            this.Name = "ImageEditing";
            this.Text = "ImageEditing";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button BrightenImage;
    }
}