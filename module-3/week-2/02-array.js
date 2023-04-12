// 1 - Definição de Arrays

// 1.1 Array literal
const nomesAlunos = ["Ana", "Beatriz", "Carla", "Daiana"];
const mediasAlunos = [7, 8, 5, 10,];
const numerosPrimos = [2, 3, 5, 7, 11];
let listaVazia = [];
let tudoMisturado = [1.1, true, "azul"];

// let soma = mediasAlunos[0]+mediasAlunos[1]+mediasAlunos[2]+mediasAlunos[3];
// let media = soma / 4;
// console.log("A média do aluno é: " + media);

// 1.2 Spread operator
let a = [1, 2, 3];
let b = [0, ...a, 4];

// console.log(b);

// 1.3 Array Constructor
let c = new Array(5, 4, 3, 2, 1);

// console.log(c);

// 1.4 Array.of
let d = Array.of(11, 12, 13);

// console.log(d);

// 1.5 Array.from
let e = Array.from(d);