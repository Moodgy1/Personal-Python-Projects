#include <cs50.h>
#include <stdio.h>

typedef struct
{
    int y1;
    int y2;
    int x1;
    int x2;
}
slope;

int main (void)
{
    slope userinp[1];
    userinp[0].y1 = get_int("What's y1? ");
    userinp[0].y2 = get_int("What's y2? ");
    userinp[0].x1 = get_int("What's x1? ");
    userinp[0].x2 = get_int("What's x2? ");
    int ansy = userinp[0].y1 - userinp[0].y2;
    int ansx = userinp[0].x1 - userinp[0].x2;
    float slopee = ansy / ansx;
    printf("The slope is: %f\n", slopee);
}