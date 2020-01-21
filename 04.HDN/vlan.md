# VLAN 이란

## VLAN의 탄생 배경

- VLAN은 Switch Network에서 Broadcast Traffic으로 인한 부하를 줄이기 위해서 탄생하였다.

![vlan](./imgs/vlan.png)

- VLAN 공부를 시작하게 되면, 너무도 흔하게 접하게 되는 VLAN이 3개로 분리되어 있는 그림이다. 물리적으로는 1개의 Switch에 연결되어 있지만, 실제 LAN 통신 동작으로 보면 서로 분리되어 동작한다. PC들이 보내는 broadcast 트래픽은 Server나 Laptop으로 보내지지 않는다. 마찬가지로 Server가 보내는 broadcast 트패픽은 server들에게만 전달되고, Laptop들에게만 보내진다. 실제 물리적으로는 하나의 Switch에 연결되어 있지만, 가상의 LAN(VLAN)으로 분리가 되어있다. 그래서 Virtual LAN이라고 이름이 붙여졌다.

## VLAN에 대한 오해 1 - VLAN에는 무조건 Tag가 붙는다?

Broadcast Traffic이 어떻게 다른 VLAN으로는 보내지지 않고, 같은 VLAN으로만 보내질 수 있을까?  위의 그림과 같이 **Switch 내에서만 VLAN을 분리하는 경우 Tag하고는 아무런 관계가 없이 동작한다.** 스위치가 트래픽을 받아서 다른 포트로 forwarding을 하는 동안에도 tag는 전혀 붙여지지 않고, 떼어지지도 않는다. Tag란 것 자체가 전혀 개입되지 않는다. Switch의 설정으로 각 포트가 어떤 VLAN에 속하는 지를 정해주게되고, 그러면 Switch는 어떤 prot들이 VLAN 10에 속하고, 어떤 port들이 VLAN 20, 30에 각각 속하는지를 설정 된 값들을 보고 알 수 있다. Switch가 각 port들이 어는 VLAN에 속해 있는지 정보를 알고 있기 때문에, Switch가 broadcast 트래픽을 각각의 VLAN에 속한 port들로만 flooding을 시켜 주는 것이다.

## LAN 통신의 기본

1. 삼테이블(Routing, ARP Table, MAC Table)을 알면 LAN 통신이 보인다.

2. LAN이란 ARP Request(Broadcast) packet이 미치는(도달하는) 범위의 네트워크이다.

3. Switch는 broadcast Frame을 수신 포트를 제외한 다른 모든 포트로 브로드캐스트한다.

4. Switch는 Frame이 수신되면, Source MAC address와 수신 port 정보를 이용하여 MAC Table을 만든다.

5. Switch는 MAC Table에 Destination MAC address가 없는 Unicast Frame이나 Multicast Frame의 경우에 수신 port를 제외한 모든 port로 flooding한다.

6. 브로드캐스트 및 Flooding 패킷의 특성으로 인하여 Switch간 연결에 폐루프(closed loop)가 형성되면 looping 현상이 발생한다.

7. Switch looping 현상을 자동으로 차단해 주기 위해서 사용되는 프로토콜 STP(Spanning Tree Protocol)이다.

8. 최근 네트워크 스위치 장비들은 Convergense Time(장애 발생 후 우회 패스로 절체 완료 되기까지의 시간)이 2초 이내로 짧은 RSTP(Rapid Spanning Tree Protocol)를 기본적으로 사용한다.

9. 동일 LAN간 통신은 직접 상대방 IP로 ARP Request를 보내서, ARP Reply를 동일 LAN의 상대로부터 받고 직접 패킷을 전달한다.

10. ARP Request는 동일 LAN상의 모든 Node로 전달이 되는데, Target IP와 동일한 IP를 가진 Node만 ARP Reply를 보낸다.

11. ARP Request를 받은 LAN상의 Node들 중 IP가 Target IP와 같지 않은 다른 Node들은 자신들의 ARP Table을 update한다. * ARP update가 표준상의 기본 동작이지만, 보안을 이유로 update하지 않도록 구현할 수 있다.

12. 다른 LAN간 통신은 라우터(Gateway) IP로 ARP Request를 보내서, ARP Reply를 Router로부터 받고, 패킷을 라우터로 전달한다.

13. Subnet은 동일 LAN의 크기를 지정해 주는 것이며, 같은 Subnet에 속하는 상대방과는 직접 전달로 통신한다.

14. Interface에 IP와 Subnet을 설정하면, 직접 전달 가능한 동일 LAN에 대해서는 directly connected(연결됨) route entry가 생성된다.

15. Router가 브로드캐스트 패킷을 수신해서 처리하고, 다른 Interface로 전달하지 않기 때문에 브로드캐스트 패킷은 Route를 통과하지 못한다.

16. Router는 자신의 Interface MAC을 달고 오는 프레임을 수신해서 처리한다. 패킷의 목적지 IP가 자기 Interface의 IP와 같으면, CPU로 수신해서 직접 처리하고, 자기 Interface가 속한 LAN에 직접 연결된 IP이면 직접 전달을 하며, 다른 LAN에 속한 IP인 경우에는 Routing Table을 참조하여 다른 라우터로 전달한다.

    

