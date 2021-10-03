:one: [짝지어 제거하기(프로그래머스)](./07_string/1_remove_by_pair.md)

:two: [뉴스클러스터링(프로그래머스)](./07_string/2_news_clustering.md)

:three: [튜플(프로그래머스)](./07_string/3_tuple.md)

:four: [영어 끝말잇기(프로그래머스)](./07_string/4_end_to_end.md)

:four: [숫자 문자열과 영단어(2021 카카오 채용연계형 인턴쉽)](./07_string/5_number_string.md)

---

##### **string 이차원 배열 정렬**

```java
public void sort(String[][] tickets) {
        Arrays.sort(tickets, new Comparator<String[]>() {
            public int compare(String[] o1, String[] o2) {
                /* 1. 내림차순 1번째 열 기준 */
                if(o1[1].compareTo(o2[1]) > 0)
                    return 1;
                else
                    return -1;
                
                /* 2. 오름차순 1번째 열 기준 */
            	if(o1[1].compareTo(o2[1]) < 0)
                    return 1;
                else
                    return -1
            }
        });
    }
```

