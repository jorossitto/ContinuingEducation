namespace AppCore.FormsUI
{
    partial class ImageBrightening
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
            this.Submit = new System.Windows.Forms.Button();
            this.brightnessTxt = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // Submit
            // 
            this.Submit.DialogResult = System.Windows.Forms.DialogResult.OK;
            this.Submit.Location = new System.Drawing.Point(286, 41);
            this.Submit.Name = "Submit";
            this.Submit.Size = new System.Drawing.Size(75, 23);
            this.Submit.TabIndex = 0;
            this.Submit.Text = "Submit";
            this.Submit.UseVisualStyleBackColor = true;
            this.Submit.Click += new System.EventHandler(this.Submit_Click);
            // 
            // brightnessTxt
            // 
            this.brightnessTxt.Location = new System.Drawing.Point(27, 38);
            this.brightnessTxt.Name = "brightnessTxt";
            this.brightnessTxt.Size = new System.Drawing.Size(234, 23);
            this.brightnessTxt.TabIndex = 1;
            this.brightnessTxt.TextChanged += new System.EventHandler(this.brightnessTxt_TextChanged);
            // 
            // ImageBrightening
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(381, 92);
            this.Controls.Add(this.brightnessTxt);
            this.Controls.Add(this.Submit);
            this.Name = "ImageBrightening";
            this.Text = "ImageBrightening";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button Submit;
        private System.Windows.Forms.TextBox brightnessTxt;
    }
}