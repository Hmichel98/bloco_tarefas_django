let lista = document.querySelectorAll(".list-group-item");

for (ponto of lista) {
    ponto.addEventListener("contextmenu", (e) => {e.preventDefault()})
}

function concluir(tarefa, evento) {
    if (evento.buttons === 1) {
        tarefa.style.backgroundColor="lightgreen";
    } else if (evento.buttons === 2) {
        tarefa.style.backgroundColor="white";
    }
    
}