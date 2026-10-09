<div align="center">

# ✦ Design Excellence

### Projete com intenção. Desenvolva com precisão. Entregue sem concessões desnecessárias.

Uma **Agent Skill para design de produtos digitais de alto nível**, que orienta agentes de IA a criar, auditar, aprimorar e implementar interfaces originais, acessíveis, responsivas e preparadas para produção.

Da **direção de arte e UX** aos **design systems, código front-end semântico e controle de qualidade** — sem os clichês visuais frequentemente produzidos por IA.

[![Agent Skills](https://img.shields.io/badge/Padr%C3%A3o-Agent%20Skills-2563eb)](https://agentskills.io/specification)
[![Idioma](https://img.shields.io/badge/Padr%C3%A3o-Ingl%C3%AAs-18181b)](SKILL.md)
[![Português](https://img.shields.io/badge/Tradu%C3%A7%C3%A3o-PT--BR-009739)](SKILL.pt-BR.md)
[![Acessibilidade](https://img.shields.io/badge/Meta-WCAG%202.2%20AA-0f766e)](https://www.w3.org/TR/WCAG22/)
[![Abordagem](https://img.shields.io/badge/Abordagem-Mobile%20First-7c3aed)](references/03-responsive-mobile-first.md)
[![GitHub](https://img.shields.io/badge/GitHub-Enevinel-181717?logo=github)](https://github.com/Enevinel/design-excellence-skill-ai)

**[Conheça a skill](SKILL.md) · [Instalação](#-instalação) · [Exemplos](#-exemplos-de-uso) · [Guias](#-guias-de-referência) · [Contribuição](#-contribuindo)**

**[English](README.md)** · **Português (Brasil)**

</div>

---

## ✨ Sobre o projeto

O **Design Excellence** foi criado para tornar o design produzido por IA mais criterioso, original, utilizável e tecnicamente consistente. Ele não se limita a pedir uma "interface bonita": estabelece um processo para compreender o produto, tomar decisões justificáveis, implementar corretamente e revisar o resultado.

> **Design de excelência não é uma coleção de efeitos. É um sistema de decisões que torna um produto mais claro, autêntico e fácil de usar.**

### O que ele faz?

- **Orienta:** define público, objetivos do produto, identidade visual e direcionamento antes de escolher um estilo.
- **Projeta:** organiza tipografia, cores, composição, hierarquia, imagens e padrões de interação com intenção.
- **Adapta:** começa pelo **mobile** e depois considera cuidadosamente **tablet, desktop e telas maiores**.
- **Inclui:** prioriza legibilidade, contraste real, teclado, tecnologias assistivas, zoom e redução de movimento.
- **Implementa:** favorece HTML semântico, componentes reutilizáveis, design tokens, CSS sustentável e padrões adequados de React/Next.js.
- **Otimiza:** considera performance, SEO, clareza do conteúdo, conversão e schema.org/JSON-LD **quando fizer sentido**.
- **Audita:** avalia estados de interface, riscos de usabilidade, barreiras de acessibilidade e prontidão para produção — não somente screenshots.

## 🎯 O diferencial

Muitas interfaces criadas por IA parecem bonitas à primeira vista, mas repetem os mesmos padrões: cards muito arredondados, gradientes decorativos, esferas brilhantes, sombras excessivas, bento grids sem propósito, contraste fraco e layouts pensados apenas para desktop.

Esta skill exige que o agente **justifique suas escolhas visuais** e rejeite efeitos que não melhoram a experiência.

| Problema comum em designs de IA | Princípio do Design Excellence |
| --- | --- |
| Hero com gradiente genérico e efeitos chamativos | Direção de arte própria, orientada ao produto e à marca |
| Um card para cada informação | Estruturar o conteúdo conforme significado e prioridade |
| Bordas, cantos e sombras exagerados | Detalhes contidos, espaçamento e hierarquia visual |
| Desktop comprimido para caber no celular | **Mobile → tablet → desktop**, com decisões próprias em cada etapa |
| Cores bonitas, mas texto ilegível | Verificar **contraste real entre texto e fundo** |
| `div` clicável e títulos apenas visuais | Controles nativos, HTML semântico e hierarquia de headings |
| Telas estáticas sem estados de carregamento ou erro | Interações completas, feedback e recuperação |
| Promessas de "acessível" ou "rápido" sem provas | Metas explícitas, testes, evidências e limitações claras |

**O objetivo não é fazer todos os produtos parecerem iguais. É fazer cada produto ter uma identidade própria e funcionar bem.**

## 🧠 Princípios fundamentais

| Princípio | Como a skill aplica |
| --- | --- |
| **Direção de arte intencional** | A marca orienta tipografia, cores, composição e movimento; tendências são opcionais. |
| **4-point grid system** | Base de espaçamento de `4px`, com ritmo dominante de `8px`, sem obrigar todos os valores tipográficos a serem múltiplos de quatro. |
| **Responsividade mobile first** | Layouts guiados pelo conteúdo e testados em celulares, tablets, desktops, zoom e mudanças de orientação. |
| **Acessibilidade desde o início** | WCAG 2.2 AA como meta web aplicável; teclado, foco, rótulos, reflow, movimento reduzido e contraste. |
| **Implementação semântica** | Uso adequado de `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`, `h1`–`h3`, links, botões e formulários. |
| **Interações completas** | Estados de carregamento, vazio, erro, sucesso, desabilitado e recuperação com feedback claro. |
| **Dados estruturados relevantes** | schema.org/JSON-LD quando aplicável a conteúdo público; diferenciar de validação com Zod/JSON Schema. |
| **Qualidade de produção** | Design tokens, componentes acessíveis, Core Web Vitals, testes e decisões documentadas. |

### Acessibilidade é requisito, não acabamento

Para conteúdo web aplicável, a skill busca **WCAG 2.2 AA**: contraste mínimo de **4,5:1** para texto normal, **3:1** para texto grande que se enquadre nos critérios e, em geral, **3:1** para informações essenciais de interface não textuais, respeitando condições e exceções da norma.

Recomenda áreas de toque em torno de **44×44 CSS px**, quando viável, como objetivo de usabilidade, distinguindo essa recomendação do critério **WCAG 2.2 AA de 24×24 CSS px ou exceções aplicáveis**. Testes automáticos, sozinhos, não comprovam conformidade com a WCAG.

## 🛠️ Modos de uso

| Modo | Quando usar | Resultado esperado |
| --- | --- | --- |
| **Criação** | "Crie uma landing page SaaS." | Direção de produto, hierarquia, sistema responsivo e justificativas. |
| **Redesign** | "Modernize esta interface sem perder a marca." | Melhorias baseadas em problemas reais, não uma mudança visual aleatória. |
| **Auditoria** | "Revise acessibilidade e UX em todos os dispositivos." | Problemas priorizados, riscos e correções práticas. |
| **Design system** | "Crie tokens e padrões reutilizáveis." | Cores, tipografia, espaçamento, componentes e estados consistentes. |
| **Implementação** | "Desenvolva isto em Next.js e TypeScript." | Código semântico, responsivo e sustentável, com os estados necessários. |
| **Avaliação crítica** | "Diga o que parece feito por IA." | Crítica objetiva dos clichês, da hierarquia e das escolhas visuais. |

## 🔍 Antes e depois: decisões de design

**Exemplo 1 — Homepage de marketing**

**Antes:** Gradiente roxo, três esferas brilhantes, cinco cards iguais, título vago e vários botões concorrendo pela atenção.

**Depois:** Proposta de valor específica, ação principal clara, tipografia expressiva sem exagero, seções sustentadas por evidências e composição pensada primeiro para mobile.

**Exemplo 2 — Dashboard SaaS**

**Antes:** Indicadores em cards decorativos, pouco contraste nas tabelas, controles ocultos no tablet e ausência de estados vazios ou de carregamento.

**Depois:** Indicadores fáceis de comparar, agrupamento útil dos dados, tabelas acessíveis, filtros responsivos e estados de erro, carregamento e vazio definidos.

**Exemplo 3 — Formulário de cadastro**

**Antes:** Campos identificados apenas por placeholder, erros vagos, áreas de toque pequenas e layout de duas colunas pensado só para desktop.

**Depois:** Rótulos persistentes, instruções claras para corrigir erros, controles adequados, navegação lógica por teclado e fluxo mobile acessível em uma coluna.

*Os exemplos ilustram decisões recomendadas pela skill, não resultados mensurados de um produto específico.*

## 📦 Instalação

A skill segue a [especificação Agent Skills](https://agentskills.io/specification). **Instale o repositório completo**, não apenas o `SKILL.md`: as instruções dependem de `references/`, `assets/` e, opcionalmente, `scripts/`.

### OpenAI Codex — no projeto

Na raiz do projeto:

```bash
mkdir -p .agents/skills
git clone https://github.com/Enevinel/design-excellence-skill-ai.git \
  .agents/skills/design-excellence
```

### Claude Code — no projeto

```bash
mkdir -p .claude/skills
git clone https://github.com/Enevinel/design-excellence-skill-ai.git \
  .claude/skills/design-excellence
```

### Outros agentes compatíveis

Clone ou copie o repositório para uma pasta chamada **`design-excellence`**, dentro do diretório de skills configurado para a sua ferramenta. Mantenha `SKILL.md` na raiz dessa pasta, acompanhado de `references/`, `assets/` e `scripts/`. A descoberta e a ativação variam conforme o agente e o ambiente.

**Requisitos:** a leitura da skill não exige dependências de execução. O verificador opcional de contraste usa **Python 3**, apenas com a biblioteca padrão. Se a pasta já estiver instalada, atualize o clone Git existente em vez de clonar novamente no mesmo caminho.

## 🚀 Exemplos de uso

Depois de instalar, você pode usar comandos em linguagem natural:

**Criar uma homepage original**

```text
Use design-excellence para criar a homepage de um SaaS premium.
Comece pelo mobile e adapte para tablet e desktop.
Evite o visual genérico de IA e explique a direção de arte.
```

**Auditar um produto existente**

```text
Avalie esta interface considerando WCAG 2.2 AA, contraste real,
HTML semântico, navegação por teclado, fluxos de usuário e
responsividade mobile/tablet/desktop. Priorize problemas críticos.
```

**Criar um design system**

```text
Crie um design system original com 4-point grid,
tokens semânticos, temas claro/escuro acessíveis, tipografia,
estados dos componentes e orientações para implementação.
```

**Implementar em React / Next.js**

```text
Implemente este design em Next.js e TypeScript.
Reutilize os componentes existentes, escreva HTML semântico,
trate estados importantes e use JSON-LD apenas se necessário.
```

**Eliminar padrões visuais de IA**

```text
Faça uma crítica rigorosa deste design. Identifique bordas
excessivas, cards exagerados, brilho desnecessário, hierarquia
fraca e outros clichês de IA. Proponha uma direção mais madura.
```

## ⚙️ Como funciona

O agente segue um fluxo prático:

1. **Compreender:** público, objetivos, tarefas essenciais, marca e limitações.
2. **Estruturar:** hierarquia da informação, navegação, conteúdo e jornadas.
3. **Direcionar:** escolher uma direção de arte original e justificável.
4. **Sistematizar:** definir tokens, hierarquia tipográfica e espaçamento de quatro pontos.
5. **Adaptar:** projetar primeiro para mobile e depois para tablet e desktop.
6. **Implementar:** interações acessíveis, código semântico e validação ou dados estruturados quando pertinentes.
7. **Validar:** executar os testes disponíveis e declarar o que ainda precisa ser verificado.
8. **Refinar:** remover ruído visual e resolver problemas que impedem uma entrega de qualidade.

Os arquivos de referência devem ser **consultados conforme a necessidade**, sem carregar todos em toda execução.

## 📚 Guias de referência

O repositório oferece dez guias especializados:

| Guia | Abordagem |
| --- | --- |
| [01 — Tendências e direção de arte](references/01-trends-and-direction.md) | Identidade e adoção criteriosa de tendências |
| [02 — Sistema visual](references/02-visual-system.md) | Tipografia, cores, espaçamento, tokens e hierarquia |
| [03 — Responsividade](references/03-responsive-mobile-first.md) | Mobile, tablet, desktop, orientação e zoom |
| [04 — Acessibilidade](references/04-accessibility.md) | WCAG, contraste, foco e tecnologias assistivas |
| [05 — Semântica, SEO e schema](references/05-semantics-seo-schema.md) | HTML, React/Next.js, JSON-LD e validação |
| [06 — Interação e conteúdo](references/06-interaction-content.md) | Movimento, estados, formulários e microcopy |
| [07 — Performance e validação](references/07-performance-validation.md) | Core Web Vitals, testes e verificações de produção |
| [08 — Padrões de produto](references/08-product-patterns.md) | SaaS, dashboards, marketing e e-commerce |
| [09 — Critérios de qualidade](references/09-quality-gates.md) | Bloqueios de entrega e pontuação interna |
| [10 — Exemplos de implementação](references/10-implementation-examples.md) | Padrões práticos de interface e código |

## 🧪 Verificador de contraste

Use o script incluído para calcular o contraste entre **pares de cores hexadecimais opacas**:

```bash
python3 scripts/check_contrast.py --fg '#171717' --bg '#ffffff'
python3 scripts/check_contrast.py --fg '#6b7280' --bg '#ffffff' --large
python3 scripts/check_contrast.py --fg '#8b8b8b' --bg '#ffffff' --ui --json
python3 scripts/test_contrast.py
```

Ele **não** avalia automaticamente transparências, imagens ao fundo, gradientes, navegação por teclado ou acessibilidade ponta a ponta. A revisão visual e os testes com tecnologias assistivas continuam necessários.

## 📁 Estrutura do repositório

```text
design-excellence-skill-ai/
├── README.md               # Documentação em inglês (padrão)
├── README.pt-BR.md         # Documentação em português
├── SKILL.md                # Instruções em inglês (padrão)
├── SKILL.pt-BR.md          # Tradução das instruções
├── references/             # 10 guias detalhados em inglês
├── assets/                 # Briefings, revisão e tokens CSS
└── scripts/
    ├── check_contrast.py   # Calculadora de contraste
    └── test_contrast.py    # Testes unitários
```

O agente deve carregar **`SKILL.md` por padrão**. O arquivo `SKILL.pt-BR.md` é uma tradução opcional: instruções em inglês **não obrigam** o agente a responder em inglês. Ele deve respeitar o idioma do usuário. O repositório publicado não depende de uma pasta `locales/`.

## 📖 Padrões e referências

A skill utiliza referências públicas como [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/), [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/), [Google Material Design](https://m3.material.io/), [Microsoft Fluent 2](https://fluent2.microsoft.design/), [Vercel Geist](https://vercel.com/geist/introduction), [dados estruturados do Google](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) e [Design Trends 2026 no Behance](https://www.behance.net/gallery/239027109/Design-Trends-2026).

São **referências de qualidade**, não vínculos institucionais, endossos nem certificados de aprovação dessas organizações.

## ⚠️ Limitações

Design Excellence é um **conjunto de instruções para agentes de IA**, não um editor visual independente, um executor de testes de navegador, uma certificação de design nem uma garantia de implementação sem erros. O resultado depende do modelo, das ferramentas disponíveis, do contexto e das validações realmente realizadas.

A [pontuação interna de qualidade](references/09-quality-gates.md) é uma referência de revisão — **não** um certificado de acessibilidade ou aprovação de terceiros. Uma interface visualmente impressionante ainda pode falhar em usabilidade e acessibilidade e precisa ser corrigida.

## 🤝 Contribuindo

Contribuições são bem-vindas! Abra uma [issue](https://github.com/Enevinel/design-excellence-skill-ai/issues) para indicar requisitos pouco claros, sugerir melhorias ou apresentar falhas reproduzíveis. Envie um [pull request](https://github.com/Enevinel/design-excellence-skill-ai/pulls) com mudanças objetivas, justificativas e exemplos sempre que possível.

Priorize **clareza, acessibilidade, responsividade, correção técnica e originalidade** em vez de simplesmente acrescentar regras ou efeitos visuais.

## 👤 Autor

**Lenivene Bezerra** — **[Enevinel](https://github.com/Enevinel)**

**Repositório:** https://github.com/Enevinel/design-excellence-skill-ai

---

<div align="center">

**Um bom design causa uma impressão. Um design excelente conquista confiança em cada interação.**

Se o projeto ajudar você a criar experiências digitais melhores, considere deixar uma ⭐ no GitHub.

</div>
