# 06 — Interações, motion, formulários e conteúdo

## Design de interação: previsível, reversível e responsivo

Cada gesto deve corresponder a uma intenção e oferecer feedback. Um CTA deve responder, um envio deve informar progresso e erros devem dar caminho de recuperação. Não substitua um fluxo compreensível por uma animação impressionante.

### Estados por componente (avaliar pertinência)

| Componente | Estados/ações essenciais |
|---|---|
| Botão | padrão, hover (mouse), foco, pressionado, loading, sucesso/erro, disabled verdadeiro |
| Campo | vazio, com valor, foco, preenchimento automático, erro, instrução, success quando útil |
| Menu | fechado, aberto, item atual, navegação teclado, escape/fora, retorno de foco |
| Modal | abertura, foco inicial, travamento adequado, fechar, retorno de foco, mobile e scroll |
| Tabela/lista | carregando, vazio, erro, paginação/filtros, estados de seleção, ordenação acessível |
| Notificação | tipo, duração adequada, possibilidade de fechar/recuperar, anúncio não intrusivo |
| Upload | seletor e drop alternativos, progresso, tipo/tamanho, erro e retry |
| Checkout | edição, custos totais, confirmação, falha de pagamento e recuperação |

Estados `disabled` devem ser usados quando realmente não há ação possível, com mensagem explicativa se o motivo for relevante; considere descrever validações sem desabilitar indefinidamente o CTA.

## Motion com causalidade

Use animação **quando esclarece movimento, transição, estado ou identidade**. Um pequeno deslocamento pode mostrar relação pai-filho; fade suave pode sinalizar conteúdo atualizado. Evite scroll-jacking, parallax agressivo, motion infinito ou transições que atrasam tarefas.

- Animações de interface muitas vezes cabem em **120–300ms** como ponto de partida editorial; não é padrão obrigatório. Duração deve acompanhar distância, hierarquia e contexto.
- Anime preferencialmente `transform`/`opacity` quando possível; respeite o compositor e dispositivos modestos.
- `prefers-reduced-motion: reduce` implica reduzir/desabilitar efeitos não essenciais, **não apenas torná-los um pouco mais rápidos**.
- O componente deve funcionar integralmente sem animação.
- Nunca esconda informações atrás de hover sem suporte a touch, teclado e leitores de tela.

## Microcopy: clareza e humanidade sem ruído

- CTAs são ações específicas: “Criar proposta”, “Ver preços”, “Agendar demonstração”, não “Começar a revolução”.
- Feedback de erro diz **o que houve** e **como resolver**: “Não conseguimos enviar. Verifique a conexão e tente novamente.”
- Empty states ajudam a iniciar uma tarefa real: “Nenhum pedido neste período. Ajuste os filtros.”
- Confirmação em ações destrutivas especifica objeto, consequência e, se aplicável, desfazer.
- Copy reduz ansiedade em pagamentos e privacidade explicando termos e dados coletados.
- Tipografia deve acomodar plural, números, valores monetários e localização.

## Acessibilidade de mensagens e feedback

- Use rótulo visível para inputs; placeholder **não substitui label**.
- Erros do formulário devem ter texto, `aria-invalid` e descrição conectada.
- Anuncie status relevantes uma vez; evite excesso de `aria-live` e toasts simultâneos.
- Não faça campos “saltarem” em layout ao apresentar erro; reserve espaço ou planeje reflow.
- Para indicadores de progresso, ofereça representação textual de etapa/porcentagem quando fizer sentido.

## Privacidade, confiança e ética

- Não manipule usuário com dark patterns: contadores inventados, urgência falsa, pré-seleção enganosa, botões de cancelamento disfarçados ou custos ocultos.
- Provas sociais apenas quando existem; depoimentos reais com permissão; números verificáveis.
- Nunca use “antes/depois” enganoso como prova de resultados; identifique dados de exemplo.
- Colete apenas informação necessária; não apresente campos opcionais como obrigatórios.

## Avaliar motion como sistema

Documente `trigger`, `estado inicial/final`, `duração`, `easing`, `comportamento reduzido`, `impacto de desempenho` e `feedback assistivo`. Motion sem documentação vira dívida técnica.
