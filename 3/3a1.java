/******************************************************************************************
Title :-Write a program to simulate go-back-n of sliding window protocol in peer to peer
Class :- TE-B   Batch :- 3
Roll No :- 54
******************************************************************************************/
import java.io.*;
import java.net.*;
import java.util.*;

class gobackser
{
public static void main(String args[])throws IOException
{
System.out.println("...........Server..........");
System.out.println("Waiting for connection....");
InetAddress addr=InetAddress.getByName("Localhost");
ServerSocket ss=new ServerSocket(5000);

Socket client=new Socket();
client=ss.accept();

BufferedInputStream in=new BufferedInputStream(client.getInputStream());
DataOutputStream out=new DataOutputStream(client.getOutputStream());

System.out.println("Received request for sending frames");
int p=in.read();

boolean f[]=new boolean[p];

int pc=in.read();
System.out.println("Sending....");

if(pc==0)
{
for(int i=0;i<p;++i)
{
System.out.println("sending frame number "+i);
out.write(i);
out.flush();
System.out.println("Waiting for acknowledgement");
try
{
Thread.sleep(7000);
}
catch(Exception e){}

int a=in.read();
System.out.println("received acknowledgement for frame "+i+" as "+a);
}
out.flush();
}
else
{
for(int i=0;i<p;++i)
{
if(i==2)
{
System.out.println("sending frame no "+i);
}
else
{
System.out.println("sending frame no "+i);
out.write(i);
out.flush();
System.out.println("Waiting for acknowledgement ");
try
{
Thread.sleep(7000);
}
catch(Exception e){}

int a=in.read();

if(a!=255)
{
System.out.println("received ack for frame no: "+i+" as "+a);
f[i]=true;
}
}// end of inner else
}// end of for

// check which frames have not been ack

for(int a=0;a<p;++a)
{
if(f[a]==false)
{
System.out.println("Resending frame "+a);
out.write(a);
out.flush();
System.out.println("Waiting for ack ");
try
{
Thread.sleep(5000);
}
catch(Exception e){}

int b=in.read();
System.out.println("received ack for frame no: "+a+" as "+b);
f[a]=true;
}
}
out.flush();
}// end of else which is for error 

in.close();
out.close();
client.close();
ss.close();
System.out.println("Quiting");

}// end main method
}// end main class

/* OUTPUT 

gescoe@gescoe-OptiPlex-3020:~/Desktop/Kaveri$ javac gobackser.java
gescoe@gescoe-OptiPlex-3020:~/Desktop/Kaveri$ java gobackser

...........Server..........
Waiting for connection....
Received request for sending frames
Sending....
sending frame no 0
Waiting for acknowledgement 
received ack for frame no: 0 as 0
sending frame no 1
Waiting for acknowledgement 
received ack for frame no: 1 as 1
sending frame no 2
sending frame no 3
Waiting for acknowledgement 
sending frame no 4
Waiting for acknowledgement 
Resending frame 2
Waiting for ack 
received ack for frame no: 2 as 2
Resending frame 3
Waiting for ack 
received ack for frame no: 3 as 3
Resending frame 4
Waiting for ack 
received ack for frame no: 4 as 4
Quiting

gescoe@gescoe-OptiPlex-3020:~/Desktop/Kaveri$ javac gobackser.java
gescoe@gescoe-OptiPlex-3020:~/Desktop/Kaveri$ java gobackser

...........Server..........
Waiting for connection....
Received request for sending frames
Sending....
sending frame number 0
Waiting for acknowledgement
received acknowledgement for frame 0 as 0
sending frame number 1
Waiting for acknowledgement
received acknowledgement for frame 1 as 1
sending frame number 2
Waiting for acknowledgement
received acknowledgement for frame 2 as 2
sending frame number 3
Waiting for acknowledgement
received acknowledgement for frame 3 as 3
Quiting
gescoe@gescoe-OptiPlex-3020:~/Desktop/Kaveri$ 

*/
