/* Labb 2 i DD1352 Algoritmer, datastrukturer och komplexitet    */
/* Se labbanvisning under kurssidan http://www.csc.kth.se/DD1352 */
/* Ursprunglig författare: Viggo Kann KTH viggo@nada.kth.se      */
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;

public class Main {

  public static List<String> readWordList(BufferedReader input) throws IOException {
    LinkedList<String> list = new LinkedList<String>();
    while (true) {
      String s = input.readLine(); //read the input till # occurs
      if (s.equals("#"))
        break;
      list.add(s);
    }
    return list;
  }

  public static void main(String args[]) throws IOException {
    //    long t1 = System.currentTimeMillis();
    BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in, "UTF-8"));//InputStreamReader reads bytes and decodes them into characters using a specified charset.
    // Säkrast att specificera att UTF-8 ska användas, för vissa system har annan
    // standardinställning för teckenkodningen.
	//The safest way to specify that UTF-8 is used, for some systems have different default character encoding.
    List<String> wordList = readWordList(stdin);
    String word;
    while ((word = stdin.readLine()) != null) {
      ClosestWords closestWords = new ClosestWords(word, wordList); //(Misspelledword, word from dictionary)
      System.out.print(word + " (" + closestWords.getMinDistance() + ")");
      for (String w : closestWords.getClosestWords())
        System.out.print(" " + w);
      System.out.println();
    }
    //    long tottime = (System.currentTimeMillis() - t1);
    //    System.out.println("CPU time: " + tottime + " ms");

  }
}
