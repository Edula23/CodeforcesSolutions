#include <iostream>
using namespace std;
int main(){
    int people;
    cin>>people;
    int arr[people];
    string output;
    for(int i=0; i<people; i++){
        cin>>arr[i];
    }
    for(int i=0; i<people; i++){
        if(arr[i]==1){
            output="HARD";
            break;
        }
        else{
           output="EASY";
        }

    }
    cout<<output;
    return 0;
}
