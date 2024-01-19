const dicionario = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'
  };
  
  function fraseParaMorse(frase) {
    const palavras = frase.toLowerCase().split(' ');
  
    const traducao = palavras.map((palavra) => {
      return palavra.split('').map((letra) => {
        if (dicionario[letra]) {
          return dicionario[letra];
        } else {
          // Se a letra não estiver no dicionário, mantenha a letra original
          return letra;
        }
      }).join(' ');
    }).join('   '); // Três espaços representam um espaço entre palavras em código Morse
  
    return traducao;
  }
  
  // Exemplo de uso
  const fraseDigitada = prompt('Digite a frase que você deseja traduzir para código Morse:');
  const resultadoMorse = fraseParaMorse(fraseDigitada);
  console.log(resultadoMorse);
  