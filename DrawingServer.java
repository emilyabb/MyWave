
/*
* lots of code copied from http://personalwebs.coloradocollege.edu/~mwhitehead/courses/2011/CP341_MobileComp/Assignments/1/1.html
* some help from http://sharkysoft.com/tutorials/jsa/content/037.html
*/



import java.net.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.Toolkit;

public class DrawingServer extends JFrame{

	BufferedReader br;

	public static void main(String[] args){
	
		DrawingServer ds = new DrawingServer();
		ds.go();
	}

// bicu@578#@

	public void go(){
		int port = 6060;

		//listen for connections
		SocketServer my_server = new SocketServer(port);

		//connection		
		Socket my_socket = my_server.accept();

		//send screen size
		Toolkit tk = Toolkit.getDefaultToolkit();
		PrintWriter pw = new PrintWriter(new OutputStream(my_socket.getOutputStream()));
		pw.print(tk.getScreenSize().width + " " + pw.print(tk.getScreenSize().height);

		//BufferedReader
		BufferedReader br = new BufferedReader(new InputStreamReader(mySocket.getInputStream()));

		this.repaint();

		}
	}

	public void paintComponent(Graphics g) {
		super.paintComponent(g);  //without this no background color set

		String line = br.readLine();
		while (line != null){
			String[] ars = line.split(" ");

			g2d.setColor(new Color(Integer.toInt(ars[5]), Integer.toInt(ars[6]), Integer.toInt(ars[7])));

			int x1 = Integer.toInt(ars[1]);
			int y1 = Integer.toInt(ars[2]);
			int width = Integer.toInt(ars[3]) - x1;
			int height = Integer.toInt(ars[4]) - y1;


			if (ars[0].compareToIgnoreCase("line") == 0)			
				g.drawLine(x1,y1, Integer.toInt(ars[3]), Integer.toInt(ars[4]));

			else if (ars[0].compareToIgnoreCase("rect") == 0)
				g.drawRect(x1,y1,width,height);

			else if (ars[0].compareToIgnoreCase("rectf") == 0)
				g.fillRect(x1,y1,width,height);

			else if (commands[0].compareToIgnoreCase("ellipse") == 0)
				g.drawOval(x1,y1,width,height);

			else if (commands[0].compareToIgnoreCase("ellipsef") == 0)
				g.fillOval(x1,y1,width,height);

			else if (commands[0].compareToIgnoreCase("point") == 0)
				g.drawLine(x1,y1,x1,x2);
		}
}



