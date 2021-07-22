import java.math.BigInteger;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
public class Main{
	public static void main(String[] args) throws IOException {
	BufferedReader buff=new BufferedReader(new InputStreamReader(System.in));
  String input[] = buff.readLine().split(" ");
  BigInteger money = new BigInteger(input[0]);
  BigInteger cr_cnt = new BigInteger(input[1]);
  if (money.signum()==1 && money.intValue() <= Math.pow(10, 10000) &&cr_cnt.intValue() <= Math.pow(10, 10000)&&cr_cnt.signum()==1) 
  {
    System.out.println(money.divide(cr_cnt));
    System.out.println(money.remainder(cr_cnt));
		}
	}
}
