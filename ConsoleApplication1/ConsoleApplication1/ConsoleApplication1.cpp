#include<iostream>
using namespace std;
const int N = 1e5 + 10;
int a[N] = {};

bool flag = false, first = true;
int main()
{
	int n;
	cin >> n;
	int target;
	int begin, end;
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}
	cin >> target;
	for (int i = 0; i < n; i++)
	{
		if (target == a[i])
		{
			if (first)
			{
				begin = i;
				end = i;
				flag = true;
			}
			else
			{
				end = i;
			}
		}
	}
	if (flag)
	{
		first = -1;
		end = -1;
	}
	cout << first << ' ' << endl;
	return 0;
}