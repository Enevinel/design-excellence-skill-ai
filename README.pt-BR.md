# Design Excellence

[Read in English](../../README.md) · [Skill em inglês (padrão)](../../SKILL.md)

**Skill de Design Director + Product Design + UX + Acessibilidade + Front-end Engineering**, orientada para interfaces web/mobile, SaaS, e-commerce, dashboards e design systems.

> Design memorável é aquele que permanece claro, acessível e funcional quando a novidade visual passa.

## Por que existe

IA consegue gerar layouts rapidamente, mas frequentemente repete soluções genéricas: cards por toda parte, gradientes roxos, sombras pesadas, bordas e raios exagerados, hierarquia ruim e interfaces excelentes apenas no desktop. Esta skill exige intenção, evidência e revisão crítica.

Seu padrão mínimo inclui **mobile first → tablet → desktop**, WCAG 2.2 AA como meta para web, contrastes verificáveis, **4-point grid**, tipografia legível, HTML semântico, UX completa (inclusive estados de erro) e performance real. Usa tendências de 2026 com critério — não como checklist decorativo.

## Instalação

Copie a pasta raiz `design-excellence/` para o diretório de skills de seu agente, seguindo o manual do produto. **Por padrão, o `SKILL.md` e as referências na raiz estão em inglês**. Esta pasta contém tradução integral da documentação e dos guias. Para ativar o português como idioma das instruções em uma cópia local, substitua o `SKILL.md` da raiz por este arquivo e os diretórios `references/` e `assets/` pelos desta pasta, mantendo `scripts/` e o nome da pasta `design-excellence`. O arquivo central obrigatório é `SKILL.md`; os `references/` são carregados sob demanda. Não é necessário instalar bibliotecas para ler a skill.

Exemplo de organização (os caminhos concretos variam entre agentes):

```text
skills/
└── design-excellence/
    ├── SKILL.md                 # Inglês — padrão
    ├── README.md                # Inglês — padrão
    ├── references/              # 10 guias em inglês
    ├── assets/                  # Modelos em inglês e tokens CSS
    ├── scripts/                 # Validador e testes de contraste
    └── locales/
        └── pt-BR/
            ├── SKILL.md         # Tradução em português
            ├── README.md        # Este documento
            ├── references/      # 10 guias em português
            └── assets/          # Modelos em português
```

**Idioma de resposta:** a skill deve responder no idioma do usuário, mesmo com instruções internas em inglês.

## Exemplos de uso

- “Use a skill design-excellence para redesenhar minha homepage sem estética genérica de IA. Comece pelo mobile e preserve a identidade da marca.”
- “Audite este dashboard com WCAG 2.2 AA, contraste, semântica, fluxos, responsividade e qualidade visual; proponha correções por impacto.”
- “Implemente este design em Next.js, TypeScript e Tailwind, reutilizando meus componentes, com estados completos e SEO/schema quando aplicável.”
- “Crie um design system original, com 4-point grid, tokens, tipografia, estilos dark/light e componentes acessíveis.”

## Ferramenta de contraste

Requer Python 3, sem dependências externas:

```bash
python3 scripts/check_contrast.py --fg '#171717' --bg '#ffffff'
python3 scripts/check_contrast.py --fg '#6b7280' --bg '#ffffff' --large
python3 scripts/check_contrast.py --fg '#8b8b8b' --bg '#ffffff' --ui --json
python3 scripts/test_contrast.py
```

O script verifica matematicamente contraste WCAG para cores hex **opacas**. Não avalia gradientes, imagens, pixels renderizados, blur, alpha, localização de componentes, foco ou todos os critérios WCAG: esses casos exigem inspeção da interface e testes adicionais.

## Fontes e critérios

A skill se apoia em **WCAG 2.2**, **WAI-ARIA APG**, **Apple Human Interface Guidelines**, **Google Material Design**, **Microsoft Fluent 2**, **Vercel Geist**, documentação de **SEO/JSON-LD do Google** e pesquisa visual **Design Trends 2026** no Behance. Os links diretos e as distinções entre normas e preferências estão documentados nos guias.

**Nota:** não há associação, endosso, verificação ou certificação dessas empresas. A proposta é almejar um nível comparável de rigor, sem alegar aprovação formal.

## Critérios de sucesso

A rubrica em `references/09-quality-gates.md` emprega gates bloqueantes (acessibilidade, tarefas quebradas, conteúdo enganoso etc.) e uma avaliação heurística de 0 a 100. A nota é uma ferramenta interna de review, não uma certificação de design ou WCAG.

## Autoria

**Autor: Lenivene Bezerra** · **Organização: Enevinel** · **Versão: 1.1.0**. O campo `metadata.author` é utilizado por ser compatível com a especificação Agent Skills. Idioma padrão: inglês; tradução completa: português brasileiro.
