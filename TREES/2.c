//write a program to calculate the size of the tree
// size - number of nodes in the tree

#include <stdio.h>
#include <stdlib.h>
struct node{
    int data;
    struct node *left;
    struct node *right;
};
struct node *createnode(int d){
    struct node *temp = (struct node*)malloc(sizeof(struct node));
    temp->data = d;
    temp->left=NULL;
    temp->right=NULL;
    return temp;
}

void size(struct node *root, int *count){
    if(root ==NULL){
        return;
    }
    *count +=1;
    size(root->left,count);
    size(root->right,count);
}
void main()
{
    struct node *root = createnode(1);
    root->left = createnode(2);
    root->right = createnode(3);
    root->left->left = createnode(4);
    root->left->right = createnode(5);
    int count = 0;
    size(root, &count);
    printf("Size of the tree: %d", count);
}