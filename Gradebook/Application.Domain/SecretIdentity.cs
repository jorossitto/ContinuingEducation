﻿using System.Collections.Generic;

namespace AppFramework.Domain
{
    public class SecretIdentity
    {
        public int Id { get; set; }
        public string RealName { get; set; }
        public int? SamuraiId { get; set; }
        //public Samurai samurai { get; set; }
    }
}
