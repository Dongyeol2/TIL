###### 문제 설명

## 카카오 프렌즈 컬러링북

출판사의 편집자인 어피치는 네오에게 컬러링북에 들어갈 원화를 그려달라고 부탁하여 여러 장의 그림을 받았다. 여러 장의 그림을 난이도 순으로 컬러링북에 넣고 싶었던 어피치는 영역이 많으면 색칠하기가 까다로워 어려워진다는 사실을 발견하고 그림의 난이도를 영역의 수로 정의하였다. (영역이란 상하좌우로 연결된 같은 색상의 공간을 의미한다.)

그림에 몇 개의 영역이 있는지와 가장 큰 영역의 넓이는 얼마인지 계산하는 프로그램을 작성해보자.

![alt text](http://t1.kakaocdn.net/codefestival/apeach.png)

위의 그림은 총 12개 영역으로 이루어져 있으며, 가장 넓은 영역은 어피치의 얼굴면으로 넓이는 120이다.

### 입력 형식

입력은 그림의 크기를 나타내는 `m`과 `n`, 그리고 그림을 나타내는 `m × n` 크기의 2차원 배열 `picture`로 주어진다. 제한조건은 아래와 같다.

- `1 <= m, n <= 100`
- `picture`의 원소는 `0` 이상 `2^31 - 1` 이하의 임의의 값이다.
- `picture`의 원소 중 값이 `0`인 경우는 색칠하지 않는 영역을 뜻한다.

### 출력 형식

리턴 타입은 원소가 두 개인 정수 배열이다. 그림에 몇 개의 영역이 있는지와 가장 큰 영역은 몇 칸으로 이루어져 있는지를 리턴한다.

### 예제 입출력

| m    | n    | picture                                                      | answer |
| ---- | ---- | ------------------------------------------------------------ | ------ |
| 6    | 4    | [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]] | [4, 5] |

### 예제에 대한 설명

예제로 주어진 그림은 총 4개의 영역으로 구성되어 있으며, 왼쪽 위의 영역과 오른쪽의 영역은 모두 `1`로 구성되어 있지만 상하좌우로 이어져있지 않으므로 다른 영역이다. 가장 넓은 영역은 왼쪽 위 `1`이 차지하는 영역으로 총 5칸이다.



### 문제 풀이

```java
class Solution {
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static int numberOfArea;
    static int maxSizeOfOneArea;
    static boolean[][] visited;
    int[] answer = new int[2];
    int temp_answer = 0;
    
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        visited = new boolean[m][n];

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(visited[i][j] == true)
                    continue;
                visited[i][j] = true;
                temp_answer++;
                dfs(i, j, visited, picture);
                if(picture[i][j] != 0)
                    numberOfArea++;
                System.out.println("i : "+i+" j : "+j);
                if(maxSizeOfOneArea < temp_answer)
                    maxSizeOfOneArea = temp_answer;
                temp_answer = 0;
            }
        }
        
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
    public void dfs(int x, int y, boolean[][] visited, int[][] picture) {
        if(picture[x][y] == 0)
            return;
        
        for(int i = 0; i < 4; i++) {
            int rx = x + dx[i];
            int ry = y + dy[i];
            
            if(rx < 0 || rx >= picture.length || ry < 0 || ry >= picture[0].length || visited[rx][ry] == true || picture[rx][ry] == 0)
                continue;
            if(picture[x][y] == picture[rx][ry]) {
                visited[rx][ry] = true;
                temp_answer++;
                dfs(rx, ry, visited, picture);
            }
        }
    }
}
```

