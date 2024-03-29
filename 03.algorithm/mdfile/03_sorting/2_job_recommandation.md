###### 문제 설명

개발자가 사용하는 언어와 `언어 선호도`를 입력하면 그에 맞는 직업군을 추천해주는 알고리즘을 개발하려고 합니다.

아래 표는 5개 직업군 별로 많이 사용하는 5개 언어에 `직업군 언어 점수`를 부여한 표입니다.

| 점수 | SI         | CONTENTS   | HARDWARE   | PORTAL     | GAME       |
| ---- | ---------- | ---------- | ---------- | ---------- | ---------- |
| 5    | JAVA       | JAVASCRIPT | C          | JAVA       | C++        |
| 4    | JAVASCRIPT | JAVA       | C++        | JAVASCRIPT | C#         |
| 3    | SQL        | PYTHON     | PYTHON     | PYTHON     | JAVASCRIPT |
| 2    | PYTHON     | SQL        | JAVA       | KOTLIN     | C          |
| 1    | C#         | C++        | JAVASCRIPT | PHP        | JAVA       |

예를 들면, SQL의 SI `직업군 언어 점수`는 3점이지만 CONTENTS `직업군 언어 점수`는 2점입니다. SQL의 HARDWARE, PORTAL, GAME `직업군 언어 점수`는 0점입니다.

`직업군 언어 점수`를 정리한 문자열 배열 `table`, 개발자가 사용하는 언어를 담은 문자열 배열 `languages`, `언어 선호도`를 담은 정수 배열 `preference`가 매개변수로 주어집니다. 개발자가 사용하는 언어의 `언어 선호도` x `직업군 언어 점수`의 총합이 가장 높은 직업군을 return 하도록 solution 함수를 완성해주세요. 총합이 같은 직업군이 여러 개일 경우, 이름이 사전 순으로 가장 빠른 직업군을 return 해주세요.

------

##### 제한사항

- `table`의 길이 = 5
  - `table`의 원소는 `"직업군 5점언어 4점언어 3점언어 2점언어 1점언어"`형식의 문자열입니다. `직업군`, `5점언어`, `4언어`, `3점언어`, `2점언어`, `1점언어`는 하나의 공백으로 구분되어 있습니다.
  - `table`은 모든 테스트케이스에서 동일합니다.
- 1 ≤ `languages` 의 길이 ≤ 9
  - `languages`의 원소는 `"JAVA"`, `"JAVASCRIPT"`, `"C"`, `"C++"` ,`"C#"` , `"SQL"`, `"PYTHON"`, `"KOTLIN"`, `"PHP"` 중 한 개 이상으로 이루어져 있습니다.
  - `languages`의 원소는 중복되지 않습니다.
- `preference`의 길이 = `languages` 의 길이
  - 1 ≤ `preference`의 원소 ≤ 10

- `preference`의 i번째 원소는 `languages`의 i번째 원소의 `언어 선호도`입니다.
- return 할 문자열은 `"SI"`, `"CONTENTS"`, `"HARDWARE"`, `"PORTAL"`, `"GAME"` 중 하나입니다.

------

##### 입출력 예

| table                                                        | languages                  | preference | result       |
| ------------------------------------------------------------ | -------------------------- | ---------- | ------------ |
| `["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]` | `["PYTHON", "C++", "SQL"]` | [7, 5, 5]  | `"HARDWARE"` |
| `["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]` | `["JAVA", "JAVASCRIPT"]`   | [7, 5]     | `"PORTAL"`   |



------

##### 입출력 예 설명

**입출력 예 #1**

각 직업군 별로 점수를 계산해보면 아래와 같습니다.

아래 사진은 `개발자 언어 선호도` 나타낸 표입니다.

![tc1_preference.PNG](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/9a711ad6-4a8e-4028-b100-0280a4e3a7dd/tc1_preference.PNG)

아래 사진은 개발자가 선호하는 언어의 `직업군 언어 점수`를 나타낸 표입니다.

![tc1_score.PNG](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/1ef5a88a-8109-415d-b611-a6320410b1e1/tc1_score.PNG)

따라서 점수 총합이 41로 가장 높은 `"HARDWARE"`를 return 해야 합니다.

**입출력 예 #2**

각 직업군 별로 점수를 계산해보면 아래와 같습니다.

아래 사진은 `개발자 언어 선호도` 나타낸 표입니다.

![tc2_preference.PNG](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/e49d818b-938a-4cc3-8d2a-27783f2e1af5/tc2_preference.PNG)

아래 사진은 개발자가 선호하는 언어의 `직업군 언어 점수`를 나타낸 표입니다.

![tc2_score.PNG](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/0624156e-e1d3-4299-b554-470815322a79/tc2_score.PNG)
점수 총합이 55로 가장 높은 직업군은 "SI" 와 "PORTAL"입니다.
따라서 사전 순으로 먼저 오는 `"PORTAL"`을 return 해야 합니다.



##### **문제 풀이**

```java
import java.util.*;

class Solution {
    public String solution(String[] table, String[] languages, int[] preference) {
        String[][] totalArr = new String[5][languages.length];
        String[][] tableArr = new String[5][6];
        
        for(int i = 0; i < tableArr.length; i++) {
            String[] str = table[i].split(" ");
            for(int j = 0; j < tableArr[0].length; j++) {
                tableArr[i][j] = str[j];
            }
        }
        
        int[] total = new int[5];
        int[] score = {0, 5, 4, 3, 2, 1};
        for(int i = 0; i < tableArr.length; i++) {
            for(int j = 1; j < tableArr[0].length; j++) {
                for(int k = 0; k < languages.length; k++) {
                    if(tableArr[i][j].equals(languages[k])) {
                        total[i] += preference[k]*score[j];
                    }
                }
            }
        }
        
        Map<String,Integer> eachMap = new HashMap<String,Integer>();
        for(int i = 0; i < total.length; i++) {
            eachMap.put(tableArr[i][0], total[i]);
        }
        
        List<Map.Entry<String, Integer>> scoreList = new LinkedList<>(eachMap.entrySet());
        scoreList.sort(new Comparator<Map.Entry<String, Integer>>() {
            @Override
            public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
	            return o2.getValue() - o1.getValue();
            }
        });
        
        List<String> maxList = new ArrayList<String>();
        int max = scoreList.get(0).getValue();   
        String answer = "";
        for(int i = 0 ; i < scoreList.size(); i++) {
            if(scoreList.get(i).getValue() == max)
                maxList.add(scoreList.get(i).getKey());
        }
        Collections.sort(maxList);
        answer = maxList.get(0);
        return answer;
    }
}
```

