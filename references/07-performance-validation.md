# 07 — Performance, métricas e validação contínua

## Metas de experiência (não promessas)

Os limiares de Core Web Vitals considerados bons pelo Google são:

- **LCP ≤ 2.5 s**: principal conteúdo carregado.
- **INP ≤ 200 ms**: resposta a interações.
- **CLS ≤ 0.1**: estabilidade do layout.

Verifique **p75** de dados reais quando disponíveis, separando mobile/desktop e dados de laboratório/campo. Fonte: https://web.dev/articles/vitals

### Requisitos práticos

- Imagens: dimensões explícitas, formatos modernos quando compatíveis, `srcset`/`sizes` coerentes, corte planejado, lazy load fora da primeira dobra; evite `loading="lazy"` na imagem provável de LCP.
- Fontes: pesos reduzidos, subsets, `font-display`, preload seletivo, fallback métrico; não carregue cinco famílias para hero.
- Layout: reserve altura para mídia e anúncios, evite fontes e banners causando deslocamento; testar expansão de erros.
- JavaScript: reduza código cliente e bibliotecas pesadas; code splitting, server rendering/cache onde faz sentido, listas virtualizadas somente quando necessário.
- Vídeo/3D: lazy load e fallback estático, pause fora da tela, não exigir GPU poderosa para compreender produto; evite WebGL supérfluo.
- Interação: evite re-render global, handlers pesados na thread principal e drag com tarefas síncronas custosas.
- Redes lentas: skeleton/placeholder coerente, timeout, retry, progresso e feedback.

## Pipeline de QA para implementação

1. **Análise estática:** lint, formatação, TypeScript/typecheck, imports, dependências.
2. **Build e testes:** unidade/integração/E2E onde houver; não dizer “compila” sem executar.
3. **A11y automática:** axe-core/Playwright/Lighthouse para checagem parcial; registrar findings, nunca presumir AA completo.
4. **A11y manual:** teclado puro, leitor de tela quando disponível, zoom, cor, foco, motion, forms.
5. **Visual:** comparação nas larguras da matriz mobile/tablet/desktop e estados extremos (empty, error, nome longo, muitas linhas, locale).
6. **Dados:** conteúdo e links reais, preços verdadeiros, erro/latência, sem números inventados.
7. **Performance:** Lighthouse para laboratório, Web Vitals/RUM para campo. Explicitar limitação do ambiente.
8. **Robustez:** offline, erros HTTP, imagem ausente, sem JS quando aplicável, novas abas e deep links.
9. **Privacidade e segurança:** XSS em dados renderizados, sanitização, formulários com validação no servidor; não vazar dados em logs ou JSON-LD.

## Testes exemplares em Playwright (quando projeto permitir)

```ts
import { test, expect } from '@playwright/test';

test('a página preserva landmarks e heading principal', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('main')).toHaveCount(1);
  await expect(page.getByRole('heading', { level: 1 })).toHaveCount(1);
  await expect(page.getByRole('navigation')).toBeVisible();
});

for (const width of [320, 390, 768, 1024, 1440]) {
  test(`sem overflow horizontal não intencional em ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 900 });
    await page.goto('/');
    const overflow = await page.evaluate(
      () => document.documentElement.scrollWidth > document.documentElement.clientWidth
    );
    expect(overflow).toBe(false);
  });
}
```

**Atenção:** o teste acima assume página com `nav` e um único `h1`; adapte quando o caso real diferir. Scroll interno legítimo em tabelas ou sliders pode ser permitido sem overflow global. O teste automático de `main` não detecta se ele contém a informação correta.

### Critério para entrega

Relate `o que executou`, `o que passou`, `o que falhou`, `o que não conseguiu testar`, `próximos passos`. Não confunda a ausência de violações reportadas por ferramenta com acessibilidade plena.
