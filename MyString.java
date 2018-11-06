import java.util.Arrays;

class MyString {

	public static void main(String args[]){

		String s1="abc";
		String s2="def";
		s1 = s2;
		s1 = "changed";

		System.out.println("s1, s2 " + s1 + "," + s2);

		MyString mystr = new MyString();
		int[] input = new int[]{1,2,3,4,5,6};
		System.out.println("Input " + Arrays.toString(input));
		int[] output = mystr.swap(input);
		System.out.println("Output" + Arrays.toString(output));

	}

	public int[] swap(int[] input){

		int j = input.length - 1 ;
		for (int i=0; i < j ; i++){
			int temp = input[i];
			input[i] = input[j];
			input[j]=temp;
		}

		return input;

	}


}

