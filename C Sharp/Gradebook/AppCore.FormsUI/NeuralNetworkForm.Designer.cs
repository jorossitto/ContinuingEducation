namespace AppCore.FormsUI
{
    partial class NeuralNetworkForm
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
            this.Training = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // Training
            // 
            this.Training.Location = new System.Drawing.Point(294, 60);
            this.Training.Name = "Training";
            this.Training.Size = new System.Drawing.Size(179, 55);
            this.Training.TabIndex = 0;
            this.Training.Text = "Train Network";
            this.Training.UseVisualStyleBackColor = true;
            this.Training.Click += new System.EventHandler(this.Training_Click);
            // 
            // NeuralNetworkForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.Training);
            this.Name = "NeuralNetworkForm";
            this.Text = "NeuralNetworkForm";
            this.Load += new System.EventHandler(this.NeuralNetworkForm_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button Training;
    }
}