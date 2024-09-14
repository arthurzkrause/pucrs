# PATADA - Pet Shop

Este é o site da **PATADA**, uma loja virtual voltada para produtos e serviços de pet shop. O site é dividido em seções, cada uma oferecendo informações e funcionalidades diferentes, incluindo produtos para cães e gatos, serviços de vacinação e um sistema de cadastro de clientes.

## Funcionalidades Principais

### 1. Página Inicial (`index.html`)
- **Cabeçalho e Navegação**: O site tem um cabeçalho fixo com o nome "PATADA" e um menu de navegação que leva às diferentes seções do site: Home, Cadastro e Serviços de Vacinação.
- **Imagem Estática**: Logo após o cabeçalho, há uma imagem decorativa de destaque.
- **Seções de Produtos**: A página inicial apresenta duas seções de produtos:
  - **Produtos para Cães**: Exibe uma lista de produtos para cães, como rações, petiscos e suplementos.
  - **Produtos para Gatos**: Oferece produtos voltados para gatos, como rações e petiscos.
- **Serviços de Vacinação**: A página também inclui uma seção que apresenta as vacinas oferecidas para cães e gatos.

### 2. Cadastro de Cliente (`cadastro.html`)
- **Formulário de Cadastro**: Nesta página, os clientes podem se cadastrar preenchendo suas informações pessoais, como nome, email, senha, endereço e dados sobre seus pets.
- **Carrossel de Imagens**: Um carrossel de imagens com 6 slides é exibido logo abaixo do cabeçalho, destacando serviços ou imagens promocionais da loja.
- **Campo para Upload de Foto**: O cliente pode fazer upload de uma foto de seu pet durante o cadastro.
- **Envio de Formulário**: Os dados preenchidos são enviados para um endereço de email específico (através de uma integração com o serviço `FormSubmit`).

### 3. Rodapé
- **Endereço**: Mostra o endereço fictício da loja.
- **Atendimento**: Links para a central de atendimento, FAQ e outras informações úteis para os clientes.
- **Redes Sociais**: Links para as redes sociais da PATADA (Facebook e Instagram).
- **Políticas**: Inclui links para a política de privacidade, política de entrega e devolução e política de compra da loja.

## Tecnologias Usadas

- **HTML5**: Estrutura básica do site.
- **CSS3**: Usado para estilizar o site e torná-lo visualmente agradável.
- **JavaScript**: Incluído para o funcionamento do carrossel de imagens.
- **Bootstrap Icons**: Usado para ícones de redes sociais.

## Estrutura de Arquivos

- `index.html`: Página inicial da loja.
- `cadastro.html`: Página de cadastro do cliente.
- `css/style.css`: Arquivo de estilos para todas as páginas do site.
- `js/script.js`: Arquivo JavaScript com a funcionalidade do carrossel.
- `imagens/`: Pasta com as imagens usadas no carrossel e nos produtos.

## Como Usar

1. Clone ou baixe o repositório.
2. Abra o arquivo `index.html` em seu navegador para visualizar a página principal.
3. Acesse o link "Cadastro" no menu de navegação para testar a funcionalidade de cadastro de cliente.
4. Navegue pelas seções para visualizar produtos para cães, gatos e serviços de vacinação.

## Personalização

Você pode personalizar o site alterando as imagens e textos para adaptá-lo às suas necessidades. Basta substituir as imagens na pasta `imagens/` e editar o conteúdo dos arquivos HTML e CSS conforme desejado.

## Créditos

Site desenvolvido por **Arthur zKrause**.
