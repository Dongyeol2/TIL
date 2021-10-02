:one: [거리두기 확인하기(BPS)](./06_graph/1_check_the_distance.md)

:one: [네트워크(DFS)](./06_graph/2_network.md)

---



### 깊이 우선 탐색(DFS) / 너비 우선 탐색(BFS)

그래프를 탐색하는 방법에는 크게 **깊이 우선 탐색(DFS)**과 **너비 우선 탐색(BFS)**이 있습니다.

 

📌여기서 그래프란, **정점(node)과 그 정점을 연결하는 간선(edge)으로 이루어진 자료구조의 일종**을 말하며,

그래프를 탐색한다는 것은 **하나의 정점으로부터 시작하여 차례대로 모든 정점들을 한 번씩 방문하는 것**을 말합니다.


*그래프와 트리의 차이가 궁금하다면? 👇🏻*

닫기

![img](https://blog.kakaocdn.net/dn/dKZgB7/btqB6YFI2Q9/kj4O1ZgTrxTZiyqFplXRF0/img.png)그래프와 트리의 차이

큰 특징만 말하자면, 그래프 중에서 **방향성이 있는 비순환 그래프**를 트리라고 말합니다.

 

#### **1. 깊이 우선 탐색 (DFS, Depth-First Search)**

#### **:** **최대한 깊이 내려간 뒤, 더이상 깊이 갈 곳이 없을 경우 옆으로 이동**



![img](https://blog.kakaocdn.net/dn/xC9Vq/btqB8n5A25K/GyOf4iwqu8euOyhwtFuyj1/img.gif)출처 https://developer-mac.tistory.com/64



 

**💡 깊이 우선 탐색의 개념**

루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에

**해당 분기를 완벽하게 탐색**하는 방식을 말합니다.

 

예를 들어, 미로찾기를 할 때 최대한 한 방향으로 갈 수 있을 때까지 쭉 가다가

더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와서

그 갈림길부터 다시 다른 방향으로 탐색을 진행하는 것이 깊이 우선 탐색 방식이라고 할 수 있습니다.

 

\1. 모든 노드를 방문하고자 하는 경우에 이 방법을 선택함

\2. 깊이 우선 탐색(DFS)이 너비 우선 탐색(BFS)보다 **좀 더 간단함**

\3. 검색 속도 자체는 너비 우선 탐색(BFS)에 비해서 **느림**

 

#### **2. 너비 우선 탐색 (BFS, Breadth-First Search)**

#### **: 최대한 넓게 이동한 다음, 더 이상 갈 수 없을 때 아래로 이동**

 



![img](https://blog.kakaocdn.net/dn/c305k7/btqB5E2hI4r/ea7vFo08tkDYo4c8wkfVok/img.gif)출처 https://developer-mac.tistory.com/64



 

**💡 너비 우선 탐색의 개념**

루트 노드(혹은 다른 임의의 노드)에서 시작해서 **인접한 노드를 먼저** **탐색**하는 방법으로,

시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법입니다.

 

주로 두 노드 사이의 **최단 경로**를 찾고 싶을 때 이 방법을 선택합니다.

ex) 지구 상에 존재하는 모든 친구 관계를 그래프로 표현한 후 Sam과 Eddie사이에 존재하는 경로를 찾는 경우

 

\* 깊이 우선 탐색의 경우 - 모든 친구 관계를 다 살펴봐야 할지도 모름

\* 너비 우선 탐색의 경우 - Sam과 가까운 관계부터 탐색

 

 

 

#### **3. 깊이 우선 탐색(DFS) 과 너비 우선 탐색(BFS) 비교**

 



![img](https://blog.kakaocdn.net/dn/cQYkI8/btqB8oDsMGe/EEYm0cKGYhxTR0kJhGiJPK/img.gif)출처 https://namu.wiki/w/BFS



 

| **DFS(깊이우선탐색)**                             | **BFS(너비우선탐색)**                   |
| ------------------------------------------------- | --------------------------------------- |
| 현재 정점에서 갈 수 있는 점들까지 들어가면서 탐색 | 현재 정점에 연결된 가까운 점들부터 탐색 |
| 스택 또는 재귀함수로 구현                         | 큐를 이용해서 구현                      |

**💡\**DFS와 BFS의 시간복잡도\****

두 방식 모두 조건 내의 모든 노드를 검색한다는 점에서 시간 복잡도는 동일합니다.

DFS와 BFS 둘 다 다음 노드가 방문하였는지를 확인하는 시간과 각 노드를 방문하는 시간을 합하면 됩니다.

 

N은 노드, E는 간선일 때

> 인접 리스트 : O(N+E)
> 인접 행렬 : O(N²)

일반적으로 E(간선)의 크기가 N²에 비해 상대적으로 적기 때문에

인접 리스트 방식이 효율적임

 

 

더보기



#### **3. 깊이 우선 탐색(DFS)과 너비 우선 탐색(BFS) 활용한 문제 유형/응용**

DFS, BFS은 특징에 따라 사용에 더 적합한 문제 유형들이 있습니다.



1) 그래프의 **모든 정점을 방문**하는 것이 주요한 문제

단순히 모든 정점을 방문하는 것이 중요한 문제의 경우 DFS, BFS 두 가지 방법 중 어느 것을 사용하셔도 상관없습니다.

둘 중 편한 것을 사용하시면 됩니다.



2) **경로의 특징**을 저장해둬야 하는 문제

예를 들면 각 정점에 숫자가 적혀있고 a부터 b까지 가는 경로를 구하는데 경로에 같은 숫자가 있으면 안 된다는 문제 등, 각각의 경로마다 특징을 저장해둬야 할 때는 DFS를 사용합니다. (BFS는 경로의 특징을 가지지 못합니다)

 

3) **최단거리** 구해야 하는 문제

미로 찾기 등 최단거리를 구해야 할 경우, BFS가 유리합니다.

왜냐하면 깊이 우선 탐색으로 경로를 검색할 경우 *처음으로 발견되는 해답이 최단거리가 아닐 수 있지만,* 
너비 우선 탐색으로 현재 노드에서 가까운 곳부터 찾기 때문에경로를 탐색 시 먼저 찾아지는 해답이 곧 최단거리기 때문입니다.

 

이밖에도 

\- 검색 대상 그래프가 정말 크다면 DFS를 고려
\- 검색대상의 규모가 크지 않고, 검색 시작 지점으로부터 원하는 대상이 별로 멀지 않다면 BFS

 

#### **4. DFS와 BFS을 사용한 JAVA코드**

 

**DFS 알고리즘**에 경우 두 가지 방법으로 풀 수 있는데,

첫 번째로 **스택**을 이용하는 것

두 번째로 **재귀함수**를재귀 함수를 이용하는 것인데, 재귀 함수를 이용하는 것이 가장 보편적이고 짧은 코드를 작성할 수 있다.

 

재귀 함수란 함수 내부에서 함수가 자기 자신을 또다시 호출하는 함수를 의미합니다.

이러한 재귀 호출은 자기가 자신을 계속해서 호출하므로, 끝없이 반복되기 때문에

함수 내에 **재귀 호출을 중단하도록 조건이 변경될 명령문을 반드시 포함**해야 합니다.

```JAVA
/* 인접 리스트 이용 */
class Graph {
  private int V;
  private LinkedList<Integer> adj[];
 
  Graph(int v) {
      V = v;
      adj = new LinkedList[v];
      // 인접 리스트 초기화
      for (int i=0; i<v; ++i)
          adj[i] = new LinkedList();
  }
  void addEdge(int v, int w) { adj[v].add(w); }
   
  /* DFS */
  void DFS(int v) {
      boolean visited[] = new boolean[V];
 
      // v를 시작 노드로 DFSUtil 재귀 호출
      DFSUtil(v, visited);
  }
  
  /* DFS에 의해 사용되는 함수 */
  void DFSUtil(int v, boolean visited[]) {
      // 현재 노드를 방문한 것으로 표시하고 값을 출력
      visited[v] = true;
      System.out.print(v + " ");
 
      // 방문한 노드와 인접한 모든 노드를 가져온다.
      Iterator<Integer> it = adj[v].listIterator();
      while (it.hasNext()) {
          int n = it.next();
          // 방문하지 않은 노드면 해당 노드를 시작 노드로 다시 DFSUtil 호출
          if (!visited[n])
              DFSUtil(n, visited);
      }
  }
}
```

 

**BFS 알고리즘**은 큐(Queue)를 사용해서 문제를 해결하면 됩니다.

```JAVA
class Graph {
  private int V;
  private LinkedList<Integer> adj[];
 
  Graph(int v) {
    V = v;
    adj = new LinkedList[v];
    for (int i=0; i<v; ++i)
      adj[i] = new LinkedList();
  }
 
  void addEdge(int v, int w) { adj[v].add(w); }
 
  /* BFS */
  void BFS(int s) {
    boolean visited[] = new boolean[V]; //방문여부 확인용 변수
    LinkedList<Integer> queue = new LinkedList<Integer>(); //연결리스트 생성
 
    visited[s] = true;
    queue.add(s);
 
    while (queue.size() != 0) {
      // 방문한 노드를 큐에서 추출(dequeue)하고 값을 출력
      s = queue.poll();
      System.out.print(s + " ");
 
      // 방문한 노드와 인접한 모든 노드를 가져온다.
      Iterator<Integer> i = adj[s].listIterator();
      while (i.hasNext()) {
        int n = i.next();
        
        // 방문하지 않은 노드면 방문한 것으로 표시하고 큐에 삽입(enqueue)
        if (!visited[n]) {
          visited[n] = true;
          queue.add(n);
        }
      }
    }
  }
}
```



출처: https://devuna.tistory.com/32 [튜나 개발일기]