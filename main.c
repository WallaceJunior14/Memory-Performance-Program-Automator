#include <sys/time.h>
#include <stdio.h>

struct pix
{
    unsigned int r, g, b;
};

// tam de 0 a 19.000
#define TAM 18000

struct pix color [TAM][TAM];

int main() {
    double ti, tf, tempo;
    ti = tf = tempo = 0;

    struct timeval tempo_inicio, tempo_fim;
    gettimeofday(&tempo_inicio, NULL);

    // CODIGO
    /*
    for (int i = 0; i < TAM; i++)
    {
        for (int j = 0; j < TAM; j++)
        {
            color[i][j].r = 
                (
                    color[i][j].r +
                    color[i][j].g +
                    color[i][j].b 
                )/3;
        }
    }
    */
    for (int i = 0; i < TAM; i++)
    {
        for (int j = 0; j < TAM; j++)
        {
            color[j][i].r = 
                (
                    color[j][i].r +
                    color[j][i].g +
                    color[j][i].b 
                )/3;
        }
    }
    //COGIDO

    gettimeofday(&tempo_fim, NULL);

    tf = (double) tempo_fim.tv_usec + ((double) tempo_fim.tv_sec * (1000000.0));
    ti = (double) tempo_inicio.tv_usec + ((double) tempo_inicio.tv_sec * (1000000.0));

    tempo = (tf - ti) / 1000;
    printf("Tempo gasto em milesegundos. %.3f\n", tempo);
}