/**************************************************************************************
Title:- Write a program to simulate go-back-n of sliding window protocol in peer to peer
Class :-     Batch :
Roll No :- 
**************************************************************************************/

import java.io.*;
import java.net.*;
import java.math.*;
import java.util.*;

class gobackcli
{

public static void main(String args[])throws IOException
{
InetAddress addr=InetAddress.getByName("Localhost");
System.out.println(addr);

Socket connection=new Socket(addr,5000);

BufferedInputStream in=new BufferedInputStream(connection.getInputStream());
DataOutputStream out=new DataOutputStream(connection.getOutputStream());
Scanner scr=new Scanner(System.in);// this will be used to accept i/p from console


System.out.println(".......Client........");
System.out.println("Connect");
System.out.println("Enter the number of frames to be requested to the server");
int c=scr.nextInt();

out.write(c);
out.flush();

System.out.println("Enter the type of trans. Error=1 ; No Error=0");
int choice=scr.nextInt();
out.write(choice);

int check=0;
int i=0;
int j=0;

if(choice==0)
{
for(j=0;j<c;++j)
{
i=in.read();
System.out.println("received frame no: "+i);
System.out.println("Sending acknowledgement for frame no: "+i);
out.write(i);
out.flush();
}
out.flush();
}
else
{
for(j=0;j<c;++j)
{
i=in.read();
if(i==check)
{
System.out.println("received frame no: "+i);
System.out.println("Sending acknowledgement for frame no: "+i);
out.write(i);
++check;
}
else
{
--j;
System.out.println("Discarded frame no: "+i);
System.out.println("Sending NEGATIVE ack");
out.write(-1);
}
out.flush();
}
}//end of else for error

in.close();
out.close();
System.out.println("Quiting");

}// end of main method
}// end of main class

/* OUTPUT

gescoe@gescoe-OptiPlex-3020:~/Desktop/Kaveri$ javac gobackcli.java
gescoe@gescoe-OptiPlex-3020:~/Desktop/Kaveri$ java gobackcli

Localhost/127.0.0.1
.......Client........
Connect
Enter the number of frames to be requested to the server
5
Enter the type of trans. Error=1 ; No Error=0
1
received frame no: 0
Sending acknowledgement for frame no: 0
received frame no: 1
Sending acknowledgement for frame no: 1
Discarded frame no: 3
Sending NEGATIVE ack
Discarded frame no: 4
Sending NEGATIVE ack
received frame no: 2
Sending acknowledgement for frame no: 2
received frame no: 3
Sending acknowledgement for frame no: 3
received frame no: 4
Sending acknowledgement for frame no: 4
Quiting

gescoe@gescoe-OptiPlex-3020:~/Desktop/Kaveri$ javac gobackcli.java
gescoe@gescoe-OptiPlex-3020:~/Desktop/Kaveri$ java gobackcli

Localhost/127.0.0.1
.......Client........
Connect
Enter the number of frames to be requested to the server
4
Enter the type of trans. Error=1 ; No Error=0
0
received frame no: 0
Sending acknowledgement for frame no: 0
received frame no: 1
Sending acknowledgement for frame no: 1
received frame no: 2
Sending acknowledgement for frame no: 2
received frame no: 3
Sending acknowledgement for frame no: 3
Quiting
gescoe@gescoe-OptiPlex-3020:~/Desktop/Kaveri$ 

*/
