#include <stdio.h>
#include <cs50.h>
#include <math.h>

// Exponents in C

int main(void)
{
    long long base;
    long long exponent;
    int stop = -1;
    
    do
    {
        base = get_long_long("\nChoose the base. ");
        if(base <= 0)
        {
            printf("Please dont use the number 0 or any negative numbers. ");
        }
    }
    while(base < 0 || base == 0);

    do
    {
        exponent = get_long_long("\nChoose the exponent. ");
        if(exponent <= 0)
        {
            printf("Please dont use the number 0 or any negative numbers.\n ");
        }
    }
    while(exponent < 0 || exponent == 0);

    long long answer = pow(base, exponent);

    printf("With %lli as the base, and %lli as the exponent. It would be equal to %lli ", base, exponent, answer);
}   

