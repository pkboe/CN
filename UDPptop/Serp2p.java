
import java.io.*;
import java.net.*;

public class p2pserver
{
 public static void main(String args[]) throws IOException 
 {
    DatagramSocket ss = null; 
    
			
	ss = new DatagramSocket(9000); 
	
		  
	byte[] receiveData = new byte[512];  
	
	byte[] sendData  = new byte[512]; 
	
		  
	System.out.println(" UDP Server socket is created and waiting for client");
		
	while(true) 
	 { 
  	   DatagramPacket receivePacket =new DatagramPacket(receiveData, receiveData.length); 
  
	   ss.receive(receivePacket); 
  
	   String message = new String(receivePacket.getData()); 
	  

	   System.out.println("Client Says: "+message);
		
	   InetAddress IPAddress = receivePacket.getAddress(); 
  
	   int port = receivePacket.getPort(); 
		  
	   message = "Thanks";
  
	   sendData = message.getBytes(); 
  
	   DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress,port); 
  
	   ss.send(sendPacket); 
		  	 	
	   if(message.equals("Thanks")) break;
	  } 	
	 ss.close();
	 System.out.println("Server Stopped by User program");
  }
}

