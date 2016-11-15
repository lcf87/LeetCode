#include <stdio.h>

int myatoi(char *s) {
	char c;
	int length = 0;

	while ((c = *s++) != '\0' || c != '.') {
		length++;
	}

	printf("length: %d\n", length);
	return 0;
}


int main(int argc, char const *argv[])
{
	/* code */
	myatoi("");
	return 0;
}