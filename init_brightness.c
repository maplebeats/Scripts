#include <stdio.h>

void main(void)
{
    FILE *fp;
    if(!(fp=fopen("/sys/class/backlight/intel_backlight/brightness","wb")))
    {
        printf("open file failed");
    }
    else
    {
        fputs("500\n",fp);
    }
    fclose(fp);
}

