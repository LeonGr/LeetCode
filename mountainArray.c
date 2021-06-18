#include <stdbool.h>
#include <stdio.h>

#define SIZE(x) (sizeof(x) / sizeof((x)[0]))

bool validMountainArray(int* arr, int arrSize){
    int i;
    int j;
    for (i = 0; i < arrSize - 1; i++) {
        if (arr[i] > arr[i+1]) {
            j = i+1;
            break;
        } else if (arr[i] == arr[i+1]) {
            return false;
        }
    }

    for (j; j < arrSize - 1; j++) {
        if (arr[j] <= arr[j+1]) {
            return false;
        }
    }

    return i > 0 && j > 0;
}

int main() {
    int valid[] = {0, 2, 3, 4, 5, 2, 1, 0};
    int invalid[] = {2, 1};

    printf("%d\n", validMountainArray(valid, SIZE(valid)));
    printf("%d\n", validMountainArray(invalid, SIZE(invalid)));

    return 0;
}
