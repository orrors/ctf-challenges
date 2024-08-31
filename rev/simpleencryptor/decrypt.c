#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
  FILE *fd = fopen("flag.enc.backup", "rb");
  ulong seed = 0;
  fread(&seed, 4, 1, fd);

  fseek(fd, 0, SEEK_END);
  int flag_size = ftell(fd) - 4;
  fseek(fd, 4, SEEK_SET); // go back to byte 4

  uint8_t *uvar = (uint8_t *)malloc(sizeof(uint8_t) * flag_size);
  ulong *var38 = (ulong *)malloc(sizeof(ulong) * flag_size);
  unsigned char *flag = (unsigned char *)malloc(sizeof(unsigned char) * flag_size);

  // read encrypted flag
  fread(flag, flag_size, 1, fd);

  // get random values
  srand(seed); // the seed from the encrypted file
  for (int i = 0; i < flag_size; i++) {
    uvar[i] = rand();
    var38[i] = rand() & 7;
  }

  // decrypt
  for (int i = flag_size - 1; i >= 0; i--) {
    flag[i] = flag[i] >> var38[i] | flag[i] << 8 - var38[i];
    flag[i] = flag[i] ^ uvar[i];
  }

  printf("%s\n", flag);

  free(flag);
  free(uvar);
  free(var38);
  fclose(fd);

  return 0;
}
