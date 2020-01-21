# LAN 통신이란?

## 1. 삼테이블을 이해하면 LAN 통신은 끝

- 학습목표 : Switching & Routing 기본 개념을 확실하게 정립하자

##  삼테이블이란?

1.  Routing Table
2. ARP Table
3. MAC Table

## LAN이란?

-  **ARP Request 패킷이 미치는(도달하는) 범위의 네트워크**이다.(Local Area Network의 정의)
- L2 Switch와 Hub만으로 연결된 네트워크는 하나의 LAN이다. L2 Switch를 아무리 많이 연결해도 하나의 LAN이다.
- Router의 각 interface는 각각 서로 다른 LAN을 구성한다.

![LAN](./imgs/lan.png)

## LAN 통신의 기본

- 위의 그림과 같이 일반적인 LAN 환경에서 PC0와 PC1과 통신하는 과정을 통해서 LAN 통신이 어떻게 이루어지는지 보자

1. PC0에서 통신할 상대방 PC1의 IP 주소를 알아낸다.

2. PC1과 통신하기 위해서 메시지를 전송한다. - 예를들어 PC1로 ping을 하거나, 메신저를 이용하여 메시지를 전송한다.

3. **Routing Table**에서 PC1의 IP 주소로 가려면, 어떤 interface로 나가야 하고, *next hop IP*가 무엇인지 찾는다.

4. *next hop IP*의 MAC Address가 **ARP Table**에 등록되어 있는지 찾는다.

5. **ARP Table**에 *Next hop IP*의 MAC Address가 없다면 MAC Address를 알아오기 위해서 ARP request 메시지를 전송한다.

6. Switch는 ARP Request 메시지를 수신하면 source MAC Address를 보고, PC0의 **MAC Table entry**를 만든다.

   /- PC0의 MAC Address와 Frame이 수신된 port번호를 MAC Table에 기록한다.

7. Switch는 ARP Request 메시지를 모든 LAN port로 전송(브로드캐스트)한다. ARP 패킷은 LAN 구간 끝까지 어디든지 날라간다.

8. ARP Request를 수신한 PC1은 자신의 ARP Table에 PC0의 IP와 MAC Address를 등록하고 ARP reply 메시지를 전송한다.

   /- PC1의 Routing Table에는 PC0에 대한 routing entry가 등록되어있지 않다면, PC1은 ARP reply를 전송할 수 없다.

   /- PC1의 ARP Table에는 ARP Request메시지를 받으면서 이미 PC0의 MAC Address가 등록되어 있다.

9. Switch는 ARP reply 메시지를 수신하면, sorce MAC Address를 보고, PC1의 **MAC Table entry**를 만든다.

10. PC0은 ARP reply 메시지를 수신하면, **ARP Table**에는 PC1의 IP와 MAC Address를 등록하고, PC1으로 전송되어야 할 패킷의 Destination MAC에 PC1의 MAC Address를 부착하고 메시지를 전송한다.

11. Switch는 PC0가 전송한 Ethernet Frame을 수신하면, Destination MAC Address가 MAC Table에 존재하는지 찾는다.

12. Switch는 MAC Table에 PC1의 정보가 등록되어 있으므로 PC1이 연결되어 있는 port로 메시지를 전송(Unicast)한다.

13. PC1은 Destination MAC Address가 자신의 NIC MAC Address와 동일하므로 메시지를 수신하여 IP Layer로 전달하고, IP Layer에는 Destination IP가 자신의 IP와 동일하므로 IP 패킷을 수신한다.

# ARP는 이더넷 통신의 핵심

## ARP의 개요

- ARP(Address Resolution Protocol)의 핵심은 ARP Request가 broadcast된다는 것이다.

  ex) LAN 통신을 하고자 하는 상대방 PC나 서버의 IP는 아는데 MAC Address를 모를때, ARP Request를 패킷을 보내고, ARP reply를 받아서 MAC Address를 알아내서 패킷을 상대방에게 보낼 수 있게 되는 것이다.

- 이름에서도 알 수 있듯이 주소를 변환해 주는 프로토콜(하드웨어 주소)이다. 변환이라기 보다는 주소를 알아내는 프로토콜이라고 표현해야 더 적당할 듯.

  ![arp](./imgs/arp.png)

- 위와 같은 네트워크가 있다고 할 때 Host A가 Server B에게 데이터를 보낸다고 가정해보자. **네트워크에서 통신은 IP 주소로만 이루어지는 것처럼 보이지만 실제로는 하드웨어 주소가 필요**하다.
- IP 주소는 아는데 하드웨어 주소(MAC address)를 모르는 경우이다. 그래서 다른 컴퓨터와 통신을 할때는 먼저 ARP가 상대방 컴퓨터의 하드웨어 주소를 알아내기 위하여 작동을 하게 된다.
  1. HOST A는 네트워크 상에 자기의 IP 주소, 하드웨어 주소(MAC Address), 그리고 Server B 의 IP 주소, 하드웨어 주소에는 이더넷 상의 Broadcast 주소인 00:00:00:00:00:00를 ARP 패킷 헤더에 채워서 보내게 되며 메세지 타입은 Request로 설정하게 된다.

## 네트워크를 위한 ARP의 속도 향상 방법

- ARP 프로토콜의 기본적인 기능은 목적지 호스트의 하드웨어 주소를 알아내는 것이다. 또한 ARP 프로세스는 기본적으로 브로드캐스트를 기반으로 하는 특성 때문에 발생하는 네트워크의 부하를 방지하기 위하여 다음의 기능을 제공한다,

  1. ARP Cache

     ARP Request를 통하여 얻은 하드웨어 주소는 다음에 또 사용할 수 있으므로 ARP Cache Table에 일정 시간 동안 저장하게 된다. 다음에 데이터를 보낼 때 ARP Cache를 검사하여 있으면 브로드캐스트를 이용하지 않고 바로 보낸다. 브로드캐스트가 줄어서 네트워크의 성능은 향상된다.

     - 일정시간을 짧게 설정하는 경우 : 설정 값이 짧으면 네트워크의 호스트들은 지속적으로 ARP Cache Table의 Entry를 교체하게 되고 이로써 많은 브로드캐스트를 전송하게 되며 네트워크의 성능은 떨어지게 된다.
     - 일정시간을 길게 설정하는 경우 : 어떤 호스트에 다른 IP 주소가 할당될 때마다 ARP Cache Table에 이전의 하드웨어 주소가 남아 있어서 문제를 일으키게 된다.

     결론적으로 **일정 시간 동안 저장하게 되는 이유는 호스트의 IP 주소 변경, 혹은 NIC의 교체 등과 같이 IP 주소와 하드웨어 주소의 바인딩 정보가 변경되었을 경우 기존의 ARP Cache Table에 저장된 정보로 통신을 하게 될 경우 통신이 안되는 상황이 발생 할 수 있다.** 그러므로 ARP Cache Table에 저장된 Entry는 일정 시간이 지나게 되면 지워지는 것이다. 이것을 Life Time이라고 한다.

  2. ARP Refinement

     **성능 향상을 위한 또 다른 기능은 다른 호스트들의 ARP Request에 담겨있는 호스트의 IP 주소와 하드웨어 주소를 참조하여 자신의 ARP Cache Table에 저장하는 방법이다.** ARP Request 메세지를 받은 모든 호스트들은 Sender의 IP 주소와 MAC Address를 저장하게 된다. 이렇게 되면 다음 번에 데이터를 보낼때 브로드캐스트의 횟수를 줄여 네트워크의 성능향상을 꾀하게 된다.

  3. Static Entry

     Static Entry는 ARP Cache Table에 고정으로 IP주소와 하드웨어 주소(MAC Address)를 맵핑하는 방법이다. ARP Cache의 Life Time이 존재하지 않는다. 그러나 Static Entry는 시스템이 자주 이전되거나 시스템의 주소가 자주 바뀌면 관리하기 어렵다는 단점이 있다.

## ARP Process와 ARP Header 구조

![arp2](./imgs/arp2.png)

1. 호스트 A가 호스트 C에게 데이터를 보낸다고 가정해보자. 그러면 호스트 A가 제일 먼저 하는일은 위의 그림과는 다르게 호스트 C가 호스트 A와 같은 네트워크인지 다른 네트워크인지를 먼저 알아낸다.(서브넷 마스크를 이용)
2. 그림과 같은 네트워크라면 다음 하는일이 ARP Cache Table에서 호스트 C의 하드웨어 주소가 있는지 파악한 후 있으면 그걸 사용하고 없으면 ARP Process를 진행시킨다.(1. ARP Cache is Checked)
3. ARP Process를 진행하므로 당연히 네트워크 상에 브로드캐스트로 ARP Request메세지가 뿌려진다.(2. ARP Request is Sent)
4. 네트워크에 있는 호스트들은 브로드캐스트로 뿌려진 ARP Request 메세지를 받고 자기 ARP Cache Entry에 추가한다.(3. ARP Entry is Added)
5. ARP Request 메세지를 받은 호스트중 한대만이 이에 응답한다. 여기서는 호스트 C, 자기 하드웨어 주소를 ARP Reply메세지로 응답한다. 단 여기서는 유니캐스트로 응답한다.(4. ARP Reply is Sent)
6. ARP Reply 메세지를 받은 호스트 A는 호스트 C의 정보를 ARP Cache Table에 추가한다.(5. ARP Entry is Added)
7. ARP Process는 종료되고 프레임이 호스트 C에 전송된다.(6. IP Packet is Sent)

if) 호스트 C가 같은 네트워크가 아니라면 어떻게 될까?

- 호스트 A는 Default Gateway의 하드웨어 주소를 알아내서 네트워크 밖으로 내보내게 된다. 그 다음은 Router가 프레임을 호스트 C에게 전송한다.

![arp3](./imgs/arp3.png)

- ARP Header는 위의 그림과 같이 생겼다. octet이란 8bit을 의미한다.
- Hardware type : 요청된 하드웨어 주소의 종류를 나타낸다. 16bit를 차지하며 십진수 형태로 되어있다. RFC 170에 하드웨어 주소의 종류가 나와있다.
- Protocol type : 사용되는 상위 계층 프로토콜을 나타내는 필드이다. 16bit를 차지한다. IP에만 결속된 것은 아니며, 하드웨어 주소를 찾고자 하는 모든 상위 계층 프로토콜에 의해 사용될 수 있다. 이러한 이유로 상위 계층 프로토콜을 구분하기 위해서 Protocol type 필드가 존재한다.
- Hardware address length : Source 및 Destination address 길이를 나타내며 8bit를 차지한다.
- Operation code : ARP 패킷의 목적을 나타낸다.(Request인지 Reply인지) 16bit를 차지한다.
- Source hardware address : ARP 패킷을 전송하는 시스템의 하드웨어 주소를 나타내며, 패킷은 Request 또는 Reply일 수 있다. 차지하는 bit는 하드웨어 주소의 형태에 따라 달라지나 보통은 Ethernet을 사용하므로 48bit를 차지하게 된다.
- Source protocol address : ARP 패킷을 전송하는 시스템의 상위 계층 프로토콜 주소를 나타내며 패킷은 Request 또는 Reply일 수 있다. 차지하는 bit는 상위 계층 프로토콜에 따라 변하나 보통 IP를 사용하므로 32bit가 된다.
- Destination hardware address : ARP 패킷을 받는 시스템의 하드웨어 주소를 나타내며, ARP Request라면 00:00:00:00:00:00 으로 채워질 것이다. 역시 차지하는 bit는 하드웨어 주소의 형태에 따라 달라지며 보통은 Ethernet을 사용하므로 48bit를 차지하게 된다.
- Source protocol address : ARP 패킷을 받는 시스템의 상위 계층 프로토콜의 주소를 나타내며 패킷은 Requset 또는 Reply일 수 있다. 차지하는 bit는 상위 계층 프로토콜에 따라 변하나 보통 IP를 사용하므로 32bit가 된다.

## Ethernet switch는 Plug & Play가 된다?

- **트랜스패런트 브리징(Transparent Bridging)** : switch가 MAC Table을 스스로 생성하고 이 MAC Table을 참조하여 수신되는 프레임을 목적지로 전송하는 과정

  1. 이더넷 프레임이 수신되면, source MAC address를 읽어서 수신 port번호와 함께 MAC Table에 기록한다.(**Learning**)
  2. Destination MAC address가 *MAC Table에 등록되어 있지 않은 Unicast 프레임*이거나, ARP Request와 같은 브로드캐스트인 경우, 수신 port를 제외한 다른 모든 port로 프레임을 전송한다.(**Flooding**)
  3. Destination MAC address가 MAC Table에 등록되어 있고, 등록되어 있는 port번호가 프레임이 수신된 port번호와 동일한 경우 해당 프레임은 버린다.(**Filtering**)
  4. Destination MAC address가 MAC Table에 등록되어 있고, 등록되어 있는 port 번호가 프렘임이 수신된 port번호와 동일하지 않은 Unicast인 경우 등록되어 있는 port로 프레임을 전송한다.(**Forwarding**)
  5. MAC Table에 Entry가 등록될때 Timer도 같이 start 되며, 해당 Entry의 MAC address를 source MAC으로 하는 프레임이 수신되면 Timer가 reset되어 다시 시작된다. 기본적으로 Timer가 5분이 경과되면 해당 Entry는 MAC Table에서 삭제된다.(**Aging**)

  위에서 설명한 **Learning, Flooding, Filtering, Aging**의 과정을 모두 합쳐서 트랜스패런트 브리징이라고 한다. 스위치의 이 트랜스패런트 브리징 기능으로 인해서 스위치에 전원만 인가하면 운영자가 별다른 설정을 하지 않아도 스위치는 알아서 MAC Table을 만들고 스위칭을 수행할 수 있다.