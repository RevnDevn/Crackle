namespace Crackle
{
    public class FoodRecallQueryResult
    {
        public ResultsMeta Meta { get; set; } = new();
        public List<FoodRecall> Results { get; set; } = new();
    }
}
