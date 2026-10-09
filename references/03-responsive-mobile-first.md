# 03 — Mobile first, tablet de verdade e design adaptativo

## Ordem de desenho e implementação

1. **Mobile (320–428px como amostragem):** conteúdo essencial, prioridade, sequência de leitura, alcance das ações, alvos, largura e formulários.
2. **Intermediário (aprox. 600–767):** priorize composição sem sobras ou colunas artificiais.
3. **Tablet (ex.: 768–1024):** reveja navegação, densidade, split view, orientação, touch e conteúdo simultâneo.
4. **Desktop (1280+):** permita comparação, navegação persistente, densidade inteligente e variações de layout; evite largura de leitura excessiva.
5. **Ultra-wide:** limite áreas de leitura, preserve espaços negativos e organize painéis; não expanda tudo até as bordas.

Esses tamanhos são **pontos de teste**, não divisões oficiais universais. Os breakpoints devem aparecer quando o conteúdo exigir.

## Fundamentos responsivos

- CSS base sem media query corresponde a mobile. Amplie com `@media (min-width: ...)` e, para componentes, avalie `@container`.
- Use `minmax(0, 1fr)`, `max-width`, `min-width: 0`, `overflow-wrap: anywhere` quando útil para impedir overflow.
- Use CSS Grid para estruturas bidimensionais e Flexbox para alinhamento de fluxos locais.
- Evite alturas fixas em cards de texto, CTA, modal e conteúdo dinâmico; considere expansão por localização.
- Para imagens: `aspect-ratio`, `object-fit`, recorte intencional por formato, dimensões para evitar CLS e texto alternativo apropriado.
- Para gráficos: legenda persistente, eixo legível e opção de tabela/texto; no smartphone considere comparação por item ou scroll **restrito à tabela** com contexto de cabeçalho.
- Tabelas grandes: preserve significados, prefira scroll horizontal **localizado e sinalizado**, em vez de transformar valores com relação tabular em cards aleatórios.
- Menu mobile: affordance clara, botão verdadeiro com nome e estado expandido, foco e Escape quando aplicável. Não esconder a navegação mais importante em camadas excessivas.
- Telas de login/cadastro: teclado virtual, tipos corretos `inputmode`, autocomplete, foco, safe area e fluxos interrompidos.
- Respeite área segura (`env(safe-area-inset-*)`) quando barras/fixed UI chegarem às bordas.
- `100vh` pode falhar com barras móveis; avalie `100dvh`, `100svh` e fallback.

## Tablet é uma experiência própria

Em 768–1024, uma sidebar persistente pode consumir largura demais. Considere sidebar recolhível, two-pane quando há tarefa mestre-detalhe, barra de ações simplificada e flexibilidade portrait/landscape. Evite forçar três colunas pequenas só para reutilizar desktop.

**Teste tablet em pé e deitado**. O meio termo visual normalmente é onde os sistemas falham.

## Conteúdo e SEO mobile-first

Google recomenda design responsivo e usa o conteúdo da versão mobile para indexação: https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing

Por isso:
- Mantenha título, texto importante, links e dados estruturados equivalentes em mobile/desktop.
- Não dependa de gesto, hover, clique ou JS tardio para expor ao crawler o conteúdo essencial.
- Quando precisar condensar, use disclosure/acordeão semanticamente correto; não remova informação essencial.

## Matriz de teste mínima

| Contexto | Testar |
|---|---|
| 320px / smartphone pequeno | Sem overflow, botões acionáveis, textos longos |
| 360–428px / smartphone comum | Hierarquia, CTA, safe area, teclado virtual |
| 600px intermediário | Mudanças suaves sem buracos no layout |
| 768px tablet retrato | Navegação, densidade, touch, formulário |
| 1024px tablet paisagem | Dual pane, conteúdo, navegação e scroll |
| 1280–1440px desktop | Hierarquia, leitura, alinhamento, foco |
| 1920px / ultrawide | Máximo de largura, não alongar parágrafos |
| Zoom 200% texto / 400% página | Reflow, não clipping/overlap quando aplicável |
| Teclado, touch e mouse | Alternativas ao hover e dragging |
| Texto 2x / tradução 30–50% maior | Sem cortes de campo, label ou CTA |

**Critério de reprovação:** o design funciona “só no Figma” ou quebra no tablet, zoom e textos reais.
