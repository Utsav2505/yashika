#include <iostream>
using namespace std;

// hey there
int i;
// int main()
// {
//     cout << "enter a no.";
//     cin >> i;
//     int j = 1;
//     do
//     {
//         cout << i << "*" << j << '=' << i * j << endl;
//         j++;
//     } while (j <= 10);

//     return 1;
// }

// int main()
// {
//     for (int i = 0; i < 40; i++)
//     {
//         cout << i << endl;
//         if (i == 2)
//         {
//             break;
//         }
//     }
//     return 1;
// }

// int main()
// {
//     for (int i = 0; i < 40; i++)
//     {
//         if (i == 2)
//         {
//             continue;
//             ;
//         }
//         cout << i << endl;
//     }
//     return 1;
// }

// int main()
// {
//     // int a[4];
//     int a[4] = {1, 2, 3, 4};
//     for (i = 0; i < 4; i++)
//     {
//         cout << a[i] << endl;
//     }
// }

// int main()
// {
//     int a[6] = {23, 34, 5, 45, 57, 43};
//     int *p = a;
//     cout << *p << endl;
//     cout << *(p + 1) << endl;
//     cout << *(p + 2) << endl;
//     cout << *(p + 3) << endl;
//     cout << *(p + 4) << endl;
//     cout << *(p + 5) << endl;
// }

// int main()
// {
//     int x = 5;
//     int &a = x;
//     cout << x << endl;
//     cout << a << endl;
//     return 1;
// }

// int &swapbyreference(int &a, int &b)
// {
//     int temp = a;
//     a = b;
//     b = temp;
//     return a;
// }

// int main()
// {
//     int x = 3, y = 6;
//     cout << x << "and" << y << endl;
//     swapbyreference(x, y) = 766;
//     cout << x << "and" << y << endl;
// }

// int main()
// {
//     int x = 5;
//     int &a = x;
//     cout << x << endl;
//     cout << a << endl;
//     a = 3;
//     cout << x << endl;
//     cout << a << endl;
//     return 1;
// }

// int sum(int a, int b)
// {
//     return a + b;
// }

// int sum(int a, int b, int c)
// {
//     return a + b + c;
// }

// int main()
// {
//     cout << sum(4, 6) << endl;
//     cout << sum(4, 6, 5) << endl;
//     return 2;
// }

// object oriented programming:

// int main()
// {
//     int a[4] = {1, 2, 3, 4};
//     int *p = a;
//     cout << *p << endl;
//     cout << *(p + 1) << endl;
//     cout << *(p + 2) << endl;
//     cout << *(p + 3) << endl;
//     return 1;
// }

// class Complex
// {
//     int a = 4, b = 6;
// public:
//     friend Complex sumcomplex(void);
// };

// Complex sumcomplex(void)
// {
//     Complex obj1;
//     cout << obj1.a << "and" << obj1.b << endl;
//     return obj1;
// }

// int main()
// {
//     Complex summm;
//     summm = sumcomplex();
//     return 0;
// }

// class c2;

// class c1
// {
//     int val1;
//     friend void exchange(c1 &x, c2 &y);

// public:
//     void setData(int a)
//     {
//         val1 = a;
//     }
//     void displayData(void)
//     {
//         cout << val1 << endl;
//     }
// };

// class c2
// {
//     int val2;
//     friend void exchange(c1 &x, c2 &y);

// public:
//     void setData(int a)
//     {
//         val2 = a;
//     }
//     void displayData(void)
//     {
//         cout << val2 << endl;
//     }
// };

// void exchange(c1 x, c2 y)
// {
//     int temp = x.val1;
//     x.val1 = y.val2;
//     y.val2 = temp;
// }

// class Complex
// {
//     int a = 5;
//     int b = 100;

// public:
//     // Complex(void)
//     // {
//     //     a = 10;
//     //     b = 7;
//     // }
//     void printNumbers(void)
//     {
//         cout << a << "+" << b << "i" << endl;
//     }
// };

// int main()
// {
//     Complex c1;
//     c1.printNumbers();
//     return 0;
// }

#include <cmath>
class Point
{
    int x, y;

public:
    friend void printDistance(Point q1, Point q2);
    Point(int a = 0, int b = 0)
    {
        x = a;
        y = b;
    }

    void displayPoints(void)
    {
        cout << "the point is (" << x << "," << y << ")" << endl;
    }
};

void printDistance(Point q1, Point q2)
{
    float dist = sqrt(pow((q1.x - q2.x), 2) + pow((q1.y - q2.y), 2));
    cout << "the distance between points is " << dist << endl;
}

int main()
{
    Point p1(3, 4), p2(10), p3;
    p1.displayPoints();
    p2.displayPoints();
    p3.displayPoints();

    printDistance(p1, p2);
    return 0;
}

// void area(int a, int b)
// {
//     cout << a << "and" << b << endl;
// }

// void area(char a, char b)
// {
//     cout << a << "the" << b << endl;
// }

// int main()
// {
//     area(1, 2);
//     return 0;
// }
