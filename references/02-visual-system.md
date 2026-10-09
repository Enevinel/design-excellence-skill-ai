# 02 — Linguagem visual, design tokens e 4-point grid

## Uma interface, uma gramática

Toda interface deve compartilhar princípios de proximidade, alinhamento, repetição, contraste, hierarquia e gestalt. Escolhas visuais isoladas produzem fragmentação; o design system converte decisões em tokens auditáveis.

### Primitivos e decisões

1. **Cor:** roles `canvas`, `surface`, `surface-muted`, `content-primary`, `content-secondary`, `border-subtle`, `interactive`, `interactive-hover`, `interactive-foreground`, `focus`, `success`, `warning`, `danger` e variações dark.
2. **Tipografia:** famílias, pesos, escala, comprimento de linha, trackings e estilos semânticos (`display`, `h1`, `h2`, `body`, `label`, `caption`, `data`). A função é mais importante que o tamanho nominal.
3. **Espaçamento:** use **4pt grid** em CSS px para UI web. Estabeleça base 4 e priorize 8 para ritmo. Escala 4/8/12/16/20/24/32/40/48/64/80/96 (não precisa usar todos).
4. **Bordas:** `1px` discreto é uma ferramenta de separação; não circunde tudo; divisores podem ser substituídos por respiro e alinhamento.
5. **Radius:** pequeno/médio/grande por contexto e marca. Prefira um sistema com poucos degraus a usar arredondamento aleatório. Cantos de botão, card e modal não precisam ter o mesmo valor.
6. **Elevação:** sombras para hierarquia de sobreposição, não em cada card. Painéis podem ser separados por cor de superfície, sem glow.
7. **Grid:** colunas, margens laterais, gutters, largura de texto e largura máxima; evite esticar parágrafos na largura do monitor.
8. **Iconografia:** família coerente, mesmo peso óptico, metáforas compreensíveis e sempre um label quando a ação possa ser ambígua.
9. **Visual assets:** direitos de uso, coerência de cor e direção de fotografia; evite stock sintético e rostos falsamente atribuídos a clientes.

### 4-point grid: como aplicar corretamente

O 4-point grid descreve **distâncias sistemáticas**, não uma imposição matemática universal. A regra dominante vale para padding, gap, margem, dimensões de controles e escala de layout. Exceções com propósito: `1px` de borda, offsets ópticos, proporção de imagens, composição tipográfica, ícones produzidos em grids próprios e medições nativas de plataformas.

Exemplo de pares e escalas:

| Uso | Faixa inicial sugerida, ajustar ao produto |
|---|---|
| Entre label e input | 4–8px |
| Gap de controles relacionados | 8–12px |
| Padding de controle | 12–16px horizontal e altura confortável |
| Espaço entre grupos de formulário | 16–24px |
| Padding de seção mobile | 16–24px |
| Padding de seção tablet | 24–40px |
| Padding de seção desktop | 40–80px |
| Gap entre seções marcantes | 48–96px conforme densidade |

Não transforme a tabela em constantes obrigatórias. Composição editorial espaçosa e dashboards densos terão necessidades distintas.

### Tipografia: critérios reais

- Prefira texto de corpo em torno de **16px CSS ou mais**, sujeito a fonte, legibilidade, produto e zoom; legendas menores não podem carregar informação crítica sem solução acessível.
- Para conteúdo longo, linha com aproximadamente **45–75 caracteres** como ponto de partida editorial; não é regra WCAG.
- `line-height`: texto corrido frequentemente se beneficia de `1.45–1.7`; títulos de proporção mais compacta. Respeite personalização de espaçamento (WCAG 1.4.12).
- Diferencie `h1` de `h2` pela composição, não apenas por “aumentar 4px”. Use `clamp()` em texto fluido com limites legíveis.
- Numerais tabulares (`font-variant-numeric: tabular-nums`) em tabelas e dashboards; números alinhados à direita para comparação.
- Truncamento deve preservar acesso ao conteúdo integral; evite reticências em preço, nome importante, campo de erro e identificador.
- Não use uppercase/tracking largo em textos extensos; evita cansaço e perda de acessibilidade.

### Contraste cromático e semântico

Defina os pares **foreground/background**, incluindo states. Teste texto sobre: canvas, surface, CTA, alertas, imagens/gradientes, hover, focus e dark mode. Cor de marca não é automaticamente cor legível para texto. Se a paleta não permite boa leitura, adapte **luminosidade dos papéis** sem alterar necessariamente a cor institucional no logo.

Use ferramenta `scripts/check_contrast.py` para pares hex opacos, depois avalie pixels reais. Desabilitado pode ter contrastes distintos sob WCAG (elementos inativos têm exceção em certos critérios), mas deve permanecer compreensível visualmente e nunca ser a única indicação de uma restrição relevante.

### Tokens como contrato entre design e código

Consulte o exemplo operacional `assets/tokens.example.css`. Tokens primitivos e semânticos podem coexistir: `--blue-600` descreve tinta, `--color-action` descreve intenção. Componentes consomem preferencialmente tokens **semânticos**.

### Checklist de maturidade

- Mesmo item visual possui o mesmo propósito em todas as telas.
- Tipografia organiza o conteúdo mesmo sem decoração.
- Um único componente não possui cinco variantes quase iguais sem necessidade.
- Não há “números mágicos” replicados para gap, radius e cor.
- Light/dark são projetos intencionais, não inversão automática de cor.
- O sistema aceita tradução, zoom, conteúdo longo e estados excepcionais.
