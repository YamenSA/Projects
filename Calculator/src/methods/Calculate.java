package methods;

public class Calculate {

	private int zahl1;
	private int zahl2;

	public Calculate(int zahl1, int zahl2) {
		this.zahl1 = zahl1;
		this.zahl2 = zahl2;
	}

	public Calculate(int zahl1) {
		this(zahl1, 1);
	}

	public int add() {
		return zahl1 + zahl2;
	}

	public int subtract() {
		return zahl1 - zahl2;
	}

	public int multiply() {
		return zahl1 * zahl2;
	}

	public int divide() {
		if (zahl2 != 0) {
			return zahl1 / zahl2;
		} else {
			throw new IllegalArgumentException("Teilen durch null ist nicht definiert");
		}
	}

	public int potenzieren() {
		int erg = 1;
		if (zahl2 == 1) {
			return zahl1;
		} else if (zahl2 == 0) {
			return 1;
		} else {
			for (int i = 0; i < zahl2; i++) {
				erg = erg * zahl1;
			}
			return erg;
		}

	}

	public double wurzel() {
		return Math.sqrt(zahl1);

	}

	public int vorzeichenWechseln() {
		return -1 * zahl1;
	}

	public int getZahl1() {
		return zahl1;
	}

	public void setZahl1(int zahl1) {
		this.zahl1 = zahl1;
	}

	public int getZahl2() {
		return zahl2;
	}

	public void setZahl2(int zahl2) {
		this.zahl2 = zahl2;
	}

}
