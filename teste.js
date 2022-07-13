/*
function alteraNum(x){
    x = 3
    console.log("depois: x = " + x)
}
let y = 1
console.log("antes: " + y)
alteraNum(y)
console.log("depois: " + y)
*/

function calculaProximaIdade(idade) {
    idade += 1;
    console.log(idade);
}

function calculaProximasIdades(idades) {
    for (let i = 0; i < idades.length; i += 1) {
        idades[i] += 1;
    }
    console.log(idades);
}

function calculaIdadesDaqui5Anos(idades) {
     for (let i = 0; i < idades.length; i += 1) {
        idades[i] += 5;
    }
    console.log(idades);
}

const idadeStefany = 21;
calculaProximaIdade(idadeStefany);

const idadesAmigos = [idadeStefany, 20, 23, 18, 7];
calculaProximasIdades(idadesAmigos);

calculaIdadesDaqui5Anos(idadesAmigos);

