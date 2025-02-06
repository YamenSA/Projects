package methods;

import java.io.File;
import java.util.Scanner;

import javax.swing.ImageIcon;
import javax.swing.JFrame;

public class Main {

	public static void main(String[] args) {

		// JFrame = a GUI window to add components to

		// creates a frame
		JFrame frame = new JFrame();

		// setting size
		frame.setSize(500, 500);
		// sets title of frame
		frame.setTitle("Calculator");
		// exist out of application
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		// make frame visible
		frame.setVisible(true);

		// creates an Icon for the frame, upper left corner
		ImageIcon image = new ImageIcon("calculator.png");
		
		//change the Icon of the frame
		frame.setIconImage(image.getImage()); 

		Scanner input = new Scanner(System.in);

		

		File file = new File("calculator.png");
		if (!file.exists()) {
		    System.out.println("❌ Bild nicht gefunden: " + file.getAbsolutePath());
		} else {
		    System.out.println("✅ Bild gefunden: " + file.getAbsolutePath());
		}

		
		
//		int ersteZahl = input.nextInt();
//		int zweiteZahl = input.nextInt();

//		Calculate cal = new Calculate(ersteZahl, zweiteZahl);

	}

}
