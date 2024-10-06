import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        String rock = """
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """;

        String paper = """
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """;

        String scissors = """
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """;

        System.out.println("Welcome to the Rock Paper Scissors game!");
        System.out.println("-".repeat(80));
        System.out.println("Here are your choices:");
        System.out.println("r: Rock");
        System.out.println("p: Paper");
        System.out.println("s: Scissors");

        Scanner scanner = new Scanner(System.in);

        List<String> possibleChoices = Arrays.asList("r", "p", "s");
        String userSelectedMove = "";

        while (!possibleChoices.contains(userSelectedMove)) {
            System.out.println("What is your choice? (r/p/s): ");
            userSelectedMove = scanner.next().toLowerCase();
            if (!possibleChoices.contains(userSelectedMove)) {
                System.out.println("Invalid move. Please try again.");
            }
        }

        String computerSelectedMove = possibleChoices.get(new Random().nextInt(possibleChoices.size()));

        if (userSelectedMove.equals(computerSelectedMove)) {
            System.out.println("your move: " + userSelectedMove);
            System.out.println("computer move: " + computerSelectedMove);
            System.out.println("It's a tie :|");
        } else if (userSelectedMove.equals("r")) {
            processGame(rock, paper, scissors, "s", "p", computerSelectedMove);
        } else if (userSelectedMove.equals("p")) {
            processGame(paper, rock, scissors, "r", "s", computerSelectedMove);
        } else if (userSelectedMove.equals("s")) {
            processGame(scissors, paper, rock, "p", "r", computerSelectedMove);
        }
    }

    private static void processGame(String userMoveArt, String winningArt, String losingArt, 
                                    String winningMove, String losingMove, String computerSelectedMove) {
        if (computerSelectedMove.equals(winningMove)) {
            System.out.println("your move:");
            System.out.println(userMoveArt);
            System.out.println("computer move: " + computerSelectedMove);
            System.out.println(winningArt);
            System.out.println("You won :)");
        } else if (computerSelectedMove.equals(losingMove)) {
            System.out.println("your move:");
            System.out.println(userMoveArt);
            System.out.println("computer move: " + computerSelectedMove);
            System.out.println(losingArt);
            System.out.println("You loose :(");
        }
    }
}