# Subnet VS Supernet

- **Classful vs Classless**

  옛날에는 IP를 class로 구분하여 A class, B class, C class, D class, E class로 구분했었다.

  ![classful](./imgs/classful.png)

  그림 1, 그림 2, 그림 3에 각각 A class, B class, C class의 예제를 하나씩 나타내어 보았다. 각 그림에서 윗 부분에 Network bits와 Host bits라고 표시하였다. A,B,C 각 class별로 Network bits와 Host bits를 따로 적어보면 아래와 같다

  A class : Network bits(8 bits), Host bits(24 bits)

  B class : Network bits(16 bits), Host bits(16 bits)

  C class : Network bits(24 bits), Host bits(8 bits)

  [Subnet은 LAN의 크기를 정해주는 것][]인데, Subnet에서 Subnet mask의 1로 표시되는 부분이 network bits이고, 0으로 표시되는 부분이 host bits이다. ['직접 ARP request를 보내서 MAC address를 알아와서 직접 통신을 할 수 있는 LAN의 크기를 알려주는 것이 Subnet이다'][]

## Subnetting

```
- IPv4의 주소고갈 문제를 해결하기 위해 제안된 방법(서브넷팅, 슈퍼넷팅, IPv6, VPN, NAT, DHCP) 중 하나

- 네트워크를 다시 여러 개의 작은 네트워크(서브넷)으로 나누는 기법 (슈퍼넷팅과 반대되는 개념)

- 서브넷팅 공식 1 : y = 2^2x - 2 (x = 호스트 부분 비트수, y = 사용가능한 호스트 수)
  호스트 개수가 주어졌을 때 사용(서브넷 마스크에서 뒤쪽부터 y개가 호스트 id가 되는 것임)
  
- 서브넷팅 공식 2 : y = 2^x (x = 네트워크 부분 비트수, y = 사용가능한 네트워크 수)
  네트워크 개수가 주어졌을 때 사용(서브넷 마스크에서 기존 네트워크 id 부터 y 개가 네트워크부가 되는 것임)
```







## Supernetting

```
- IPv4의 주소고갈 문제를 해결하기 위해 제안된 방법 중 하나

- 여러개의 네트워크를 하나의 네트워크로 합치는 기법(서브넷팅과 반대되는 개념)

- 여러 네트워크 주소들의 공통부분을 네트워크 부분으로 설정한다.
```



**※ CIDR(Classless Inter-Domain Routing)**

/- Class의 개념을 없애고 서브넷 마스크를 이용해서 라우팅하는 기법(즉, Prefix 정보를 이용해 라우팅)

/- 슈퍼넷칭을 수행하므로 라우팅 정보량이 줄어든다. (여러개의 네트워크가 하나의 네트워크로 합쳐지므로)

/- CIDR = 슈퍼넷팅이라고 알고있는 사람이 많지만, CIDR도 서브넷팅을 수행한다. (그러므로 주소 공간의 낭비도 막아줌)

/- 즉, CIDR = 서브넷팅 + 슈퍼넷팅 + Prefix

**※ VLSM(Variable Length Subnet Mask)**

/- 서브넷팅을 여러번 수행하는 기법

/- 서브넷팅처럼 모두 동일한 크기의 서브넷을 만드는 것이 아니라, 서로 다른 크기의 서브넷을 만든다.

**※ Classful vs Classless**

/- Classful 방식 : Class 방식을 사용

/- Classless 방식 : Class 방식을 사용하지 않음

**※ 서브넷 마스크(Subnet Mask)** : IP 주소에서 '네트워크 부분'과 '호스트 부분'을 구분해서 나타내주는 역할을 한다.

즉, 네트워크 부분에 해당하는 비트는 1, 호스트 부분에 해당하는 비트는 0으로 쓴다.

첫번째 예시 : Class A는 디폴트 서브넷 마스크 1111 1111 . 0000 0000 . 0000 0000 . 0000 0000 = 255 . 0 . 0 . 0

두번째 예시 : Class B의 디폴트 서브넷 마스크 1111 1111 . 1111 1111 . 0000 0000 . 0000 0000 = 255 . 255 . 0 . 0

**서브넷 마스크의 표현**은 IP 주소 끝에 '/'문자를 쓰고, 다음에 네트워크 부분에 해당하는 비트개수를 쓴다. (Prefix 표기법)

예를들어, '192.168.0.3'이라는 IP주소의 서브넷 마스크가 '1111 1111 . 1111 1111 . 1111 1111 . 0000 0000 = 255 . 255 . 255 . 0'이라면 '192.168.0.3/24'라고 쓴다.

![subnet](./imgs/subnet.png)