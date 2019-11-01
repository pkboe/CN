/*---------------------------------------------------------------
Assignment No:
Write a program using TCP socket for wired network for following 
a. Say Hello to Each other ( For all students) 
b. File transfer ( For all students) 
c. Calculator (Arithmetic) 
d. Calculator (Trigonometry) 
Demonstrate the packets captured traces using Wireshark Packet Analyzer Tool for peer to peer mode
Roll No.:
Batch:
---------------------------------------------------------------*/

#include<sys/types.h>
#include<sys/socket.h>
#include<stdio.h>
#include<netinet/in.h> 
#include <unistd.h>
#include<string.h> 
#include <arpa/inet.h>

void main()
{
int b,sockfd,connfd,sin_size,l,n,len;
char operator;
int op1,op2,result;
if((sockfd=socket(AF_INET,SOCK_STREAM,0))>0)
printf("socket created sucessfully\n");  //socket creation
//printf("%d\n", sockfd);                 //on success 0 otherwise -1

struct sockaddr_in servaddr;              
struct sockaddr_in clientaddr;

servaddr.sin_family=AF_INET;
servaddr.sin_addr.s_addr=inet_addr("127.0.0.1");
servaddr.sin_port=6006;

if((bind(sockfd, (struct sockaddr *)&servaddr,sizeof(servaddr)))==0)
printf("bind sucessful\n");   
	//bind() assigns the
     //  address  specified  by  addr  to  the  socket  referred  to by the file
      // descriptor sockfd.  addrlen  specifies  the  size,  in  bytes,  of  the
     //  address structure pointed to by addr.  Traditionally, this operation is
      // called “assigning a name to a socket”.
 	//printf("%d\n",b);

if((listen(sockfd,5))==0) //listen for connections on a socket
printf("listen sucessful\n");
//printf("%d\n",l);

sin_size = sizeof(struct sockaddr_in);
if((connfd=accept(sockfd,(struct sockaddr *)&clientaddr,&sin_size))>0);
printf("accept sucessful\n");
//printf("%d\n",connfd);
read(connfd, &operator,10);
read(connfd,&op1,sizeof(op1));
read(connfd,&op2,sizeof(op2));
switch(operator) {
        case '+': result=op1 + op2;
         printf("Result is: %d + %d = %d\n",op1, op2, result);
         break;
        case '-':result=op1 - op2;
                printf("Result is: %d - %d = %d\n",op1, op2, result);
                break;
        case '*':result=op1 * op2;
                printf("Result is: %d * %d = %d\n",op1, op2, result);
                break;
        case '/':result=op1 / op2;
                printf("Result is: %d / %d = %d\n",op1, op2, result);
                break;
        default: 
                printf("ERROR: Unsupported Operation");
    }
  
write(connfd,&result,sizeof(result));   
close(sockfd);
}

/*
gescoe@gescoe-OptiPlex-3020:~/Desktop/TEA84$ cd TCP
gescoe@gescoe-OptiPlex-3020:~/Desktop/TEA84/TCP$ gcc scalculator.c
gescoe@gescoe-OptiPlex-3020:~/Desktop/TEA84/TCP$ ./a.out
socket created sucessfully
listen sucessful
^Z
[1]+  Stopped                 ./a.out
gescoe@gescoe-OptiPlex-3020:~/Desktop/TEA51/TCP$ gcc scalculator.c
gescoe@gescoe-OptiPlex-3020:~/Desktop/TEA51/TCP$ ./a.out
socket created sucessfully
bind sucessful
listen sucessful
accept sucessful
Result is: 22 + 45 = 67
gescoe@gescoe-OptiPlex-3020:~/Desktop/TEA51/TCP$ 
gescoe@gescoe-OptiPlex-3020:~/Desktop/TEA51/TCP$ gcc scalculator.c
gescoe@gescoe-OptiPlex-3020:~/Desktop/TEA51/TCP$ ./a.out
socket created sucessfully
bind sucessful
listen sucessful
accept sucessful
Result is: 54 * 20 = 1080
gescoe@gescoe-OptiPlex-3020:~/Desktop/TEA51/TCP$ 
*/
