//2017.10.18
int main(){
    int m,n,i,j,k,q=0,M=0,N;
    int a[10000];
    scanf("%d%d", &m, &n);
    if(m!=2 && m%2==0)
        m++;

    for(i=m; i<=n; i++){
        k=0;
        for(j=1; j<=i/2; j++){
            if(i%j==0){
                k++;
                if(k>1)
                    j=i;
            }
        }
        if(k==1){
            M+=i;
            q++;
        }
        if(q==1){
            N=i;
            q=-10000;
        }
    }

    if(M==0)
        printf("%d",-1);
    else printf("%d\n%d",M,N);
    return 0;
}