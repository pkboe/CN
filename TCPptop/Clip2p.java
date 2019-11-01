


import java.net.*;
import java.io.*;

public class p2pclient{
	public static void main(String args[])throws Exception{  
	                   
	                   Socket s=new Socket("localhost",3344);                   	                          
	                   DataInputStream din=new DataInputStream(s.getInputStream());  
		DataOutputStream dout=new DataOutputStream(s.getOutputStream());  
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));  
		  
		String str="",str2="";  
		while(!str.equals("stop")){  
		str=br.readLine();  
		dout.writeUTF(str);  
		dout.flush();  
		str2=din.readUTF();  
		System.out.println("Server says: "+str2);  
		}  
	  
		dout.close();  
		din.close();
		s.close();  
	}
}


