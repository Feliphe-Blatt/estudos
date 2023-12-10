
const paragrafos = document.querySelector('.paragrafos');

const ps = paragrafos.querySelectorAll('p');

const estiloCorpo = getComputedStyle(document.body);
const corDoCorpo = estiloCorpo.backgroundColor;

for(let p of ps){
    p.style.backgroundColor = corDoCorpo;
    p.style.color = '#ffffff';
}
