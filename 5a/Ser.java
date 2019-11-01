// TCP Server Side :  Hello Client-Server Program  M L Dhore  16/08/2013

import java.io.*;
import java.net.*;

public class tcpserver
{
  public static void main(String args[]) throws IOException
  {
	ServerSocket ss = null;
	Socket socket =null;
			
	String message;
		
	ss = new ServerSocket(8000);
	System.out.println("Server socket is created and waiting for client");
		
	socket = ss.accept();
	DataOutputStream ostream = new DataOutputStream(socket.getOutputStream());
	DataInputStream istream = new DataInputStream(socket.getInputStream());
		
	if(socket.getTcpNoDelay()) socket.setTcpNoDelay(true);
	 // to disable Nagle's Algorithm

	message = istream.readUTF(); // read operation

	System.out.println("Client Says: "+message);
		
	message = "Hello";

	ostream.writeUTF(message);   // write operation

	System.out.println("Reply to Client:" +message);
	ostream.writeUTF("Pranil");

	socket.close();
	ostream.close();
	istream.close();
  }
}
