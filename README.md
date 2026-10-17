# MKT-N1 — Relatório de Fechamento das UCs de E-commerce

Hotsite estático em HTML5, CSS3, JavaScript Vanilla e Bootstrap 5 para documentar projetos, registros, processo, aprendizados e recomendações da turma MKT-N1.

## Como executar

Abra `index.html` diretamente no navegador ou use o Live Server do Visual Studio Code. A página utiliza Bootstrap e Bootstrap Icons via CDN; para execução totalmente offline, baixe essas dependências e substitua os links no `index.html`.

## Estrutura

```text
index.html
css/style.css
js/app.js
js/projects.js
assets/images/galeria/   # fotos locais
assets/images/screenshots/ # screenshots dos seis projetos
assets/videos/            # vídeos locais
```

## Como adicionar fotos

Coloque arquivos JPG, JPEG, PNG ou WebP em `assets/images/galeria`. Para alterar categorias, filtros e legendas, edite o array `cats` em `js/app.js`. A galeria já inclui lazy loading e modal.

## Como adicionar vídeos

Coloque o arquivo em `assets/videos` e altere o `<source>` em `index.html`. Mantenha `controls` e `preload="metadata"`; não use autoplay.

## Como adicionar screenshots

Cada projeto possui uma página própria em `projeto.html?id=1` até `projeto.html?id=6`. As screenshots capturadas das homes estão em `assets/images/screenshots/projeto01-01.png` até `projeto06-01.png`. Para trocar uma imagem, substitua o arquivo mantendo o nome ou atualize o campo `screenshots` em `js/projects.js`.

## Como alterar os projetos

Edite somente `js/projects.js` para atualizar nome, segmento, URL, público, descrição, recursos, análise de marketing, solução tecnológica e screenshots.

## Publicação

O projeto pode ser publicado como site estático em GitHub Pages, Netlify, Vercel ou hospedagem convencional. No GitHub Pages, suba a pasta em um repositório, selecione a branch e a pasta raiz em **Settings → Pages**.

## Roadmap curricular e roteiros em PDF

O arquivo `assets/docs/Plano-de-Curso-339-Tecnico-em-Marketing.pdf` é uma cópia do plano de curso fornecido para análise. A página `conteudo.html?pagina=roadmap` apresenta uma matriz UC por UC, associando fundamentos e tecnologias ao momento pedagógico recomendado, sem alterar as UCs, cargas horárias ou correquisitos oficiais.

Os quatro roteiros completos para download ficam em `assets/docs/roadmaps`:

- Trilha linear integrada;
- Projeto transversal de um negócio;
- Laboratório digital por desafios;
- Agência-escola e portfólio profissional.

Os PDFs são propostas de implementação e não substituem o Plano de Curso oficial.
Eles seguem a identidade visual do site e incluem capa, orientação de uso, etapas didáticas, entregáveis, checkpoints, tecnologias por momento, avaliação formativa e matriz UC por UC. Para regenerá-los após alterar os dados, execute `python scripts/generate_roadmaps_rich.py`.

## Checklist docente e formulário de avaliação

A página `conteudo.html?pagina=checklist` mantém o checklist de preparação e acrescenta uma avaliação fechada do desenvolvimento das equipes. São 18 perguntas organizadas em seis temas: letramento digital; estratégia e pesquisa; produção visual e conteúdo; tecnologia e IA; e-commerce, CRM e ERP; colaboração e projeto.

Cada pergunta usa a escala `1` (não evidenciado), `2` (inicial), `3` (em desenvolvimento), `4` (consolidado) ou `N/A` (não observado). As respostas ficam salvas localmente no navegador, e a página calcula uma leitura geral para orientar a próxima intervenção pedagógica.

O formulário imprimível, com explicação de cada opção, evidências/comentários e plano de ação, está em `assets/docs/formularios/formulario-avaliacao-desenvolvimento-equipes.pdf`. Para regenerá-lo, execute `python scripts/generate_checklist_form.py`.

## Observações

As seis aplicações foram consultadas no ambiente de origem em 17/10/2026. Os textos descrevem somente elementos identificados nas páginas e rotas acessíveis. A home foi capturada em screenshot para cada projeto. Os conteúdos foram divididos entre a home executiva, `projetos.html`, páginas individuais de projeto e `conteudo.html?pagina=...` para os eixos do relatório.
