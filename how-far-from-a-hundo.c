#include <stdio.h>

int main() {
    // Write C code here
    int n;
    
    do
    {
        printf("How old are you?: ");
        scanf("%d", &n);
    }
    while (n < 0 || n == 0);
if (n == 99)
        {
        printf("You are 1 year away from 100!");
        }   
        else
            {
            printf("You are %d years away from 100!", 100 - n);
        
            }
}