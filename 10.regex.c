#include <stdio.h> 

/*
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
isMatch("ab", ".*c") → false
isMatch("aaa", "a*a") → true

 */
bool isMatch(char* s, char* p) {
    int match = 0;
    char pattern;
    bool wild = false;

    while ((pattern = *p++) != '\0') {
    	printf("loop \n");

    	// move with the pattern
    	wild = (*p == '*');

    	if (wild)
    		// move to next if next is *
    		p++;
    	if (*s == '\0')
    		return false;

    	printf("wild: %d\n", wild);
    	
    	// start matching 
    	if (pattern == '.') {
    		if (wild) {
    			// don't care from here
    			while (*s++ != '\0');
    		} else {
    			// move to the next letter
    			s++;
    		}
    	} else {
    		// matching letters
    		if (wild) {
    			// with wild card
    			// skip if the letter doesn't match
    			if (*s != pattern)
    				continue;
    			// move next until the pattern changes
    			// TODO deal with a*a == aaa here
    			else 
    				while (*s == pattern) {
    					printf("s: %c\n", *s);
    					s++;
    				}


    		} else {
    			// match only one
    			if (*s == pattern) {
    				s++;
    			} else {
    				return false;
    			}
    		}
    	}
    }

    // if the matching is incomplete
    return (*s == '\0');
}



int main(int argc, char const *argv[])
{
	/* code */
	printf("%d\n", isMatch("aaa", "a*"));
	return 0;
}