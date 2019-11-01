#include<iostream>
using namespace std;
int main()
{
	int fs,gs;
	cout<<"Enter the size of data";
	cin>>fs;
	cout<<"\nEnter the size of key value";
	cin>>gs;
	int *f=new int[fs];
	int *g=new int[gs];
	cout<<"\nEnter the Data\n";
	for(int i=0;i<fs;i++)
		cin>>f[i];
	cout<<"\nEnter key:\n";
	for(int i=0;i<gs;i++)
		cin>>g[i];
	cout<<"Sender Side:\nData:";
	for(int i=0;i<fs;i++)
		cout<<f[i];
	cout<<"\nKEY:";
	for(int i=0;i<gs;i++)
		cout<<g[i];
	int rs=gs-1,j,i,k;

	int *temp=new int[fs+rs];
	cout<<"\nData after appending 0's:";
	for(i=0;i<fs;i++)
		temp[i]=f[i];
	for(i=fs;i<rs;i++)
		temp[i]=0;
	for(int i=0;i<fs+rs;i++)
		cout<<temp[i];
	for(i=0;i<fs;i++)
	{
		j=0;
		k=i;
		if(temp[k]>=g[j])
		{
			for(j=0,k=i;j<gs;j++,k++)
			{
				if((temp[k]==1 && g[j]==1)||(temp[k]==0 && g[j]==0))
					temp[k]=0;
				else
					temp[k]=1;
			}
		}
	}
	int *crc=new int[rs];
	for(i=0,j=fs;i<rs;i++,j++)
		crc[i]=temp[j];
	cout<<"\nCRC bits:";
	for(int i=0;i<rs;i++)
		cout<<crc[i];
	cout<<"\nTransmitted frame:";
	int *tf=new int[fs+rs];
	for(i=0;i<fs;i++)
		tf[i]=f[i];
	for(i=fs,j=0;j<rs;i++,j++)
		tf[i]=crc[j];
	for(int i=0;i<fs+rs;i++)
		cout<<tf[i];
	
	for(i=0;i<fs+rs;i++)
		temp[i]=tf[i];
	cout<<"\nReceiver Side:\nReceived Data:";
	for(int i=0;i<fs+rs;i++)
		cout<<temp[i];
	for(i=0;i<fs;i++)
	{
		j=0;
		k=i;
		if(temp[k]>=g[j])
		{
			for(j=0,k=i;j<gs;j++,k++)
			{
				if((temp[k]==1 && g[j]==1)||(temp[k]==0 && g[j]==0))
					temp[k]=0;
				else
					temp[k]=1;
			}
		}
	}
	for(i=0,j=fs;i<rs;i++,j++)
		crc[i]=temp[j];
	cout<<"\nRemainder bits:";
	for(int i=0;i<rs;i++)
		cout<<crc[i];
	
	int flag=0;
	for(int i=0;i<rs;i++)
		if(crc[i]!=0)
			flag=1;

	if(flag==0)
		cout<<"correct";
	else
		cout<<"incorrect";
}