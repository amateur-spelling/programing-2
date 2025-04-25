Console.Write("Enter # of copies to print: ");
int copies = int.Parse(Console.ReadLine());
double price = 0;
double cost = 0;
// && and, || or, ! not, 
if (copies > 0 && copies <= 99) price = 0.30;
else if (copies > 99 && copies <= 499) price = 0.28;
else if (copies > 500 && copies <= 749) price = 0.27;
else if (copies > 750 && copies <= 999) price = 0.26;
else if (copies > 1000) price = 0.25;
else Console.WriteLine("Invalid number of copies!");
cost = price * copies;
Console.Write("Price per copy: " + price);
Console.ReadLine();
Console.Write("Total cost: $" + cost);
Console.ReadLine();