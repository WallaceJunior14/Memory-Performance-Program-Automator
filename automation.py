import subprocess
import os

# Criar o conteúdo do arquivo .c
c_code = """#include <sys/time.h>
#include <stdio.h>

struct pix
{
    unsigned int r, g, b;
};

#define TAM {TAM}

struct pix color[TAM][TAM];

int main() {
    double ti, tf, tempo;

    struct timeval tempo_inicio, tempo_fim;
    gettimeofday(&tempo_inicio, NULL);

    {PROGRAM}

    gettimeofday(&tempo_fim, NULL);

    tf = (double)tempo_fim.tv_usec + ((double)tempo_fim.tv_sec * 1000000.0);
    ti = (double)tempo_inicio.tv_usec + ((double)tempo_inicio.tv_sec * 1000000.0);

    tempo = (tf - ti) / 1000.0;
    printf("Tempo gasto em milissegundos: %.3f\\n", tempo);
    return 0;
}
"""

# Definição de algoritmos
program_1 = """
    for (int i = 0; i < TAM; i++)
    {
        for (int j = 0; j < TAM; j++)
        {
            color[i][j].r = 
                (
                    color[i][j].r +
                    color[i][j].g +
                    color[i][j].b 
                ) / 3;
        }
    }
"""

program_2 = """
    for (int i = 0; i < TAM; i++)
    {
        for (int j = 0; j < TAM; j++)
        {
            color[j][i].r = 
                (
                    color[j][i].r +
                    color[j][i].g +
                    color[j][i].b 
                ) / 3;
        }
    }
"""

programs = [program_1, program_2]

# Definir valores para TAM -> 100 a 19000
tam_values = [100, 500, 1000, 5000, 10000, 15000, 19000]

temp_filename = "temp_code.c"
output_filename = "temp_executable.out"

times_program_1 = []
times_program_2 = []

for i, program in enumerate(programs):
    for tam in tam_values:
        # Substituir {TAM} e {PROGRAM}
        code_with_tam = c_code.replace("{TAM}", str(tam)).replace("{PROGRAM}", program)

        # Criar/Alterar o arquivo .c
        with open(temp_filename, "w") as f:
            f.write(code_with_tam)

        # Compilar o código .c
        compile_result = subprocess.run(["gcc", temp_filename, "-o", output_filename], stderr=subprocess.PIPE)

        if compile_result.returncode != 0:
            print(f"Erro ao compilar o código C para TAM={tam}:")
            print(compile_result.stderr.decode())
            continue

        # Executar o programa compilado
        execution_result = subprocess.run([f"./{output_filename}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if execution_result.returncode != 0:
            print(f"Erro ao executar o programa para TAM={tam}:")
            print(execution_result.stderr.decode())
            continue

        # Ler o tempo de execução da saída do programa executado
        output = execution_result.stdout.decode().strip()
        print(f"Saída para TAM={tam}: {output}")

        # Extrair o tempo e salvar
        try:
            if "Tempo gasto em milissegundos" in output:
                time_ms = float(output.split(":")[1].strip())
                if i == 0:
                    times_program_1.append((tam, time_ms))
                elif i == 1:
                    times_program_2.append((tam, time_ms))
            else:
                print(f"Formato de saída inesperado para TAM={tam}")
        except ValueError:
            print(f"Erro ao processar a saída para TAM={tam}: formato inválido")

# Remover arquivos temporários
if os.path.exists(temp_filename):
    os.remove(temp_filename)
if os.path.exists(output_filename):
    os.remove(output_filename)

# Imprimir as tabelas de resultados
print("\nTabela de resultados para Program 1:")
print("TAM\tTempo (ms)")
for tam, time in times_program_1:
    print(f"{tam}\t{time:.3f}")

print("\nTabela de resultados para Program 2:")
print("TAM\tTempo (ms)")
for tam, time in times_program_2:
    print(f"{tam}\t{time:.3f}")
