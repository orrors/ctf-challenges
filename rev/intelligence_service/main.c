#include <stdio.h>

int main() {
  int iVar1;
  long uVar2;
  bool areConstDiff;
  long const1;
  long const2;

  const1 = 0x41bb6670;
  const2 = 0x6a676117;
  uVar2 = const2;
  do {
    const2 = uVar2;
    iVar1 = (int)const1;
    areConstDiff = const1 != const2;
    const1 = const2;
    uVar2 = (long)(int)(iVar1 - (int)const2);
  } while (areConstDiff);

	printf(" %lx\n", const2  - 0xde6dad39);
}
