#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;
int main(){
    int n, h, output=0;
    cin>>n>>h;
    int arr[n];
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }
    for(int i=0; i<n; i++){
      if(arr[i]>h){
        output+=2;
      }
      else if(arr[i]<=h){
        output++;
      }
    }
    cout<<output;

    return 0;
}
