using AppCore.Data;
using AppCore.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AppCore.Repository
{
    public class SpeakerRepository
    {
        private BusinessDBContext context;
        public SpeakerRepository(BusinessDBContext context)
        {
            this.context = context;
        }

        public SpeakerRepository()
        {
            this.context = new BusinessDBContext();
        }

        public IEnumerable<Speaker> GetSpeakers()
        {
            return context.Speakers.ToList();
        }

        public void AddSpeaker(Speaker speaker)
        {
            try
            {
                context.Speakers.Add(speaker);
            }
            catch (Exception)
            {
                //potentially handled exception, log
                throw;
            }
        }

        public bool SaveChanges()
        {
            return context.SaveChanges() > 0;
        }
    }
}
