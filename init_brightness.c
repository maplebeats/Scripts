#include <stdio.h>

#define LIGHT 500

int main(int argc,char *argv[])
{
    FILE *fp;
    if(!(fp=fopen("/sys/class/backlight/intel_backlight/brightness","wb")))
        printf("open file failed");
    else
        fputs("LIGHT\n",fp);
    fclose(fp);
    return 0;
}

