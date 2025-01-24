int getNext(int n) {
    int totalSum = 0;
    while (n > 0) {
        int digit = n % 10;
        totalSum += digit * digit;
        n /= 10;
    }
    return totalSum;
}

int isHappy(int n) {
    int slow = n, fast = getNext(n);

        while (fast != 1 && slow != fast) {
        slow = getNext(slow);          
        fast = getNext(getNext(fast)); 
    }

    return fast == 1;
}
