/**************************************************************
ASSIGNMENT NO. 11  (Group A)
Name: Harsh Maithia
Class: TE Computer 
Batch: TEB -1
Roll No. 01
Problem statement :-Write a program for DNS lookup. Given an IP address input, it should return URL and vice-
versa.
***************************************************************/
//DNSLookup.java
// Print out DNS Record for an Internet Address
import javax.naming.directory.Attributes;
import javax.naming.directory.InitialDirContext;
import javax.naming.NamingEnumeration;
import javax.naming.NamingException;
import java.net.InetAddress;
import java.net.UnknownHostException;

public class DNSLookup
{
    public static void main(String args[])
    {
        // explain what program does and how to use it 
        if (args.length != 1)
        {
            System.err.println("Print out DNS Record for an Internet Address");
            System.err.println("USAGE: java DNSLookup domainName|domainAddress");
            System.exit(-1);
        }
        try
        {
            InetAddress inetAddress;
            // if first character is a digit then assume is an address
            if (Character.isDigit(args[0].charAt(0)))
            {   // convert address from string representation to byte array
                byte[] b = new byte[4];
                String[] bytes = args[0].split("[.]");
                for (int i = 0; i < bytes.length; i++)
                {
                    b[i] = new Integer(bytes[i]).byteValue();
                }
                // get Internet Address of this host address
                inetAddress = InetAddress.getByAddress(b);
            }
            else
            {   // get Internet Address of this host name
                inetAddress = InetAddress.getByName(args[0]);
            }
            // show the Internet Address as name/address
            System.out.println(inetAddress.getHostName() + "/" + inetAddress.getHostAddress());
            // get the default initial Directory Context
            InitialDirContext iDirC = new InitialDirContext();
            // get the DNS records for inetAddress
            Attributes attributes = iDirC.getAttributes("dns:/" + inetAddress.getHostName());
            // get an enumeration of the attributes and print them out
            NamingEnumeration attributeEnumeration = attributes.getAll();
            System.out.println("-- DNS INFORMATION --");
            while (attributeEnumeration.hasMore())
            {
                System.out.println("" + attributeEnumeration.next());
            }
            attributeEnumeration.close();
        }
        catch (UnknownHostException exception)
        {
            System.err.println("ERROR: No Internet Address for '" + args[0] + "'");
        }
        catch (NamingException exception)
        {
            System.err.println("ERROR: No DNS record for '" + args[0] + "'");
        }
    }
}

/*

gescoe@gescoe-OptiPlex-3020:~$ cd Desktop
gescoe@gescoe-OptiPlex-3020:~/Desktop$ javac DNSLookup.java

gescoe@gescoe-OptiPlex-3020:~/Desktop$ java DNSLookup flipkart.com
flipkart.com/163.53.78.128
-- DNS INFORMATION --
A: 163.53.78.128
gescoe@gescoe-OptiPlex-3020:~/Desktop$ java DNSLookup diablo.cs.fsu.edu
diablo.cs.fsu.edu/128.186.122.12
-- DNS INFORMATION --
A: 128.186.122.12

gescoe@gescoe-OptiPlex-3020:~/Desktop$ java DNSLookup yahoo.com
yahoo.com/206.190.36.45
-- DNS INFORMATION --
NS: ns4.yahoo.com., ns5.yahoo.com., ns2.yahoo.com., ns1.yahoo.com., ns3.yahoo.com.
gescoe@gescoe-OptiPlex-3020:~/Desktop$ 
*/
