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

main();