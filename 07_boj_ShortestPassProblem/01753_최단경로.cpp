#include<iostream>
#include<vector>
#include<queue>
#include<climits>

#define MAX_V 20000

using namespace std;
// ���ͽ�Ʈ�� �˰��� ���
// �켱 ���� ť ���
 int main() {
	int V, E;	// ���� ����, ���� ����
	int K;		// ������ ��ȣ(1~V)
	cin >> V >> E;
	cin >> K;
	
	vector<int> dist(V+1, INT_MAX);	// ��������� �� ������ �ִ� �Ÿ� ����
	dist[K] = 0;					// �ڽŰ� �Ÿ��� 0

	// ���� (u, v)�� ����ġ�� W�϶� mat[u] = (W, v)
	vector< pair<int, int> > mat[MAX_V + 1];

	for (int i = 0; i < E; ++i) {
		int u, v, w;
		cin >> u >> v >> w;
		mat[u].push_back(make_pair(w, v));
	}

	// ���� �� �Ÿ��� �켱������ �ǹǷ�, �Ÿ��� pq�� ������ -�Ÿ��� �־�����
	// ���� �� �Ÿ��� -�� ���̸� ���� �۾����Ƿ� ���� �켱������ ����
	priority_queue< pair<int, int> > pq;
	pq.push(make_pair(0, K));	// ���������� ������������ �ִܰŸ� 0

	while (!pq.empty()) {
		// ���� ��ġ ������ ��´�
		int here = pq.top().second;	// ���� ���� ��ȣ
		int cost = -pq.top().first;	// ���� �������� ����� ���(�ּ� ���)
		pq.pop();

		if (dist[here] < cost) {
			// ������� ���� ��뺸�� �� ����� �̹� �߰� �Ǿ��ٸ�
			// pq���� ���ŵ��� �ƹ��͵� ���ϰ� ���� ���� �˻�
			// dist�� �̹� ���ŵǾ����� ���� �� pq���� �����ϴ� ���� ��ٷӱ� ����
			continue;
		}

		// ���� ���� ������ ������ �˻��Ѵ�
		for (int i = 0; i < (int)mat[here].size(); ++i) {
			int there = mat[here][i].second;			// ��������
			int candiDist = cost + mat[here][i].first;	// ���� ������ ��� + �������� �������� �Ÿ�

			if (candiDist < dist[there]) {
				// ���� ���� ����� ������ ���� ��뺸�� �� ���
				dist[there] = candiDist;	// dist ����
				pq.push(make_pair(-candiDist, there));
			}
		}

	}

	// c++ ��½� endl��� \n �� ����� ��
	// �ð� �ʰ��� ����

	for (int i = 1; i <= V; ++i) {
		if (dist[i] == INT_MAX) {
			cout << "INF" << "\n";
		}
		else {
			cout << dist[i] << "\n";
		}
	}

	return 0;
}