// 2017.10.14
int main(){
    int i, j, n, x[50], y[50], z[50] = {0}, k = 0;
    scanf("%d", &n);
    for(i=0; i<n; i++){
        scanf("%d%d", &x[i], &y[i]);
    }
    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            if(i != j){
                if(x[i]<x[j] && y[i]<y[j]){
                    z[i]++;
                }
            }
        }
    }
    for(i=0;i<n;i++){
        printf("%d ",z[i]+1);
    }
    return 0;
}