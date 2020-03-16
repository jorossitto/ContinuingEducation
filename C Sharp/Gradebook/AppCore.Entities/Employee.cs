namespace AppCore.Entities
{
    public class Employee
    {
        public int EmployeeId { get; set; }
        public string Name { get; set; }

        public int LocationId { get; set; }

        //TODO fix barista change it to role.
        public bool Barista { get; set; }
    }
}