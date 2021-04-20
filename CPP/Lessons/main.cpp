#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    int a, b;
    cout << "Inserisci due numeri" << endl;
    cin >> a >> b;
    if (b == 0)
    {
        cout << "Non posso dividere per 0, operazione abortita\n";
        return 1;
    }
    cout << a << " diviso " << b << " fa " << a / b << endl;
    return 0;
}
