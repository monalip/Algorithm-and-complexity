/* Labb 2 i DD1352 Algoritmer, datastrukturer och komplexitet    */
/* Se labbanvisning under kurssidan http://www.csc.kth.se/DD1352 */
/* Ursprunglig författare: Viggo Kann KTH viggo@nada.kth.se      */
import java.util.ArrayList;
import java.util.List;

public class ClosestWords {
  ArrayList<String> closestWords = new ArrayList<String>();

  int closestDistance = 50;
  int count=1; 
  int res,i,j;
  int addLetter;
  int deleteLetter;
  private String lastWord = "";
  private int M[][];
  int partDist(String w1, String w2, int w1len, int w2len) {
	//if words are same return 0
	  if(w1.equals(w2))
		  return 0;
	  // if length difference more than the already found closest distance then skip thta word and move for next word
	  int length_diff =Math.abs(w1len - w2len);
	  if(length_diff > closestDistance)
		  return length_diff;
	  // if first p letters are same then start calculating matrix at pIndex
	  int PIndex =0;
	  while(lastWord.length() > PIndex && w2len > PIndex && lastWord.charAt(PIndex) == w2.charAt(PIndex))
	  {
		  PIndex++;
	  }
	 
		for(j=1+PIndex;j<=w2len;j++)
		{
			boolean val = true;
			for(i=1;i<=w1len;i++)
			{
				//substitution if the letter is not same and if voth the letter are same we do nothing
				res=M[i-1][j-1] + (w1.charAt(i - 1) == w2.charAt(j - 1) ? 0 : 1);
				//addletter
				addLetter=M[i-1][j] + 1;
				if(addLetter < res)
					res = addLetter;
				deleteLetter = M[i][j-1] + 1;
				if(deleteLetter < res)
					res = deleteLetter;
				M[i][j]=res;
				if(M[i][j] <= closestDistance)
				{
					val = false;
				}
				
			}
			if(val)
				return closestDistance + 1;
		}
		lastWord = w2;
		return M[w1len][w2len];
  }

  int Distance(String w1, String w2) {//misspelled word and dictionary word Calculate the minimum distance
	  
	 
    return partDist(w1, w2, w1.length(), w2.length()); //partDist(ma,maska,2,5)
     
  }

  public ClosestWords(String w, List<String> wordList) {//input word and list of words passed as parameter
	  M = new int [w.length()+1][41];
	  for(int i=0;i<=w.length();i++)
	  {
		  M[i][0]=i;
		  
	  }  
  
	 for(int i=0;i<41;i++)
	  {
		  M[0][i]=i;
	  }
		  
	  for (String s : wordList) {

	      int dist = Distance(w, s);
	      //System.out.println("d(" + w + "," + s + ")=" + dist);
	      if (dist < closestDistance || closestDistance == 50) {
	        closestDistance = dist;
	        closestWords.clear();
	        closestWords.add(s);
	      }
	      else if (dist == closestDistance)
	        closestWords.add(s);
	      if(dist == 0)
	        break;
	    }
	  }

  int getMinDistance() {
    return closestDistance;
  }

  List<String> getClosestWords() {
    return closestWords;
  }
}
