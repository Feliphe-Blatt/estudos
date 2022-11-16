const nome = prompt('Nome completo:');

document.body.innerHTML += `Seu nome completo é: ${nome};<br/>`;
document.body.innerHTML += `Seu nome tem ${nome.length} letras;<br/>`;
document.body.innerHTML += `A segunda letra do seu nome é: '${nome[1]}';<br/>`;
document.body.innerHTML += `O primmerio índice da letra 'a': ${nome.indexOf('a')};<br/>`;
document.body.innerHTML += `O primmerio índice da letra 'a': ${nome.lastIndexOf('a')};<br/>`;
document.body.innerHTML += `As 3 últimas letras do seu nome: '${nome.slice(-3)}';<br/>`;
document.body.innerHTML += `Seu nome separado por palavras fica assim: ${nome.split(' ')};<br/>`;
document.body.innerHTML += `Maiúsculo: ${nome.toUpperCase()};<br/>`;
document.body.innerHTML += `Minúsculo: ${nome.toLowerCase()};<br/>`;
