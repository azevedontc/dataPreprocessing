# dataPreprocessing
Introduction to KDD and data preprocessing / Introdução ao KDD e pré-processamento de dados

Este projeto implementa uma análise de predição de doenças cardiovasculares utilizando modelos de aprendizado de máquina. As doenças cardiovasculares são a principal causa de morte globalmente, e este projeto busca criar modelos eficazes para prever a ocorrência dessas doenças com base em dados clínicos.

Requisitos
Para executar este projeto, você precisará de Python instalado em seu sistema, junto com as seguintes bibliotecas:

Pandas
Numpy
Scikit-learn
Você pode instalar todas as dependências necessárias com o seguinte comando:

bash
Copy code
pip install pandas numpy scikit-learn
Estrutura de Diretório
O projeto inclui os seguintes arquivos e diretórios:

heart-2024-1-1bimestre.csv: Dataset utilizado nas análises.
main.py: Script principal contendo o código de análise e modelagem.
Configuração do Ambiente
Certifique-se de que seu ambiente Python está configurado com todas as bibliotecas necessárias, conforme listado nos requisitos. Recomenda-se usar um ambiente virtual para instalar e gerenciar as dependências.

Como Executar
Clone o repositório para sua máquina local usando:
bash
Copy code
git clone URL_DO_REPOSITORIO
Substitua URL_DO_REPOSITORIO pela URL do repositório GitHub onde este projeto está hospedado.
Navegue até o diretório do projeto clonado:
bash
Copy code
cd caminho_para_o_projeto
Execute o script main.py:
bash
Copy code
python main.py
Saída Esperada
Ao executar o script main.py, você verá a seguinte saída no console:

Uma visualização das primeiras linhas dos dados.
Informações sobre os tipos de dados e a contagem de valores nulos.
Resultados das métricas de avaliação para cada modelo treinado (Árvore de Decisão, SVM, k-NN), incluindo precisão, recall e f1-score.
