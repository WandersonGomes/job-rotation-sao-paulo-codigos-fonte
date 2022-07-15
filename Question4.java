/*
 * Autor: Wanderson Gomes da Costa
 * E-mail: dersom100@gmail.com
 * 
 * Problema:
    * 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
    * 
    * SP - R$ 67.836,43
    * RJ - R$ 36.678,66
    * MG - R$ 29.229,88
    * ES - R$ 27.165,48
    * Outros - R$ 19.849,53
    * 
    * Escreva um programa na linguagem que desejar onde calcule o percentual de representacao que cada estado teve dentro do valor total mensal da 
    * distribuidora.
 * 
 * Executar:
    * Para executar voce precisa instalar o Java em sua maquina e depois rodar os seguintes comandos em seu terminal:
    * 
    * javac Question4.java
    * java Question4
 */
class Question4 {
    public static void main(String[] args) {
        //uma maneira melhor para trabalhar com valores monetarios 
        //seria com BigInteger, porem irei considerar que o problema
        // quer um resultado "razoavel"
        double faturamentoSaoPaulo = 67836.43;
        double faturamentoRioJaneiro = 36678.66;
        double faturamentoMinasGerais = 29229.88;
        double faturamentoEspiritoSanto = 27165.48;
        double faturamentoOutros = 19849.53;

        double totalFaturado =  faturamentoSaoPaulo + 
                        faturamentoRioJaneiro +
                        faturamentoMinasGerais +
                        faturamentoEspiritoSanto +
                        faturamentoOutros;
        
        double percentualSaoPaulo = (faturamentoSaoPaulo/totalFaturado) * 100;
        double percentualRioJaneiro = (faturamentoRioJaneiro/totalFaturado) * 100;
        double percentualMinasGerais = (faturamentoMinasGerais/totalFaturado) * 100;
        double percentualEspiritoSanto = (faturamentoEspiritoSanto/totalFaturado) * 100;
        double percentualOutros = (faturamentoOutros/totalFaturado) * 100;

        System.out.println("PERENTUAL DE PARTICIPACAO NO FATURAMENTO MENSAL DA DISTRIBUIDORA:");
        System.out.println(String.format("SP: %.2f%%", percentualSaoPaulo));
        System.out.println(String.format("RJ: %.2f%%", percentualRioJaneiro));
        System.out.println(String.format("MG: %.2f%%", percentualMinasGerais));
        System.out.println(String.format("ES: %.2f%%", percentualEspiritoSanto));
        System.out.println(String.format("Outros: %.2f%%", percentualOutros));
    }
}