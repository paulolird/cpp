#include <iostream>
#include <string>

using namespace std;

int main()
{
    string str;
    int i,j,k;
    int siz=0;
    char init;
    cout << "input your string: "<<endl;
    cin >> str;
    cout<< str.length()<<endl;
    for (i=0; i<str.length(); i++)
    {
        //init==str[i];
        for (j=i+1; j<str.length(); j++)
        {
            if (j==i)
            {
                if (siz<j-i)
                {
                    siz=j-i;
                }
                break;
            }
        }
    }
    cout << "size of longest non-repeating string is : "<< siz<<endl;
    for (k=i; k<j; k++)
    {
        cout << str[k];
    }
    cin >> str;
    return 0;
}
