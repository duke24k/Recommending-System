import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.text.DecimalFormat;
import java.util.Random;

public class DataGen {
	public static void main(String[] args) throws IOException{
		Random random = new Random();
		File file = new File("data3.txt");
		if(!file.exists()){
			file.createNewFile();
		}
		PrintWriter pw = new PrintWriter(file);
		StringBuilder data = new StringBuilder();
		String[] edu_level = {"B.S.", "Freshman", "Sophemore", "Junior", "Senior", "M.S", "M.A", "M.E"};
		String[] industry = {"Retail/management", "Economic", "Business", "Art/psychology", "Social work", "IT/Engineering", "undeclared"};
		DecimalFormat df = new DecimalFormat("#.#");
		
//		double num;
		System.out.println("------");
		for(int i = 0; i < 200; i++){
			for(int j = 0; j < 28; j++){
				if(j < 6){
					data.append(String.valueOf(Math.round(getNum(random.nextGaussian() * 2 + 7, 10))));
					data.append("|");
				}else if(j < 19){
					data.append(String.valueOf(df.format(getNum(((random.nextGaussian() + 3) / 4.0), 1))));
					data.append("|");
				}else if(j < 25){
					data.append(String.valueOf(Math.round(getNum(random.nextGaussian() * 5 + 23, 30))));
					data.append("|");
				}else if(j == 25){
					data.append(edu_level[random.nextInt(edu_level.length)]);
					data.append("|");
				}else if(j == 26){
					data.append(industry[random.nextInt(industry.length)]);
					data.append("|");
				}else{
					data.append(String.valueOf(Math.round(getNum(random.nextGaussian() * 2 + 5, 6))));
					data.append("\n");
				}
			}
		}
		pw.write(data.toString());
		pw.close();
	}
	public static double getNum(double num, int max){
		if(num > max)
			return (double)max;
		if(num < 0)
			return 0;
		return num;
	}
}
