

:one: [복서 정렬하기(프로그래머스)](./sorting/1_box_sorting.md)

:two: [직업군 추천하기(프로그래머스)](./sorting/2_job_recommandation.md)

---

### ArrayList 정렬하기 (오름차순, 내림차순, 사용자 정의)

1. Collections.sort()
   - 오름차순 정렬
   - 내림차순 정렬
   - 대소문자 구분없이 정렬
2. List.sort() - Java 8이후
   - 오름차순 정렬
   - 내림차순 정렬
   - 대소문자 구분없이 정렬
3. 사용자 정의
   - Comparable
   - Comparator



#### 1. Collections.sort()

```java
public static void sort(List<T> list)
public static void sort(List<T> list, Comparator<? super T> c)
```

**오름 차순 / 내림 차순 / 대소문자 구분없이 정렬**

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class SortArrayList {
	public static void main(String[] args) {

    	// ArrayList 준비
    	ArrayList<String> list = new ArrayList<>(Arrays.asList("C", "A", "B", "a"));
    	System.out.println("원본 : " + list); // [C, A, B, a]
    
    	// 오름차순으로 정렬
    	Collections.sort(list);
    	System.out.println("오름차순 : " + list); // [A, B, C, a]
    
    	// 내림차순으로 정렬
    	Collections.sort(list, Collections.reverseOrder());
    	System.out.println("내림차순 : " + list); // [a, C, B, A]
    
    	// 대소문자 구분없이 오름차순
    	Collections.sort(list, String.CASE_INSENSITIVE_ORDER);
		System.out.println("대소문자 구분없이 오름차순 : " + list); // [a, A, B, C]
	
    	// 대소문자 구분없이 내림차순
		Collections.sort(list, Collections.reverseOrder(String.CASE_INSENSITIVE_ORDER));
		System.out.println("대소문자 구분없이 내림차순 : " + list); // [C, B, a, A]
	}
}

출처: https://hianna.tistory.com/569 [어제 오늘 내일]
```

- `Collections.sort(list);`

  ArrayList를 오름차순으로 정렬

- `Collections.sort(list, Collections.reverseOrder());`

  Collections.sort()의 2번째 파라미터로 내림차순 정렬을 나타내는 `Comparator`를 전달해서,

  ArrayList를 내림차순으로 정렬

- `Collections.sort(list, String.CASE_INSENSITIVE_ORDER);`

  `String.CASE_INSENSITIVE_ORDER`를 전달하면, 대소문자 구분없이 오름차순으로 정렬.

  여기서 'a'와 'A'는 같은 순위로 취급되므로, 원래의 순서를 유지.

- `Collections.sort(list, Collections.reverseOrder(String.CASE_INSENSITIVE_ORDER));`

  대소문자 구분없이, 내림차순으로 정렬

#### 2. List.sort() - Java 8이후

```java
default void sort(Comparator<? super E> c)
```

**오름 차순 / 내림 차순 / 대소문자 구분없이 정렬**

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class SortArrayList {
	public static void main(String[] args) {

		// ArrayList 준비
		ArrayList<String> list = new ArrayList<>(Arrays.asList("C", "A", "B", "a"));
		System.out.println("원본 : " + list); // [C, A, B, a]
		
		// 오름차순으로 정렬
		list.sort(Comparator.naturalOrder());
		System.out.println("오름차순 : " + list); // [A, B, C, a]
		
		// 내림차순으로 정렬
		list.sort(Comparator.reverseOrder());
		System.out.println("내림차순 : " + list); // [a, C, B, A]
		
		// 대소문자 구분없이 오름차순 정렬
		list.sort(String.CASE_INSENSITIVE_ORDER);
		System.out.println("대소문자 구분없이 오름차순 : " + list); // [a, A, B, C]
		
		// 대소문자 구분없이 내림차순 정렬
		list.sort(Collections.reverseOrder(String.CASE_INSENSITIVE_ORDER));
		System.out.println("대소문자 구분없이 내림차순 : " + list); // [C, B, a, A]
	}
}

출처: https://hianna.tistory.com/569 [어제 오늘 내일]
```

Collections 객체를 사용하는 대신 List객체의 sort()메소드를 사용하여 정렬

sort()의 파라미터로 Comparator를 넘겨주는데, 앞의 예제와 달리 Comparator 객체에서 Comparator를 가져와서 넘겨준다.



## **3. 사용자 정의**

사용자가 정의한 객체를, 사용자가 원하는 방식으로 정렬하기 위해서 **Comparable 인터페이스를 구현**하여, 객체의 정렬 방식을 지정할 수도 있고, **Comparator** 인터페이스를 구현하여, Custom Comparator 를 직접 만들 수 도 있다. 

### Comparable

Collections.sort() 메소드는 객체를 정렬할 때, 해당 객체의 Comparable을 구현한 compareTo() 메소드를 참조하여, 정렬 순서를 결정한다.

따라서, 정렬할 객체가 Comparable interface를 구현하고, compareTo() 메소드 안에 정렬 기준이 정의된다면, Collections.sort() 메소드를 사용하여 객체를 정렬할 수 있습니다.

```java
import java.util.ArrayList;
import java.util.Collections;
 
public class SortArrayList {
    public static void main(String[] args) {
 
        // ArrayList 준비
        ArrayList<Fruit> list = new ArrayList<>();
        list.add(new Fruit("Apple", 2000));
        list.add(new Fruit("Orange", 3000));
        list.add(new Fruit("Banana", 1000));
        System.out.println("원본 : " + list); // [[ Apple: 2000 ], [ Orange: 3000 ], [ Banana: 1000 ]]
 
        // price순 오름차순으로 정렬
        Collections.sort(list);
        System.out.println("오름차순 : " + list); // [[ Banana: 1000 ], [ Apple: 2000 ], [ Orange: 3000 ]]
 
        // price순 내림차순으로 정렬
        Collections.sort(list, Collections.reverseOrder());
        System.out.println("내림차순 : " + list); // [[ Orange: 3000 ], [ Apple: 2000 ], [ Banana: 1000 ]]
 
    }
}
 
class Fruit implements Comparable<Fruit> {
    private String name;
    private int price;
 
    public Fruit(String name, int price) {
        this.name = name;
        this.price = price;
    }
 
    @Override
    public int compareTo(Fruit fruit) {
        if (fruit.price < price) {
            return 1;
        } else if (fruit.price > price) {
            return -1;
        }
        return 0;
    }
 
    @Override
    public String toString() {
        return "[ " + this.name + ": " + this.price + " ]";
    }
}
```

ArrayList안의 Fruit 객체를 price 순으로 정렬하기 위해서, Comparable interface를 implements 하고, compareTo() 메소드를 override



### Comparator

사용자가 직접 **Comparator interface를 implements**하여 Comparator를 만들 수 있다.

이 Comparator는 Collections.sort() 또는 List.sort() 메소드의 파라미터로 전달되어, 정렬의 기준이 됩니다.

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
 
public class SortArrayList {
    public static void main(String[] args) {
 
        // ArrayList 준비
        ArrayList<Fruit> list = new ArrayList<>();
        list.add(new Fruit("Apple", 2000));
        list.add(new Fruit("Orange", 3000));
        list.add(new Fruit("Banana", 1000));
        System.out.println("원본 : " + list); // [[ Apple: 2000 ], [ Orange: 3000 ], [ Banana: 1000 ]]
 
        // price순 오름차순으로 정렬
        Collections.sort(list, new FruitPriceComparator());
        System.out.println("price 순 오름차순 : " + list); // [[ Banana: 1000 ], [ Apple: 2000 ], [ Orange: 3000 ]]
 
        // price순 내림차순으로 정렬
        Collections.sort(list, new FruitPriceComparator().reversed());
        System.out.println("price 순 내림차순 : " + list); // [[ Orange: 3000 ], [ Apple: 2000 ], [ Banana: 1000 ]]
 
        // name순 오름차순으로 정렬
        Collections.sort(list, new FruitNameComparator());
        System.out.println("price 순 오름차순 : " + list); // [[ Apple: 2000 ], [ Banana: 1000 ], [ Orange: 3000 ]]
 
        // name순 내림차순으로 정렬
        Collections.sort(list, new FruitNameComparator().reversed());
        System.out.println("price 순 내림차순 : " + list); // [[ Orange: 3000 ], [ Banana: 1000 ], [ Apple: 2000 ]]
 
    }
}
 
class FruitPriceComparator implements Comparator<Fruit> {
    @Override
    public int compare(Fruit f1, Fruit f2) {
        if (f1.price > f2.price) {
            return 1;
        } else if (f1.price < f2.price) {
            return -1;
        }
        return 0;
    }
}
 
class FruitNameComparator implements Comparator<Fruit> {
    @Override
    public int compare(Fruit f1, Fruit f2) {
        return f1.name.compareTo(f2.name);
    }
}
 
class Fruit {
    String name;
    int price;
 
    public Fruit(String name, int price) {
        this.name = name;
        this.price = price;
    }
 
    @Override
    public String toString() {
        return "[ " + this.name + ": " + this.price + " ]";
    }
}
```

위 예제에서는 아래 2개의 Comparator를 정의

- FruitPriceComparator - price 순으로 정렬
- FruitNameComparator - name 순으로 정렬

위 두 Comparator는 Comparator interface를 implements하고, compare() 메소드를 override 하고 있다.

 

기본적으로 오름차순으로 정렬하기 위해서는 compare()메소드의 '첫번째 파라미터 > 두번째 파라미터' 이면 양수를, '첫번째 파라미터 < 두번째 파라미터' 이면 음수를, 같으면 0을 리턴해야 한다.

FruitNameComparator의 경우 compare() 메소드 안에서, 문자열을 비교하기 위해 사용된 compareTo() 메소드가 문자열의 크기 순서에 따라서 양수, 0, 음수를 리턴하기 때문에 다른 조건문없이 compareTo()에서 리턴하는 값을 그대로 리턴



출처: https://hianna.tistory.com/569 [어제 오늘 내일]