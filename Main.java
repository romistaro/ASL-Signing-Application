import java.util.Scanner;
import score.ScoreReader;
import score.FingerTrackUI;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the ASL Signing Test!");
        System.out.print("Enter your username: ");
        String username = scanner.nextLine();

        User user = new User(username);
        System.out.println("Hello, " + user.getUsername() + "!");

        System.out.print("Do you want to start the Test? (yes/no): ");
        String startGameInput = scanner.nextLine();

        if (startGameInput.equalsIgnoreCase("yes")) {
            
            System.out.println("Starting the test...");
            FingerTrackUI.main(username);
        } else {
            System.out.println("Goodbye!");
        }

        // Reading and displaying the score
        String filePath = "./FingerTracker/score.txt";
        ScoreReader scoreReader = new ScoreReader(filePath);
        ScoreReader.Score score = scoreReader.getScore();
        if (score != null) {
            int value = score.getValue();
            System.out.println("Your current score: " + value);
        } else {
            System.out.println("Failed to read the score.");
        }
        
        scanner.close();
    }
}
