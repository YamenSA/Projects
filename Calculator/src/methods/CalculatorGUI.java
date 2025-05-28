package methods;

import javax.swing.ImageIcon;
import javax.swing.JFrame;

class CalculatorGUI {

	public static void main(String[] args) {

		JFrame frame = new JFrame("Taschenrechner");

		frame.setSize(400, 600);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setLocationRelativeTo(null);

		ImageIcon icon = new ImageIcon(CalculatorGUI.class.getResource("/res/calculator.png"));
		frame.setIconImage(icon.getImage());

		frame.setVisible(true);

	}

}
