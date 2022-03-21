

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int pg[20],oft,pno,n,fn,psize;
	int stradr=5000;
	printf("Enter the number of pages ");
	scanf("%d",&n);
	if(n>50)
	{
		printf("Invalid number of pages");
		return(0);
	}
	printf("Enter the page size: ");
	scanf("%d",&psize);
	printf("Enter the number of frames: ");
	scanf("%d",&fn);
	printf("Enter the frame numbers for the pages(-1 if invalid):\n");
	for(int i=0;i<n;i++)
	{
		printf("Enter for page %d: ",i);
		scanf("%d",&pg[i]);
	}
	printf("\nPhysical Address Space is %d\n\n",fn*psize);
	printf("Logical Address Space is %d\n",n*psize);
	printf("\nPage table:");
	printf("\nPageNo.\tAddress\tFrameNo.\n-------\t-------\t-------\n");
	for(int i=0;i<n;i++)
	{
		int temp;
		if(pg[i]!=-1){
			temp=stradr+(pg[i]*psize);
			printf("%d\t%d\t%d\t\n",i,temp,pg[i]);
		}
		else
			printf("%d\t \t%d\t\n",i,pg[i]);	
	}
	printf("\n");
	int f=1;
	while(f==1)
	{
		printf("Enter the logical address(PageNo. Offset): ");
		scanf("%d %d",&pno,&oft);
		if(pno<n)
		{
			if(pg[pno]==-1)
			{
				printf("The required page is not availabe in any of the frames\n");
			}
			else
			{
				int temp;
				if(oft<psize){
					temp=stradr+(pg[pno]*psize)+oft;
					printf("The physical address is %d\n",temp);
				}
				else
					printf("Invalid offset\n");
			}
		}
		else
			printf("Invalid PageNo.\n");
		printf("To continue press 1 else 0....");
		scanf("%d",&f);
	}
	return(1);
}

paging.c
Displaying paging.c.