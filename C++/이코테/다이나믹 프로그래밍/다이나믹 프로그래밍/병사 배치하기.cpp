#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;

int n;//���� ��
vector<int> v; //�迭�� �����ϰ� ����� �� �ְ���.(���� ����)

int main(void) {
	cin >> n; //���� �� �Է�
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;//������ ������ �Է�
		v.push_back(x);
	}
	//������ ������ '���� ���� �κ� ����' ������ ��ȯ
	reverse(v.begin(), v.end()); //reverse(itr.first, itr.last)
	//���̳��� ���α׷����� ���� 1���� DP���̺� �ʱ�ȭ
	int dp[2000];
	for (int i = 0; i < n; i++)dp[i] = 1;
	//���� �� �����ϴ� �κ� ����(LIS)�˰��� ���� 
	for (int i = 1; i < n; i++)
		for (int j = 0; j < i; j++)
			if (v[j] < v[i])dp[i] = max(dp[i], dp[j] + 1);
	int maxValue = 0;
	for (int i = 0; i < n; i++)maxValue = max(maxValue, dp[i]);
	cout << n - maxValue << '\n';
}


