//enabling generation of pcap files.
//ping application for client and server.
//Necessary header files.
#include "ns3/core-module.h" 
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/applications-module.h"
#include "ns3/netanim-module.h" //added netnim header file
#include "ns3/mobility-module.h"

//Namespace
using namespace ns3;

//logging module
NS_LOG_COMPONENT_DEFINE ("FirstScriptExample");

//main program
int main (int argc, char *argv[])
{

//enabling log of available modules
  LogComponentEnable ("UdpEchoClientApplication", LOG_LEVEL_INFO);
  LogComponentEnable ("UdpEchoServerApplication", LOG_LEVEL_INFO);

//creating nodes
  NodeContainer nodes;
  nodes.Create (2);

//creating network interfaces- in this case a point-to-point interface
  PointToPointHelper pointToPoint;
  pointToPoint.SetDeviceAttribute ("DataRate", StringValue ("5Mbps"));
  pointToPoint.SetChannelAttribute ("Delay", StringValue ("2ms"));

//creating network device contatiner and install it on the nodes
  NetDeviceContainer devices;
  devices = pointToPoint.Install (nodes);

//install protocol stack in nodes 
  InternetStackHelper stack;
  stack.Install (nodes);

//set network address for interface
  Ipv4AddressHelper address;
  address.SetBase ("10.1.1.0", "255.255.255.0");

  Ipv4InterfaceContainer interfaces = address.Assign (devices);

//install applications in nodes
  UdpEchoServerHelper echoServer (9);

  ApplicationContainer serverApps = echoServer.Install (nodes.Get (1));

//set application start and stop time
  serverApps.Start (Seconds (1.0));
  serverApps.Stop (Seconds (10.0));

  UdpEchoClientHelper echoClient (interfaces.GetAddress (1), 9);
  echoClient.SetAttribute ("MaxPackets", UintegerValue (1));
  echoClient.SetAttribute ("Interval", TimeValue (Seconds (1.0)));
  echoClient.SetAttribute ("PacketSize", UintegerValue (1024));

  ApplicationContainer clientApps = echoClient.Install (nodes.Get (0));
  clientApps.Start (Seconds (2.0));
  clientApps.Stop (Seconds (10.0));

//assingning fixed position to noeds. optional, but if skipped, gives warning for animation
  MobilityHelper mobility;
  mobility.SetMobilityModel ("ns3::ConstantPositionMobilityModel");
  mobility.Install(nodes);

//creating a bounding box for NetAnim
// AnimationInterface::SetBoundary(0,0,70,70);
//above line required ns3.19 and bellow version
  AnimationInterface anim("first.xml");
  AnimationInterface::SetConstantPosition(nodes.Get(0),10,25);
//client 0, x=10, y=25
  AnimationInterface::SetConstantPosition(nodes.Get(1),40,25);
 //client 0, x=10, y=25
 anim.EnablePacketMetadata(true);

//it will enable all pcap files.
 pointToPoint.EnablePcapAll ("first");

//run the simulator
  Simulator::Run ();

//release resources at the end of the simulation
  Simulator::Destroy ();
  return 0;
}
