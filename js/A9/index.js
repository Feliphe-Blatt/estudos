let lista = [1, 'batata', 'pão', 'vermelho', 22];

console.log(`\nTipo da variável 'lista': ${typeof(lista)} ;\n`);

console.log(lista instanceof Array);

console.log(`\nO 2º índice da lista é: ${lista[1]} .\n`);

lista.push('Novo item da lista');

lista.unshift('Inserindo item no ínicio da lista');

const ultimoItemRemovido = lista.pop();

const primeiroItemRemovido = lista.shift();

console.log(lista + ' \n');

console.log(ultimoItemRemovido + ' \n');

console.log(primeiroItemRemovido + ' \n');

delete lista[0]; // O item fica como vazio

console.log(lista);

console.log(lista.slice(1, -1));

console.log(lista);