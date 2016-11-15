#include <stdio.h>

int reverse(int x) {
    int deno = 1;
    int digits[10] = {-1};
    int i = 0;
    int neg;
    int new_x = 0;

    if (x < 0) {
    	neg = 1;
    	x = -1 * x;
    }
    
    for(;deno < x; deno *=10, i++) {
        digits[i] = (x / deno) % 10;
        // printf("deno: %d\n", deno);
        // printf("digits: %d\n", digits[i]);
    }

    int len = i;

    // reconstruction
    for (i = 0, deno/=10; i < len; i++, deno/=10) {
    	new_x += digits[i] * deno;
    	printf("digits: %d\n", new_x);
    }


    return (neg) ? -1*new_x : new_x;
 }

 int main(int argc, char const *argv[])
 {
 	/* code */
 	printf("\n\n%d\n", reverse(1000000003));
 	return 0;
 }