
const elementos = [
    {tag: 'p', conteudo: 'Qualquer Coisa'},
    {tag: 'p', conteudo: '<b>Qualquer Coisa só que em negrito</b>\n'},
    {tag: 'form', conteudo: '<input type="button" value="OK">'}
];

const container = document.querySelector('.container');
const section = document.createElement('section');

for(let i=0; i< elementos.length; i++){
    let {tag, conteudo} = elementos[i];
    let NovaTag = document.createElement(tag);
    NovaTag.innerHTML = conteudo;
    section.appendChild(NovaTag);
}

container.appendChild(section);
