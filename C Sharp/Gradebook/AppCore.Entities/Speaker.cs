using System.Collections.Generic;
//using System.Windows.Forms;

namespace AppCore.Entities
{
    public class Speaker
    {
        public Speaker()
        {
            Certifications = new List<Certification>();
            Sessions = new List<Session>();
        }
        public int SpeakerId { get; set; }
        public int ConferenceId { get; set; }
        public Conference Conference { get; private set; }
        public virtual List<Session> Sessions { get; private set; }
        public virtual List<Certification> Certifications { get; private set; }

        public string FirstName { get; set; }
        public string MiddleName { get; set; }
        public string LastName { get; set; }
        public string Email { get; set; }
        public string Employer { get; set; }
        public int? YearsExperiance { get; set; }
        public string Company { get; set; }
        public string CompanyUrl { get; set; }
        public bool? HasBlog { get; set; }
        public string BlogUrl { get; set; }
        public string Browser { get; set; }
        public int? RegistrationFee { get; set; }
        public string Twitter { get; set; }
        public string GitHub { get; set; }
    }
}