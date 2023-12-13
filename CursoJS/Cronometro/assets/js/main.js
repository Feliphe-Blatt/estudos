function escopo() {

    const cronometro = document.querySelector('.cronometro');
    let segundos = 0;
    let timer;

    function pegaSegundos(seg){
        const data = new Date(seg * 1000);
        return data.toLocaleTimeString('pt-BR', {hour12: false, timeZone: 'UTC'});
    }

    function iniciaCronometro(){
        timer = setInterval(function(){
            segundos++;
            cronometro.innerHTML = pegaSegundos(segundos);
        }, 1000);
    }

    document.addEventListener('click', function(event){
        const element = event.target;

        if(element.classList.contains('zerar')){
            cronometro.classList.remove('pausado');
            clearInterval(timer);
            segundos = 0;
            cronometro.innerHTML = '00:00:00';
        }
        if(element.classList.contains('iniciar')){
            cronometro.classList.remove('pausado');
            clearInterval(timer);
            iniciaCronometro();
        }
        if(element.classList.contains('pausar')){
            cronometro.classList.add('pausado');
            clearInterval(timer);
        }
    });
}
escopo();
