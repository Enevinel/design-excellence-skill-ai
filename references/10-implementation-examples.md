# 10 — Exemplos de implementação (adaptar ao contexto real)

## 1. Mobile-first sem excesso de breakpoints

```css
.page {
  width: min(100% - 32px, 1200px);
  margin-inline: auto;
}

.feature-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: var(--space-6); /* 24px */
}

.hero__title {
  max-width: 18ch;
  font-size: clamp(2rem, 1.25rem + 3vw, 4.5rem);
  line-height: 1.08;
  letter-spacing: -0.035em;
  text-wrap: balance;
}

@media (min-width: 48rem) { /* tablet quando o layout precisar */
  .page { width: min(100% - 64px, 1200px); }
  .feature-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}

@media (min-width: 72rem) { /* desktop quando conteúdo permitir */
  .feature-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}
```

O breakpoint depende do componente e conteúdo. `72rem` é um exemplo, não preset universal. O seletor `--space-6` representa o sexto token de espaçamento do exemplo; prefira nomes consistentes com o projeto.

## 2. Focus e reduced motion

```css
:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 3px;
}

html { scroll-behavior: smooth; }

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

Esse é um fallback simples; em produtos sofisticados, substitua animações essenciais por alternativas acessíveis em vez de zerar indiscriminadamente feedback funcional.

## 3. Formulário realmente semântico

```tsx
function EmailField({ error }: { error?: string }) {
  const id = 'email';
  return (
    <div className="field">
      <label htmlFor={id}>E-mail profissional</label>
      <input
        id={id}
        name={id}
        type="email"
        autoComplete="email"
        inputMode="email"
        aria-invalid={Boolean(error)}
        aria-describedby={error ? 'email-error' : undefined}
        required
      />
      {error && <p id="email-error">{error}</p>}
    </div>
  );
}
```

Nota: IDs fixos servem para **uma instância por página**. Para componentes repetidos, use `useId()` para gerar IDs únicos para `label`/ajuda/erro.

## 4. Navegação semântica e CTA verdadeiro

```tsx
export function MainNavigation() {
  return (
    <header className="site-header">
      <nav aria-label="Navegação principal">
        <a href="/">Início</a>
        <a href="/recursos">Recursos</a>
      </nav>
      <a className="button button--primary" href="/cadastro">Criar conta</a>
    </header>
  );
}
```

O CTA navega, então é `<a>` estilizado como botão. Uma ação local (`onClick`) deve utilizar `<button>`.

## 5. Checklist para code review

- [ ] HTML reflete significado do conteúdo e hierarquia real?
- [ ] Responsividade começa no CSS base (mobile), incluindo tablet?
- [ ] Tokens de cores e espaçamento substituem valores mágicos?
- [ ] Contrastes verificados e foco visível?
- [ ] Interações completas com teclado, mouse e touch?
- [ ] Estados `loading`, `empty`, `error` e `success` fazem sentido?
- [ ] Texto e layout resistem a tradução, zoom e conteúdo longo?
- [ ] Fontes/imagens não causam CLS e fluxo crítico não carrega JS excessivo?
- [ ] `schema.org` só foi implementado se a página e os dados justificam?
- [ ] Os testes e limitações da entrega foram informados honestamente?
