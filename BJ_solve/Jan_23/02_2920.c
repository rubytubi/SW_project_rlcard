#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int num[8];
    
    for(int i = 0; i < 8; i++)
    {
        scanf("%d", &num[i]);
    }

    int num1 = 0;
    int num2 = 0;

    for(int i = 0; i < 8; i++)
    {
        if((num[i] == i + 1) && (num[i] + num[7 - i]) == 9)
        num1++;

        else if((num[i] == 8 - i) && (num[i] + num[7 - i]) == 9)
        num2++;
    }
    
    if(num1 == 8)
    printf("ascending\n");
    else if(num2 == 8)
    printf("descending\n");
    else
    printf("mixed\n");
   
    return 0;
}