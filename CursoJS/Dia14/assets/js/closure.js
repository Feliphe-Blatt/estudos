function escopo(){
    
    //  Closure
    
    function criaMultiplicador(mult){
        return function (x){
            return mult * x;
        };
    }
    const duplica = criaMultiplicador(2);
    
    const triplica = criaMultiplicador(3);

    const quadriplica = criaMultiplicador(4);

    const numero = 1.5;
    console.log(`Duplicando ${numero} = ${duplica(numero)};`);
    console.log(`Triplicando ${numero} = ${triplica(numero)};`);
    console.log(`Quadriplicando ${numero} = ${quadriplica(numero)};`);
}
escopo();