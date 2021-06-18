class DuplicateZeros {
    public void duplicateZeros(int[] arr) {
        System.out.println("Called");

        int[] temp = new int[arr.length];
        int n = 0;
        int i = 0;

        while (n < arr.length) {
            if (arr[i] == 0) {
                n++;
                arr[i+1] = 0;
            }

            n++;
            i++;
        }

        System.out.println("arr in function:");
        for (int a : arr) {
            System.out.print(a + ", ");
        }
    }

    public static void main(String[] args) {
        int[] numbers = new int[]{1, 0, 2, 3, 0, 4, 5, 0};

        new DuplicateZeros().duplicateZeros(numbers);

        System.out.println("");

        System.out.println("arr in main:");
        for (int n : numbers) {
            System.out.print(n + ", ");
        }
    }
}
