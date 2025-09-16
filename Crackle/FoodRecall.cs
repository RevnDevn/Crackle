using Microsoft.AspNetCore.Components.QuickGrid;

namespace Crackle
{
    public class FoodRecall
    {
        public int Event_Id { get; set; }

        public string State { get; set; }

        public string City { get; set; }
        public string Recalling_Firm { get; set; }
        public string Status { get; set; }

        // Static readonly property that returns an empty FoodRecall object
        private static readonly FoodRecall emptyInstance = new FoodRecall
        {
            Event_Id = 0,
            State = string.Empty,
            City = string.Empty,
            Recalling_Firm = string.Empty,
            Status = string.Empty
        };

        public static FoodRecall Empty => emptyInstance;
    }
}
