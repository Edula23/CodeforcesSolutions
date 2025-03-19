#include <iostream>
using namespace std;
int main(){
    int rooms, output=0;
    cin>>rooms;
    for(int i=0; i<rooms; i++){
        int a, b;
        cin>>a>>b;
        if(b-a>=2){
            output++;
        }
    }
    cout<<output;
    return 0;
}
