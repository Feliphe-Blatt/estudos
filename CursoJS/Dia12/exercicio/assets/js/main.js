
const paragrafos = document.querySelector('.paragrafos');

const ps = paragrafos.querySelectorAll('p');

const estiloCorpo = getComputedStyle(document.body);
const corDoCorpo = estiloCorpo.backgroundColor;

for(let p of ps){
    p.style.backgroundColor = corDoCorpo;
    p.style.color = '#ffffff';
}

const pegaFoto = document.getElementById('imagem');

const paisagem = (larg, alt) => alt > larg ? "É retrato" : "É paisagem";

console.log(paisagem(1920, 1080));
