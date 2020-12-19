// 2018.09.23
#include <stdio.h>

typedef struct {
	int vv[100000];
	int front,lear;//[,)
}queue;

void init(queue *q, int n);
void push(queue *q, int num);
int pop(queue *q);
int main() {
	int i, n , m,count;
	queue a;
	queue *q = &a;	//포인터 사용
	scanf("%d %d", &n, &m);
	count = n;
	init(q, n);	// 큐 초기화

	printf("<");
	while(count > 1) {
		for (i = 0; i < m-1; i++)
			push(q, pop(q));
		printf("%d, ",pop(q));
		count--;
	}
	printf("%d>",q->vv[q->front]);
	

	return 0;
}
void init(queue *q ,int n) {
	int i;
	q->front = 0;
	q->lear = n;
	for (i = 0; i < n; i++)
		q->vv[i] = i + 1;
}
void push(queue *q, int num) {
	q->vv[q->lear] = num;
	q->lear = (q->lear+1)%100000;
}
int pop(queue *q) {
	int ret = q->vv[q->front];
	q->front = (q->front+1)%100000;
	return ret;
}