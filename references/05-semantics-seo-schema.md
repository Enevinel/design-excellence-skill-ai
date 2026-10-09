# 05 — HTML semântico, estrutura, SEO e schemas

## HTML pela função, não pelo formato

```html
<a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header">
  <a href="/" aria-label="Início — Nome da marca">Marca</a>
  <nav aria-label="Navegação principal">
    <ul><li><a href="/solucoes">Soluções</a></li></ul>
  </nav>
</header>
<main id="conteudo">
  <section aria-labelledby="titulo-principal">
    <h1 id="titulo-principal">Uma proposta de valor específica</h1>
    <p>Explicação que deixa o benefício claro.</p>
    <a href="/contato">Solicitar demonstração</a>
  </section>
  <section aria-labelledby="beneficios">
    <h2 id="beneficios">Benefícios comprováveis</h2>
    <article><h3>Benefício A</h3><p>Detalhe.</p></article>
  </section>
  <aside aria-label="Informações complementares">...</aside>
</main>
<footer class="site-footer">...</footer>
```

**Observações:**
- `header`/`footer` podem ocorrer em `article` e outros contextos; não são obrigatoriamente globais.
- `section` representa tópico, normalmente com título; `div` é preferível para wrappers puramente visuais.
- `article` é unidade autocontida, reutilizável; não use para cada célula decorativa.
- `aside` serve ao conteúdo relacionado, não como nome obrigatório para toda sidebar de navegação.
- `h1` geralmente principal por documento; título visual e nível semântico são conceitos diferentes.
- Nunca salte títulos só para obter aparência. Heading order coerente, sem obrigação de sequência linear artificial se a estrutura legítima justificar.
- Uma página normalmente tem um `main` visível; use múltiplos `nav` com nomes distintos se necessário.
- Tabelas reais usam `caption`, `thead`, `tbody`, `th scope` e valores numéricos acessíveis.
- `button` executa ação; `<a href>` navega. Não use link com `href="#"` para simular botão.

## SEO técnico para páginas indexáveis

1. Título `title` específico e útil; meta description fiel ao conteúdo (não garante snippet).
2. URL canônica pertinente, status HTTP real, sitemap e robots adequados ao escopo.
3. Hierarquia de headings, links descritivos, `alt`, conteúdo visível e equivalente no mobile.
4. Idioma e internacionalização (`lang`, `hreflang` quando necessário).
5. Open Graph / cards sociais quando houver compartilhamento; metadados não substituem copy.
6. Evite conteúdo principal dependente de clique, hardcoded em imagem ou só em canvas.
7. Nunca invente reviews, estrelas ou Rich Results garantidos.

## `schema.org` para dados estruturados — CONDICIONAL

**Primeiro pergunte:** a página é pública? O tipo de entidade existe no conteúdo real? Está contemplado nas políticas do Google e Schema.org? Há dados legítimos, atuais e disponíveis ao visitante?

| Tipo | Quando avaliar | Quando não usar |
|---|---|---|
| `Organization` | Página institucional com dados verídicos | Landing sem identificação/organização real |
| `BreadcrumbList` | Navegação hierárquica visível e coerente | Breadcrumb fictício |
| `Product`/`Offer` | Página de produto/compra com dados reais | Página institucional sem oferta real |
| `Article` | Conteúdo editorial efetivamente publicado | Cards com teaser ou textos genéricos |
| `LocalBusiness` | Empresa local com presença legítima | SaaS puramente digital sem local público pertinente |
| `FAQPage` | Somente se elegível segundo políticas vigentes e conteúdo corresponder | Adicionar para “forçar” resultado rico |

**Google recomenda JSON-LD**, se suportado. JSON-LD deve corresponder ao conteúdo público real. Um rich result nunca é garantido. Confira documentação específica antes de implementar: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data

### Exemplo mínimo contextual (ajustar e validar; valores ilustrativos)

```tsx
const organization = {
  '@context': 'https://schema.org',
  '@type': 'Organization',
  name: company.name,
  url: company.publicUrl,
};

// Inserir em página institucional indexável quando os dados forem públicos,
// reais e validados; serializar de modo seguro para HTML.
<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
    __html: JSON.stringify(organization).replace(/</g, '\\u003c'),
  }}
/>
```

Valide com **Rich Results Test** e **Schema Markup Validator** quando aplicáveis; validação sintática não garante elegibilidade de pesquisa.

## Schema para formulários — categoria diferente

Quando houver captura de dados, use contrato tipado (p.ex. TypeScript + Zod) e verifique no servidor, sem depender apenas da validação do cliente:

```ts
import { z } from 'zod';

export const leadSchema = z.object({
  name: z.string().trim().min(2).max(120),
  email: z.email(),
  consent: z.literal(true), // apenas se houver base legal e consentimento aplicável
});
```

Validação deve produzir mensagens claras associadas ao campo. Não force checkbox de consentimento quando outra base legal é a correta; política de privacidade, LGPD e coleta mínima são decisões de produto/jurídico.

## SSR, hidratação e semântica em React/Next

- Preserve HTML útil antes de JS quando o conteúdo permitir.
- Evite DOM inválido (button dentro de button, link dentro de link), IDs duplicados e renderizações divergentes entre server/client.
- Não use ARIA redundante ou enganoso para “passar auditoria”.
- Se houver fluxo privado/autenticado, **não injete schema público sem motivo**.

Fontes: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main ; https://www.w3.org/WAI/ARIA/apg/ ; https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing
