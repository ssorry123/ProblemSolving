//2017.10.17
int main(){
    int n, i, j, p, k=0, z=0;
    int a[100];
    scanf("%d",&n);
    for(i=0; i<n; i++)
        scanf("%d", &a[i]);
        
    
    for(i=0; i<n; i++){
        k=0;
        p=a[i];
        if(p!=2 && p%2==0)
            p=0;
        for(j=1; j<=p/2; j++){
            if(p%j==0)
                k++;
            if(k>1)
                j=p;
        }
        if(k==1)
            z++;
    }
    printf("%d",z);
    return 0;
}