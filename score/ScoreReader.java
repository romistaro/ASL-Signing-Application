package score;
import java.io.*;

public class ScoreReader {
    private String filePath;

    public ScoreReader(String filePath) {
        this.filePath = filePath;
    }

    public Score getScore() {
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line = reader.readLine();
            int scoreValue = Integer.parseInt(line);
            return new Score(scoreValue);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static class Score {
        private int value;

        public Score(int value) {
            this.value = value;
        }

        public int getValue() {
            return value;
        }
    }
}
