#include <iostream>

int sum_of_even_fibonacci_terms(int limit) {
	int result = 0;
	int prev = 1;
	int current = 1;
	int old_current = 0;
	while (current < limit) {
		old_current = current;
		current += prev;
		prev = old_current;
		if (current % 2 == 0) {
			result += current;
		}
	}
	return result;
}

void time_test() {
	long int result = 0;
	for (int i = 0; i < 100'000; i++) {
		result = sum_of_even_fibonacci_terms(4'000'000);
	}
	std::cout << result << '\n';
}

int main(int argc, char** argv) {
	if (argc > 1) {
		time_test();
	}
	else {
		std::cout << sum_of_even_fibonacci_terms(4'000'000) << '\n';
	}
	return 0;
}
