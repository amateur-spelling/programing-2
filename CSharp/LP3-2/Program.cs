Console.Write("Enter the diameter of the pizza in inches: ");
int diameter = int.Parse(Console.ReadLine());
int sum = 0.05 * diameter ** 2;
Console.Write("Cost to make your pizza: " + sum)