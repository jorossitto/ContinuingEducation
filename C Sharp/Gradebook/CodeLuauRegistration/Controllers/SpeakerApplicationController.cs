using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using CodeLuauRegistration.Models;
using AppCore.Repository;
using AppCore.Entities;
using AppCore.Data;

namespace CodeLuauRegistration.Controllers
{
    public class SpeakerApplicationController : Controller
    {


        //Post: /SpeakerApplication/
        [HttpPost]
        public ActionResult Index(SpeakerApplicationModel model)
        {
            var speakerRepository = new SpeakerRepository();
            
            if(ModelState.IsValid)
            {
                //speakerRepository.AddSpeaker(model);

                var speaker = new Speaker()
                {
                    FirstName = model.FirstName,
                    LastName = model.LastName,
                    Email = model.Email,
                    Employer = model.Employer,
                    YearsExperiance = model.YearsExperiance,
                    BlogUrl = model.BlogUrl,
                    //Browser = new BusinessLayer.WebBrowswer(Request.Browser.Type, Request.Browser.MajorVersion)
                };

                foreach (var certification in model.Certifications)
                {
                    speaker.Certifications.Add(certification);
                }
                foreach (var session in model.Sessions)
                {
                    speaker.Sessions.Add(new Session());
                }
                return View("Congrats");
            }
            return View(model);
        }
    }
}
