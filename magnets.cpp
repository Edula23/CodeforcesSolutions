#include <iostream>
using namespace std;
int main(){
    int testCases, output=1, a, b;
    cin>>testCases;
    int arr[testCases];
    for(int i=0; i<testCases; i++){
        cin>>arr[i];
    }
    for(int i=0; i<testCases-1; i++){
        if(arr[i+1]==arr[i]){
            continue;
        }
        else{
            output++;
        }
    }
    cout<<output-1;
    return 0;
}
