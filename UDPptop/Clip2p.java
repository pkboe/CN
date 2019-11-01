
import java.io.*;
import java.net.*;

public class p2pclient
{
  public static void main(String args[]) throws IOException
  {
	 String message = null;
	 DatagramSocket cs = null; 
			
	 cs = new DatagramSocket();  
 	  
	 byte[] receiveData = new byte[512];   

	 byte[] sendData  = new byte[512]; 
			  
	 System.out.println(" UDP Client socket is created and waiting for server");
		
     InetAddress IPAddress = InetAddress.getByName("localhost"); 
  
     int port = 9000;
		  
	 message = "Hello Server";
  
	 sendData = message.getBytes(); 
  
	 DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress,port); 
  
	 cs.send(sendPacket); 
	   
	 DatagramPacket receivePacket =new DatagramPacket(receiveData, receiveData.length); 
  
	 cs.receive(receivePacket); 
  
	 message = new String(receivePacket.getData());  
	
	 System.out.println("Server Says: "+message);
		
	}
}



