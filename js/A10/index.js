function funcaoQualquer (parametro){
    console.log(`Escreve qualquer coisa, ${parametro}!`);

    return `Escreve qualquer coisa, ${parametro}!`;
}

funcaoQualquer();  // Sem parâmetro retorna undefined onde o parâmetro é 'mencionado'
funcaoQualquer('Feliphe');

console.log(funcaoQualquer('Feliphe')); // executou o log dentro da função além de ter retornado a frase!

function matematica(x=1, y=2){  // Caso não seja indicado parâmetros, estes são os valores padrão
    return x + y;
}

console.log(matematica());

console.log(matematica(3, 4));

const raiz = function nomeDaFuncaoEscondido(parametro){  // função anônima
    return parametro ** 0.5;
};

const dobro = parametro => parametro * 2; // Arrow function que simplifica tamanho

console.log(dobro(3));