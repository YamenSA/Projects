package methods;

public class Calculator {

	public static double add(double a, double b) {
		return a + b;
	}

	public static double subtract(double a, double b) {
		return a - b;
	}

	public static double multiply(double a, double b) {
		return a * b;
	}

	public static double divide(double a, double b) {
		if (b == 0) {
			throw new IllegalArgumentException("Teilen durch null ist nicht definiert");
		}
		return a / b;
	}

	public static double potenzieren(double a, double b) {
		return Math.pow(a, b);
	}

	public static double wurzel(double a) {
		if (a < 0) {
			throw new IllegalArgumentException("Negative Werte sind nicht erlaubt!");
		}
		return Math.sqrt(a);
	}

	public static double vorzeichenWechseln(double a) {
		return -a;
	}
}
