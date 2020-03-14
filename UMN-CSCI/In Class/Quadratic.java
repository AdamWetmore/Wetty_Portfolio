// wetmo029
public class Quadratic {

	float aValue;
	float bValue;
	float cValue;
	
	public Quadratic(float a, float b, float c) {

		this.aValue = a;
		this.bValue = b; // coefficients in ax^2 + bx + c  form
		this.cValue = c;
	} // Quadratic method

	
	public Quadratic add(Quadratic other) {

		float newAValue = this.aValue + other.aValue;
		float newBValue = this.bValue + other.bValue; // Determines values for sum
		float newCValue = this.cValue + other.cValue;

		Quadratic result = new Quadratic(newAValue,newBValue,newCValue); // Instantiates new object using sums values
		return result;
	} // add class


	public Quadratic subtract(Quadratic other) {

		float newAValue = this.aValue - other.aValue;
		float newBValue = this.bValue - other.bValue; // Determines values for difference
		float newCValue = this.cValue - other.cValue;

		Quadratic result = new Quadratic(newAValue,newBValue,newCValue); // Instantiates new object using difference values
		return result;
	} // subtract class

	public Roots findRoots() {

		Roots result = new Roots(aValue,bValue,cValue);
		return result;
	} // findRoots method


	public String toString() {

		String s = aValue + "x**2 "; // leading coefficient will be placed in front of its term

		if (bValue < 0) { // determines if bValue is negative
			s = s + "- " + (bValue * -1); // prevents output from being "x - -2.0"
		}
		else { // bValue must be positive
			s = s + "+ " + bValue;
		}
		s = s + "x ";

		if (cValue < 0) { // once again determines sine of coefficient
			s = s + "- " + (cValue * -1);
		}
		else {
			s = s + "+ " + cValue;
		}
		return s;
	} // toString method

	// getter methods
	public float getAValue() {
		return aValue;
	}

	public float getBValue() {
		return bValue;
	}

	public float getCValue() {
		return cValue;
	}


	public boolean equals(Object other) {
		Quadratic temp; // will allow object to be cast as a Quadratic if need be
		if (other instanceof Quadratic) {
			temp = (Quadratic) other;
			if ((this.aValue - temp.getAValue()) < .0001 && (this.bValue - temp.getBValue()) < .0001 && (this.cValue - temp.getCValue()) < .0001) { // Determines if the difference in the floats is roughly zero
				if ((this.aValue - temp.getAValue()) > -.0001 && (this.bValue - temp.getBValue()) > -.0001 && (this.cValue - temp.getCValue()) > -.0001) { // In case the difference is negative
					return true;
				}
			}
		}
		return false;
	} // equals method

	public static void main(String[] args) {

		// Test Cases

		Quadratic Q1 = new Quadratic(1,2,3);
		Quadratic Q2 = new Quadratic(-2,2,-2);
		Quadratic Q3 = new Quadratic(1,2,3);
		Quadratic Q4 = new Quadratic(-6,12,-6);
		// testing the constructer and toString methods
		System.out.println("\n4 Quadratic objects have been instantiated using this classes constructor method\nThey will be represented in string form as follows\n\nQ1:  " + Q1 + "\n\nQ2:  " + Q2 + "\n\nQ3:  " + Q3 + "\n\nQ4:  " + Q4 + "\n\n");
		// testing the add method
		System.out.println("The add method will be used to add multiple objects,\n\nQ1 + Q2: (Q1.add(Q2))\n\n" + Q1.add(Q2) + "\n\nQ3 + Q4:  (Q3.add(Q4))\n\n" + Q3.add(Q4) + "\n\nand Q1 + Q2 + Q3:  (Q1.add(Q2.add(Q3)))\n\n" + Q1.add(Q2.add(Q3)) + "\n\n");
		System.out.println("It can be seen that the commutative property is followed with this method \nif the following functions are executed,\n\nQ2 + Q1:  (Q2.add(Q1))\n\n" + Q2.add(Q1) + "\n\nand Q4 + Q3:  (Q4.add(Q3))\n\n" + Q4.add(Q3));
		// testing the subtract method
		System.out.println("\n\nThe same process will be followed with the subtract method. Obviously,\nthe commutative property will not be followed. This will be shown,\n\nQ2 - Q3:\n\n" + Q2.subtract(Q3) + "\n\nQ3 - Q2:\n\n" + Q3.subtract(Q2) + "\n\nand Q3 - (Q2 - Q1):\n\n" + Q3.subtract(Q2.subtract(Q1)));
		// testing the findRoots method
		System.out.println("\n\nThe Roots class alongside the Complex4 class will be used to determine\nand return the zeroes of the quadratic function\n\nQ1:  " + Q1.findRoots() + "\n\nQ2:  " + Q2.findRoots() + "\n\nQ3:  " + Q3.findRoots() + "\n\nQ4:  " + Q4.findRoots());
		// testing the equals method
		System.out.println("\n\nThe equals method will be used to show whether or not different objects\nof the Quadratic class as well as others are equal to eachother.\n\nQ1 == Q2  -->  " + Q1.equals(Q2) + "\n\nQ1 == Q3  -->  " + Q1.equals(Q3) + "\n\nQ4 == Q4  -->  " + Q4.equals(Q4) + "\n\nQ4 == Q4's roots  -->  " + Q4.equals(Q4.findRoots()) + "\n*Since Roots is a different class there is no way they can be equal");
		// testing the getter methods
		System.out.println("\n\nLastly, the getters will be shown.\n\nQ1's A value:  " + Q1.getAValue() + "\n\nQ3's B value:  " + Q3.getBValue() + "\n\nQ4's C value:  " + Q4.getCValue());
	} // main method
} // Quadratic class

