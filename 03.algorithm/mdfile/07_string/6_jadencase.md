###### 문제 설명

JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

##### 제한 조건

- s는 길이 1 이상인 문자열입니다.
- s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
- 첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )

##### 입출력 예

| s                       |         return          |
| ----------------------- | :---------------------: |
| "3people unFollowed me" | "3people Unfollowed Me" |
| "for the last week"     |   "For The Last Week"   |



##### **문제 풀이**

```java
/* 런타인 에러 43.8 (왜 런타임인지 모르겠다.. O(n)인데*/ 

import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] str = s.toLowerCase().split(" ");
        
        for(int i = 0; i < str.length; i++) {
            String first = String.valueOf(str[i].charAt(0)).toUpperCase();
            if(i == str.length-1)
                answer += first + str[i].substring(1, str[i].length());
            else
                answer += first + str[i].substring(1, str[i].length()) + " ";
        }
        
        return answer;
    }
}
```



##### **문제풀이2**

```java
/* 
split() 함수 이용 x
StringBuilder() 사용 
*/

import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        String first = String.valueOf(s.charAt(0)).toUpperCase();
        
        answer.append(first);
        for(int i = 1; i < s.length(); i++) {
            String idx = String.valueOf(s.charAt(i));
            if(idx.equals(" "))
                answer.append(' ');
            else if(s.charAt(i-1) == ' ')
                answer.append(idx.toUpperCase());
            else
                answer.append(idx.toLowerCase());
        }
        
        return answer.toString();
    }
}
```

