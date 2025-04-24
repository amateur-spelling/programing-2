Console.Write("Enter the diameter of the pizza in inches: ");
int diameter = int.Parse(Console.ReadLine());
double sum = 0.05 * diameter * diameter + 0.65 + 1;
Console.Write("Cost to make your pizza: $" + sum);