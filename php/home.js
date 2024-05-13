const firebaseConfig = {
    apiKey: "AIzaSyA3gOHi9Q6aHQ5seN5S9bbNmQpPQFMGXFs",
    authDomain: "magnus-c4b38.firebaseapp.com",
    projectId: "magnus-c4b38",
    storageBucket: "magnus-c4b38.appspot.com",
    messagingSenderId: "458576341456",
    appId: "1:458576341456:web:6117f4a9160b8667b8f1d5"
};
firebase.initializeApp(firebaseConfig);

// Verifica se o usuário está autenticado e redireciona para a página apropriada
firebase.auth().onAuthStateChanged(function(user) {
    if (user) {
        document.getElementById('userInfo').style.display = 'block';
        document.getElementById('userName').textContent = user.displayName || 'Nome de usuário não disponível';
        document.getElementById('userPhoto1').src = user.photoURL || 'default-avatar.jpg'; 
        document.getElementById('userPhoto').src = user.photoURL || 'default-avatar.jpg'; 

     
        firebase.firestore().collection('users').doc(user.uid).get().then(function(doc) {
            if (doc.exists) {
                document.getElementById('userDescription').textContent = doc.data().description || 'Nenhuma descrição disponível';
            } else {
                console.log('Nenhum documento encontrado!');
            }
        }).catch(function(error) {
            console.error('Erro ao obter descrição:', error);
        });

     
        carregarPostagens();
    } else {
        window.location.href = 'index.html'; 
    }
});

// Função para carregar as postagens
function carregarPostagens() {
    firebase.firestore().collection('posts').orderBy('timestamp', 'desc').get().then(function(querySnapshot) {
        const userPostsContainer = document.getElementById('userPosts');
        userPostsContainer.innerHTML = ''; 
        querySnapshot.forEach(function(doc) {
            const postagem = doc.data();
            const postHtml = `
                <div class="post">
                    <p><strong>${postagem.author}</strong> - ${postagem.timestamp.toDate().toLocaleString()}</p>
                    <p>${postagem.content}</p>
                    ${postagem.imageURL ? `<img src="${postagem.imageURL}" alt="Imagem do Post">` : ''}
                </div>
            `;
            userPostsContainer.innerHTML += postHtml;
        });
    }).catch(function(error) {
        console.error("Erro ao carregar postagens:", error);
    });
}


// Função para desconectar o usuário
function logout() {
    firebase.auth().signOut().then(function() {
        window.location.href = 'index.html'; 
    }).catch(function(error) {
        console.error('Erro ao desconectar:', error);
    });
}

function editProfile() {
    const user = firebase.auth().currentUser;
    if (user) {
        document.getElementById('emailInput').style.display = 'block';
        document.getElementById('emailInput').value = user.email;
    } else {
        document.getElementById('emailInput').style.display = 'none';
    }
    document.getElementById('editProfileModal').style.display = 'block';
}



function closeModal() {
    document.getElementById('editProfileModal').style.display = 'none';
}

// Função para salvar as alterações no perfil
function saveChanges() {
    const newName = document.getElementById('nameInput').value;
    const newEmail = document.getElementById('emailInput').value;
    const newDescription = document.getElementById('descriptionInput').value;
    const newPhoto = document.getElementById('photoInput').files[0];

    const user = firebase.auth().currentUser;

  
    if (newName) {
        user.updateProfile({
            displayName: newName
        }).then(function() {
            document.getElementById('userName').textContent = newName;
        }).catch(function(error) {
            console.error('Erro ao atualizar nome:', error);
        });
    }

    if (newEmail) {
        user.updateEmail(newEmail).then(function() {
            document.getElementById('userEmail').textContent = newEmail;
        }).catch(function(error) {
            console.error('Erro ao atualizar email:', error);
        });
    }

    if (newPhoto) {
        const storageRef = firebase.storage().ref().child('user_photos/' + user.uid);
        storageRef.put(newPhoto).then(function(snapshot) {
            snapshot.ref.getDownloadURL().then(function(downloadURL) {
                user.updateProfile({
                    photoURL: downloadURL
                }).then(function() {
                    document.getElementById('userPhoto').src = downloadURL;
                }).catch(function(error) {
                    console.error('Erro ao atualizar foto:', error);
                });
            });
        });
    }


    if (newDescription) {
        firebase.firestore().collection('users').doc(user.uid).update({
            description: newDescription
        }).then(function() {
            document.getElementById('userDescription').textContent = newDescription;
        }).catch(function(error) {
            console.error('Erro ao atualizar descrição:', error);
        });
    }

    closeModal();
}

function fazerPostagem() {
    const user = firebase.auth().currentUser;
    if (user) {
        const postContent = document.getElementById('postContent').value;
        const postImage = document.getElementById('postImage').files[0];

        if (postContent || postImage) {
            const dataAtual = new Date();
            const dia = String(dataAtual.getDate()).padStart(2, '0');
            const mes = String(dataAtual.getMonth() + 1).padStart(2, '0');
            const ano = dataAtual.getFullYear();
            const hora = String(dataAtual.getHours()).padStart(2, '0');
            const minuto = String(dataAtual.getMinutes()).padStart(2, '0');
            const dataHora = `${dia}/${mes}/${ano} ${hora}:${minuto}`;


            const postData = {
                author: user.displayName || 'Nome de usuário não disponível', 
                content: postContent + '\n', 
                timestamp: firebase.firestore.FieldValue.serverTimestamp()
            };

          
            if (postImage) {
                const storageRef = firebase.storage().ref().child('user_posts/' + user.uid + '/' + postImage.name);
                storageRef.put(postImage).then(function(snapshot) {
                    snapshot.ref.getDownloadURL().then(function(downloadURL) {
                        postData.imageURL = downloadURL;
                      
                        salvarPostagem(postData);
                    });
                }).catch(function(error) {
                    console.error("Erro ao fazer upload da imagem:", error);
                });
            } else {
               
                salvarPostagem(postData);
            }
        } else {
            console.log("A postagem está vazia.");
        }
    } else {
        console.log("Usuário não autenticado.");
    }
}

function salvarPostagem(postData) {
    firebase.firestore().collection('posts').add(postData).then(function() {
        console.log("Postagem feita com sucesso!");
  
        carregarPostagens();
    }).catch(function(error) {
        console.error("Erro ao fazer postagem:", error);
    });
}



window.addEventListener('DOMContentLoaded', (event) => {

    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
            carregarPostagens(user); 
        } else {
            console.log('Usuário não autenticado.');
        }
    });
});

function carregarPostagens() {
    const user = firebase.auth().currentUser;
    if (user) {
        firebase.firestore().collection('posts').orderBy('timestamp', 'desc').get().then(function(querySnapshot) {
            const userPostsContainer = document.getElementById('userPosts');
            userPostsContainer.innerHTML = ''; 
            querySnapshot.forEach(function(doc) {
                const postagem = doc.data();

                if (postagem.author === user.displayName) {
                    const postHtml = `
                        <div class="post">
                            <p><strong>${postagem.author || 'Autor Desconhecido'}</strong> - ${postagem.timestamp ? postagem.timestamp.toDate().toLocaleString() : 'Data Desconhecida'}</p>
                            <p>${postagem.content.replace(/\n/g, '<br>')}</p>
                            ${postagem.imageURL ? `<img src="${postagem.imageURL}" alt="Imagem do Post">` : ''}
                            <button onclick="excluirPost('${doc.id}')">Excluir</button>
                        </div>
                    `;
                    userPostsContainer.innerHTML += postHtml;
                }
            });
        }).catch(function(error) {
            console.error("Erro ao carregar postagens:", error);
        });
    }
}


// Função para excluir um post
function excluirPost(postId) {
    firebase.firestore().collection('posts').doc(postId).delete().then(function() {
        console.log("Postagem excluída com sucesso!");
    
        carregarPostagens();
    }).catch(function(error) {
        console.error("Erro ao excluir postagem:", error);
    });
}

function renderizarPost(post) {
    const user = firebase.auth().currentUser;
    const postHtml = `
        <div class="post">
            <p><strong>${post.author}</strong> - ${post.timestamp.toDate().toLocaleString()}</p>
            <p>${post.content}</p>
            ${user && post.author === user.displayName ? `<button onclick="excluirPost('${post.id}')">Excluir</button>` : ''}
        </div>
    `;
    document.getElementById('userPosts').innerHTML += postHtml;
}

function openProfileSection() {
    document.getElementById('userProfileSection').style.display = 'block';
  
    carregarPerfil();
    carregarPostagens();

}

// Função para carregar informações do perfil do usuário
function carregarPerfil() {
    const user = firebase.auth().currentUser;
    if (user) {
        document.getElementById('userInfo').style.display = 'block';
        document.getElementById('userName').textContent = user.displayName || 'Nome de usuário não disponível';
        document.getElementById('userPhoto').src = user.photoURL || 'default-avatar.jpg';

      
        firebase.firestore().collection('users').doc(user.uid).get().then(function(doc) {
            if (doc.exists) {
                document.getElementById('userDescription').textContent = doc.data().description || 'Nenhuma descrição disponível';
            } else {
                console.log('Nenhum documento encontrado!');
            }
        }).catch(function(error) {
            console.error('Erro ao obter descrição:', error);
        });

    
        document.getElementById('userPostsOutrosUsuarios').innerHTML = '';
    } else {
        console.log('Usuário não autenticado.');
    }
}


function carregarPostagensOutrosUsuarios() {
    firebase.firestore().collection('posts').orderBy('timestamp', 'desc').get().then(function(querySnapshot) {
        const userPostsContainer = document.getElementById('userPostsOutrosUsuarios');
        userPostsContainer.innerHTML = ''; 
        querySnapshot.forEach(function(doc) {
            const postagem = doc.data();
            const user = firebase.auth().currentUser;
    
            if (user && postagem.author !== user.displayName) {
                const postHtml = `
                    <div class="post">
                        <p><strong>${postagem.author || 'Autor Desconhecido'}</strong> - ${postagem.timestamp ? postagem.timestamp.toDate().toLocaleString() : 'Data Desconhecida'}</p>
                        <p>${postagem.content.replace(/\n/g, '<br>')}</p>
                        ${postagem.imageURL ? `<img src="${postagem.imageURL}" alt="Imagem do Post">` : ''}
                    </div>
                `;
                userPostsContainer.innerHTML += postHtml;
            }
        });
    }).catch(function(error) {
        console.error("Erro ao carregar postagens de outros usuários:", error);
    });
}



window.addEventListener('DOMContentLoaded', (event) => {

    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
          
            carregarPostagens(); 
          
            carregarPostagensOutrosUsuarios(); 
        } else {
            console.log('Usuário não autenticado.');
        }
    });
});


// Função para voltar à página inicial
function returnToHomePage() {
   
    document.getElementById('userPostsOutrosUsuarios').innerHTML = '';
    
   
    document.getElementById('userProfileSection').style.display = 'none';

    carregarPostagensOutrosUsuarios();
    
 
}
