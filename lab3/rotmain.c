#include <stdio.h>
#include <stdlib.h>

struct avlNode {
   int balance; /* -1 Left, 0 balanced, +1 Right */
   int val;
   struct avlNode *left;
   struct avlNode *right;
};
typedef struct avlNode avlNode;

int main(void){
    avlNode * x= NULL;
    add_bst(&x, 4);
    add_bst(&x, 2);
    add_bst(&x,10);
    add_bst(&x, 8);
    add_bst(&x,7);
    add_bst(&x, 9);
    add_bst(&x,11);

    printf("\n\nTree:\n");
    printTreeInOrder(x);
    dblrotate(&x,0);
    printTreeInOrder(x);
                if (isAVL(&x)){
                        printf("This is AVL");
                            }else{
               printf("Not AVL");}

               return 0;
}
