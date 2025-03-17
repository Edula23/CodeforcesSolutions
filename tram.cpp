#include <iostream>
//#include <bits/stdc++.h>
#include <string>>
using namespace std;
int tram(int &a, int &b, int &total){
      total+=(b-a);
      //cout<<total;
      return total;
}
void sortingArray(int arr[], int size){
    int temp;
    for(int i=0; i<size; i++){
        if(i+1<size && arr[i]>arr[i+1]){
            temp = arr[i];
            arr[i]= arr[i+1];
            arr[i+1]=temp;
        }
        else if(i+1>=size){
            break;
        }
        else{
            continue;
        }

    }}
   /*for(int i=0; i<size; i++){
        if(i+1<size && arr[i]>arr[i+1]){
            temp = arr[i];
            arr[i]= arr[i+1];
            arr[i+1]=temp;
        }}
   }*/
int main() {
  int nStops, output, total=0;
  cin>>nStops;
  int arr[nStops];
  for(int i=0; i<nStops; i++){
    int a, b;
    cin>>a>>b;
    arr[i] = tram(a, b, total);

  }
sortingArray(arr, nStops);
output= arr[nStops-1];
cout<<output;
    return 0;
}
