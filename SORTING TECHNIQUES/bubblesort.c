//bubble sort in c

#include<stdio.h>
void bs(int a[], int n)
{
    int i,j,t;
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-1;j++){
            if(a[j]>a[j+1]){
                t=a[j];
                a[j]=a[j+1];
                a[j+1]=t; // swap
            }
        }
    }
}
void main(){
    int a[] = {5,3,8,6,7,2};
    int size, i;
    size = sizeof(a)/sizeof(a[0]);
    printf("Unsorted array: ");
    for(i=0;i<size;i++){
        printf("%d ", a[i]);
        bs(a, size);
        printf("\nSorted array: ");
        for(i=0;i<size;i++){
            printf("%d ", a[i]);
        }
    }

}