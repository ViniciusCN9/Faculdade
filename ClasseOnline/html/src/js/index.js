async function login(event){
    event.preventDefault()
    
    const opcao = event.target.elements.radio.value
    const usuario = event.target.elements.usuario.value
    const senha = event.target.elements.senha.value

    const configuracaoUsuarios = await (await fetch('./src/config/usuarios.json')).json()
    
    let usuarioExiste = false
    let usuarioId = 0
    configuracaoUsuarios.usuarios.forEach(e => {
        if (e.usuario === usuario && e.senha === senha && e.opcao === opcao) {
            usuarioExiste = true
            usuarioId = e.id
        }
    });

    if (usuarioExiste && usuarioId !== 0) {
        localStorage.setItem('ID', usuarioId);
        if (opcao === 'p') {
            window.location="src/html/professor.html";
        } 
        else if (opcao === 'a') {
            window.location="src/html/aluno.html";
        }
    } else {
        const alerta = document.getElementById("alerta")
        alerta.removeAttribute("hidden")
    }
}