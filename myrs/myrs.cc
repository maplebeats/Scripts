#include <myrs.h>

using namespace std;

int spawn(const char * program,char* const argv[])
{
    pid_t epid;
    int fdm,fds;
    char * ptr;
    fdm  = posix_openpt(O_RDWR);
    grantpt(fdm);
    unlockpt(fdm);
    ptr = ptsname(fdm);
    fds = open(ptr,O_RDWR);
    epid = fork();
    if(epid==0){
        if(setsid()<0)
            cout<<"setsid error"<<endl;
        if(ioctl(fds, TIOCSCTTY, (char *)0)<0)
            cout<<"TIOCSCTTY error"<<endl;
        if (dup2(fds, STDIN_FILENO) != STDIN_FILENO)
            cout<<"dup2 error to 0"<<endl;
        if (dup2(fds, STDOUT_FILENO) != STDOUT_FILENO)
            cout<<"dup2 error to 1"<<endl;
        if (dup2(fds, STDERR_FILENO) != STDERR_FILENO)
            cout<<"dup2 error to 2"<<endl;
        if (fds!=STDIN_FILENO && fds!=STDOUT_FILENO && fds!=STDERR_FILENO)
            close(fds);
        int j;
        for(j=3;j<1024;j++)
        {
            close(j);
        }
        execvp(program, argv);
    }
    else
    {
        const char * passwd="tiantian\r";
        char * buff;
        buff = (char *)malloc(4096);
        struct epoll_event ev,events[20];
        int efd;
        efd = epoll_create(3);
        ev.data.fd=fdm;
        ev.events=EPOLLIN|EPOLLET;
        if (epoll_ctl(efd , EPOLL_CTL_ADD, fdm, &ev) != 0)
            cout<<"epoll ctl error"<<endl;
        int count=0; //sub program exit
        int count2=0; //subprocess zombie
        while(1)
        {
            int num,i;
            num = epoll_wait(efd,events,3,500);
            if(count2==5){
                return -4;
            }
            count2++;
            for(i=0;i<num;i++){
                if(events[i].data.fd == fdm)
                {
                    int afd = events[i].data.fd;
                    if(events[i].events&EPOLLIN){
                        int re;
                        re =read(fdm, buff, 4096);
                        string word(buff);
                        if((word.find("total size is",0)!=string::npos)&&(word.find("speedup is",0)!=string::npos))
                        {
                            free(buff);
                            return 0;
                        }
                        if(re==2 && count==5)
                        {
                            return -1;
                        }
                        else if(re==2)
                        {
                            count++;
                        }
                        ev.data.fd=afd;
                        ev.events=EPOLLOUT|EPOLLET;
                        epoll_ctl(efd,EPOLL_CTL_MOD,afd,&ev);
                    }
                    else if(events[i].events&EPOLLOUT)
                    {
                        sleep(1);
                        //if find password in buff,send password.if find sucess exit;
                        string word(buff);
                        memset(buff,0,4096);
                        if((word.find("assword",0)!=string::npos)){
                            write(fdm,passwd,strlen(passwd));
                        }
                        else if((word.find("yes",0)!=string::npos)||(word.find("YES",0)!=string::npos))
                        {
                            write(fdm,"yes\n",5);
                        }
                        ev.data.fd=afd;
                        ev.events=EPOLLIN|EPOLLET;
                        epoll_ctl(efd,EPOLL_CTL_MOD,afd,&ev);
                    }
                    else
                    {
                        cout<<"epoll listen error"<<endl;
                        return -2;
                    }
                }
                else
                {
                    cout<<"the fd is not fdm"<<endl;
                    return -3;
                }
            }
        }
    }
    return 0;
}

int main(int argc, char *argv[])
{
    char * p4;
    p4=(char *)malloc(1024);
    sprintf(p4,"%s@%s:%s",argv[1],argv[2],argv[4]);
    char* params[] = {"rsync","-avp",argv[3],p4,NULL};
    int ret;
    ret = spawn(params[0],params);
    cout<<ret<<endl;
    free(p4);
}
