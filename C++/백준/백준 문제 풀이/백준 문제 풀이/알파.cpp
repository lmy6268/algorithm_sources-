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
//		cin >> x >> y; //�������ǥ�� ������ ��ǥ ��� 
//		int dis = y - x;//�� ��ǥ ������ �Ÿ�
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
		y -= x; x = 0; // y�� y-x���� ���� �Ͽ� �� �� ���� �Ÿ��� ���� ��, x=0���� �ξ� ���Ӱ� ���
		while (y > (x + 1)*(x + 2))++x; //���⼭ x�� ���� close��  ���� �����ΰ�?
		cout << "X�� ��:" << x << "\n";
		y -= (x*(x + 1));//y�� remain ����..
		cout << x * 2 + y / (x + 1) + (y % (x + 1) != 0) << "\n";
	}
}