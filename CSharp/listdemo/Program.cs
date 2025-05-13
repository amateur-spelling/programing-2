List<int> nums = new List<int>() { 1, 2, 3 };
nums.Add(2);
nums.Add(7);
//List<TYPE> name = new List<TYPE>();
nums.Remove(7);
Console.WriteLine("Length: " + nums.Count);
Console.WriteLine(String.Join(", ", nums));

foreach (int n in nums)
    Console.WriteLine(n); 
