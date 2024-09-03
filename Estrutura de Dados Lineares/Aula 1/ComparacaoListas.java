import java.util.ArrayList;
import java.util.LinkedList;

public class ComparacaoListas {

    public static void main(String[] args) {
        // Criando uma instância de ArrayList para armazenar inteiros
        ArrayList<Integer> arrayList = new ArrayList<>();
        // Criando uma instância de LinkedList para armazenar inteiros
        LinkedList<Integer> linkedList = new LinkedList<>();

        // Medindo o tempo de inserção no ArrayList
        long tempoInicio = System.nanoTime();  // Captura o tempo inicial em nanossegundos
        for (int i = 0; i < 100000; i++) {  // Loop para adicionar 100.000 elementos no ArrayList
            arrayList.add(i);  // Adiciona o elemento i ao final do ArrayList
        }
        long tempoFim = System.nanoTime();  // Captura o tempo final após a inserção
        // Calcula e imprime o tempo total gasto na inserção no ArrayList
        System.out.println("Tempo de inserção no ArrayList: " + (tempoFim - tempoInicio) + " ms");

        // Medindo o tempo de inserção no LinkedList
        tempoInicio = System.nanoTime();  // Captura o tempo inicial em nanossegundos novamente
        for (int i = 0; i < 100000; i++) {  // Loop para adicionar 100.000 elementos no LinkedList
            linkedList.add(i);  // Adiciona o elemento i ao final do LinkedList
        }
        tempoFim = System.nanoTime();  // Captura o tempo final após a inserção
        // Calcula e imprime o tempo total gasto na inserção no LinkedList
        System.out.println("Tempo de inserção no LinkedList: " + (tempoFim - tempoInicio) + " ms");
    }
}
