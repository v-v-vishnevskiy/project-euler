#include <iostream>

long int sum_of_multiples_of_3_and_5(int limit) {
	long int result = 0;
	for (int i = 1; i < 1000; i++) {
		if (i % 3 == 0 or i % 5 == 0) {
			result += i;
		}
	}
	return result;
}

void time_test() {
	long int result = 0;
	for (int i = 0; i < 10000; i++) {
		result = sum_of_multiples_of_3_and_5(1000);
	}
	std::cout << result << '\n';
}

int main(int argc, char** argv) {
	if (argc > 1) {
		time_test();
	}
	else {
		std::cout << sum_of_multiples_of_3_and_5(1000) << '\n';
	}
	return 0;
}
