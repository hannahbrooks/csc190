#include <stdio.h>
#include <stdlib.h>

unsigned char prng(unsigned char x,unsigned char pattern) {
   unsigned char oldbit0 = x & 0x1; /* extract bit 0 */
   unsigned char r = x >> 1;        /* shift right   */
   unsigned char newbit7 = oldbit0 << 7; /* move bit0 to the bit7 pos */
   r = r | newbit7; /* rotate the old value of bit 0 into the bit 7 pos */
   return r^pattern;
}

int crypt(char *data,unsigned int size, unsigned char password){
  
  char prngVal = password;
  char newchar = 0;
  char oldchar = 0;
  int i = 0;
  int j = 0;
  int length = 0;

  while (j == 0){
    if (data[length] != '\0'){
      length += 1;
    }
    else{
      j = 6;
      break;
    }
  }
  
  length += 1;

  if (length != size+1){
    return -1;
  }
  
  if (password == 0){
    return -1;
  }
  
  for (i=0;i<size;i++){
    oldchar = data[i];
    prngVal = prng(prngVal,0xb8);
    data[i] = oldchar^prngVal;
  }
  
  for (j=0;j<size;j++){
    oldchar = data[j];
    prngVal;
  }
  
  return 0;
}
