
let valorUsuario = 500;
let valorPadrao = valorUsuario || 0; // Valor padrao seria '0' até que o usuário mudar

dataNasc = new Date(1996, 1, 21, 1, 30);  // nesse caso o date confere onde o usuário está e transforma para UTC

let dataAtual = new Date();

console.log(dataAtual.toLocaleDateString('pt-BR', {dateStyle: 'full'}));

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function pegaSemana(a) {
    const semana = a.getDay();
    switch (semana) {
        case 0:
            return 'Domingo';
        case 1:
            return 'Segunda';
        case 2:
            return 'Terça';
        case 3:
            return 'Quarta';
        case 4:
            return 'Quinta';
        case 5:
            return 'Sexta';
        case 6:
            return 'Sábado';
    }
}
function pegaDia(a) {
    return a.getDate();
}
function pegaMes(a) {
    let mes = a.getMonth();
    switch (mes) {
        case 0:
            return 'Janeiro';
        case 1:
            return 'Fevereiro';
        case 2:
            return 'Março';
        case 3:
            return 'Abril';
        case 4:
            return 'Maio';
        case 5:
            return 'Junho';
        case 6:
            return 'Julho';
        case 7:
            return 'Agosto';
        case 8:
            return 'Setembro';
        case 9:
            return 'Outubro';
        case 10:
            return 'Novembro';
        case 11:
            return 'Dezembro';
    }
}
function pegaAno(a) {
    return a.getFullYear();
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function nasceuEm(a){
    return `Nasceu no dia ${pegaDia(a)} de ${pegaMes(a)} de ${pegaAno(a)}, às ${a.getHours(a)}h ${a.getMinutes(a)}min e ${a.getSeconds(a)}seg`;
}
function traduzData(a) {
    return `\nHoje é ${pegaSemana(a)}, dia ${pegaDia(a)} de ${pegaMes(a)} do ano de ${pegaAno(a)}!`;
}
function dizHora(a) {
    return `São ${a.getHours()}h ${a.getMinutes()}min e ${a.getSeconds()}seg!`;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
console.log(nasceuEm(dataNasc));
console.log(traduzData(dataAtual));
console.log(dizHora(dataAtual));
