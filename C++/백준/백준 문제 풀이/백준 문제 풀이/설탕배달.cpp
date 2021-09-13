#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int dp[5001];
	fill_n(dp, 5001, 5001); //�迭 �ʱ�ȭ 
	dp[3] = 1; dp[5] = 1; //3�� 5�� �� ���� 1������ ������ �� �����Ƿ�
	int n = 0;
	cin >> n; //n�� �Է¹���
	for (int i = 6; i <= n; i++) //���̳��� ���α׷������� �ذ� 
	{
		if (dp[i - 3] != 5001)  
		{
			dp[i] =  dp[i - 3] + 1;
		}
		if (dp[i - 5] != 5001) {
			dp[i] = min(dp[i], dp[i - 5] + 1);
		}
	}
	if (dp[n] == 5001) cout << -1 << "\n"; // ���� �� �������� �ʴ� �ٸ�, -1 ���
	else cout << dp[n] << "\n";
	return 0;
}