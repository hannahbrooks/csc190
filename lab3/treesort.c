#include <stdio.h>
#include <stdlib.h>

struct bstNode {
   int val;
   struct bstNode *l;
   struct bstNode *r;
   };
typedef struct bstNode bstNode;

int printTreeInOrder(bstNode* root){
   if (root != NULL)
   {
      printTreeInOrder(root->l);
      printf("%d \n", root->val);
      printTreeInOrder(root->r);
   }
   return 0;
}


int add_bst(bstNode** root,int val) {
   if (root == NULL){
      return -1;
   }if (*root == NULL){
      (*root)=(bstNode*)malloc(sizeof(bstNode));
      if (*root == NULL){
         return -1;
      }else{
         ((*root)->val)=val;
      }
   }else{
      if (val<((*root)->val)){
         add_bst((&(*root)->l), val);
      }if(val>((*root)->val)){
         add_bst((&(*root)->r), val);
      }return 0;
   }
}

int main(void){
   bstNode * x= NULL;
   int val = 0;
   int cnt =0;
   while(scanf("%d", &val)!=EOF){
      cnt=cnt+1;
      add_bst(&x, val);
   }
   printTreeInOrder(x);
   return 0;
}

