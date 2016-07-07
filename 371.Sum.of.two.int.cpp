#include <stdio.h>

int getSum(int a, int b) {
    return a | b;
}

int main(int argc, char const *argv[])
{
	printf("%d\n", getSum(5,2));
	return 0;
}