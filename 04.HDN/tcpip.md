# TCP/IP 란

`TCP/IP`는 패킷 통신 방식의 인터넷 프로토콜인 `IP`와 전송 조절 프로토콜인 `TCP`로 이루어져 있다.

`IP`는 패킷 전달 여부를 보증하지 않고, 패킷을 보낸 순서와 받는 순서가 다를 수 있다. `TCP`는 `IP`위에서 동작하는 프로토콜로, 데이터의 전달을 보증하고 보낸 순서대로 받게 해준다. `HTTP`, `FTP`, `SMTP`,등 `TCP`를 기반으로 한 많은 수의 애플리케이션 프로토콜들이 `IP`위에서 동작하기 때문에, 묶어서 `TCP/IP`로 부르기로 한다.

인터넷 통신의 대부분은 패킷통신을 기본으로 하고 있다. `TCP/IP`는 이러한 패킷 통신을 위한 인터넷의 규약이다. `IP`는 데이터의 조각들을 최대한 빨리 목적지로 보내는 역할을 한다. 조각들의 순서가 뒤바뀌거나 일부가 누락되더라도 크게 상관하지 않고 보내는 데 집중을 한다. `TCP`는 `IP`보다 느리지만 꼼꼼한 방식을 사용한다. 도착한 조각을 점검하여 줄을 세우고 망가졌거나 빠진 조각을 다시 요청한다. 두 방식의 조합을 통하여 인터넷 데이터 통신을 하는 것을 묶어 `TCP/IP`라고 부른다.

# TCP 3 Way-Handshake & 4 Way-Handshake

## 1. TCP 3 Way-Handshake

`TCP`는 장치들 사이에 논리적인 접속을 성립(establish)하기 위하여 three-way handshake를 사용한다.

`TCP 3 Way Handshake`는 `TCP/IP`프로토콜을 이용해서 통신을 하는 응용프로그램이 데이터를 전송하기 전에 먼저 **정확한 전송을 보장**하기 위해 상대방 컴퓨터와 사전에 세션을 수립라는 과정을 의미

Client > Server : TCP SYN

Server > Client : TCP SYN ACK

Client > Server : TCP ACK

SYN : `Synchronize Sequence Number`, ACK : `Acknowledment`

* TCP의 3 Way-Handshake 역할

  - 양쪽 모두 데이터를 전송할 준비가 되었다는 것을 보장하고, 실제로 데이터 전달이 시작하기전에 한 쪽이 다른 쪽이 준비되었다는 것을 알 수 있도록 한다.

  - 양쪽 모두 상대편에 대한 초기 순차일련번호를 얻을 수 있도록 한다.

    ![3way](./imgs/3way.png)

* TCP의 3 Way Handshake 과정

  1. STEP 1

     A 클라이언트는 B서버에 접속을 요청하는 SYN 패킷을 보낸다. 이때 A클라이언트는 SYN을 보내고 SYN/ACK 응답을 기다리는 SYN_SENT 상태가 되는 것이다.

  2. STEP 2

     B 서버는 SYN 요청을 받고 A 클라이언트에게 요청을 수락한다는 ACK와 SYN Flag가 설정된 패킷을 발송하고 A가 다시 ACK로 응답하기를 기다린다. 이때 B서버는 SYN_RECEIVED 상태가 된다.

  3. STEP 3

     A 클라이언트는 B 서버에게 ACK를 보내고 이후로부터는 연결이 이루어지고 데이터가 오가게 되는것이다.

     위와 같은 방식으로 통신하는 것이 신뢰성 있는 연결을 맺어 준다는 TCP의 3 Way Handshake 방식이다.

## 2. TCP 4 Way-Handshake

3 Way-Handshake는 TCP의 연결을 초기화 할 때 사용한다면, 4 Way-Handshake는 세션을 종료하기 위해 수행되는 절차이다.

![4way](./imgs/4way.png)

- TCP의 4 Way Handshake 과정

  1. STEP 1

     클라이언트가 연결을 종료하겠다는 FIN플래그를 전송한다.

  2. STEP 2

     서버는 일단 확인 메시지를 보내고 자신의 통신이 끝날때까지 기다리는데 이 상태가 **TIME_WAIT** 상태이다.

  3. STEP 3

     서버가 통신이 끝났으면 연결이 종료되었다고 클라이언트에게 FIN플래그를 전송한다.

  4. STEP 4

     클라이언트는 확인했다는 메시지를 보낸다.

- 궁금증 1. Server에서 FIN을 전송하기 전에 전송한 패킷이 Routing 지연이나 패킷 유실로 인한 재전송 등으로 인해 FIN 패킷보다 늦게 도착하는 상황이 발생한다면?

  -> Client에서 세션을 종료시킨 후 뒤늦게 도착하는 패킷이 있다면 이 패킷은 Drop되고 데이터는 유실될것이다. 이러한 상황에 대비하여 Client는 Server로부터 FIN을 수신하더라도 일정시간(default : 240sec)동안 세션을 남겨놓고 잉여 패킷을 기다리는 과정을 거치데 되는데 이 과정을 `TIME_WAIT`이라고 한다.