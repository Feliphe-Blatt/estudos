let num1 = 54321.12345;
const num2 = 12345.54321;

num1 -= num2;

num1 = parseFloat(num1.toFixed(9));

document.body.innerHTML += `Valor do número com '<b>fixed</b>': <b>R$ ${num1}</b>;<br/>`;
