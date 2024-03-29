# 순위 검색

###### 문제 설명

**[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]**

카카오는 하반기 경력 개발자 공개채용을 진행 중에 있으며 현재 지원서 접수와 코딩테스트가 종료되었습니다. 이번 채용에서 지원자는 지원서 작성 시 아래와 같이 4가지 항목을 반드시 선택하도록 하였습니다.

- 코딩테스트 참여 개발언어 항목에 cpp, java, python 중 하나를 선택해야 합니다.
- 지원 직군 항목에 backend와 frontend 중 하나를 선택해야 합니다.
- 지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 합니다.
- 선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 합니다.

인재영입팀에 근무하고 있는 `니니즈`는 코딩테스트 결과를 분석하여 채용에 참여한 개발팀들에 제공하기 위해 지원자들의 지원 조건을 선택하면 해당 조건에 맞는 지원자가 몇 명인 지 쉽게 알 수 있는 도구를 만들고 있습니다.
예를 들어, 개발팀에서 궁금해하는 문의사항은 다음과 같은 형태가 될 수 있습니다.
`코딩테스트에 java로 참여했으며, backend 직군을 선택했고, junior 경력이면서, 소울푸드로 pizza를 선택한 사람 중 코딩테스트 점수를 50점 이상 받은 지원자는 몇 명인가?`

물론 이 외에도 각 개발팀의 상황에 따라 아래와 같이 다양한 형태의 문의가 있을 수 있습니다.

- 코딩테스트에 python으로 참여했으며, frontend 직군을 선택했고, senior 경력이면서, 소울푸드로 chicken을 선택한 사람 중 코딩테스트 점수를 100점 이상 받은 사람은 모두 몇 명인가?
- 코딩테스트에 cpp로 참여했으며, senior 경력이면서, 소울푸드로 pizza를 선택한 사람 중 코딩테스트 점수를 100점 이상 받은 사람은 모두 몇 명인가?
- backend 직군을 선택했고, senior 경력이면서 코딩테스트 점수를 200점 이상 받은 사람은 모두 몇 명인가?
- 소울푸드로 chicken을 선택한 사람 중 코딩테스트 점수를 250점 이상 받은 사람은 모두 몇 명인가?
- 코딩테스트 점수를 150점 이상 받은 사람은 모두 몇 명인가?

즉, 개발팀에서 궁금해하는 내용은 다음과 같은 형태를 갖습니다.

```
* [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?
```

------

#### **[문제]**

지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열 info, 개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열 query가 매개변수로 주어질 때,
각 문의조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

#### **[제한사항]**

- info 배열의 크기는 1 이상 50,000 이하입니다.
- info 배열 각 원소의 값은 지원자가 지원서에 입력한 4가지 값과 코딩테스트 점수를 합친 "개발언어 직군 경력 소울푸드 점수" 형식입니다.
  - 개발언어는 cpp, java, python 중 하나입니다.
  - 직군은 backend, frontend 중 하나입니다.
  - 경력은 junior, senior 중 하나입니다.
  - 소울푸드는 chicken, pizza 중 하나입니다.
  - 점수는 코딩테스트 점수를 의미하며, 1 이상 100,000 이하인 자연수입니다.
  - 각 단어는 공백문자(스페이스 바) 하나로 구분되어 있습니다.
- query 배열의 크기는 1 이상 100,000 이하입니다.
- query의 각 문자열은 "[조건] X" 형식입니다.
  - [조건]은 "개발언어 and 직군 and 경력 and 소울푸드" 형식의 문자열입니다.
  - 언어는 cpp, java, python, - 중 하나입니다.
  - 직군은 backend, frontend, - 중 하나입니다.
  - 경력은 junior, senior, - 중 하나입니다.
  - 소울푸드는 chicken, pizza, - 중 하나입니다.
  - '-' 표시는 해당 조건을 고려하지 않겠다는 의미입니다.
  - X는 코딩테스트 점수를 의미하며 조건을 만족하는 사람 중 X점 이상 받은 사람은 모두 몇 명인 지를 의미합니다.
  - 각 단어는 공백문자(스페이스 바) 하나로 구분되어 있습니다.
  - 예를 들면, "cpp and - and senior and pizza 500"은 "cpp로 코딩테스트를 봤으며, 경력은 senior 이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 500점 이상 받은 사람은 모두 몇 명인가?"를 의미합니다.

------

##### **[입출력 예]**

| info                                                         | query                                                        | result        |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------- |
| `["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]` | `["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]` | [1,1,1,1,2,4] |

##### **입출력 예에 대한 설명**

지원자 정보를 표로 나타내면 다음과 같습니다.

| 언어   | 직군     | 경력   | 소울 푸드 | 점수 |
| ------ | -------- | ------ | --------- | ---- |
| java   | backend  | junior | pizza     | 150  |
| python | frontend | senior | chicken   | 210  |
| python | frontend | senior | chicken   | 150  |
| cpp    | backend  | senior | pizza     | 260  |
| java   | backend  | junior | chicken   | 80   |
| python | backend  | senior | chicken   | 50   |

- `"java and backend and junior and pizza 100"` : java로 코딩테스트를 봤으며, backend 직군을 선택했고 junior 경력이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 100점 이상 받은 지원자는 1명 입니다.
- `"python and frontend and senior and chicken 200"` : python으로 코딩테스트를 봤으며, frontend 직군을 선택했고, senior 경력이면서 소울 푸드로 chicken을 선택한 지원자 중 코딩테스트 점수를 200점 이상 받은 지원자는 1명 입니다.
- `"cpp and - and senior and pizza 250"` : cpp로 코딩테스트를 봤으며, senior 경력이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 250점 이상 받은 지원자는 1명 입니다.
- `"- and backend and senior and - 150"` : backend 직군을 선택했고, senior 경력인 지원자 중 코딩테스트 점수를 150점 이상 받은 지원자는 1명 입니다.
- `"- and - and - and chicken 100"` : 소울푸드로 chicken을 선택한 지원자 중 코딩테스트 점수를 100점 이상을 받은 지원자는 2명 입니다.
- `"- and - and - and - 150"` : 코딩테스트 점수를 150점 이상 받은 지원자는 4명 입니다.





**Collections.binarySerch() **

java.util.Collections.binarySearch() 함수는 정렬된 리스트에서 object 위치를 반환하는 java.util.Collections 클래스 메소드이다.

반드시 정렬된 상태여야 한다. 이진 탐색으로 값을 찾기 때문에 정렬이 되어 있지 않으면 이진 탐색을 할 수가 없다.

search 대상을 찾았을 때는 그 대상의 위치를, 만약 찾지 못했을 때는 (- insertion point) -1 에 해당하는 값을 리턴하게 된다.

insertion point는 해당 리스트에 그 key가 존재했다면, 그 key가 삽입되었을 위치를 말한다.

지정한 comparator를 사용해 list의 요소를 비교할 수 없을 때나, key를 비교할 수 없을 때 **ClassCastExciption**이 발생 할 수 있다.



##### **문제 풀이**

```java
import java.util.*;

class Solution {
    Map<String, Integer> Wordmap = new HashMap<>();
    List<List<Integer>> ScoreList = new ArrayList<>();

    public int[] solution(String[] info, String[] query) {
        //조합을 bitmap으로 구하기 위해 WordMap에 모든 원소값 indexing
        Wordmap.put("-", 0);
        Wordmap.put("cpp", 1);
        Wordmap.put("java", 2);
        Wordmap.put("python", 3);
        Wordmap.put("backend", 1);
        Wordmap.put("frontend", 2);
        Wordmap.put("junior", 1);
        Wordmap.put("senior", 2);
        Wordmap.put("chicken", 1);
        Wordmap.put("pizza", 2);
        for (int i = 0; i < 4*3*3*3; ++i)
            ScoreList.add(new ArrayList<>());
        
        for (String str : info) {
            // info의 각 string을 공백을 기준으로 string 배열에 삽입
            String[] word = str.split(" ");
            // int 배열에 각 info들의 index 삽입
            int[] arr = {Wordmap.get(word[0]) *3*3*3,
                         Wordmap.get(word[1]) *3*3,
                         Wordmap.get(word[2]) *3,
                         Wordmap.get(word[3])};
            // str[4]는 score 
            int score = Integer.parseInt(word[4]);
            
            //1을 4번 shift(4가지 항목)하게 되면 10000(2진수) = 16
            for(int i = 0; i < (1<<4); ++i) {
                int idx = 0;
                // '-'이 아닌 각 항목의 원소값 idx에 삽입
                for(int j = 0; j < 4; ++j) {
                    if((i & (1 << j)) != 0) {
                        idx += arr[j];
                    }
                }
                ScoreList.get(idx).add(score);
            }
        }
        // scoreList 정렬 = BinarySearch하기 위해
        for (int i =0; i < 4*3*3*3; ++i)
            Collections.sort(ScoreList.get(i));
        
        int[] answer = new int[query.length];
        for(int i = 0; i < query.length; ++i) {
            String[] word = query[i].split(" ");
            //query에서 검색을 위한 idx
            int idx = Wordmap.get(word[0]) *3*3*3 +
                Wordmap.get(word[2]) *3*3 +
                Wordmap.get(word[4]) *3 +
                Wordmap.get(word[6]);
            int score = Integer.parseInt(word[7]);
            int ret = Collections.binarySearch(ScoreList.get(idx), score);
            
            //BinarySearch를 통해 150을 찾을떄, 만약 150점을 갖는 수가 없으면 1을 더한 음수값이 반환되기 때문에 0보다 작을 경우 -(ret+1) 처리
            if(ret < 0) {
                ret = -(ret + 1);
            } else {
                //binarySearch를 통해서는 가장 작은 index가 무엇인지는 알 수 없음 우리가 필요한 것은 LOW BOUND index값이 필요함
                for(int j = ret - 1; j >= 0; --j) {
                    if(ScoreList.get(idx).get(j) == score) {
                        ret = j;
                    } else {
                        break;
                    }
                }
            }
            // 결과는 해당 index의 전체 크기에서 low bound의 수를 빼야한다.(점수는 00점 이상이기 때문)
            answer[i] = ScoreList.get(idx).size() - ret;
        }
        
        return answer;
    }
}
```

