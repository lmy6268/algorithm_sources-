#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int dp[5001];
	fill_n(dp, 5001, 5001); //배열 초기화 
	dp[3] = 1; dp[5] = 1; //3과 5일 때 각각 1봉지씩 가져갈 수 있으므로
	int n = 0;
	cin >> n; //n을 입력받음
	for (int i = 6; i <= n; i++) //다이나믹 프로그래밍으로 해결 
	{
		if (dp[i - 3] != 5001)  
		{
			dp[i] =  dp[i - 3] + 1;
		}
		if (dp[i - 5] != 5001) {
			dp[i] = min(dp[i], dp[i - 5] + 1);
		}
	}
	if (dp[n] == 5001) cout << -1 << "\n"; // 만약 딱 떨어지지 않는 다면, -1 출력
	else cout << dp[n] << "\n";
	return 0;
}