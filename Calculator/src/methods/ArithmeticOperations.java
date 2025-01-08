package methods;

import java.util.Scanner;

public class ArithmeticOperations {

	public static Scanner input = new Scanner(System.in);

	public static double add(double ersteZahl, double zweiteZahl) {

		return ersteZahl + zweiteZahl;
	}

	public static double sub(double ersteZahl, double zweiteZahl) {
		return ersteZahl - zweiteZahl;
	}

	public static double multiply(double ersteZahl, double zweiteZahl) {
		return ersteZahl * zweiteZahl;
	}

	public static double divide(double ersteZahl, double zweiteZahl) {

		if (zweiteZahl == 0) {
			System.out.println("Teilen durch 0 ist nicht möglich");
		}

		return ersteZahl / zweiteZahl;
	}

	public static void main(String[] args) {

		double ersteZahl = input.nextDouble();
		double zweiteZahl = input.nextDouble();

		System.out.println((int) add(ersteZahl, zweiteZahl));
		System.out.println((int) sub(ersteZahl, zweiteZahl));
		System.out.println((int) multiply(ersteZahl, zweiteZahl));
		System.out.println((int) divide(ersteZahl, zweiteZahl));

	}

}
