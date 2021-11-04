//BOJ1011
#include<algorithm>
#include<iostream>
#include<cmath>
using namespace std;

int main(void) {
	int T = 0;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int x, y = 0; 
		int step = 0;
		cin >> x >> y; //출발지좌표와 목적지 좌표 얻기 
		int dis = y - x;//두 좌표 사이의 거리
		int close = sqrt(dis);
		step = close * 2 - 1;
		int remain = pow(close, 2);
		if (remain != 0) {
			step = remain <= close ? step + 1 : step + 2;
		}
		cout << step << "\n";
	}
	return 0;

}