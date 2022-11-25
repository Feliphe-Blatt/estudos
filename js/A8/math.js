let num1 = 0.7;
let num2 = 0.1;

let num3 = (num1 + num2).toFixed(2); // IEEE 754-2008

console.log(num3);

let num4 = 5.4786284;
let num5 = 5.50;
let num6 = 5.5267346;

num4 = Math.floor(num4);
console.log(num4);

num5 = Math.ceil(num5);
console.log(num5);

num6 = Math.round(num6);
console.log(num6);

console.log(Math.max(1, 10, -5, 7, 56));
console.log(Math.min(1, 10, -5, 7, 56));

const randomico = Math.random() * (10 - 5) + 5;
console.log(randomico.toFixed(2));

console.log(Math.PI.toFixed(2));

console.log(Math.pow(2, 3));

let infinito = 100 / 0; // CUIDADO! Retorna 'True' indicando que a conta foi realizada normalmente

console.log(infinito);