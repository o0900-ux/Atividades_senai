var firebaseConfig = {
    apiKey: "AIzaSyD4yp2qXBKP2ucmIgVicLVcm0G-EDimyJU",
    authDomain: "magnus-saude.firebaseapp.com",
    projectId: "magnus-saude",
    storageBucket: "magnus-saude.appspot.com",
    messagingSenderId: "990674908965",
    appId: "1:990674908965:web:920811faf9b2d187760ccc",
    measurementId: "G-3KM9Y50Y6E"
};

firebase.initializeApp(firebaseConfig);
var db = firebase.firestore();
var auth = firebase.auth();

function main() {
    auth.onAuthStateChanged(function(user) {
        if (user) {
            console.log("Usuário autenticado:", user.email);
        } else {
            console.log("Usuário não autenticado. Redirecionando para login.");
            window.location.href = "../index.html";
        }
    });
}

function redirecionar() {
    window.location.href = "/Html/Termosdeuso.html"; 
}

function redirecionar2() {
    window.location.href = "/Html/perguntas.html"; 
}

// Função para fazer logout
function logout() {
    auth.signOut().then(function() {
        console.log("Usuário desconectado com sucesso.");
        window.location.href = "../index.html";  
    }).catch(function(error) {
        console.error("Erro ao desconectar:", error);
    });
}

document.getElementById('logoutButton').addEventListener('click', function(event) {
    event.preventDefault();
    logout();
});

window.onload = function() {
    const elemento1 = document.getElementById("t");
    if (elemento1) {
        elemento1.addEventListener("click", redirecionar);
    }

    const elemento2 = document.getElementById("pf");
    if (elemento2) {
        elemento2.addEventListener("click", redirecionar2);
    }
};

main();
