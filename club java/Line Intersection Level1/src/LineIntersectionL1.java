public class LineIntersectionL1 {
    public static void main(String[] args) {
        Point p1 = new Point(1, 2);
        Point p2 = new Point(2, 3);
        Point p3 = new Point(-1, -1);
        Point p4 = new Point(2, 2);

        Line line1 = new Line(p1, p2);
        Line line2 = new Line(p3, p4);
        Line line3 = new Line(p1, p4);
        Line line4 = new Line(p3, p2);

        System.out.println(isLineIntersection(line1, line2)); // false
        System.out.println(isLineIntersection(line1, line3)); // true
        System.out.println(isLineIntersection(line2, line1)); // false
        System.out.println(isLineIntersection(line4, line4)); // false
        System.out.println(isLineIntersection(line3, line4)); // true
    }

    /**
     * Purpose: Find if two line intersect (meet and cross)
     *        : Assume line has infinite length
     * Parameter: Line line1 - a line of two Points with infinite length
     *          : Line line2 - a line of two Points with infinite length
     * Returns: boolean -  true if line intersect. Otherwise false
     * Pre-Condition: a line has infinite length
     * Post-Condition: none
     **/
    public static boolean isLineIntersection(Line line1, Line line2) {
        Point a1 = line1.getA();
        Point b1 = line1.getB();
        Point a2 = line2.getA();
        Point b2 = line2.getB();

        double slope1 = (b1.getY() - a1.getY()) / (b1.getX() - a1.getX());
        double slope2 = (b2.getY() - a2.getY()) / (b2.getX() - a2.getX());

        return !(slope1 == slope2);
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

class Line {
    private Point a;
    private Point b;
    public Line(Point a, Point b) {
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
