글에 앞서..

재귀적 호출에 대한 개념을 먼저 알아보자. 그 이유는 알고리즘에서 해당 호출방식을 자주 활용하기 때문이다.

### 재귀함수의 기본적인 이해란

:grey_question:재귀함수란?
함수내에서 자기 자신을 다시 호출하는 함수
자신이 수행할 작업을 유사한 형태의 여러 조각으로 쪼갠 뒤 그 중 한 조각을 수행하고, 나머지를 자기 자신을 호출해 실행하는 함수

:grey_question: 재귀함수 호출 방식

```java
void RecurciveFunction(void)
{
	printf("Recursive function example1 \n")
	RecursiveFunction();
}
```

**기저사례 (base case)**
:arrow_right: 더 이상 쪼개지지 않는 가장 작은 작업, 즉 최소한의 작업에 도달했을 때 답을 곧장 반환하는 조건문에 포함될 내용

:arrow_right: 기저 사례를 선택할 때는 존재하는 모든 입력이 항상 기저 사례의 답을 이용해 계산될 수 있도록 신경써야 한다.

# 완전 탐색(Exchustive search)

:one: 완전탐색이란?

:arrow_right: '무식하게 푼다(brute-force)'는 컴퓨터의 빠른 계산 능력을 이용해 가능한 경우의 수를 일일이 나열하면서 답을 찾는 방법을 의미. 이렇게 **가능한 방법을 전부 만들어 보는 알고리즘을 뜻한다.**

:arrow_right: 완전 탐색은 컴퓨터의 빠른 계산 속도를 잘 이용하는 방법이다.

:arrow_right: **예제** n개의 원소 중 m개를 고르는 모든 조합을 출력하는 코드

```java
//n : 전체 원수의 수
//picked : 지금까지 고른 원소들의 번호
//toPick : 더 고를 원소의 수일 때, 앞으로 toPick개의 원소를 고르는 모든 방법을 출력한다.
void pick(int n, vector<int>& picked, int toPick) {
	//기저 사례 : 더 고를 원소가 없을 때 고른 원소들을 출력한다.
	if(toPick == 0) {
		printPicked(pick);
		return;
	}
	//고를 수 있는 가장 작은 번호를 계산한다.
	int smallest = picked.empty() ? 0 : picked.back() + 1;
	//이 단계에서 원소 하나를 고른다.
	for(int next = smallest; next < n; ++next) {
		picked.push_back(next);
		pick(n, picked, toPick - 1);
		picked.pop_back();
	}
}
```

:two: 완전 탐색 방법

- Brute Force : for문과 if문을 이용하여 처음부터 끝까지 탐색하는 방법

- 비트마스크

- 순열 : 순열의 시간복잡도 O(N!)

- 백트랙킹

- BFS

  위의 5가지 방법을 이용한 완전탐색 방법 모두를 익혀야 한다.

  모든 경우의 수를 탐색하는 방법은 문제를 접했을 때 가장 쉬운 방법이지만, 기초라고도 볼 수 있다.

  그리고 문제에서 제한조건과 위의 몇 가지 SKILL을 추가하여 푼다면 문제 해결 시간을 크게 향상 시킬 수 있다.

:three: 완전 탐색 문제

```
1. (백준 10974) 모든순열 (https://www.acmicpc.net/problem/10974)
2. (백준 10819) 차이를 최대로 (https://www.acmicpc.net/problem/10819)
3. (백준 6603) 로또 (https://www.acmicpc.net/problem/6603)
4. (백준 2309) 일곱난쟁이 (https://www.acmicpc.net/problem/2309)
5. (백준 10971) 외판원 순회 2 (https://www.acmicpc.net/problem/10971)
6. (백준 1759) 암호 만들기 (https://www.acmicpc.net/problem/1759)

```



```java
1. (백준 10974) 모든순열 (https://www.acmicpc.net/problem/10974)

import java.util.*;

public class back10974 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		int[] arr = new int[n];
		int[] output = new int[n];
		boolean[] visited = new boolean[n];
		for(int i = 0; i < n; i++) {
			arr[i] = i+1;
		}
		perm(arr, output, visited, 0, n, n);
	}
	
	static void perm(int[] arr, int[] output, boolean[] visited, int depth, int n, int r) {
		if(depth == r) {
			print(output, r);
			return;
		}
		for(int i = 0; i < n; i++) {
			if(visited[i] != true) {
				visited[i] = true;
				output[depth] = arr[i];
				perm(arr, output, visited, depth+1, n, r);
				visited[i] = false;
			}
		}
	}
	
	static void print(int[] output, int r) {
		for(int i = 0; i < r; i++) {
			System.out.print(output[i] + " ");
		}
		System.out.println();
	}
}
```

```java
2. (백준 10819) 차이를 최대로 (https://www.acmicpc.net/problem/10819)
/* 코드 너무 더러움. 다시 짤것. */

import java.util.*;

public class back10819 {
	static int maximum = 0;
	static int cnt = 0;
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		int size = 1;
		int arr[] = new int[n];
		int output[] = new int[n];
		boolean visited[] = new boolean[n];
		for(int i = 0; i< n; i++) {
			arr[i] = input.nextInt();
			size = size * (i+1);
		}
		int[] max = new int[size];
		perm(arr, output, visited, max, 0, n, n);
	}
	static void perm(int[] arr, int[] output, boolean[] visited, int[] max, int depth, int n, int r) {
		if(depth == r) {
			cal(output, max, r);
			return;
		}
		for(int i = 0; i < n; i++) {
			if(visited[i] != true) {
				visited[i] = true;
				output[depth] = arr[i];
				perm(arr, output, visited, max, depth+1, n, r);
				visited[i] = false;
			}
		}
	}
	static void cal(int[] output, int[] max, int r) {
		int result = 0;
		for(int i = 0; i < r-1; i++) {
			if(output[i] - output[i+1] < 0)
				result -= output[i] - output[i+1];
			else
				result += output[i] - output[i+1];
		}
		if(maximum < result)
			maximum = result;
		print(max, maximum);
	}
	static void print(int[] max, int maximum) {
		max[cnt++] = maximum;
		if(cnt == max.length)
			System.out.println(max[cnt-1]);
	}
}

```

