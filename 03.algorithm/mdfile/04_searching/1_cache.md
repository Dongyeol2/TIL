###### 문제 설명

## 캐시

지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.
이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.

어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.

### 입력 형식

- 캐시 크기(`cacheSize`)와 도시이름 배열(`cities`)을 입력받는다.
- `cacheSize`는 정수이며, 범위는 0 ≦ `cacheSize` ≦ 30 이다.
- `cities`는 도시 이름으로 이뤄진 문자열 배열로, 최대 도시 수는 100,000개이다.
- 각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 도시 이름은 최대 20자로 이루어져 있다.

### 출력 형식

- 입력된 도시이름 배열을 순서대로 처리할 때, "총 실행시간"을 출력한다.

### 조건

- 캐시 교체 알고리즘은 `LRU`(Least Recently Used)를 사용한다.
- `cache hit`일 경우 실행시간은 `1`이다.
- `cache miss`일 경우 실행시간은 `5`이다.

### 입출력 예제

| 캐시크기(cacheSize) | 도시이름(cities)                                             | 실행시간 |
| ------------------- | ------------------------------------------------------------ | -------- |
| 3                   | ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"] | 50       |
| 3                   | ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"] | 21       |
| 2                   | ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"] | 60       |
| 5                   | ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"] | 52       |
| 2                   | ["Jeju", "Pangyo", "NewYork", "newyork"]                     | 16       |
| 0                   | ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]                 | 25       |



##### **문제 풀이**

```java
import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        List<String> cache = new ArrayList<String>();
        for(int i = 0; i < cities.length; i++)
            cities[i] = cities[i].toLowerCase();
        
        if(cacheSize != 0)
            cache.add(cities[0]);
        int processTime = 5;
        
        for(int i = 1; i < cities.length; i++) {
            if(cache.size() < cacheSize) {
                if(cache.contains(cities[i])) {
                    cache.remove(cache.indexOf(cities[i]));
                    cache.add(cities[i]);
                    processTime += 1;   
                }
                else {
                    cache.add(cities[i]);
                    processTime = processTime+5;
                }
            }
            else {
                if(cache.contains(cities[i])) {
                    cache.remove(cache.indexOf(cities[i]));
                    cache.add(cities[i]);
                    processTime += 1;
                }
                
                else {
                    if(cacheSize != 0) {
                        cache.remove(0);
                        cache.add(cities[i]);  
                    }
                    processTime = processTime+5;
                }
            }
        }
        
        int answer = processTime;
        return answer;
    }
}
```



**Least Recently Used 알고리즘이란?**

\- 가장 오랫동안 참조되지 않은 페이지를 교체하는 기법

\- 컴퓨터의 자원은 한정적이며, 한도내에서 최고의 효율을 얻기 위해 여러 알고리즘이 존재, 그 중에 하나.

  (FIFO,OPT,LRU,LFU,MFU 등등..)

**방법** 

**첫번째 :** 페이지에 저장 된 데이터가 언제 사용되었는지를 알 수 있게하는 부분을 구현해서 제일 오랫동안 참조되지 않는 데이터를 제거 하는 방법.

**두번째 :** 페이지에 데이터를 큐 형식으로 저장하는 방식.

​      페이지내에 데이터가 존재한다면 데이터를 페이지 내에서 제거하고 맨 위로 다시 올리고,

​      존재하지 않는다면, 바로 입력하여 맨 아래에 있는 데이터를 삭제하는 과정을 진행.

**예제 그림**

![img](https://blog.kakaocdn.net/dn/cNYCeD/btqQIbdtmtF/8WszlVIyeSgKS3DNcb2em0/img.png)

위 그림에서 **7번, 9번**같은 상황은 참조하는 값이 이미 페이지에 존재하며 **Cache Hit** 라고 하며, 

나머지 상황들이 존재하지 않을때 새로 교체 됨으로 **Cache Miss** 라고한다.