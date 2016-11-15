#include <stdio.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    // 
}

int binaryInsertion(int* array, int len, int insertion) {
	int high = len;
	int low = 0;
	int mid = (high + low) / 2;

	while (low <= high) {
		if (insertion > array[mid])
			low = mid + 1;
		else if (insertion < array[mid])
			high = mid - 1;
		else if (insertion == array[mid])
			break;

		mid = (high + low) / 2;
	}

	return mid;
}

int main() {
	int a[] = {1,2,3,4,5,6};
	printf("insert at %d\n", binaryInsertion(a, 5, 1));
}