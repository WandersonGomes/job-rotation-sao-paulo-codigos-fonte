/*
Author: Wanderson Gomes da Costa
E-mail: dersom100@gmail.com

Problema:
    Dado um vetor que guarda o valor de faturamento diario de uma distribuidora, faca um programa, na linguagem que desejar, que calcule e retorne:
    * O menor valor de faturamento ocorrido em um dia do mes;
    * O maior valor de faturamento ocorrido em um dia do mes;
    * Numero de dias no mes em que o valor de faturamento diario foi superior a media mensal.

    IMPORTANTE:
    a) Usar o json ou xml disponivel como fonte dos dados do faturamento mensal; (Obs.: EU NAO RECEBI, ENTAO RESOLVI CRIAR UM!)
    b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no calculo da media; 

Executar:
    Primeiro faca a instalacao do NodeJS: https://www.nodejs.org
    E execute o seguinte comando em seu terminal:

    node question3.js
*/

//FUNCOES PROPRIAS
const calcularMenorValorFaturamento = (faturamento_mes) => {
    const faturamento_mes_filtrado = faturamento_mes.filter((valor) => valor !== null);
    faturamento_mes_filtrado.sort();

    return faturamento_mes_filtrado[0];
}

const calcularMaiorValorFaturamento = (faturamento_mes) => {
    const faturamento_mes_filtrado = faturamento_mes.filter((valor) => valor !== null);
    faturamento_mes_filtrado.sort();

    return faturamento_mes_filtrado.pop();
}

const calcularNumeroDiasFaturamentoMaiorMedia = (faturamento_mes) => {
    const faturamento_mes_filtrado = faturamento_mes.filter((valor) => valor !== null);
    faturamento_mes_filtrado.sort();

    const media = faturamento_mes_filtrado.reduce((total, valor) => total + valor)/faturamento_mes_filtrado.length;

    return faturamento_mes_filtrado.filter((valor) => valor > media).length;
}

const main = () => {
    try {
        //carrega o json com os dados de faturamento
        const json_dados_faturamento = require('./dados_faturamento.json');

        //carrega os dados do mes
        const mes = 'julho'
        const faturamento_mes = json_dados_faturamento[mes]

        //resultados
        const menorValorFaturamento = calcularMenorValorFaturamento(faturamento_mes);
        const maiorValorFaturamento = calcularMaiorValorFaturamento(faturamento_mes);
        const numeroDiasFaturamentoMaiorMedia = calcularNumeroDiasFaturamentoMaiorMedia(faturamento_mes);

        console.log(`O valor do menor faturamento foi de: ${menorValorFaturamento}`);
        console.log(`O valor do maior faturamento foi: ${maiorValorFaturamento}`)
        console.log(`Numero de dias com faturamento maior que a media: ${numeroDiasFaturamentoMaiorMedia}`)
    } catch (e) {
        console.error(e);
    }
}

main();



