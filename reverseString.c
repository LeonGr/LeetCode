#include <stdio.h>

void reverseString(char* s, int sSize){
    int i;
    int x = sSize / 2;
    unsigned char test = -1;
    printf("%d", test);
    for (i = 0; i < x; i++) {
        unsigned char temp = s[i];
        int index = sSize - i - 1;
        s[i] = s[index];
        s[index] = temp;

        //s[i] = s[i] ^ s[index];
        //s[index] = s[index] ^ s[i];
        //s[i] = s[i] ^ s[index];
    }
}

int main() {
    char string[] = "hello there";
    int length = sizeof(string) / sizeof(string[0]);

    reverseString(string, length);

    for (int i = 0; i < length; i++) {
        printf("%c", string[i]);
    }

    return 0;
}
