#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    // 완주자는 참석자보다 한명 적음
    // 정렬 후, 다른 것이 나오면 해당 참가자는 탈락
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());

    for (int i = 0; i < participant.size(); ++i) {
        if (participant[i] == completion[i]) {
            continue;
        }
        else {
            answer = participant[i];
            break;
        }
    }

    return answer;
}