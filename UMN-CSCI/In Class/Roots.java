// wetmo029
public class Roots {

    private Complex4 firstRoot;
    private Complex4 secondRoot;


    public Roots(float a, float b, float c) {
        double aValue = (double) a;
        double bValue = (double) b; // Coefficients in Qudratic Form (ax^2 + bx + c)
        double cValue = (double) c;
        double discriminantValue = (bValue * bValue) - (4 * aValue * cValue); // Value under radical in Quadratic formula (-b +/- sqrt(dV))/2a

        if (discriminantValue > 0) { // discriminantValue is positive
            firstRoot = new Complex4((-bValue + Math.sqrt(discriminantValue)) / (2 * aValue), 0); // Assigning plus or minus values according to Quadratic Formula
            secondRoot = new Complex4((-bValue - Math.sqrt(discriminantValue)) / (2 * aValue), 0); // Complex will be zero since it only has real roots
        } else if (discriminantValue < 0) { //discriminantValue is negative
            firstRoot = new Complex4((-bValue / (2 * aValue)), (Math.sqrt(discriminantValue * -1)) / (2 * a)); // Real part determined by -b/2a from Quadratic Formula
            secondRoot = new Complex4((-bValue / (2 * aValue)), -(Math.sqrt(discriminantValue * -1)) / (2 * a)); // Complex will be is determined by sqrt(discriminant)/2a
        } else { // discriminantValue == 0
            firstRoot = new Complex4((-bValue / (2 * aValue)), 0); // Both will have the same value since there is only one root
            secondRoot = new Complex4((-bValue / (2 * aValue)), 0);
        }
    } // Roots method

    public String toString() {
        String s = "First root: " + firstRoot + "\nSecond root: " + secondRoot; // "x + ni" form
        return s;
    } // toString method

    public static void main(String[] args) {

        // Test cases

            Roots R1 = new Roots(1,4,5); // 2 Complex roots
            Roots R2 = new Roots(-4,-2,8); // 2 Real roots
            Roots R3 = new Roots(2,4,2); // 1 Real root
            System.out.println("\n\nThe following is a string representation of the roots of the object R1 which, in \nquadratic form is x^2 + 4x + 5, it should havetwo complext roots since it \nnever crosses the x axis\n\n");
            System.out.println(R1);
            System.out.println("\n\nThis is the same string representation of R2 (-4x^2 - 2x + 8) it should have \ntwo real roots since it crosses the x axis twice\n\n");
            System.out.println(R2);
            System.out.println("\n\nThis is the same string representation of R3 (2x^2 + 4x + 2) it should have \njust one real root since it only touches the x axisonce. Both roots will be \nprinted but their values will be equal\n\n");
            System.out.println(R3);
        } // main method
    } // Roots class
