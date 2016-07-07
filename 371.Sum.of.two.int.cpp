#include <stdio.h>

/*
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
 */

int getSum(int a, int b) {
	int carry;
	while (b) {
		// b will be the shifted carry after the first iteration
		// xor will always add up 2 bits, let alone the carry
		// so, say at the 2nd iteration, if the second digit is zero,
		// together with the carry, the bit will be 1 and no more carry
		// or else, the bit is already 1, xoring with carry (1) will produce a
		// sum and another carry for the next bit
		carry = a & b;
		a = a ^ b;

		// moves the carry left one bit at a time
		// as it will be in the 01000 kinda way
		b = carry << 1;
	}
	return a;
}

int main(int argc, char const *argv[])
{
	printf("%d\n", getSum(3,4));
	return 0;
}






