#include <stdio.h>
#include <stdlib.h>

struct avlNode {
   int balance; /* -1 Left, 0 balanced, +1 Right */
   int val;
   struct avlNode *left;
   struct avlNode *right;
};
typedef struct avlNode avlNode;

struct qNode {
   avlNode *pval;
   struct qNode *nxt;
};
typedef struct qNode qNode;

int height(avlNode *root){
   if (root==NULL){
       return 0;
   }
else{
   int x= height(root->left);
   int y= height(root->right);
   if (y>x){
       return 1+y;}
   else{
       return 1+x;}
   }
   }

int getBalance(avlNode *N){
    if (N==NULL){
        return 0;
    }
    return height(N->left)- height (N->right);
}

int isAVL(avlNode **root){
    int leftheight;
    int rightheight;
    int diff;
    if (*root==NULL){
        return 1;}
    leftheight=height((*root)->left);
    rightheight=height((*root)->right);
    if (leftheight>rightheight){
        diff = leftheight-rightheight;
    }else{
        diff = rightheight-leftheight;}

     if (diff<=1 && isAVL(&((*root)->left)) && isAVL(&((*root)->right))){
        return 1;
    }
    else{
        return 0;
    }
    }

int rotate(avlNode **root, unsigned int Left0_Right1){
    avlNode *y=NULL;
    if (Left0_Right1==0){
 /* go mcfrickin left */
    y = (avlNode *)malloc(sizeof(avlNode));
    y->val = (*root)->val;
    y->left = (*root)->left;
    y->right =((*root)->right)->left;
    *root = (*root)->right;
    (*root)->left = y;
    return 1;}
    else if (Left0_Right1==1){
/* go mcfrickin right */
    y = (avlNode *)malloc(sizeof(avlNode));
    y->val = (*root)->val;
    y->right = (*root)->right;
    y->left =((*root)->left)->right;
    *root = (*root)->left;
    (*root)->right = y;
    return 1; }
}

int dblrotate(avlNode **root, unsigned int MajLMinR0_MajRMinL1){
    if (root==NULL){
       return 0;}
    if (MajLMinR0_MajRMinL1==0){
        rotate(&(*root)->right, 1);
        rotate(root,0);
    }
    else if (MajLMinR0_MajRMinL1 ==1){
        rotate(&((*root)->left), 0);
        rotate(root, 1);
    }
    return 1;

}

int add_bst(avlNode** root,int val) {
    if (root == NULL){
        return -1;
    }if (*root == NULL){
        (*root)=(avlNode*)malloc(sizeof(avlNode));
        if (*root == NULL){
            return -1;
        }else{
            ((*root)->val)=val;
        }
    }else{
        if (val<((*root)->val)){
            add_bst((&(*root)->left), val);
        }if(val>((*root)->val)){
            add_bst((&(*root)->right), val);
        }
    }
    return 0;
}


int printTreeInOrder(avlNode* root){
    if (root != NULL)
    {
        printTreeInOrder(root->left);
        printf("%d \n", root->val);
        printTreeInOrder(root->right);
    }
    return 0;
}

