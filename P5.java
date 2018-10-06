public class P5 {

    public static void main(String args[]) {

        int i = 20;
        boolean found = false ;
        while (!found) {
            for (int j=2; j<=20; j++){
                if (i%j == 0) {
                    found = true;
                    continue;
                }
					else {
                    found = false;
                    break;
                }
            }
            if (found)  System.out.print(i);

            i++;
        }

    }
}
