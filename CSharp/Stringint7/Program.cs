Console.Write("Enter a string: ");
string word = Console.ReadLine().ToLower();

int v = 0;
int c = 0; 

for (int i = 0; i < word.Length; i++)
{
    char letter = word[i];
    if (letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u') v++;
    else if (letter >= 'a' && letter <= 'z') c++;

}
Console.WriteLine("{0} contains {1} vowels and {2} consonants", word, v, c);
Console.ReadLine();