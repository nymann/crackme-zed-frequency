# Crackme Zed Frequency

### How to test solution

```sh
# git clone the repo, then:
docker build -t license -f docker/Dockerfile .
docker run -it license
```

<details>
<summary>Ghidra reversed</summary>

```c
int main(int argc,char **argv)

{
  int character;
  FILE *key_file_stream;
  long in_FS_OFFSET;
  int i;
  int local_b4;
  uint auStack168 [28];
  char local_38 [26];
  undefined local_1e;
  long local_10;

  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  if (argc < 2) {
    printf("usage: %s <keyfile>\n",*argv);
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  key_file_stream = fopen(argv[1],"rt");
  for (i = 0; i < 0x1a; i = i + 1) {
                    /* initialize the first 26 elements in the array to 0 */
    auStack168[i] = 0;
  }
                    /* for each character in the file */
  while (character = fgetc(key_file_stream), character != -1) {
                    /* If character is not lowercase a to z */
    if ((character < 0x61) || (0x7a < character)) {
                    /* If character is uppercase A to Z */
      if ((0x40 < character) && (character < 0x5b)) {
                    /* Set austack[char - 'A'] = austack[char - 'A'] + 1 */
        auStack168[character + -0x41] = auStack168[character + -0x41] + 1;
      }
    }
    else {
                    /* character is lowercase [a;z] */
      auStack168[character + -0x61] = auStack168[character + -0x61] + 1;
    }
  }
  printf("the generated key is: ");
                    /* print 25 characters of the generated key */
  for (local_b4 = 0; local_b4 < 0x1a; local_b4 = local_b4 + 1) {
    printf("%d",(ulong)auStack168[local_b4]);
    local_38[local_b4] = (char)auStack168[local_b4] + '0';
  }
  local_1e = 0;
  putchar(10);
  character = strcmp(local_38,"01234567890123456789012345");
  if (character == 0) {
    puts("you succeed!!");
  }
  else {
    puts("you failed!!");
  }
  if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
    return 0;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}
```

</details>
