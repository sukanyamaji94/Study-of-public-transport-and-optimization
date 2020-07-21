#include<stdio.h>
#include<conio.h>
#define INFINITY 9999
#define MAX 74

void dijkstra(int G[MAX][MAX],int n,int startnode);

int main()
{
	int array[MAX][MAX],i,j,n,u;
	printf("Enter no. of vertices:");
	scanf("%d",&n);

	FILE* fp = fopen("dis_mat_used.txt", "r");

	for(i = 0; i < 74; i++)
	{
	    for(j = 0; j < 74; j++)
	    {
	        fscanf(fp, "%d", &array[i][j]);
	    }
    }



	/*printf("\nEnter the starting node:");
	scanf("%d",&u);*/
	for(i=0;i<n;i++)
	dijkstra(array,n,i);
    fclose(fp);
	return 0;
}

void dijkstra(int G[MAX][MAX],int n,int startnode)
{

	int cost[MAX][MAX],distance[MAX],pred[MAX];
	int visited[MAX],count,mindistance,nextnode,i,j;

	//pred[] stores the predecessor of each node
	//count gives the number of nodes seen so far
	//create the cost matrix
	for(i=0;i<n;i++)
		for(j=0;j<n;j++)
			if(G[i][j]==999999)
				cost[i][j]=INFINITY;
			else
				cost[i][j]=G[i][j];

	//initialize pred[],distance[] and visited[]
	for(i=0;i<n;i++)
	{
		distance[i]=cost[startnode][i];
		pred[i]=startnode;
		visited[i]=0;
	}

	distance[startnode]=0;
	visited[startnode]=1;
	count=1;

	while(count<n-1)
	{
		mindistance=INFINITY;

		//nextnode gives the node at minimum distance
		for(i=0;i<n;i++)
			if(distance[i]<mindistance&&!visited[i])
			{
				mindistance=distance[i];
				nextnode=i;
			}

			//check if a better path exists through nextnode
			visited[nextnode]=1;
			for(i=0;i<n;i++)
				if(!visited[i])
					if(mindistance+cost[nextnode][i]<distance[i])
					{
						distance[i]=mindistance+cost[nextnode][i];
						pred[i]=nextnode;
					}
		count++;
	}
    FILE* fpn = fopen("onlyroutes19.txt", "a");

	//print the path and distance of each node
	for(i=0;i<n;i++)
		if(i!=startnode)
		{
			printf("\nDistance of node%d=%d",i,distance[i]);
			printf("\nPath=%d",i);
            //
            if(distance[i]!=999999){
                //fprintf(fpn,"\nDistance of node%d=%d from %d",i,distance[i],startnode);
                fprintf(fpn,"\n%d",i);
                }

			j=i;
			do
			{
				j=pred[j];
				printf("<-%d",j);
				//fputs(j,fpn);
				  fprintf(fpn,",%d", j);
			}while(j!=startnode);
	}
	fclose(fpn);
}
