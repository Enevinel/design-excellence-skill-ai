# 04 — Acessibilidade inclusiva: WCAG 2.2 AA + ergonomia

**Referência normativa:** https://www.w3.org/TR/WCAG22/
**Padrões de interação:** https://www.w3.org/WAI/ARIA/apg/
**Apple:** https://developer.apple.com/design/human-interface-guidelines/accessibility
**Microsoft:** https://fluent2.microsoft.design/accessibility

## Contraste — medir, não supor

- Texto normal e imagem de texto não incidental: **4.5:1** (WCAG AA, SC 1.4.3).
- Texto grande: **3:1**; grande = pelo menos **18pt (~24 CSS px)** em peso normal ou **14pt (~18.66 CSS px)** bold, assumindo escala CSS padrão.
- Componentes de UI e partes gráficas necessárias para compreender ou operar: **3:1** em relação a cores adjacentes pertinentes (SC 1.4.11), observadas exceções.
- Não equipare um badge colorido a semântica: incorpore texto/ícone/label.
- Teste cores efetivamente renderizadas em light, dark, focus, hover, fotos e fundos com transparência. Elementos visualmente desabilitados podem ser isentos de determinados mínimos WCAG, **mas isso não elimina obrigações de informação clara**.
- `AAA` (quando explicitamente exigido) amplia alvos de contraste, mas **não é obrigatório** para cumprir AA.

## Tamanhos, foco e navegação

- Padrão ergonômico sugerido para mobile web: **44×44 CSS px** em controles importantes; em iOS, o HIG cita **44×44 pt** como dimensão padrão de controle. São métricas diferentes.
- **WCAG 2.2 AA SC 2.5.8:** alvo mínimo **24×24 CSS px** ou exceções (incluindo spacing, equivalência, inline, controle do agente ou essencialidade); não declare que 44px é obrigação WCAG.
- Foco visível (SC 2.4.7 AA) e não totalmente oculto (SC 2.4.11 AA). `Focus Appearance` (2.4.13) é **AAA**; uma borda 2px/3:1 é prática forte, não exigência universal AA.
- Ordenação de tabulação corresponde à estrutura visual/lógica; não use `tabindex>0`. Ações e dialogs devem retornar foco para origem quando apropriado.
- Todas as funções operáveis por teclado. Se houver drag/drop, ofereça alternativa por botões ou outra operação sem arrastar (SC 2.5.7 AA).
- Links são links, botões são botões, cada controle tem rótulo acessível. Ícones sem texto em controles precisam de nome claro.

## Semântica, leitura e tecnologia assistiva

- Documento com `lang="pt-BR"` ou idioma apropriado; marque mudanças de idioma quando necessárias.
- Um landmark `main`, regiões de navegação nomeadas, títulos ordenados e skip link.
- Inputs com `<label>` associado; `aria-describedby` para ajuda/erro; `aria-invalid` quando inválido; mensagens de estado com `role="status"` ou `aria-live` quando apropriado — não anuncie todas as mudanças de forma ruidosa.
- Prefira HTML nativo a ARIA: usar `div role="button"` exige implementar teclado/estado que `<button>` já fornece.
- Imagens informativas com alt conciso e contextual; decorativas com `alt=""`; figuras com legenda quando necessário. Gráficos complexos precisam resumo e dados acessíveis.
- Vídeos com legendas, e conteúdo relevante com transcrição/audiodescrição se aplicável.
- Não substitua CAPTCHA ou autenticação por tarefas de memória/cálculo sem alternativas acessíveis; facilite copiar/colar senhas e gerenciadores.

## Reflow e preferências do usuário

- Reflow sem perda de conteúdo ou funcionalidade em equivalência a viewport estreita de **320 CSS px** nos termos da WCAG 1.4.10 (com exceções justificadas para apresentação bidimensional como mapas/tabelas).
- Text resize 200% e ajustes de espaçamento sem cortar conteúdo. Respeite `prefers-reduced-motion`, `prefers-contrast` quando compatível, forced colors e configurações de fonte.
- Nunca bloqueie portrait/landscape desnecessariamente.
- `touch-action`, scroll lock e eventos de ponteiro não devem impedir navegação assistiva.

## Teste manual + automação

Axe, Lighthouse ou eslint detectam apenas subconjunto de problemas. Complemente com:

1. Percorra fluxos **somente com Tab/Shift+Tab/Enter/Space/Escape**.
2. Verifique foco em dialogs, dropdowns, date pickers, toasts, menús e página após navegação SPA.
3. Teste com VoiceOver (Safari/iOS) ou NVDA (Windows), quando possível.
4. Teste alto contraste, dark mode, zoom e movimento reduzido.
5. Confira pares reais com `scripts/check_contrast.py`; analise em imagens/gradientes manualmente ou via ferramenta de inspeção de pixels.
6. Verifique erros, instruções, estado expandido e condições sem internet.

## Linguagem de conformidade

**Correto:** “Projetado para WCAG 2.2 AA, com contraste automatizado em pares X e Y; testes de leitor de tela pendentes.”

**Incorreto:** “100% acessível, certificado WCAG AA” sem auditoria formal, escopo e evidências.
