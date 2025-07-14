#include<stdio.h>
#include<stdlib.h>
struct node
{
    struct node *left;
    int data;
    struct node *right;
};
struct node *createnode(int d)
{
    struct node *temp=(struct node*)malloc(sizeof(struct node));
    temp->data=d;
    temp->left=NULL;
    temp->right=NULL;
    return temp;
}

void inorder(struct node *root)
{
    if(root)
    {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

void preorder(struct node *root)
{
    if(root)
    {
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

void postorder(struct node *root)
{
    if(root)
    {
        postorder(root->left);
        postorder(root->right);
        printf("%d ", root->data);
    }
}
int height(struct node *root)
{
    if(root==NULL)
        return 0;
    else
    {
    int l=height(root->left);
    int r=height(root->right);
    if(l>r)
        return l+1;
    else
        return r+1;
    }
}
void main()
{
    struct node *root;
    root = createnode(1);
    root->left = createnode(2);
    root->right = createnode(3);
    root->left->left = createnode(4);
    root->left->right = createnode(5);
    root->right->left = createnode(6);
    root->right->right = createnode(7);
    root->left->left->left = createnode(8);
    printf("Inorder: ");
    inorder(root);
    printf("\nPreorder: ");
    preorder(root);
    printf("\n");
    postorder(root);
    printf("\nHeight of the tree: %d\n", height(root)); 
}
