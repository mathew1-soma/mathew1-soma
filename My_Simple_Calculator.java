import java.util.Scanner;

public class My_Simple_Calculator {
	
	static void Add() {
		
	}

	public static void main(String[] args) {
		
		//introducing the variables
		double x, y;
		int operation;
		Scanner n = new Scanner(System.in);
		
		//input for x value
		System.out.println("Enter the first value: ");
		x = n.nextDouble();
		
		//user input for y value
		System.out.println("Enter the second value: ");
		y = n.nextDouble();
		
		//list of operations to choose from
		System.out.println("\n");
		System.out.println("AVAILABLE OPERATIONS");
		System.out.println("1. Addition");
		System.out.println("2. Substruction");
		System.out.println("3. Multiplication");
		System.out.println("4. Division");
		System.out.println("\n");
		
		//user input for operations
		System.out.println("Please choose operation: ");
		operation = n.nextInt();
		
		switch(operation) {
		case 1:
			double sum = x + y;
			System.out.println(x +" + " +y+ " = "+ sum);
			break;
			
		case 2:
			double sub = x - y;
			System.out.println(x +" - " +y+ " = "+ sub);
			break;
			
		case 3:
			double mult = x * y;
			System.out.println(x +" * " +y+ " = "+ mult);
			break;
			
		case 4:
			double div = x / y;
			System.out.println(x +" / " +y+ " = "+ div);
			break;
			
		default:
			System.out.println("invalid input");
			
						
		}

	}

}
