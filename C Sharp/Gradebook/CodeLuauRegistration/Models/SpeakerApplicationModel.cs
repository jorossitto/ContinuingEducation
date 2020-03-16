using AppCore.Entities;
using System.Collections.Generic;

namespace CodeLuauRegistration.Controllers
{
    public class SpeakerApplicationModel
    {
        public SpeakerApplicationModel()
        {
        }

        public string FirstName { get; internal set; }
        public string LastName { get; internal set; }
        public string Email { get; internal set; }
        public string Employer { get; internal set; }
        public int? YearsExperiance { get; internal set; }
        public string BlogUrl { get; internal set; }
        public IEnumerable<Session> Sessions { get; internal set; }
        public IEnumerable<Certification> Certifications { get; internal set; }
    }
}