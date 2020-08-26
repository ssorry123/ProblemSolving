// 2017.10.13
int main(){
    int n, i=0, j, len, m=0;
    char a[7];
    scanf("%d", &n);
    
    while(m != n){
        m = 0;
        m += i;
        sprintf(a, "%d", i);
        len = strlen(a);
        for(j = 0; j < len; j++){
            m += a[j] - 48;
        }
        ++i;
        if(i == n+1){
            i = 1;
            break;
        }
    }
    printf("%d", i - 1);
    
    return 0;
}