package methods;

import java.awt.Color;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JTextField;

class CalculatorGUI extends JFrame {

	public CalculatorGUI() {
		setTitle("Taschenrechner");
		setSize(400, 600);
		setBackground(Color.WHITE);
		setDefaultCloseOperation(EXIT_ON_CLOSE);

		
		setVisible(true);

	}

	JTextField textField = new JTextField();

}
