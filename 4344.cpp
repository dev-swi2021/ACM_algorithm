#include <stdio.h>

int main(){
  int c,n,score, count;
  int arr[1000];
  double avg, percent[1000];
  
  scanf("%d",&c);
  
  for(int i=0;i<c;i++){
    avg = 0;
    count = 0;
    scanf("%d",&n);
    for(int j=0;j<n;j++){
      scanf("%d",&score);
      arr[j] = score;
      avg += score;
    }
    avg /= n;
    for(int j=0;j<n;j++){
      if(arr[j] > avg){
        count ++;
      }
    }
    percent[i] = ((double)count / n) * 100;
  }
  for(int i=0;i<c;i++){
    printf("%.3lf%%\n", percent[i]);
  }
  return 0;
}
    
