#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;

int n;//병사 수
vector<int> v; //배열을 유연하게 사용할 수 있게함.(스택 구조)

int main(void) {
	cin >> n; //병사 수 입력
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;//병사의 전투력 입력
		v.push_back(x);
	}
	//순서를 뒤집어 '최장 증가 부분 수열' 문제로 전환
	reverse(v.begin(), v.end()); //reverse(itr.first, itr.last)
	//다이나믹 프로그래밍을 위한 1차원 DP테이블 초기화
	int dp[2000];
	for (int i = 0; i < n; i++)dp[i] = 1;
	//가장 긴 증가하는 부분 수열(LIS)알고리즘 수행 
	for (int i = 1; i < n; i++)
		for (int j = 0; j < i; j++)
			if (v[j] < v[i])dp[i] = max(dp[i], dp[j] + 1);
	int maxValue = 0;
	for (int i = 0; i < n; i++)maxValue = max(maxValue, dp[i]);
	cout << n - maxValue << '\n';
}


