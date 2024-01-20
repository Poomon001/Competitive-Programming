public class LineIntersectionL1 {
    public static void main(String[] args) {
        Point p1 = new Point(1, 2);
        Point p2 = new Point(2, 3);
        Point p3 = new Point(-1, -1);
        Point p4 = new Point(2, 2);
        Point p5 = new Point(0, 0);
        Point p6 = new Point(1, 1);

        Segment s1 = new Segment(p1, p2);
        Segment s2 = new Segment(p3, p4);
        Segment s3 = new Segment(p1, p4);
        Segment s4 = new Segment(p6, p2);
        Segment s5 = new Segment(p1, p4);
        Segment s6 = new Segment(p4, p5);
        Segment s7 = new Segment(p3, p6);

        System.out.println(isLineIntersection(s1, s3)); // true -> meet bit not cross
        System.out.println(isLineIntersection(s2, s1)); // false -> parallel
        System.out.println(isLineIntersection(s4, s4)); // true -> meet (same line)
        System.out.println(isLineIntersection(s5, s4)); // true -> meet and cross
        System.out.println(isLineIntersection(s6, s7)); // true -> same line (diagonal)
        System.out.println(isLineIntersection(s1, s2)); // false -> parallel (diagonal)
    }

    /**
     * Purpose: Given two segments of two infinite lines. Find if the lines intersect (meet).
     *        : Assume line has infinite length
     * Parameter: Segment s1 - a segment containing two Points of an infinite line
     *          : Segment s2 - a segment containing two Points of an infinite line
     * Returns: boolean -  true if the two lines intersect. Otherwise false
     * Pre-Condition: a line has infinite length
     *              : Slope cannot be infinite
     * Post-Condition: none
     **/
    public static boolean isLineIntersection(Segment s1, Segment s2) {
        Point a1 = s1.getA();
        Point b1 = s1.getB();
        Point a2 = s2.getA();
        Point b2 = s2.getB();

        double slope1 = (b1.getY() - a1.getY()) / (b1.getX() - a1.getX());
        double slope2 = (b2.getY() - a2.getY()) / (b2.getX() - a2.getX());

        // check if they are the same line by check y-interception
        double yIn1 = yIntercept(s1, slope1);
        double yIn2 = yIntercept(s2, slope2);

        // check if they are the same line by check x-interception
        double xIn1 = xIntercept(s1, slope1);
        double xIn2 = xIntercept(s2, slope2);

        // parallel
        if(slope1 == slope2 && yIn1 != yIn2 && xIn1 != xIn2) {
            return false;
        }

        return true;
    }

    private static double yIntercept(Segment s1, double slope) {
        // y = mx + b
        double x = s1.getA().getX();
        double y = s1.getA().getY();
        double b = y - (slope * x);
        return b;
    }

    private static double xIntercept(Segment s1, double slope) {
        // y = mx + b
        double x = s1.getA().getX();
        double y = s1.getA().getY();
        double b = y - (slope * x);

        return -b / slope;
    }
}

class Point {
    private double x;
    private double y;
    public Point(double x, double y){
        this.x = x;
        this.y = y;
    }

    public double getX() {
        return this.x;
    }

    public double  getY(){
        return this.y;
    }
}

class Segment {
    private Point a;
    private Point b;
    public Segment(Point a, Point b) {
        this.a = a;
        this.b = b;
    }

    public Point getA() {
        return a;
    }

    public Point getB() {
        return b;
    }
}
