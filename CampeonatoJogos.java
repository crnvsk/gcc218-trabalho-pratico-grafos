import java.util.*;

public class CampeonatoJogos {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Criando um grafo bipartido
        Map<String, Set<Integer>> grafoBipartido = new HashMap<>();

        // Obtendo informações sobre disciplinas e horários
        System.out.println("Informe as disciplinas e os horários (ex: 'Disciplina: Horário1 Horário2'):");
        String input = scanner.nextLine();

        while (!input.equals("fim")) {
            String[] partes = input.split(":");
            String disciplina = partes[0].trim();
            String[] horariosStr = partes[1].trim().split(" ");

            Set<Integer> horarios = new HashSet<>();
            for (String horarioStr : horariosStr) {
                horarios.add(Integer.parseInt(horarioStr));
            }

            // Adicionando a disciplina e horários ao grafo bipartido
            grafoBipartido.put(disciplina, horarios);

            // Obtendo próxima entrada ou indicando fim
            System.out.println("Próxima disciplina (ou 'fim' para encerrar):");
            input = scanner.nextLine();
        }

        // Obtendo informações sobre alunos e disciplinas
        System.out.println("Informe os alunos e as disciplinas que estão cursando (ex: 'Aluno: Disciplina1 Disciplina2'):");
        input = scanner.nextLine();

        Map<String, Set<String>> alunosDisciplinas = new HashMap<>();

        while (!input.equals("fim")) {
            String[] partes = input.split(":");
            String aluno = partes[0].trim();
            String[] disciplinas = partes[1].trim().split(" ");

            // Adicionando aluno e disciplinas ao mapa
            alunosDisciplinas.put(aluno, new HashSet<>(Arrays.asList(disciplinas)));

            // Obtendo próxima entrada ou indicando fim
            System.out.println("Próximo aluno (ou 'fim' para encerrar):");
            input = scanner.nextLine();
        }

        // Encontrando horários disponíveis para treino
        encontrarHorariosDisponiveis(grafoBipartido, alunosDisciplinas);

        scanner.close();
    }

    private static void encontrarHorariosDisponiveis(Map<String, Set<Integer>> grafoBipartido, Map<String, Set<String>> alunosDisciplinas) {
        for (Map.Entry<String, Set<String>> entry : alunosDisciplinas.entrySet()) {
            String aluno = entry.getKey();
            Set<String> disciplinas = entry.getValue();
    
            Set<Integer> horariosIndisponiveis = new HashSet<>();
            for (String disciplina : disciplinas) {
                if (grafoBipartido.containsKey(disciplina)) {
                    horariosIndisponiveis.addAll(grafoBipartido.get(disciplina));
                }
            }
    
            Set<Integer> horariosDisponiveis = new HashSet<>();
            for (int i = 0; i < 24; i++) {
                if (!horariosIndisponiveis.contains(i)) {
                    horariosDisponiveis.add(i);
                }
            }
    
            System.out.println("Aluno: " + aluno);
            System.out.println("Horários disponíveis para treino: " + horariosDisponiveis);
        }
    }
    
}
