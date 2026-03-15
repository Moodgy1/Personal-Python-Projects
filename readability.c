#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text
    int tlength = strlen(text);
    int letters = 0;
    int words = 1;
    int sentences = 0;
    for (int i = 0; i < tlength; i++)
    {
        if (text[i] == ' ')
        {
            words++;
        }
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
        if (isalpha(text[i]))
        {
            letters++;
        }
    }

    // Compute the Coleman-Liau index
    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int result = round(index);
    // Print the grade level
    if (result < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (result >= 1 && result < 16)
    {
        printf("Grade %i\n", result);
    }
    else
    {
        printf("Grade 16+\n");
    }
}
