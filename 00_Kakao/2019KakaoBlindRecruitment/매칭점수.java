import java.util.*;

class HtmlInfo implements Comparable<HtmlInfo> {
    String name;
    int score;
    List<String> extLink;
    double linkScore;
    double matchScore;
    Double a;

    HtmlInfo() {
        this.name = null;
        this.score = 0; // 기본 점수
        extLink = new ArrayList<>(); // 외부 링크 (외부 링크 목록)
        this.linkScore = 0; // 링크 점수
        this.matchScore = 0; // 매칭 점수
    }

    // 출력 확인 용
    public void print() {
        System.out.println(name);
        System.out.println(score);
        System.out.println(extLink.size());
        for (String s : extLink) {
            System.out.println(s);
        }
        System.out.println(linkScore);
        System.out.println(matchScore + "\n");
    }

    // 매칭 점수 가장 높은 것을 뽑기 위해
    // 정렬 시 내림차순 정렬
    @Override
    public int compareTo(HtmlInfo o) {
        if (matchScore < o.matchScore)
            return 1;
        else if (matchScore == o.matchScore)
            return 0;
        else
            return -1;
    }

}

class Solution {
    // 출력용 함수
    public <T> void print(T t) {
        System.out.println(t);
    }

    public HtmlInfo getTest(String html, String word) {
        HtmlInfo ret = new HtmlInfo();
        String[] str = html.split("[<|>|=]"); // 전달 받은 문서를 < 또는 > 또는 = 으로 split
        boolean body = false; // 본체 부분인가?
        int bodyCount = 0; // 기본 점수 카운터

        for (int idx = 0; idx < str.length; ++idx) {
            String s = str[idx];

            // html 이름 추출
            if (s.equals("meta property")) {
                String nameTmp = str[idx + 2];
                String name = nameTmp.substring(1, nameTmp.length() - 2);
                // body에 "meta property" 내용이 나왔을때를 방지
                if (ret.name == null)
                    ret.name = name;
            }
            // 외부 링크 추출
            else if (s.equals("a href")) {
                String outTmp = str[idx + 1];
                String out = outTmp.substring(1, outTmp.length() - 1);
                ret.extLink.add(out);
            }
            // body 시작 알림
            else if (!body && s.equals("body")) {
                body = true;
                continue;
            } else if (s.equals("/body")) {
                body = false;
            }

            // 본문 문장 체크
            if (body) {
                String[] tmp = s.split("[^a-zA-Z]");// 알파벳을 제외한 모든 문자들로 토큰을 나눔
                for (String t : tmp) {
                    if (t.equalsIgnoreCase(word))
                        bodyCount++;
                }
            }
        }

        ret.score = bodyCount;
        // ret.print();
        return ret;
    }

    public int solution(String word, String[] pages) {
        int answer = 0;

        HtmlInfo[] htmlArr = new HtmlInfo[pages.length];
        Map<String, Integer> map = new HashMap<>();
        // 기본 점수, 외부 링크 파악
        for (int idx = 0; idx < pages.length; ++idx) {
            String s = pages[idx];
            htmlArr[idx] = getTest(s, word);
            map.put(htmlArr[idx].name, idx); // string -> int mapping;
        }

        // 링크 점수 갱신
        for (HtmlInfo hi : htmlArr) {
            String me = hi.name;
            int meScore = hi.score;
            List<String> out = hi.extLink;
            int meOut = out.size();

            for (String o : out) {
                if (map.containsKey(o)) {
                    HtmlInfo target = htmlArr[map.get(o)]; // 내가 참조하는 사이트
                    target.linkScore += (meScore / (double) meOut);
                }
            }
        }

        // 총 점수 갱신
        for (HtmlInfo hi : htmlArr) {
            hi.matchScore = hi.linkScore + hi.score;
        }

        Arrays.sort(htmlArr); // 정렬
        answer = map.get(htmlArr[0].name); // 매칭 1등 뽑기
        print(answer); // 정답 출력
        return answer;
    }
}