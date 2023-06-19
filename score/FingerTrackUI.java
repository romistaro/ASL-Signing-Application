import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class FingerTrackUI {
    private JFrame frame;
    private JLabel welcomeLabel;
    private JTextField secondsTextField;

    public FingerTrackUI(String username) {
        frame = new JFrame("FingerTracker");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300); // Adjusted window size
        frame.setLayout(new BorderLayout());

        welcomeLabel = new JLabel("Welcome, " + username + "!"); // Greet the user with the username
        welcomeLabel.setHorizontalAlignment(SwingConstants.CENTER);
        frame.add(welcomeLabel, BorderLayout.NORTH);

        JPanel contentPanel = new JPanel(new BorderLayout());
        frame.add(contentPanel, BorderLayout.CENTER);

        JLabel promptLabel = new JLabel("<html>Enter the amount of seconds you would like between each letter shown!</html>");
        promptLabel.setHorizontalAlignment(SwingConstants.CENTER);
        promptLabel.setPreferredSize(new Dimension(350, 50)); // Adjusted preferred size
        contentPanel.add(promptLabel, BorderLayout.NORTH);

        secondsTextField = new JTextField();
        contentPanel.add(secondsTextField, BorderLayout.CENTER);

        JButton nextButton = new JButton("Next");
        nextButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                writeToFile();
                updateLabelText();
            }
        });
        frame.add(nextButton, BorderLayout.SOUTH);
    }

    private void writeToFile() {
        String currentDirectory = System.getProperty("user.dir");
        String folderPath = currentDirectory + File.separator + "FingerTracker";
        String filePath = folderPath + File.separator + "score.txt";

        int seconds = Integer.parseInt(secondsTextField.getText());
        try {
            File folder = new File(folderPath);
            if (!folder.exists()) {
                folder.mkdirs();
            }

            FileWriter writer = new FileWriter(filePath);
            writer.write(String.valueOf(seconds));
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void updateLabelText() {
        welcomeLabel.setText("Thank you for your input!");
        secondsTextField.setText("");
    }

    public void show() {
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            SwingUtilities.invokeLater(new Runnable() {
                public void run() {
                    FingerTrackUI ui = new FingerTrackUI(args[0]);
                    ui.show();
                }
            });
        } else {
            System.out.println("Please provide a username as an argument.");
        }
    }
}
