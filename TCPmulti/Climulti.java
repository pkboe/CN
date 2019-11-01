import java.io.*;
import java.net.*;

public class multiclient {

public static void main(String args[]) throws IOException{

    InetAddress address=InetAddress.getLocalHost();
    Socket s1=new Socket("127.0.0.1", 4445); 
    String line=null;
    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    BufferedReader is=new BufferedReader(new InputStreamReader(s1.getInputStream()));
    PrintWriter os=new PrintWriter(s1.getOutputStream());     
    System.out.println("Client Address : "+address);
    System.out.println("Enter Data to echo Server ( Enter QUIT to end):");

    String response=null;
    try{
	line=br.readLine();

        while(line.compareTo("QUIT")!=0)
	    {
                os.println(line);
                os.flush();
                response=is.readLine();
                System.out.println("Server Response : "+response);
                line=br.readLine();

            }

      }
    catch(IOException e){
        e.printStackTrace();
    System.out.println("Socket read Error");
    }
    finally{

        is.close();os.close();br.close();s1.close();
                System.out.println("Connection Closed");

    }

}
}


