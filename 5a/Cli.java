//TCP Client Side : Hello Client-Server Program   M L Dhore  16/08/2013

import java.io.*;
import java.net.*;

public class tcpclient
{
 public static void main(String args[]) throws IOException
 {
	Socket cs = null;
			
	String message = "Hello";
		
	cs = new Socket("localhost",8000);
	System.out.println("Client socket is created and waiting for server");
	DataOutputStream ostream = new DataOutputStream(cs.getOutputStream());
	DataInputStream istream = new DataInputStream(cs.getInputStream());
		
	ostream.writeUTF(message); // write operation
	ostream.flush();

	if(cs.getSoTimeout()==0)cs.setSoTimeout(1800); 
	// To set timeout, 0 means infinite time out

	message = istream.readUTF(); // read operation

	System.out.println("Server Says: "+message);
	System.out.println("Server Says: "+istream.readUTF());
		
	cs.close();
	ostream.close();
	istream.close();
  }
}
