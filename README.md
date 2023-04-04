# 2023 캡디2

🏫 울산대학교

🖍️ 캡스톤디자인2

🗓️ 2023.3 ~ 2023.6

<br/>

# 🐕 개요

<img src="photo/untitled.png" width="500" height="300"/>

### 독거노인 등 외로운 사람들을 위한 다목적 로봇 애완견

<br/>

# 🖲️ 기능



> 해보고 안될거같으면 빼기
3/10 회의 후 수정 예정
> 

### 음성인식

- 음성 인식을 통해 명령
- 모든 명령은 음성인식으로 수행

<aside>
📌 STT(Speech To Text), 딥러닝
Python

</aside>

### 동작 수행

- 앉아, 돌아, 짖어, 인사 등

<aside>
📌 로봇 프로그래밍(ROS), 제어시스템
C++

</aside>

### 자율주행

- 집으로 돌아가기(개 집)
    - 배터리가 떨어진 경우, 집으로 가라고 명령 한 경우
- 집의 각 구역으로 이동 명령
    - “부엌”으로 가서 “기다려” → 부엌에 가서 앉아 동작 수행

<aside>
📌 자율주행, SLAM, LiDAR, 로봇 인지
Python, C++

</aside>

### 위급상황 인지

- 가능하면 하기(필수 아님)
- 위급상황 인지 시 자동으로 신고 또는 보호자에게 알림 및 영상 전송
    - 카메라로 촬영된 영상을 분석해 위급상황 판단
    - Pose estimation, Image classification 등
- 안되면 그냥 실시간으로 촬영된 영상 핸드폰 등에서 조회 가능한 형태로 구현

<aside>
📌 사람 자세 추정, 컴퓨터비젼, 딥러닝
Python

</aside>

### 객체 인지

- 공 따라 움직이기
- 공 던지면 쫓아가기
- 색 영역 추출

<aside>
📌 컴퓨터비젼
Python

</aside>

<br/>

# 🧑 역할 분담

<br/>

# 📊 진행상황


# How to install
```
mkdir ~/pupper/src && cd ~/pupper/src
git clone https://github.com/UAENA0516/CapstoneDesign2.git
cd ..
rosdep update
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
```


[진행상황](https://www.notion.so/f06969a9ec7e478e9c5b1ee7523a9e6d)

