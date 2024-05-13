const firebaseConfig = {
    apiKey: "AIzaSyA3gOHi9Q6aHQ5seN5S9bbNmQpPQFMGXFs",
    authDomain: "magnus-c4b38.firebaseapp.com",
    projectId: "magnus-c4b38",
    storageBucket: "magnus-c4b38.appspot.com",
    messagingSenderId: "458576341456",
    appId: "1:458576341456:web:6117f4a9160b8667b8f1d5"
  };

  firebase.initializeApp(firebaseConfig);

// Função para fazer login.
function loginUser() {
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;
  
    firebase.auth().signInWithEmailAndPassword(email, password)
      .then((userCredential) => {
        const user = userCredential.user;
        console.log("Usuário logado:", user);
        redirectToHome(); 
      })
      .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        console.error("Erro de login:", errorMessage);
      });
};

// Função para registrar um novo usuário.
function registerUser() {
    const username = document.getElementById('registro-username').value;
    const email = document.getElementById('registro-email').value;
    const password = document.getElementById('registro-password').value;
    const telefone = document.getElementById('registro-telefone').value; 

    firebase.auth().createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {
        const user = userCredential.user;

        user.updateProfile({
            displayName: username 
        }).then(() => {
            console.log("Novo usuário registrado:", user);

          
            firebase.firestore().collection('users').doc(user.uid).set({
                username: username,
                email: email,
                telefone: telefone 
            }).then(() => {
                redirectToHome(); 
            }).catch((error) => {
                console.error("Erro ao salvar dados do usuário no Firestore:", error);
            });
        }).catch((error) => {
            console.error("Erro ao atualizar perfil do usuário:", error);
        });
    })
    .catch((error) => {
        console.error("Erro ao registrar usuário:", error);
    });
};

// Função para redefinir senha.
function resetPassword() {
    const email = document.getElementById('login-email').value;

    firebase.auth().sendPasswordResetEmail(email)
      .then(() => {
        console.log("E-mail de redefinição de senha enviado!");
        alert("Um e-mail de redefinição de senha foi enviado para o seu endereço de e-mail. Verifique sua caixa de entrada.");
      })
      .catch((error) => {
        console.error("Erro ao enviar e-mail de redefinição de senha:", error);
        alert("Ocorreu um erro ao enviar o e-mail de redefinição de senha. Por favor, tente novamente.");
      });
}

function redirectToHome() {

  window.location.href = 'home.html'; 
};
