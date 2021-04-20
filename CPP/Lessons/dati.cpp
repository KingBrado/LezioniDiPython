#include <iostream>
using namespace std;

int somma(int x, int y)
{
    return x + y;
}


int main(int argc, char** argv)
{
    int a = 1;
    int b = 2;
    float c = 3.0f;
    a = 'c';
    cout << a << endl;
    cout << c/b << endl;
    cout << '2'+'4' << endl;
    a = 5;
    cout<< somma(a, b) << endl;
    return 0;
}