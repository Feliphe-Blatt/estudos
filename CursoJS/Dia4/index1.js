const nome = prompt('Digite seu nome:');
document.body.innerHTML += `Olá <b>${nome}</b>, Seja Bem-vindo(a)!<br/>`;

const quantidade = nome.length;
document.body.innerHTML += `Seu nome tem <b>${quantidade}</b> letras;<br/>`;

const letra = nome[1];
document.body.innerHTML += `A segunda letra do seu nome é: "<b>${letra}</b>";<br/>`;

const primeiroIndex = nome.indexOf('a');
document.body.innerHTML += `A letra '<b>a</b>' aparece primeiro no índice: <b>${primeiroIndex}</b>;<br/>`;

const ultimoIndice = nome.lastIndexOf('a');
document.body.innerHTML += `A letra '<b>a</b>' aparece por último no índice: <b>${ultimoIndice}</b>;<br/>`;

const divideNome = nome.split(' ');
document.body.innerHTML += `Seu nome separado: '<b>${divideNome}</b>';<br/>`;

const sobreNome = divideNome[divideNome.length-1];  // Achei conveniente usar 'array' para separar nomes
const ultimasLetras = sobreNome.slice(-3);
document.body.innerHTML += `As últimas <b>3</b> letras do seu nome são: '<b>${ultimasLetras}</b>';<br/>`;

document.body.innerHTML += `Seu nome com letras <b>Maiúsculas</b>: '<b>${nome.toUpperCase()}</b>';<br/>`;

document.body.innerHTML += `Seu nome com letras <b>Minúsculas</b>: '<b>${nome.toLowerCase()}</b>';<br/>`;
