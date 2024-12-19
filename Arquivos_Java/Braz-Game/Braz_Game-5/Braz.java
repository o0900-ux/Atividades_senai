import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.util.Properties;

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
    private static boolean chaveVerificada = false; 

    // Chave de ativação
    private static final String CHAVE_ATIVACAO = "HJUY3RT5Y6RT0POGQWER9IUYT";

    private static final String PROP_FILE = "config.properties";
    private static final String CHAVE_VERIFICADA_PROP = "chave_verificada";

    // Variáveis para controle do pulo duplo
    private long lastJumpPressTime = 0;
    private static final long DOUBLE_PRESS_DELAY = 300; // Tempo em milissegundos
    private boolean doubleJumpAvailable = false;

    public Braz() {
        super("Braz");
        setSize(WIDTH, HEIGHT);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        carregarPropriedades(); 
        if (!chaveVerificada) {
            verificarChaveAtivacao();
        }

        // Adicionando instruções do jogo
        exibirInstrucoes();

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
                    handleJump();
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

    private void verificarChaveAtivacao() {
        String chaveInserida = JOptionPane.showInputDialog(null, "Insira a chave de ativação:");
        chaveInserida = chaveInserida.replaceAll("-", "");
        if (chaveInserida != null && chaveInserida.equals(CHAVE_ATIVACAO)) {
            chaveVerificada = true;
            salvarPropriedade(CHAVE_VERIFICADA_PROP, "true"); 
        } else {
            JOptionPane.showMessageDialog(null, "Chave de ativação inválida. Tente novamente.");
            System.exit(0);
        }
    }

    private void carregarPropriedades() {
        Properties prop = new Properties();
        try (InputStream input = new FileInputStream(PROP_FILE)) {
            prop.load(input);
            String chaveVerificadaStr = prop.getProperty(CHAVE_VERIFICADA_PROP);
            chaveVerificada = Boolean.parseBoolean(chaveVerificadaStr);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    private void salvarPropriedade(String chave, String valor) {
        Properties prop = new Properties();
        try (OutputStream output = new FileOutputStream(PROP_FILE)) {
            prop.setProperty(chave, valor);
            prop.store(output, null);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    private void exibirInstrucoes() {
        String instrucoes = "Instruções do Jogo:\n" +
                "1. Use a barra de espaço para pular.\n" +
                "2. Pressione a barra de espaço duas vezes rapidamente para um pulo duplo.\n" +
                "3. Evite os obstáculos que vêm em sua direção.\n" +
                "4. Pressione 'M' para pausar o jogo.\n" +
                "5. Pressione 'C' para alternar entre modos.\n\n" +
                "Boa sorte!";
        JOptionPane.showMessageDialog(this, instrucoes, "Instruções do Jogo", JOptionPane.INFORMATION_MESSAGE);
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
        doubleJumpAvailable = false; // Reinicia a opção de pulo duplo
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

    private void handleJump() {
        long currentTime = System.currentTimeMillis();
        if (playerY == HEIGHT - PLAYER_SIZE) {
            playerDY = -15; // Pulo normal
            doubleJumpAvailable = true; // Permite o pulo duplo
            lastJumpPressTime = currentTime; // Atualiza o tempo do último pulo
        } else if (doubleJumpAvailable && currentTime - lastJumpPressTime <= DOUBLE_PRESS_DELAY) {
            playerDY = -15; // Pulo duplo
            doubleJumpAvailable = false; // Desabilita o pulo duplo
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
            doubleJumpAvailable = false; // Reseta o pulo duplo quando o jogador toca o chão
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
