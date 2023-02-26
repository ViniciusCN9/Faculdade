var usuarioId
var professorClasses = []

window.addEventListener("load", async () => {
    usuarioId = localStorage.getItem("ID")
    await carregarInformacoesUsuario()
    popularClasses()
    console.log(professorClasses)
  });

async function carregarInformacoesUsuario() {
    var configuracaoUsuarios = await (await fetch('../config/usuarios.json')).json()
    configuracaoUsuarios.usuarios.forEach(e => {
        if (e.id == usuarioId) {
            professorClasses = e.classes
        }
    });
}

function popularClasses() {
    if (professorClasses.length === 0){
        return
    }

    const alerta = document.getElementById("alerta")
        alerta.setAttribute("hidden", true)

    //continuar
}

async function criarClasse(event) {
    event.preventDefault()

    let nomeClasse = event.target.elements.nome.value
    let codigoClasse = geraStringAleatoria()

    var configuracaoUsuarios = await (await fetch('../config/usuarios.json')).json()
    configuracaoUsuarios.usuarios.forEach(e => {
        if (e.id == usuarioId) {
            e.classes.push(codigoClasse)
            console.log(codigoClasse)
        }
    });

    downloadFile()
}

function logout() {
    localStorage.removeItem("ID")
    window.location="../../index.html";
}

function geraStringAleatoria() {
    var stringAleatoria = '';
    var caracteres = 'abcdefghijklmnopqrstuvwxyz';
    for (var i = 0; i < 19; i++) {
        if (i === 5 || i === 10 || i === 15) {
            stringAleatoria += '-'
        } else {
            stringAleatoria += caracteres.charAt(Math.floor(Math.random() * caracteres.length));
        }
    }
    return stringAleatoria;
}

function downloadFile() {
    const link = document.createElement("a");
    const content = "teste";
    const file = new Blob([content], { type: 'text/plain' });
    link.href = URL.createObjectURL(file);
    link.download = "sample.txt";
    link.click();
    URL.revokeObjectURL(link.href);
}