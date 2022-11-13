let varA = 'A';
let varB = 'B';
let varC = 'C';

console.log(varA, varB, varC);

/*
let buffer = varA;
varA = varB;
varB = varC;
varC = buffer;
*/

[varA, varB, varC] = [varB, varC, varA]

console.log(varA, varB, varC);