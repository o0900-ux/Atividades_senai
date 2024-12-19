import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Braz extends JFrame {
    private static final int WIDTH = 800;
    private static final int HEIGHT = 600;
    private static final int PLAYER_SIZE = 50;
    private static final int OBJECT_WIDTH = 50;
    private static final int OBJECT_HEIGHT = 20;
    private static final int INITIAL_OBJECT_SPEED = 5;
    private static final int SPEED_INCREASE_POINTS = 3;
    private static final int DISTANCE_DECREASE_POINTS = 3;

    private int playerX;
    private int playerY;
    private int playerDY;

    private int objectX;
    private int objectY;
    private int objectSpeed;

    private int score;

    private boolean gameOver;

    public Braz() {
        super("Braz");
        setSize(WIDTH, HEIGHT);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        initializeGame();

        JPanel gamePanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                draw(g);
            }
        };
        gamePanel.setPreferredSize(new Dimension(WIDTH, HEIGHT));

        gamePanel.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (!gameOver && e.getKeyCode() == KeyEvent.VK_SPACE) {
                    jump();
                } else if (gameOver && e.getKeyCode() == KeyEvent.VK_SPACE) {
                    initializeGame(); 
                }
            }
        });
        gamePanel.setFocusable(true);
        getContentPane().add(gamePanel);
        pack();

       
        new Thread(() -> {
            while (true) {
                if (!gameOver) {
                    update();
                }
                repaint();
                try {
                    Thread.sleep(20);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }).start();
    }

    private void initializeGame() {
        playerX = WIDTH / 2 - PLAYER_SIZE / 2;
        playerY = HEIGHT - PLAYER_SIZE;
        playerDY = 0;

        objectX = WIDTH;
        objectY = HEIGHT - OBJECT_HEIGHT;
        objectSpeed = INITIAL_OBJECT_SPEED;

        score = 0;
        gameOver = false;
    }

    private void draw(Graphics g) {
        
        g.setColor(Color.RED);
        g.fillRect(playerX, playerY, PLAYER_SIZE, PLAYER_SIZE);

      
        g.setColor(Color.BLUE);
        g.fillRect(objectX, objectY, OBJECT_WIDTH, OBJECT_HEIGHT);

 
        g.setColor(Color.BLACK);
        g.drawString("Pontuação: " + score, 10, 20);

        
        if (gameOver) {
            g.drawString("Game Over!", WIDTH / 2 - 50, HEIGHT / 2);
        }
    }

    private void jump() {
        if (playerY == HEIGHT - PLAYER_SIZE) {
            playerDY = -15;
        }
    }

    private void update() {
        
        playerY += playerDY;
        playerDY += 1;

        
        if (playerX + PLAYER_SIZE >= objectX && playerX <= objectX + OBJECT_WIDTH &&
                playerY + PLAYER_SIZE >= objectY && playerY <= objectY + OBJECT_HEIGHT) {
            gameOver = true;
        }

        objectX -= objectSpeed;

        if (objectX + OBJECT_WIDTH < 0) {
            objectX = WIDTH;
            score++; 

            
            if (score % SPEED_INCREASE_POINTS == 0) {
                objectSpeed++;
                if (score % (DISTANCE_DECREASE_POINTS * SPEED_INCREASE_POINTS) == 0) {
                    objectX -= 50;
                }
            }
        }

        
        if (playerY > HEIGHT - PLAYER_SIZE) {
            playerY = HEIGHT - PLAYER_SIZE;
            playerDY = 0;
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Braz game = new Braz();
            game.setVisible(true);
        });
    }
}