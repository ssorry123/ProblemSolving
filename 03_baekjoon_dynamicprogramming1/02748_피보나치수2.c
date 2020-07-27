// writed 2018
int main()
{
    int n=0,i,j;
    char f[91][51]={0};
    f[0][50]=0;
    f[1][50]=1; 
	scanf("%d",&n);
    if(n==0){printf("0");}
    else if(n==1){printf("1");}
    else{
        for(i=2;i<=n;i++){
            do{
            j=50;
    		while((f[i-1][j]!=0 || f[i-2][j]!=0)||(f[i-1][j-1]!=0 || f[i-2][j-1]!=0)){
    		    f[i][j]+=f[i-1][j]+f[i-2][j];
    		    while(f[i][j]>=10){
                    f[i][j]-=10;f[i][j-1]+=1;
                }
    		j--;}
    		}while(f[i][j-1]!=0);
        }
        for(i=0;i<=50;i++){
            if(f[n][i]==0){
                f[n][i]=-48;
            }
        	else if(f[n][i]!=0){
                i=101;
            }
        }
        for(i=0;i<=50;i++){
            if(f[n][i]!=-48){
                printf("%c",f[n][i]+48);
            }
        }
    }
    return 0;
}