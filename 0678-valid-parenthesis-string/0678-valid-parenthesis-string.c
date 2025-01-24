#include <stdbool.h>
#include <string.h>

bool checkValidString(char* s) {
    int openCount = 0, starCount = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(') {
            openCount++;
        } else if (s[i] == ')') {
            openCount--;
        } else {
            starCount++;
        }

        if (openCount < 0) {
            if (starCount > 0) {
                openCount++;
                starCount--;
            } else {
                return false;
            }
        }
    }

    openCount = 0;
    starCount = 0;

    for (int i = strlen(s) - 1; i >= 0; i--) {
        if (s[i] == ')') {
            openCount++;
        } else if (s[i] == '(') {
            openCount--;
        } else {
            starCount++;
        }

        if (openCount < 0) {
            if (starCount > 0) {
                openCount++;
                starCount--;
            } else {
                return false;
            }
        }
    }

    return true;
}
