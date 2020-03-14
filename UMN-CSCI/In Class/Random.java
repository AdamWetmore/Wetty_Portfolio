// wetmo029
public class Random {

	int p1;
	int p2;
	int m;
	int seed;

	public Random(int p1Value, int p2Value, int mValue) {
		this.p1 = p1Value; // large prime numbers to simulate randomization
		this.p2 = p2Value;
		this.m = mValue; // max value
	} // Random method

	public void setSeed(int seed) {
		this.seed = seed; // allows more randomization without changing objects
	} // setSeed method

	public int getSeed() {
		return seed;
	} // getSeed method

	public int getMaximum() {
		return m;
	} // getMaximum method

	public int random() {

		int rNew = ((p1 * seed) + p2) % m;
		this.seed = rNew;
		return seed; // value ranging from 0 to m
	} // random method

	public int randomInteger(int low, int high) {
		if (low > high) {
			int temp;
			temp = low;
			low = high;
			high = temp;
		} // allows input error with user inputing high then low

		int lowerBound = low;
		int upperBound = high;
		double multiplier = ((double) (upperBound - lowerBound) / (m - 1)); // scalar value that will change range from 0 to upper - lower
		int randomNumber = random();
		double newRandom = randomNumber * multiplier;
		newRandom += lowerBound; // changes range to lower to upper
		return (int) newRandom;
	} // randomInteger method

	public boolean randomBoolean() {

		if ((random() % 2) == 0) { return true; }  // modular division allows for 50/50 distribution
		else { return false; }
	} // randomBoolean method

	public double randomDouble(double low, double high) {
		if (low > high) {
			double temp;
			temp = low;
			low = high;
			high = temp;
		}

		double lowerBound = low;
		double upperBound = high;
		double multiplier = ((double) (upperBound - lowerBound) / (m - 1));
		int randomNumber = random();
		double newRandom = (double) randomNumber * multiplier;
		newRandom += lowerBound;
		return newRandom;
	} // randomDouble method

	public static void main(String[] args) {

		// Test cases

		// Multiple random number objects will be instantiated
		Random R1 = new Random(15427, 33581, 4423);
		Random R2 = new Random(9697, 11701, 9803);
		Random R3 = new Random(15307, 4493, 21193);

		// setSeed method will be shown
		System.out.println("Seeds\n\nUse of the setSeed method can be shown here,\n\nOrginal seed:  " + R2.getSeed());
		R2.setSeed(1200);
		System.out.println("getSeed() is run\nNew Seed:  " + R2.getSeed() + "\n\n");

		// Testing randomInteger method
		System.out.println("Integers\n\nAn 10 index long array where each index represents a digit between 1 and 9 will be\npopulated by incrementing the index everytime the number appears\nthe value in each index will then be divided to find it's frequency\nthat value will be represented by a percentage.\n");
		int[] integers = new int[10];
		for (int i = 0; i < 10000; i++) {
			int randomValue = R1.randomInteger(0, 9);
			integers[randomValue]++;
		}

		for (int index = 0; index < integers.length - 1; index++) {
			System.out.println("Number:  " + (index + 1));
			int value = integers[index];
			int percentage = value / 100;
			System.out.println("Percentage of values:  " + percentage + "\n");
		}

		// Testing randomBoolean method
		System.out.println("\nBooleans\n\n100 random booleans will be generated and recorded, the percentages of trues\nand falses will be displayed\n");
		int[] booleans = new int[2];
		for (int i = 0; i < 100; i++) {
			boolean randBoolean = R2.randomBoolean();
			if (randBoolean == true) {
				booleans[0]++;
			} else {
				booleans[1]++;
			}

		}
		int numTrue = booleans[0];
		int numFalse = booleans[1];
		System.out.println("Using R2\n\nPercentage of trues:  " + numTrue + "\n\nPercentage of false:  " + numFalse + "\n\n");

		booleans[0] = 0;
		booleans[1] = 0;
		for (int i = 0; i < 100; i++) {
			boolean randBoolean = R3.randomBoolean();
			if (randBoolean == true) {
				booleans[0]++;
			} else {
				booleans[1]++;
			}

		}
		numTrue = booleans[0];
		numFalse = booleans[1];
		System.out.println("Using R3\n\nPercentage of trues:  " + numTrue + "\n\nPercentage of false:  " + numFalse);

		System.out.println("\n\nDoubles\n\na selection of doubles between 0.0 and 10.0 will be printed out. Then, a\nsimilar way of recording values as randomInteger will be used to show the \ndistribution of values.\n");
		for (int j = 0; j < 10; j++) {
			System.out.println(R1.randomDouble(0.0,10.0));
		}

		int[] doubles = new int[5];
		for (int i = 0; i < 10000; i++) {
			double randDouble = R3.randomDouble(0.0,10.0);
			if (randDouble < 2) { doubles[0]++; }
			else if (randDouble < 4) { doubles[1]++; }
			else if (randDouble < 6) { doubles[2]++; }
			else if (randDouble < 8) { doubles[3]++; }
			else if (randDouble < 10) { doubles[4]++; }
		}
		int number = 2;
		for (int index = 0; index < doubles.length; index++) {
			int value = doubles[index];
			int percentage = value / 100;
			System.out.println("\nPercentage of values below " + number + ": " + percentage);
			number += 2;
		}
	} // main method
} // Random class

