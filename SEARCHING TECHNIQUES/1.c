// binary search program
#include<stdio.h>
int bs(int a[], int n, int key) {
    int low, high, mid;
    low =0;
    high -= n - 1;
    while(low <= high) {
        mid = (low + high) / 2;
        if(a[mid] == key) {
            return mid; // key found
        } else if(key<a[mid]) {
            high = mid -1; // search in left half
        } else {
            low = mid + 1; // search in right half
        }
    }
    return -1;
}

void main() {
    int a[10], size,key,s;
    scanf("%d", &size);
    for(int i = 0; i < size; i++) {
        scanf("%d", &a[i]);
        scanf("%d", &key);
        s=bs(a, size, key);
        if(s == -1) {
            printf("Key not found\n");
        } else {
            printf("Key found at index %d\n", s);
        }
    }
}