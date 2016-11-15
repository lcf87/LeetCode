//
//  main.c
//  Interview
//
//  Created by Chen Luyuan on 10/20/14.
//  Copyright (c) 2014 Chen Luyuan. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#pragma mark - Prototype

#pragma mark - Convenience methods
struct node{
    int value;
    struct node* right;
    struct node* left;
};

/************************************************************
 * Queue methods
 */

struct node *queue[20];
struct node **q_ptr_add = queue;
struct node **q_ptr = queue;

void enqueue(struct node *to_enq) {
    *q_ptr_add++ = to_enq;
}

struct node *dequeue(void) {
    if (q_ptr_add == queue)
        return NULL;
    return *q_ptr++;
}

struct node* newNode(int value) {
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    newNode -> value = value;
    newNode -> right = NULL;
    newNode -> left = NULL;
    return newNode;
}

#pragma mark - Print
void printTree(struct node *root) {
    if (root) {
        printf("%d ", root -> value);
        printTree(root -> left);
        printTree(root -> right);
    }
}

#pragma mark - Height
int treeHeight(struct node *root) {
    if (!root) {
        return 0;
    }

    int left, right;

    left = treeHeight(root -> left);
    right = treeHeight(root -> right);

    left++;
    right++;

    return (left > right) ? left : right;
}

int new_height(struct node *root) {
    int left, right;

    // implemented sep 22 2016
    //
    if (!root)
        return 0;
    if (!root->left && !root->right) {
        return 1;
    }

    left = 1 + new_height(root->left);
    right = 1 + new_height(root->right);

    return (left > right) ? left : right;
}

void level_order(struct node *root) {

    if (!root)
        return;
    // have to enqueue root somewhere
    // enqueue left and right
    if (root->left)  enqueue(root->left);
    if (root->right) enqueue(root->right);

    printf("%d\n", root->value);

    return level_order(dequeue());
}

#pragma mark - Interview
// 4.3

struct node* buildTree(int array[], int low, int high) {
    if (high < low) {
        return NULL;
    } // 就是这一行屌！

    int mid = (low + high) / 2;
    struct node *root = newNode(array[mid]);
    if (low < high) {
        root -> left = buildTree(array, low, mid - 1);
        root -> right = buildTree(array, mid + 1, high);
    }
    return root;
}

int maxH = -10;


int maxSize(struct node *root, int lower, int upper) {
    if (!root)
        return 0;

    int lSize = maxSize(root->left, lower, upper);
    int rSize = maxSize(root->right,lower, upper);

    if (root->value < lower || root->value > upper)
        return -1;
    if (lSize != -1 && rSize != -1) {
        maxH = (1 + lSize + rSize > maxH) ? 1 + lSize + rSize : maxH;
        return 1 + lSize + rSize;
    }
    return -1;
    // else
}

int main(void) {
    struct node *root = newNode(16);
    struct node *l1 = newNode(1);
    struct node *l2 = newNode(3);
    struct node *l3 = newNode(2);
    struct node *l4 = newNode(4);
    struct node *l5 = newNode(5);
    struct node *l6 = newNode(7);
    struct node *l7 = newNode(9);
    struct node *l8 = newNode(8);
    struct node *l9 = newNode(12);
    struct node *l10 = newNode(10);
    struct node *l11 = newNode(14);
    struct node *l12 = newNode(13);
    struct node *r1 = newNode(19);
    struct node *r2 = newNode(15);
    struct node *r3 = newNode(23);
    struct node *r4 = newNode(18);
    struct node *r5 = newNode(25);

    root->left = l6; root->right = r1;
    l6->left = l4; l6->right = l7;
    l4->left = l3; l4->right = l5;
    l3->left = l1; l3->right = l2;
    l7->left = l8; l7->right = l9;
    // l9->left = l10; l9->right = l11;
    // l11->left = l12;

    r1->left = r2; r1->right = r3;
    r3->left = r4; r3->right = r5;

    maxSize(root, 5,12);
    printf("size: %d\n", maxH);

    free(root);
    free(l1 );
    free(l2 );
    free(l3 );
    free(l4 );
    free(l5 );
    free(l6 );
    free(l7 );
    free(l8 );
    free(l9 );
    free(l10);
    free(l11);
    free(l12);
    free(r1 );
    free(r2 );
    free(r3 );
    free(r4 );
    free(r5 );
}

void factory() {
    int array[] = {1,3,6,7,9,10,13,15,21,38};
    struct node *newTree = buildTree(array, 0, 9);
}
