# Reconhecimento de Imagem Sofia

Este projeto é uma aplicação web para classificação de imagens em tempo real usando a câmera do dispositivo. Utiliza o Teachable Machine do Google para treinar e executar modelos de machine learning diretamente no navegador.

## Funcionalidades

- **Classificação em Tempo Real**: Captura imagens da webcam e classifica em categorias pré-treinadas.
- **Interface Intuitiva**: Design moderno com Bootstrap e gradientes visuais.
- **Feedback Visual**: Barras de progresso coloridas indicando a confiança da classificação.
- **Compatibilidade**: Funciona em navegadores modernos com suporte a TensorFlow.js.

## Como Executar

1. **Clone ou Baixe o Repositório**:
   ```
   git clone <url-do-repositorio>
   cd Reconhecimento-imagem-Sofia
   ```

2. **Treine um Modelo (Opcional)**:
   - Acesse [Teachable Machine](https://teachablemachine.withgoogle.com/).
   - Treine um modelo de classificação de imagens.
   - Exporte o modelo e coloque os arquivos (`model.json`, `metadata.json` e pasta `model.weights.bin`) na pasta `my_model/`.

3. **Execute a Aplicação**:
   - Abra o arquivo `index.html` em um navegador web moderno.
   - Clique em "Permitir acesso à câmera" para iniciar.
   - Permita o acesso à câmera quando solicitado.

4. **Servidor Local (Recomendado)**:
   Para evitar problemas de CORS ao carregar o modelo, execute um servidor local:
   ```
   python -m http.server 8000
   ```
   Acesse `http://localhost:8000` no navegador.

## Estrutura do Projeto

```
Reconhecimento-imagem-Sofia/
├── index.html                 # Página principal da aplicação
├── my_model/                  # Pasta para o modelo treinado (não incluída)
│   ├── model.json
│   ├── metadata.json
│   └── model.weights.bin
└── teste-assistent-code/      # Exemplos de código Python para aprendizado
    ├── debug.py               # Script corrigido para cálculo de compras
    ├── explicacao_debug.md    # Explicação dos erros e correções em debug.py
    ├── num_primos.py          # Função otimizada para verificar números primos
    ├── explicacao_num_primo.md # Explicação da implementação de num_primos.py
    ├── refatoracao.py         # Código refatorado para cálculo de estatísticas
    └── explicacao_refatoracao.md # Explicação linha a linha de refatoracao.py
```

## Dependências

- **TensorFlow.js**: Para execução do modelo de machine learning.
- **Teachable Machine Image**: Biblioteca para carregar e usar modelos treinados.
- **Bootstrap 5**: Para estilização da interface.
- **Navegador Moderno**: Com suporte a WebRTC para acesso à câmera.

## Exemplos de Uso

### Classificação de Imagens
- Treine um modelo para reconhecer objetos (ex: maçã, banana, laranja).
- Execute a aplicação e aponte a câmera para os objetos.
- Veja as probabilidades em tempo real nas barras de progresso.

### Testes de Código Python
A pasta `teste-assistent-code` contém exemplos educacionais:

- **debug.py**: Calcula total de compras com impostos e descontos.
- **num_primos.py**: Verifica se um número é primo de forma eficiente.
- **refatoracao.py**: Calcula estatísticas básicas de uma lista de números.

Para executar os scripts Python:
```bash
cd teste-assistent-code
python debug.py
python num_primos.py
python refatoracao.py
```

## Contribuição

1. Fork o projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Autor

Sofia Almeida Cunha

## Agradecimentos

- Google Teachable Machine
- TensorFlow.js
- Bootstrap</content>
<filePath>c:\Users\SOFIAALMEIDACUNHA\Desktop\Reconhecimento-imagem-Sofia\README.md