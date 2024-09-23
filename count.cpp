#include <iostream>
#include <stdio.h>

static int E(int i){
	if (i < 1)
		return 1;
	else
		return E(i - 1) + E(i - 2) + E(i - 3);
}

int main() {
	int e = E(10);
	printf("%d", e);
	return 0;
}