import java.util.Scanner;

public class SimpleCalculator {
	public static int x;
	public static float y;
	
	static void Sum() {
		double sum = x + y;
		System.out.println(x +" + " +y+ " = "+ sum);
	}
	
	public void Sub() {
		double sub = x - y;
		System.out.println(x +" - " +y+ " = "+ sub);
	}
	
	public void Multiply() {
		double mult = x * y;
		System.out.println(x +" * " +y+ " = "+ mult);
	}
	
	public void Divide() {
		double div = x/y;
		System.out.println(x +" / " +y+ " = "+ div);
	}
	
public static void main(String[] args) {
		
		Scanner n = new Scanner(System.in);
		
		System.out.println("Enter the value of x: ");
		x = n.nextInt();
		
		System.out.println("Enter the value of y: ");
		y = n.nextFloat();
	
		SimpleCalculator s = new SimpleCalculator();
		s.Sum();
		s.Sub();
		s.Multiply();
		s.Divide();
		
		}
	

}
