
function fizzBuzz(a){
    if(typeof a != 'number'){
        return a;
    }else if(a%3 === 0  && a%5 === 0){
        return 'fizzBuzz';
    }else if(a%5 === 0){
        return 'buzz';
    }else if(a%3 === 0){
        return 'fizz';
    }else{
        return a;
    }
}

console.log(fizzBuzz('x'));

for (let i=0; i<=100; i++){
    console.log(fizzBuzz(i));
}
