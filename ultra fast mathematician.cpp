#include <iostream>
#include <string>
using namespace std;
int main(){
    string a, b, c;
    cin>>a>>b;
    for(int i=0; i<a.length(); i++){
        if(a[i]==b[i]){
            c='0';
        }
        else if(a[i]!=b[i]){
            c='1';
        }
        cout<<c;
    }

    return 0;
}
