import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Braz extends JFrame {
    private static final int WIDTH = 800;
    private static final int HEIGHT = 600;
    private static final int PLAYER_SIZE = 50;
    private static final int OBJECT_WIDTH = 50;
    private static final int OBJECT_HEIGHT = 20;
    private static final int NORMAL_INITIAL_OBJECT_SPEED = 5;
    private static final int NORMAL_SPEED_INCREASE_POINTS = 3;
    private static final int NORMAL_DISTANCE_DECREASE_POINTS = 3;
    private static final int EASY_INITIAL_OBJECT_SPEED = 7;
    private static final int EASY_SPEED_INCREASE_POINTS = 10;

    private int playerX;
    private int playerY;
    private int playerDY;

    private int objectX;
    private int objectY;
    private int objectSpeed;

    private int score;

    private boolean gameOver;
    private boolean mostrarPontuacao = true;
    private boolean pausado = false;
    private boolean easyMode = false;

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
                } else if (!gameOver && e.getKeyCode() == KeyEvent.VK_M) {
                    pausado = !pausado;
                } else if (!gameOver && e.getKeyCode() == KeyEvent.VK_C) {
                    toggleMode();
                }
                repaint();
            }
        });
        gamePanel.setFocusable(true);
        gamePanel.requestFocus();
        getContentPane().add(BorderLayout.CENTER, gamePanel);
        pack();

        new Thread(() -> {
            while (true) {
                if (!pausado) {
                    if (!gameOver) {
                        update();
                    }
                    repaint();
                }
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

        if (easyMode) {
            objectSpeed = EASY_INITIAL_OBJECT_SPEED;
        } else {
            objectSpeed = NORMAL_INITIAL_OBJECT_SPEED;
        }

        score = 0;
        gameOver = false;
    }

    private void draw(Graphics g) {

        g.setColor(Color.RED);
        g.fillRect(playerX, playerY, PLAYER_SIZE, PLAYER_SIZE);

        g.setColor(Color.BLUE);
        g.fillRect(objectX, objectY, OBJECT_WIDTH, OBJECT_HEIGHT);

        if (mostrarPontuacao) {
            g.setColor(Color.BLACK);
            g.setFont(new Font("Arial", Font.PLAIN, 15));
            g.drawString("Pontuação: " + score, 10, 20);

            if (easyMode) {
                g.drawString("NIVEL FACIL", 10, 40);
            }
        }

        if (gameOver) {
            g.setColor(Color.BLACK);
            g.setFont(new Font("Arial", Font.PLAIN, 20));
            g.drawString("Game Over!", WIDTH / 2 - 50, HEIGHT / 2);
        }

        if (pausado) {
            g.setColor(Color.RED);
            g.setFont(new Font("Arial", Font.PLAIN, 30));
            g.drawString("PAUSADO", WIDTH / 2 - 50, HEIGHT / 2);
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

            if (easyMode) {
                if (score % EASY_SPEED_INCREASE_POINTS == 0) {
                    objectSpeed++;
                }
            } else {
                if (score % NORMAL_SPEED_INCREASE_POINTS == 0) {
                    objectSpeed = NORMAL_INITIAL_OBJECT_SPEED + (score / NORMAL_SPEED_INCREASE_POINTS);
                    if (score % (NORMAL_SPEED_INCREASE_POINTS * NORMAL_DISTANCE_DECREASE_POINTS) == 0) {
                        objectX -= 50;
                    }
                }
            }
        }

        if (playerY > HEIGHT - PLAYER_SIZE) {
            playerY = HEIGHT - PLAYER_SIZE;
            playerDY = 0;
        }
    }

    private void toggleMode() {
        easyMode = !easyMode;
        initializeGame();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Braz game = new Braz();
            game.setVisible(true);
        });
    }
}

