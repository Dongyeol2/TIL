# 1. 신규 아이디 추천

###### 문제 설명

카카오에 입사한 신입 개발자 `네오`는 "카카오계정개발팀"에 배치되어, 카카오 서비스에 가입하는 유저들의 아이디를 생성하는 업무를 담당하게 되었습니다. "네오"에게 주어진 첫 업무는 새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발하는 것입니다.
다음은 카카오 아이디의 규칙입니다.

- 아이디의 길이는 3자 이상 15자 이하여야 합니다.
- 아이디는 알파벳 소문자, 숫자, 빼기(`-`), 밑줄(`_`), 마침표(`.`) 문자만 사용할 수 있습니다.
- 단, 마침표(`.`)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

"네오"는 다음과 같이 7단계의 순차적인 처리 과정을 통해 신규 유저가 입력한 아이디가 카카오 아이디 규칙에 맞는 지 검사하고 규칙에 맞지 않은 경우 규칙에 맞는 새로운 아이디를 추천해 주려고 합니다.
신규 유저가 입력한 아이디가 `new_id` 라고 한다면,

```
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
```

------

예를 들어, new_id 값이 "...!@BaT#*..y.abcdefghijklm" 라면, 위 7단계를 거치고 나면 new_id는 아래와 같이 변경됩니다.

1단계 대문자 'B'와 'T'가 소문자 'b'와 't'로 바뀌었습니다.
`"...!@BaT#*..y.abcdefghijklm"` → `"...!@bat#*..y.abcdefghijklm"`

2단계 '!', '@', '#', '*' 문자가 제거되었습니다.
`"...!@bat#*..y.abcdefghijklm"` → `"...bat..y.abcdefghijklm"`

3단계 '...'와 '..' 가 '.'로 바뀌었습니다.
`"...bat..y.abcdefghijklm"` → `".bat.y.abcdefghijklm"`

4단계 아이디의 처음에 위치한 '.'가 제거되었습니다.
`".bat.y.abcdefghijklm"` → `"bat.y.abcdefghijklm"`

5단계 아이디가 빈 문자열이 아니므로 변화가 없습니다.
`"bat.y.abcdefghijklm"` → `"bat.y.abcdefghijklm"`

6단계 아이디의 길이가 16자 이상이므로, 처음 15자를 제외한 나머지 문자들이 제거되었습니다.
`"bat.y.abcdefghijklm"` → `"bat.y.abcdefghi"`

7단계 아이디의 길이가 2자 이하가 아니므로 변화가 없습니다.
`"bat.y.abcdefghi"` → `"bat.y.abcdefghi"`

따라서 신규 유저가 입력한 new_id가 "...!@BaT#*..y.abcdefghijklm"일 때, 네오의 프로그램이 추천하는 새로운 아이디는 "bat.y.abcdefghi" 입니다.

------

#### **[문제]**

신규 유저가 입력한 아이디를 나타내는 new_id가 매개변수로 주어질 때, "네오"가 설계한 7단계의 처리 과정을 거친 후의 추천 아이디를 return 하도록 solution 함수를 완성해 주세요.

#### **[제한사항]**

new_id는 길이 1 이상 1,000 이하인 문자열입니다.
new_id는 알파벳 대문자, 알파벳 소문자, 숫자, 특수문자로 구성되어 있습니다.
new_id에 나타날 수 있는 특수문자는 `-_.~!@#$%^&*()=+[{]}:?,<>/` 로 한정됩니다.

------

##### **[입출력 예]**

| no   | new_id                          | result              |
| ---- | ------------------------------- | ------------------- |
| 예1  | `"...!@BaT#*..y.abcdefghijklm"` | `"bat.y.abcdefghi"` |
| 예2  | `"z-+.^."`                      | `"z--"`             |
| 예3  | `"=.="`                         | `"aaa"`             |
| 예4  | `"123_.def"`                    | `"123_.def"`        |
| 예5  | `"abcdefghijklmn.p"`            | `"abcdefghijklmn"`  |

##### **입출력 예에 대한 설명**

------

**입출력 예 #1**
문제의 예시와 같습니다.

**입출력 예 #2**
7단계를 거치는 동안 new_id가 변화하는 과정은 아래와 같습니다.

1단계 변화 없습니다.
2단계 `"z-+.^."` → `"z-.."`
3단계 `"z-.."` → `"z-."`
4단계 `"z-."` → `"z-"`
5단계 변화 없습니다.
6단계 변화 없습니다.
7단계 `"z-"` → `"z--"`

**입출력 예 #3**
7단계를 거치는 동안 new_id가 변화하는 과정은 아래와 같습니다.

1단계 변화 없습니다.
2단계 `"=.="` → `"."`
3단계 변화 없습니다.
4단계 `"."` → `""` (new_id가 빈 문자열이 되었습니다.)
5단계 `""` → `"a"`
6단계 변화 없습니다.
7단계 `"a"` → `"aaa"`

**입출력 예 #4**
1단계에서 7단계까지 거치는 동안 new_id("123_.def")는 변하지 않습니다. 즉, new_id가 처음부터 카카오의 아이디 규칙에 맞습니다.

**입출력 예 #5**
1단계 변화 없습니다.
2단계 변화 없습니다.
3단계 변화 없습니다.
4단계 변화 없습니다.
5단계 변화 없습니다.
6단계 `"abcdefghijklmn.p"` → `"abcdefghijklmn."` → `"abcdefghijklmn"`
7단계 변화 없습니다.

##### [문제 풀이]

```java
import java.util.*;

class Solution {
    public String solution(String new_id) {
        String answer = "";
        int i;
        
        //1. 모든 대문자 소문자 치환
        String step1 = new_id.toLowerCase();
        
        //2. 소문자, 숫자, -, _, . 제외 모든 문자 제거
        String step2 = "";
        for(i = 0; i < step1.length(); i++) {
            char ch = step1.charAt(i);
            
            if(ch >= 'a' && ch <= 'z')
                step2 += String.valueOf(ch);
            else if(ch >= '0' && ch <= '9')
                step2 += String.valueOf(ch);
            else if(ch == '-' || ch == '_' || ch == '.')
                step2 += String.valueOf(ch);
            else
                continue;
        }
        
        //3. 마침표가 2번이상 연속된 부분을 하나의 마침표로 치환
        String step3 = step2.replace("..",".");
        while(step3.contains(".."))
            step3 = step3.replace("..",".");
        
        //4. 마침표가 처음이나 끝에 위치한다면 제거
        String step4 = step3;
        if(step4.length() > 0) {
            if(step4.charAt(0) == '.')
                step4 = step4.substring(1, step4.length());
        }
        if(step4.length() > 0) {
            if(step4.charAt(step4.length()-1) == '.')
                step4 = step4.substring(0, step4.length()-1);
        }
        
        //5. 빈 문자열이라면 new_id에 "a" 대입
        String step5 = step4;
        if(step5.equals(""))
            step5 = "a";
        
        //6. 길이 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자 제거
        // 만약, 제거후 마침표가 마지막 문자열일 경우 마침표 제거
        String step6 = step5;
        if(step6.length() > 15) { 
            step6 = step6.substring(0, 15);
            if(step6.charAt(step6.length()-1) == '.')
                step6 = step6.substring(0,step6.length()-1);
        }
        
        //7. 길이 2자 이하이면 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙인다.
        String step7 = step6;
        if(0 < step7.length() && step7.length() <= 2) {
            char last = step7.charAt(step7.length() - 1);
            
            while(step7.length() < 3)
                step7 = step7+last;
        }
        
        answer = String.valueOf(step7);
        return answer;
    }
}
```



## ※ 사용된 String 함수 정리

**toUpperCase()** : 소문자 -> 대문자 치환

```java
String lower = "abcd";
String uppper = lower.toUpperCase(lower);
System.out.println(upper);
/* ABCD 출력 */
```



**toLowerCase()** : 대문자 -> 소문자 치환

```java
String upper = "ABCD";
String lower = upper.toLowerCase(upper);
System.out.println(lower);
/* abcd 출력 */
```

**replace()** : 문자 치환1</br>
**replaceAll()** : 문자 치환2 == 바꾸고 싶은 문자로 문자열을 전부 치환</br>
**replaceFirst()** : 문자 치환3 == 바꾸고싶은 문자열이 처음으로 해당할때만 치환</br>

```java
/* replace */
String a = "무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세 ";	
//replace([기존문자],[바꿀문자])
a = a.replace("대한", "민국");	
System.out.println(a);

//결과값 : 무궁화 삼천리 화려강산 민국사람 민국으로 길이 보전하세
--------------------------------------------------------------------------------
/* replaceAll */
String a = "무궁화. 삼천리. 화려강산. 대한사람. 대한으로. 길이. 보전하세 ";
//replaceAll([정규식],[바꿀문자])
a = a.replaceAll(".", "/");
System.out.println(a);

//결과값 : /////////////////////////////////////
----------------------------------------------------------------------------------
/* replaceFirst */
String a = "무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세 ";
//replaceFirst([기존문자],[바꿀문자])
a = a.replaceFirst("대한", "민국");
System.out.println(a);

//결과값 : 무궁화 삼천리 화려강산 민국사람 대한으로 길이 보전하세
```



Stringbuffer 객체일 경우 

특정문자 제거 : deleteCharAt('제거할 문자 index 위치')



문자열 자르기 : substring()
1) substring(int index)
2) substring(int beginIndex, int endIndex)



문자 비교

Character.compare(char a, char b)
두문자 같을 경우 0
첫 번째 문자가 두 번째 문자보다 작으면 음수
첫 번째 문자가 두 번째 문자보다 크면 양수 반환

==

String.matches()

문자열 비교
str1.equals(str2)

toString() / String.valueOf
toString()과 같은 경우 Null PointerExciption(NPE) 발생
valueOf는 "null"이라는 문자열로 처리 -> vlaueOf의 null 체크 방법은 "null".equals(string) 형태로 체크

contains(CharSequence s)

문자열 붙이기
Stringbuffer 일 경우
append()
str.append(string)

string일 경우
str.concat(string)