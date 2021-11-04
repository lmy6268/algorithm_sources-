//BOJ1011
#include<algorithm>
#include<iostream>
#include<cmath>
using namespace std;

//int main(void) {
//	int T = 0;
//	cin >> T;
//	for (int i = 0; i < T; i++) {
//		int x, y = 0;
//		int step = 0;
//		cin >> x >> y; //출발지좌표와 목적지 좌표 얻기 
//		int dis = y - x;//두 좌표 사이의 거리
//		int close = sqrt(dis);
//		step = close * 2 - 1;
//		int remain = dis- pow(close, 2);
//		if (remain != 0) {
//			step = remain <= close ? step + 1 : step + 2;
//		}
//		cout << step << "\n";
//	}
//	return 0;
//
//}

int main(void) {
	long T, x, y;
	cin >> T;
	while (T--) {
		cin >> x >> y;
		y -= x; x = 0; // y에 y-x값을 갖게 하여 두 점 간의 거리를 저장 후, x=0으로 두어 새롭게 사용
		while (y > (x + 1)*(x + 2))++x; //여기서 x는 위의 close와  같은 존재인가?
		cout << "X의 값:" << x << "\n";
		y -= (x*(x + 1));//y는 remain 같고..
		cout << x * 2 + y / (x + 1) + (y % (x + 1) != 0) << "\n";
	}
}