# Automação para Benchmark de Código em C

Este projeto consiste em um script Python que automatiza a execução de um código C para converter componentes RGB de imagens para escala de cinza, variando a constante TAM. A finalidade é analisar o desempenho do código para diferentes tamanhos de matriz.

## Estrutura do Projeto

O script Python realiza as seguintes etapas:

1. **Geração do Código C**:
   O código é gerado dinamicamente com o tamanho da matriz ajustado com base nos valores definidos no array `tam_values`.

2. **Compilação**:
   O código C gerado é salvo em um arquivo temporário e compilado usando o GCC.

3. **Execução**:
   O executável gerado é executado, e o tempo de execução é coletado e analisado.

4. **Limpeza**:
   Após a execução, os arquivos temporários são removidos para manter o ambiente limpo.

5. **Resultados**:
   O script imprime uma tabela de resultados com os tamanhos testados e seus respectivos tempos de execução.

## Requisitos

- **Python 3**
- **GCC (GNU Compiler Collection)**
- Sistema operacional baseado em Unix (Linux ou macOS recomendado)

## Como Usar

1. Clone este repositório ou copie o script para o seu ambiente local.
2. Certifique-se de que o GCC esteja instalado e acessível via linha de comando.
3. Execute o script Python:

   ```bash
   python3 automation.py
   ```

4. O script gerará e executará o código C para diferentes tamanhos de matriz definidos no array `tam_values`.
5. Os resultados serão exibidos no terminal em formato de tabela.

## Código C Gerado

O programa em C realiza a seguinte operação:

- Cria uma matriz bidimensional de estruturas `struct pix`, onde cada estrutura contém componentes RGB.
- Itera sobre cada elemento da matriz, realizando cálculos para ajustar o componente `r` com base na média dos valores RGB.
- Mede o tempo total de execução em milissegundos.

### Exemplo de Saída

```plaintext
Saída para TAM=100:
Tempo gasto em milissegundos: 12.345

Tabela de resultados:
TAM	Tempo (ms)
100	12.345
500	56.789
1000	234.567
...
```

## Personalização

- **Tamanhos de Matriz**:
  Para ajustar os tamanhos da matriz testados, edite o array `tam_values` no script Python:
  
  ```python
  tam_values = [100, 500, 1000, 5000, 10000, 15000, 19000]
  ```

- **Código C**:
  Se desejar alterar a lógica do programa em C, edite a variável `c_code` no script Python.

## Tratamento de Erros

- **Erro na Compilação**:
  Se ocorrer um erro ao compilar o código C, uma mensagem será exibida no terminal com detalhes do erro.

- **Erro na Execução**:
  Se o programa C não for executado corretamente, o script exibirá a mensagem de erro correspondente.

- **Formato de Saída Inválido**:
  O script valida se a saída contém o formato esperado "Tempo gasto em milissegundos" antes de tentar processar o tempo.

## Limitações

- O script foi projetado para sistemas Unix e pode não funcionar corretamente em ambientes Windows.
- A memória necessária para grandes tamanhos de matriz pode exceder os limites do sistema.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

