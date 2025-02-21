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

function formatCPF(cpf) {
    return cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
}

function formatRegistrationDate(isoDate) {
    const date = new Date(isoDate);
    return date.toLocaleDateString('pt-BR', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    });
}

function generateQRCode(data) {
    try {
        const qr = qrcode(0, 'L');
        qr.addData(data);
        qr.make();

        const qrCodeImage = qr.createImgTag();
        const imgTag = qrCodeImage.match(/src="([^"]*)"/)[1];
        document.getElementById('qr-code').src = imgTag;

        document.getElementById('qr-code-date').innerText = `Criado em: ${new Date().toLocaleString()}`;
        console.log('QR code gerado!');
    } catch (e) {
        console.error('Erro ao gerar QR code:', e);
    }
}

function fetchUserData(uid) {
    db.collection("pacientes").doc(uid).get().then(function(doc) {
        if (doc.exists) {
            var userData = doc.data();

            document.getElementById('userName').innerHTML = `<strong>${userData.nome}</strong>`;
            document.getElementById('userCpf').innerText = formatCPF(userData.cpf);
            document.getElementById('userBirthDate').innerText = userData.data_nascimento;
            document.getElementById('userAddress').innerText = userData.endereco;
            document.getElementById('userRegistrationDate').innerText = formatRegistrationDate(userData.data_cadastro);

            if (userData.foto_url) {
                document.getElementById('userAvatar').src = userData.foto_url;
            }

            const qrData = JSON.stringify({
                nome: userData.nome,
                cpf: userData.cpf,
                dataNascimento: userData.data_nascimento,
                endereco: userData.endereco,
                dataCadastro: userData.data_cadastro
            });
            generateQRCode(qrData);
        } else {
            console.error("Nenhum documento encontrado!");
        }
    }).catch(function(error) {
        console.error("Erro ao buscar os dados do usuário:", error);
    });
}

auth.onAuthStateChanged(function(user) {
    if (user) {
        fetchUserData(user.uid);
    } else {
        window.location.href = "../index.html";
    }
});
