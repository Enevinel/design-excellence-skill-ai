# 09 — Gates de reprovação e rubrica de excelência

## Gates bloqueantes — a nota não compensa uma falha crítica

Reprove ou marque como **não pronto para produção** quando houver:

- Tarefa principal impossível, CTA sem ação, fluxo crítico quebrado ou dados que não podem ser salvos com segurança.
- Contraste de texto/interação obrigatório abaixo do mínimo WCAG aplicável, ausência de teclado em ação crítica, trap de foco ou componente essencial sem nome acessível.
- Estouro horizontal global não intencional no mobile ou conteúdo crítico cortado em zoom/reflow.
- Conteúdo falso apresentado como verdadeiro (números, pessoas, depoimentos, preços, selos/certificações).
- Navegação/semântica radicalmente quebrada a ponto de tornar a experiência incompreensível a assistivos.
- Vulnerabilidade conhecida introduzida pela mudança, exposição de dados privados ou schema com afirmações falsas.
- Dependência visual essencial que não carrega em contexto realisticamente suportado e não possui fallback.

Uma falha bloqueante deve indicar `onde`, `como reproduzir`, `impacto`, `correção` e `status`.

## Rubrica heurística (0–100)

| Critério | Peso | Perguntas |
|---|---:|---|
| Clareza e UX | 18 | Usuário entende valor e conclui tarefas sem fricção? |
| Acessibilidade e inclusão | 18 | Contraste, teclado, foco, nomes, semântica e zoom? |
| Responsividade | 14 | Mobile real, tablet próprio, desktop e conteúdo longo? |
| Identidade e excelência visual | 14 | Coesão, qualidade editorial e diferenciação sem clichês? |
| Arquitetura e conteúdo | 10 | Hierarquia, rotas, microcopy, estados e dados reais? |
| Componentização e tokens | 9 | Consistência, escalas, manutenção e 4pt grid? |
| Performance e robustez | 9 | LCP/INP/CLS, estado de rede, peso de mídia/JS? |
| Semântica e SEO/schema contextual | 8 | HTML apropriado, metadados e schema legítimo? |
| **Total** | **100** | |

**Avaliação de cada eixo:** 0–4 pontos, convertidos proporcionalmente ao peso: `pontos = peso × nota_do_eixo / 4`. Use evidências; se não testado, marque `não verificado` em vez de dar 4.

### Interpretação interna (heurística, não certificação)

- `95–100`: excepcional, sem gates bloqueantes, evidência muito forte.
- `88–94`: pronto para revisão final, com ajustes pontuais.
- `75–87`: bom trabalho, mas com itens relevantes pendentes.
- `<75`: revisar fundamentos, fluxos e consistência.

**Nunca escreva “aprovado pela Apple/Google/etc.” com base nessa nota**. Trata-se de review interno.

## Protocolo de review em 2 passadas

**Passada 1 — destrutiva:** procure primeiro inconsistências, erros de fluxo, dados falsos, más decisões de tipografia, clichês de IA, tablet esquecido, quebras de zoom, cores ilegíveis, componentes supérfluos.

**Passada 2 — reconstrutiva:** priorize correções por `severidade × frequência × custo de mudança`, aplique melhorias em ordem e reteste estados afetados.

## Relatório obrigatório de saída (quando fizer auditoria)

```markdown
### Veredito
[Pronto / Pronto com ressalvas / Não pronto] — [motivo]

### Gates
- [ ] Principais tarefas e navegação
- [ ] Contrastes, teclado, foco e semântica
- [ ] Mobile/tablet/desktop e reflow
- [ ] Conteúdo real e privacidade
- [ ] Ausência de falhas bloqueantes conhecidas

### Pontuação heurística
UX __/18 | A11y __/18 | Responsividade __/14 | Visual __/14 |
Conteúdo __/10 | Sistema __/9 | Performance __/9 | SEO/Semântica __/8
Total __/100 (eixos não verificados: __)

### Prioridades
1. P0 — ... (evidência, proposta, critério de aceite)
2. P1 — ...
3. P2 — ...

### Testes realizados / não realizados
...
```

Reprovação não significa fracasso do criador: significa impedir que dívida de experiência chegue ao usuário final.
