// Importa algumas bibliotecas
#include <iostream>
#include <string>
#include <chrono> 
#include <vector> 

// Simplifica a chamada de algumas funções
using namespace std;
using namespace std::chrono;

// Define alguns macros/atalhos para simplificar o código
// Não precisa tentar entender
#define comeca_contagem high_resolution_clock::now
#define duracao(a) duration_cast<milliseconds>(a).count()
#define finaliza_contagem(a) duracao(comeca_contagem() - a)
#define imprime_tempo(a, b) cout << a << b << " ms" << endl

// Começo do programa de verdade
int main() {
    // Cria uma lista com (10k)^2 elementos
    int n = 10000;
    vector<int> lista(n*n);
    
    
    // Primeiro caso
    // Execução boa para cache
    auto inicio_1 = comeca_contagem();
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            // O "n" multiplica o "i"
            // Percorre os blocos de forma linear
            lista[n*i + j] = 1;
        }
    }
    
    auto tempo_1 = finaliza_contagem(inicio_1);
    imprime_tempo("Tempo com cache: ", tempo_1);
    
    
    // Segundo caso
    // Execução ruim para cache
    auto inicio_2 = comeca_contagem();
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            // O "n" multiplica o "j"
            // Não percorre os blocos de forma linear
            lista[i + n*j] = 1;
        }
    }
    
    auto tempo_2 = finaliza_contagem(inicio_2);
    imprime_tempo("Tempo sem cache: ", tempo_2);
    
    // Fim do programa
    return 0;
}