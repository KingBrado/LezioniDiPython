#include <iostream>

using namespace std;

int main()
{
    int x = 1;
    long y = 2;
    cout << &x << " " << &y << "\n";

    int &b = x;
    cout << b << endl;
    x += 1;
    cout << b << endl;
    cout << &b << endl;
    int *p = &x;
    cout << p << " " << *p << " " << &p << endl;

    int a = 1;
    int c = a;
    a++;
    cout << c<< endl;

    int m;
    cin >> m;
    int arr[m];
    for (unsigned i = 0; i < 10; ++i)
    {
        arr[i] = i;
    }

    for (unsigned i = 0; i < 10; ++i)
    {
        cout << arr[i] << endl;
    }

    int n;
    cin >> n;
    int *q = new int[n];
    *q = 10;
    cout << *q << endl;
    delete[] q;
    return 0;
}