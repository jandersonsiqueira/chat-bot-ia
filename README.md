# Projeto Chatbot para Restaurante Delícias da Vila

## Descrição

Este projeto consiste em um chatbot desenvolvido para o Restaurante Delícias da Vila, com o objetivo de fornecer informações detalhadas sobre o restaurante, seu cardápio, serviços e políticas. O chatbot facilita a interação com os clientes, respondendo a perguntas frequentes e oferecendo uma experiência de atendimento ao cliente eficiente e amigável.

## Objetivo

O objetivo principal deste projeto é criar um chatbot que:
- Forneça informações precisas e atualizadas sobre o Restaurante Delícias da Vila.
- Permita que os clientes obtenham detalhes sobre o cardápio, horários de funcionamento, serviços e políticas.
- Melhore a experiência do cliente, oferecendo respostas rápidas e úteis.

## Funcionalidades

- **Informações sobre o Restaurante**: Endereço, horário de funcionamento, telefone e e-mail.
- **Cardápio**: Detalhes sobre entradas, pratos principais e sobremesas, incluindo preços.
- **Tradição e História**: Informações sobre a história e tradição do restaurante.
- **Serviços**: Informações sobre reserva de mesas, serviço de entrega e eventos.
- **Política de Devolução**: Informações sobre a política de devolução de alimentos.
- **Formas de Pagamento**: Detalhes sobre os métodos de pagamento aceitos.

## Passo a Passo

1. **Configuração do Ambiente**
   - Instale as dependências necessárias, incluindo Flask e a biblioteca OpenAI.
   - Configure as variáveis de ambiente, incluindo a chave da API do OpenAI.

2. **Carregar Informações**
   - Adicione as informações do restaurante e do cardápio em um arquivo de texto (e.g., `informacoes.txt`).

3. **Desenvolver a Lógica do Chatbot**
   - Implemente a função para carregar informações do arquivo de texto.
   - Configure o cliente OpenAI com a chave da API e defina os parâmetros para a geração de respostas.

4. **Implementar as Rotas**
   - Crie uma rota para a página inicial (`/`) e uma rota para o chatbot (`/chat`).

5. **Testar o Chatbot**
   - Realize testes para garantir que o chatbot responda corretamente a perguntas sobre o restaurante e o cardápio.

## Estrutura do Projeto

```
/projeto
    /templates
        index.html
    app.py
    informacoes.txt
    README.md
```

## Exemplo de Uso

1. Acesse a página inicial do chatbot para interagir com ele.
2. Envie perguntas sobre o restaurante e receba respostas baseadas nas informações fornecidas.

## License

Este projeto é licenciado sob a permssão do DEV [Janderson](https://github.com/jandersonsiqueira).