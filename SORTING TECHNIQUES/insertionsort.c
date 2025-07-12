#include<stdio.h> 
void ins(int a[], int n){ //30 10 40 20 50 --- 10 20 30 40 50
    int i,j,temp;
    for(i=1;i<n;i++){
        temp = a[i]; // store the current element 20
        j = i - 1; // start from the previous element 2
        while(j >= 0 && a[j] > temp){ // shift elements greater than temp // 0>=0 20<10
            a[j + 1] = a[j]; // move element one position ahead  // a[2]=a[1]
            j--; // move to the next element//0
        }
        a[j + 1] = temp; // place the temp in its correct position//a[1]=temp
    }
}
void main(){
    int a[] {30,10,40,20,50};
    int size, i;
    size = sizeof(a)/sizeof(a[0]);
    printf("Unsorted array: "); 
    for(i=0;i<size;i++){
        printf("%d ", a[i]);
        ins(a, size);
        printf("\nSorted array: ");
        for(i=0;i<size;i++){
            printf("%d ", a[i]);
        }
    }

}