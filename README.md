# Achados e perdidos ![Badge](https://img.shields.io/static/v1?label=tailwindcss&message=v3.1.8&color=lightblue&style=flat&logo=TAILWINDCSS)  ![Badge](https://img.shields.io/static/v1?label=django&message=v4.1.3&color=darkgreen&style=flat&logo=DJANGO)
 
<br />
<p align="center">
  <img src="https://github.com/ImFelippe365/lost-and-found/blob/main/static/svg/logo-colorful.svg" />
</p>
<br />

Sistema desenvolvido em django capaz de gerenciar o Achados e Perdidos do IFRN - Campus Pau dos Ferros, onde é possível gerenciar os itens e suas informações para 
visualização do público. A ideia é que as pessoas estejam cientes dos itens que foram encontrados nas dependencias do campus, e que estão em boas mãos, apenas no
aguardo pela reivindicação de seu respectivo dono.

## ⚠️ Importante

Projeto desenvolvido na disciplina de Desenvolvimento de Projetos I, utilizando os conhecimentos adquiridos nas demais, como Banco de Dados,
A.P.O.O (Análise de Projeto Orientado a Objeto) e Desenvolvimento de Sistemas Web. 

## Documentação

- [📄 Requisitos funcionais/não funcionais](https://docs.google.com/document/d/1k6iyMif7JBYWqFZr6DYuE6BhKITYCGbwaOYUaZEvZ2c/edit?usp=share_link)
- [👩🏻‍💻 Casos de uso](https://drive.google.com/file/d/1amFtxJyLK-zctjWa07qfXQijiTyQHaK2/view?usp=share_link)
- [🖌️ Protótipo da interface (figma)](https://www.figma.com/file/TXJJujEIJa6hu9stL3my2E/Lost-%26-Found?node-id=610%3A2&t=RNjaDMX6VKs3griU-1)
- [⚙️ Modelo lógico](https://drive.google.com/file/d/17b4GmaiIXhSfJhieznj52OoQVe8qvc-q/view?usp=share_link)
- 💭 Diagrama de classes
- 💭 Diagrama de sequência

## Tecnologias utilizadas

- Django
- TailwindCSS

## A fazer

- [x] Criar formulários usando Django
- [x] Organizar melhor as aplicações
- [x] Autenticação via SUAP
- [x] Configurar permissões do usuário (entrar nas páginas)
- [x] Ajustar botões de cancelar dos formulários
- [x] Inserir ícone do site
- [ ] Configurar tipo de dado a ser pesquisado nos registros
- [x] Sistema de buscar e ordenar itens
- [ ] Expirar itens de acordo com data
- [x] Criar tela de confirmação para apagar item
- [x] Mostrar avisos de erros e sucessos ao tentar logar
- [x] Compartilhar postagem
- [x] Criar página de erro 404
- [x] Substitutir página padrão de erro 404
- [ ] Inserir erro de não ter permissão para acessar a página no login
- [x] Adicionar CPF a documentação e o campo do mesmo na página de "definir como entregue"
- [x] Criar imagem no figma e implementar para os itens que não tem foto
- [ ] Restringir acesso apenas para os funcionários
- [ ] Resolver bug de acessar edição do item já entregue
- [ ] Alterar estilo da data de limite para retirada

## Instalação

Antes de instalar, é importante criar um ambiente virtual e inicia-lo para baixar as dependencias dentro dele.
Para instalar e usar pelo repositório, clone o repositório e instale as dependências usando o seguinte comando no diretório raiz.

```
pip install -r requirements.txt
```

