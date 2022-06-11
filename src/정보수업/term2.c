#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

#define DEFAULT 100

// -STACK-------------------------------

#define STACK_SIZE 256
char stack[STACK_SIZE];
int idx = -1;

void push(char x) {
    if (idx >= STACK_SIZE) {
        printf("스택 오버플로우");
        return;
    }
    stack[++idx] = x;
}

char pop() {
    if (idx <= -1) {
        printf("스택이 비었습니다");
        return -1;
    }
    return stack[idx--];
}

char top() {
    if (top <= -1) {
        return -1;
    }
    return stack[idx];
}

void reset_stack() {
    idx = -1;
}

bool is_empty() {
    return idx == -1;
}

// -FUNCTION-------------------------------

bool is_operator(char x) {
    return (x == '+' || x == '-' || x == '*' || x == '/' || x == '%');
}

bool is_num(char x) {
    return ('0' <= x && x <= '9') || (x == '.');
}

int get_priority(char op) {
    switch (op) {
        case '+':
        case '-':
            return 0;
        case '*':
        case '/':
        case '%':
            return 1;
        default:
            return -1;
    }
}

bool postfix(char* formula, char* ret);

// -MAIN------------------------------

int main() {
    char formula[DEFAULT];
    char postfixed[DEFAULT];

    printf("[ Calculator ]\n");
    printf("===============================\n");

    do {
        printf("enter formula >> ");
        scanf("%s", formula);
        postfix(formula, postfixed);
        printf("postfixed >> %s\n", postfixed);
    } while (strcmp(formula, "exit") != 0);

    return 0;
}

bool postfix(char* formula, char* ret) {
    int idx = 0;
    char p;
    reset_stack();

    while (true) {
        p = formula[idx];

        if (is_num(p)) {
            strcat(ret, p);
            idx++;
        }
        /*
        else if (p == '(') {

        }
        else if (p == ')') {
        
        }
         */
        else if (is_operator(p)) {
            if (is_empty()) {
                push(p);
            }
            else {
                if (get_priority(p) > get_priority(top())) {
                    push(p);
                    idx++;
                }
                else {
                    strcat(ret, pop());
                    push(p);
                    idx++;
                }
            }
        }
        else {
            printf("알 수 없는 문자입니다.");
            return false;
        }
    }

    while (!is_empty()) {
        strcat(ret, pop());
        idx++;
    }

    strcat(ret, '\0');
    return true;
}