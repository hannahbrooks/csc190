#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *store;
    unsigned int size;
    unsigned int end;
} HeapType;


int initHeap(HeapType *pHeap, int size) {
    if (pHeap == NULL) {return -1;}
    
    (pHeap)->store = (int*)malloc(sizeof(int)*(size));
    (pHeap)->size = size;
    (pHeap)->end = 0;
    
    return 0;
}

int preOrderHelp1(int *output, int *input, int key) {
    output[*input] = key;
    *input = *input + 1;
    
    return 0;
}

int preOrderHelp2(HeapType *pHeap,int *output,int *input,int pi) {
    if (pi < (pHeap)->end) {
        preOrderHelp1(output,input,(pHeap)->store[pi]);
        preOrderHelp2(pHeap,output,input,(pi*2)+1);
        preOrderHelp2(pHeap,output,input,(pi*2)+2);
    }
    return 0;
}

int preOrder(HeapType *pHeap, int **output, int *o_size) {
    int input = 0;
    int pi = 0;
    
    (**output) = (int)malloc(sizeof(int)*(pHeap)->end);
    *o_size = (pHeap)->end;
    preOrderHelp2(pHeap,*output,&input,pi);
    
    return 0;
}

int inOrderHelp1(int *output,int *input,int key) {
    output[*input] = key;
    *input = *input + 1;
    
    return 0;
}

int inOrderHelp2(HeapType *pHeap,int *output,int *input,int pi) {
    if (pi < (pHeap)->end) {
        inOrderHelp2(pHeap,output,input,(pi*2)+1);
        inOrderHelp1(output,input,(pHeap)->store[pi]);
        inOrderHelp2(pHeap,output,input,(pi*2)+2);
    }
    return 0;
}

int inOrder(HeapType *pHeap, int **output, int *o_size) {
    int input = 0;
    int pi = 0;
    
    (**output) = (int)malloc(sizeof(int)*(pHeap)->end);
    *o_size = (pHeap)->end;
    inOrderHelp2(pHeap,*output,&input,pi);
    
    return 0;
}

int postOrderHelp1(int *output,int *input,int key) {
    output[*input] = key;
    *input = *input + 1;
    
    return 0;
}

int postOrderHelp2(HeapType *pHeap,int *output,int *input,int pi) {
    if (pi < (pHeap)->end) {
        postOrderHelp2(pHeap,output,input,(pi*2)+1);
        postOrderHelp2(pHeap,output,input,(pi*2)+2);
        postOrderHelp1(output,input,((pHeap)->store[pi]));
    }
    
    return 0;
}

int postOrder(HeapType *pHeap, int **output, int *o_size) {
    int input = 0;
    int pi = 0;
    
    (**output) = (int)malloc(sizeof(int)*(pHeap)->end);
    *o_size = (pHeap)->end;
    postOrderHelp2(pHeap,*output,&input, pi);
    
    return 0;
}



int addHeap(HeapType *pHeap, int key) {
    int childIndex = (pHeap)->end;
    int parentIndex = (childIndex-1)/2;
    
    if ((pHeap)->end == (pHeap)->size - 1) {return -1;}
    
    if (childIndex == 0) {
        (pHeap)->store[0] = key;
        (pHeap)->end = (pHeap)->end + 1;
        
        return 0;
    }
    
    while (parentIndex != childIndex) {
        if ((pHeap)->store[parentIndex] < key) {
            (pHeap)->store[childIndex] = (pHeap)->store[parentIndex];
            childIndex = parentIndex;
            parentIndex = (parentIndex-1)/2;
        }
        else {
            (pHeap)->store[childIndex] = key;
            (pHeap)->end = (pHeap)->end + 1;
            
            return 0;
        }
    }
    
    (pHeap)->store[0] = key;
    (pHeap)->end = (pHeap)->end + 1;
    
    return 0;
}

int Ugh(HeapType *pHeap,int n) {
    int pi = n;
    int ci = (2*pi)+1;
    int tmp=0;
    
    while (ci <= (pHeap)->end-1) {
        if (ci < (pHeap)->end-1) {
            if ((pHeap)->store[ci] < (pHeap)->store[ci+1]) {
                ci = ci + 1;
            }
        }
        
        if ((pHeap)->store[pi] < (pHeap)->store[ci]) {
            tmp = (pHeap)->store[pi];
            (pHeap)->store[pi] = (pHeap)->store[ci];
            (pHeap)->store[ci] = tmp;
        }
        pi = ci;
        ci = (ci*2)+1;
    }
    return 0;
}

int delHeap(HeapType *pHeap, int *key) {
    int cnt = -1;
    int index=0;
    if (pHeap == NULL) {return -1;}
    
    for (index=0;index<(pHeap)->end;index=index+1) {
        if ((pHeap)->store[index] == *key) {
            cnt = 0;
            break;
        }
    }
    
    if (cnt == -1) {return -1;}
    
    (pHeap)->store[index] = (pHeap)->store[((pHeap)->end) - 1];
    (pHeap)->end = (pHeap)->end - 1;
    Ugh(pHeap,index);
    
    return 0;
}
int main(void) {
    int i = 0;
    HeapType heap;
    int *output = NULL;
    int size;
    
    
    initHeap(&heap,10);
    addHeap(&heap,7);
    addHeap(&heap,14);
    addHeap(&heap,57);
    addHeap(&heap,98);
    addHeap(&heap,34);
    addHeap(&heap,100);
    
    for (i=0;i<heap.end;i=i+1) {
        printf("%d\n",heap.store[i]);
    }
    return 0;
}
