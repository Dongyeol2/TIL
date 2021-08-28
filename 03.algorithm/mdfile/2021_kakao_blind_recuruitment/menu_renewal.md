# 2. 메뉴 리뉴얼

###### 문제 설명

레스토랑을 운영하던 `스카피`는 코로나19로 인한 불경기를 극복하고자 메뉴를 새로 구성하려고 고민하고 있습니다.
기존에는 단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서 새로운 메뉴를 제공하기로 결정했습니다. 어떤 단품메뉴들을 조합해서 코스요리 메뉴로 구성하면 좋을 지 고민하던 "스카피"는 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성하기로 했습니다.
단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다. 또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.

예를 들어, 손님 6명이 주문한 단품메뉴들의 조합이 다음과 같다면,
(각 손님은 단품메뉴를 2개 이상 주문해야 하며, 각 단품메뉴는 A ~ Z의 알파벳 대문자로 표기합니다.)

| 손님 번호 | 주문한 단품메뉴 조합 |
| --------- | -------------------- |
| 1번 손님  | A, B, C, F, G        |
| 2번 손님  | A, C                 |
| 3번 손님  | C, D, E              |
| 4번 손님  | A, C, D, E           |
| 5번 손님  | B, C, F, G           |
| 6번 손님  | A, C, D, E, H        |

가장 많이 함께 주문된 단품메뉴 조합에 따라 "스카피"가 만들게 될 코스요리 메뉴 구성 후보는 다음과 같습니다.

| 코스 종류     | 메뉴 구성  | 설명                                                 |
| ------------- | ---------- | ---------------------------------------------------- |
| 요리 2개 코스 | A, C       | 1번, 2번, 4번, 6번 손님으로부터 총 4번 주문됐습니다. |
| 요리 3개 코스 | C, D, E    | 3번, 4번, 6번 손님으로부터 총 3번 주문됐습니다.      |
| 요리 4개 코스 | B, C, F, G | 1번, 5번 손님으로부터 총 2번 주문됐습니다.           |
| 요리 4개 코스 | A, C, D, E | 4번, 6번 손님으로부터 총 2번 주문됐습니다.           |

------

#### **[문제]**

각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders, "스카피"가 `추가하고 싶어하는` 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때, "스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

#### **[제한사항]**

- orders 배열의 크기는 2 이상 20 이하입니다.

- orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.

  - 각 문자열은 알파벳 대문자로만 이루어져 있습니다.
  - 각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.

- course 배열의 크기는 1 이상 10 이하입니다.

  - course 배열의 각 원소는 2 이상 10 이하인 자연수가 `오름차순`으로 정렬되어 있습니다.
  - course 배열에는 같은 값이 중복해서 들어있지 않습니다.

- 정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로

   

  ```
  오름차순
  ```

   

  정렬해서 return 해주세요.

  - 배열의 각 원소에 저장된 문자열 또한 알파벳 `오름차순`으로 정렬되어야 합니다.
  - 만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
  - orders와 course 매개변수는 return 하는 배열의 길이가 1 이상이 되도록 주어집니다.

------

##### **[입출력 예]**

| orders                                              | course  | result                              |
| --------------------------------------------------- | ------- | ----------------------------------- |
| `["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]`   | [2,3,4] | `["AC", "ACDE", "BCFG", "CDE"]`     |
| `["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]` | [2,3,5] | `["ACD", "AD", "ADE", "CD", "XYZ"]` |
| `["XYZ", "XWY", "WXA"]`                             | [2,3,4] | `["WX", "XY"]`                      |

##### **입출력 예에 대한 설명**

------

**입출력 예 #1**
문제의 예시와 같습니다.

**입출력 예 #2**
AD가 세 번, CD가 세 번, ACD가 두 번, ADE가 두 번, XYZ 가 두 번 주문됐습니다.
요리 5개를 주문한 손님이 1명 있지만, 최소 2명 이상의 손님에게서 주문된 구성만 코스요리 후보에 들어가므로, 요리 5개로 구성된 코스요리는 새로 추가하지 않습니다.

**입출력 예 #3**
WX가 두 번, XY가 두 번 주문됐습니다.
3명의 손님 모두 단품메뉴를 3개씩 주문했지만, 최소 2명 이상의 손님에게서 주문된 구성만 코스요리 후보에 들어가므로, 요리 3개로 구성된 코스요리는 새로 추가하지 않습니다.
또, 단품메뉴를 4개 이상 주문한 손님은 없으므로, 요리 4개로 구성된 코스요리 또한 새로 추가하지 않습니다.

##### [문제 풀이]

```java
import java.util.*;

class Solution {
    List<Map<String,Integer>> FoodMaps = new ArrayList<>();
    int[] MaxCnt = new int[11];
    
    void comb(char[] str, int pos, StringBuilder candi) {
        /* 4. order의 모든 메뉴들을 조합했을 때 나올 수 있는 조합들 */
        if(pos >= str.length) {
            /* 5. candi는 재귀를 했을 때 나오는 result 값을 나타냄 */
            int len = candi.length();
            /* 6. 2가지 이상의 단품 메뉴를 주문 했을 때의 조합을 뽑기 위함 */
            if(len >= 2) {
                int cnt = FoodMaps.get(len).getOrDefault(candi.toString(),0)+1;
                /* 7. 1-10의 HashMap에 조합과 그 조합이 몇번 나왔는지를 저장 */
                FoodMaps.get(len).put(candi.toString(), cnt);
                /* 8. 조합이 가장 많이 나온 값을 Max 값으로 지정 */
                MaxCnt[len] = Math.max(MaxCnt[len], cnt);
            }
            return;
        }
        
        /* 3. 각 order에서 나올 수 있는 모든 조합을 구하기 위해 재귀 호출 */
        comb(str, pos+1, candi.append(str[pos]));
        candi.setLength(candi.length()-1);
        comb(str, pos+1, candi);
    }
    
    public String[] solution(String[] orders, int[] course) {
        /* 1. 1-10개의 코스로 구성할 것이기 때문에 10개의 HashMap 생성 */
        for(int i = 0; i < 11; i++)
            FoodMaps.add(new HashMap<String,Integer>());
        
        /* 2. 각 order의 조합 */
        for (String str : orders) {
            char[] arr = str.toCharArray();
            Arrays.sort(arr);
            comb(arr, 0, new StringBuilder());
        }
        
        List<String> list = new ArrayList<String>();
        for(int len : course) {
            for(Map.Entry<String,Integer> entry : FoodMaps.get(len).entrySet()) {
                /* 코스의 메뉴수는 2가지 이상이며, 가장 많이 나온 조합들을 list에 저장 */
                if(entry.getValue() >= 2 && entry.getValue() == MaxCnt[len]) {
                    list.add(entry.getKey());
                }
            }
        }
        /* 오름차순으로 list 정렬 */
        Collections.sort(list);
        
        String[] answer = new String[list.size()];
        for(int i = 0; i < list.size(); i++)
            answer[i] = list.get(i);
        return answer;
    }
}
```

