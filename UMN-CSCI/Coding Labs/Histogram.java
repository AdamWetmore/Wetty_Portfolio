import java.util.Scanner;

public class Histogram {

	int[] histogram;
	int lowerBound;
	int upperBound;

	 

	public Histogram(int lowerBound, int upperBound) {

		if (lowerBound > upperBound) {
			this.lowerBound = upperBound;
			this.upperBound = lowerBound;
		}

		else {
			this.lowerBound = lowerBound;
			this.upperBound = upperBound;
		}

		this.histogram  = new int[this.upperBound - this.lowerBound + 1];
	}


	public boolean add(int i) {

		if (i > (lowerBound - 1) && i < (upperBound + 1)) {
			histogram[(i - lowerBound)] += 1;
			return true;
		}

		else {
			System.out.println("ERROR: Entry not within range");
			return false;
		}
	}


	public String toString() {

		String graph = "";
		for (int i = 0; i < histogram.length; i++) {
			graph = graph + (i + lowerBound) + ": "; //creates the header of each number in the range
			for (int j = 0; j < histogram[i]; j++) {
				graph = graph + "*";    //records instance of i in the dataset
			}
			graph = graph + "\n";    //starts next line
		}
		return graph;
	}

	public static void main(String[] args) {

		Scanner s = new Scanner(System.in);
		System.out.print("Enter a lower and upper bound for your histogram: ");
		int lowerBound = s.nextInt();
		int upperBound = s.nextInt();
		String choice;
		Histogram h1 = new Histogram(lowerBound, upperBound);
		boolean state1 = true;
		boolean state2 = true;
		while (state1 == true) {
			choice = s.nextLine();
			if (choice.equals("add")) {
				while (state2 == true) {
					System.out.print("Enter data: ");
					int number = s.nextInt();
					if (h1.add(number) == false) {
						state2 = false;
					}
				}
				state2 = true;
			}
				else if (choice.equals("print")) {
					System.out.print(h1);
				}
				else if (choice.equals("quit")) {
				state1 = false;
			}
		}
		System.out.println("Goodbye");
	}
}

