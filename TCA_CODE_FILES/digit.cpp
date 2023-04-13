#include <bits/stdc++.h>

using namespace std;

int CountDigits(int n, int d)
{
	if (n == 0)
		return 0;


	int digit = n % 10;
	if (digit == d)
		return 1 + CountDigits(n / 10, d);

	return CountDigits(n / 10, d);
}


int main()
{
	int n = 30563323;
	int d = 3;

	cout << CountDigits(n, d) << endl;
	return 0;
}