#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char s1[30];
    scanf("%s", s1);
    int count = 0;
  
    for(int i = 0; i < 30; i ++)
    {
        
    if(s1[i] == 'A' || s1[i] == 'B' || s1[i] == 'C')
    {
        count += 3;
    }
    

    else if(s1[i] == 'D' || s1[i] == 'E' || s1[i] == 'F')
    {
        count += 4;
    }

    else if(s1[i] == 'G' || s1[i] == 'H' || s1[i] == 'I')
    {
        count += 5;
    }
    else if(s1[i] == 'J' || s1[i] == 'K' || s1[i] == 'L')
    {
        count += 6;
    } 

    else if(s1[i] == 'M' || s1[i] == 'N' || s1[i] == 'O')
    {
        count += 7;
    }

    else if(s1[i] == 'P' || s1[i] == 'Q' || s1[i] == 'R' || s1[i] == 'S')
    {
        count += 8;
    }

    else if(s1[i] == 'T' || s1[i] == 'U' || s1[i] == 'V')
    {
        count += 9;
    }

    else if(s1[i] == 'W' || s1[i] == 'X' || s1[i] == 'Y' || s1[i] == 'Z')
    {
        count += 10;
    }
    }

    printf("%d\n", count);
    
    return 0;
}