import java.util.LinkedList;
import java.util.Queue;

public class GerenciamentoFilaImpressao {

    public static void main(String[] args) {
        // Criação de uma fila de impressão usando LinkedList
        Queue<String> filaImpressao = new LinkedList<>();

        // Adicionando tarefas de impressão à fila (Enfileiramento)
        filaImpressao.add("Documento1.pdf");
        filaImpressao.add("Documento2.pdf");
        filaImpressao.add("Documento3.pdf");

        // Processando a fila de impressão (Desenfileiramento)
        while (!filaImpressao.isEmpty()) {
            String documento = filaImpressao.poll();  // Retira o primeiro elemento da fila
            System.out.println("Imprimindo: " + documento);
        }       
    }
}
