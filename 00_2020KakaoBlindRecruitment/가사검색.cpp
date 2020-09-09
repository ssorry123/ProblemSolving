#include <string>
#include <vector>
#include <map>
using namespace std;

vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> answer;
    vector<vector<string> > by_len(10001);  // 문자열의 길이를 해쉬값으로
    for (int i = 0; i < words.size(); ++i) {
        int key = words[i].length();
        by_len[key].push_back(words[i]);
    }
    map<string, int> cache;

    for (int i = 0; i < queries.size(); ++i) {
        string q = queries[i];
        // 메모이제이션
        if (cache.find(q) != cache.end()) {
            answer.push_back(cache.find(q)->second);
            continue;
        }

        // ?가 앞에있는지 뒤에있는지 확인
        bool front = true;
        if (q[q.length() - 1] == '?')
            front = false;
        // 쿼리 길이와 일치하는 문자열이 없을 경우
        int key = q.length();
        if (by_len[key].empty()) {
            answer.push_back(0);
            continue;
        }

        // 와일드카드의 개수 세기
        int wildcard_cnt = 0;
        if (front) {
            for (int i = 0; i < q.length(); ++i) {
                if (q[i] == '?')
                    ++wildcard_cnt;
                else
                    break;
            }
        }
        else {
            for (int i = q.length() - 1; i >= 0; --i) {
                if (q[i] == '?')
                    ++wildcard_cnt;
                else
                    break;
            }
        }
        int cnt = 0;
        for (int i = 0; i < by_len[key].size(); ++i) {
            string w = by_len[key][i];
            string w_cut, q_cut;
            if (front) {
                w_cut = w.substr(wildcard_cnt);
                q_cut = q.substr(wildcard_cnt);
            }
            else {
                w_cut = w.substr(0, w.length() - wildcard_cnt);
                q_cut = q.substr(0, w.length() - wildcard_cnt);
            }
            if (w_cut == q_cut)
                ++cnt;
        }
        answer.push_back(cnt);
        cache.insert(make_pair(q, cnt));
    }

    return answer;
}
int main() {
    solution({"frodo", "front", "frost", "frozen", "frame", "kakao"}, { "fro??", "????o", "fr???", "fro???", "pro?" });
    return 0;
}