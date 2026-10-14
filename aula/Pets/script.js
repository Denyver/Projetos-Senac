let nome = prompt("Qual o nome do candidato?");
let idade = prompt("Qual a idade do candidato?");
let renda = prompt("Qual a renda mensal do candidato?");
let experiencia = prompt("O candidato possui condição de cuidado com pets? (sim/não)");
idade = parseInt(idade);

if (idade >= 18 && experiencia.toLowerCase() === "sim") {
    alert("Parabéns " + nome + "! Você atende aos requisitos");
} else {
    alert("Desculpe " + nome + ", você não atende aos requisitos nescessários");
}

if (renda >= 1200) {
    alert("Sua renda mensal é suficiente para cuidar de um pet!");
} else {
    alert("Infelizmente sua renda mensal não é suficiente para cuidar de um pet.");
}