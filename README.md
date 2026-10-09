<div align="center">

# ✦ Design Excellence

### Design with intention. Build with precision. Deliver without compromise.

[Leia em Português (Brasil)](README.pt-BR.md) · [Instruções da skill em Português](SKILL.pt-BR.md)
=======

An **Agent Skill for high-quality digital product design** that guides AI agents to design, audit, refine, and implement distinctive, accessible, responsive, and production-minded interfaces.

From **art direction and UX** to **design systems, semantic front-end code, and quality assurance**—without the generic visual clichés often produced by AI.

[![Agent Skills](https://img.shields.io/badge/Standard-Agent%20Skills-2563eb)](https://agentskills.io/specification)
[![Language](https://img.shields.io/badge/Default-English-18181b)](SKILL.md)
[![Português](https://img.shields.io/badge/Tradu%C3%A7%C3%A3o-PT--BR-009739)](README.pt-BR.md)
[![Accessibility](https://img.shields.io/badge/Target-WCAG%202.2%20AA-0f766e)](https://www.w3.org/TR/WCAG22/)
[![Approach](https://img.shields.io/badge/Approach-Mobile%20First-7c3aed)](references/03-responsive-mobile-first.md)
[![GitHub](https://img.shields.io/badge/GitHub-Enevinel-181717?logo=github)](https://github.com/Enevinel/design-excellence-skill-ai)

**[Explore the skill](SKILL.md) · [Installation](#-installation) · [Examples](#-usage-examples) · [Reference guides](#-reference-guides) · [Contributing](#-contributing)**

**English** · **[Português (Brasil)](README.pt-BR.md)**

</div>

---

## ✨ About the project

**Design Excellence** was created to make AI-generated design more thoughtful, original, usable, and technically sound. It does not simply request a "beautiful interface." It gives the agent a structured way to understand the product, make defensible design decisions, implement them appropriately, and review the result.

> **Great design is not a collection of effects. It is a system of decisions that makes a product clearer, more distinctive, and easier to use.**

### What does it do?

- **Directs:** establishes the audience, product goals, visual identity, and a clear design thesis before choosing a style.
- **Designs:** builds intentional typography, color, composition, hierarchy, imagery, and interaction patterns.
- **Adapts:** starts with **mobile**, then intentionally handles **tablet, desktop, and larger screens**.
- **Includes:** prioritizes readability, real contrast combinations, keyboard use, assistive technology, zoom, and reduced motion.
- **Engineers:** favors semantic HTML, reusable components, design tokens, maintainable CSS, and appropriate React/Next.js patterns.
- **Optimizes:** considers performance, SEO, content clarity, conversion, and schema.org/JSON-LD **when relevant**.
- **Audits:** evaluates UX states, usability risks, accessibility blockers, and production readiness instead of judging screenshots alone.

## 🎯 What makes it different?

Many AI-generated interfaces look polished at first glance but repeat the same patterns: huge rounded cards, decorative gradients, glowing orbs, excessive shadows, empty bento grids, weak contrast, and layouts conceived only for desktops.

This skill requires the agent to **justify visual choices** and reject effects that do not improve the experience.

| Common AI design mistake | Design Excellence principle |
| --- | --- |
| Generic gradient hero and flashy effects | A distinctive art direction grounded in the product and brand |
| A card for every piece of information | Structure content according to its meaning and priority |
| Oversized corners, borders, and shadows | Restrained details, considered spacing, and visual hierarchy |
| Desktop layout squeezed onto a phone | **Mobile → tablet → desktop**, each deliberately designed |
| Pretty colors with unreadable text | Check **rendered foreground/background contrast** |
| Clickable `div` elements and visual-only headings | Native controls, semantic HTML, and logical heading levels |
| Static mockups without loading or error states | Complete interactions, feedback, and recovery paths |
| Unverified "accessible" or "fast" claims | Explicit targets, tests, evidence, and honest limitations |

**The goal is not to make every product look alike. It is to help every product look and work like itself.**

## 🧠 Core design principles

| Principle | How the skill applies it |
| --- | --- |
| **Intentional art direction** | Brand traits drive typography, color, composition, and motion; trends are optional tools. |
| **4-point grid system** | A `4px` spacing base with a dominant `8px` rhythm, using consistent tokens without forcing every typographic value into multiples of four. |
| **Mobile-first responsiveness** | Content-driven layouts tested across small phones, tablets, desktops, zoom, and orientation changes. |
| **Accessibility by design** | WCAG 2.2 AA as the applicable web target; keyboard, focus, labels, reflow, reduced motion, and contrast checks. |
| **Semantic implementation** | Meaningful `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`, `h1`–`h3`, links, buttons, and forms. |
| **Thoughtful interaction** | Loading, empty, error, success, disabled, and recovery states with clear feedback. |
| **Relevant structured data** | schema.org/JSON-LD for eligible public content; distinguish this from Zod/JSON Schema validation. |
| **Production discipline** | Design tokens, accessible components, Core Web Vitals, testing, and documented tradeoffs. |

### Accessibility is a requirement, not a finishing touch

For applicable web content, the skill targets **WCAG 2.2 AA**, including a minimum text contrast ratio of **4.5:1** for normal text, **3:1** for qualifying large text, and generally **3:1** for essential non-text UI information, subject to the specification's conditions and exceptions.

It recommends approximately **44×44 CSS px** touch targets where practical as a usability goal, while correctly distinguishing that goal from WCAG 2.2 AA's **24×24 CSS px minimum or applicable exceptions**. Automated checks alone do not establish WCAG compliance.

## 🛠️ Ways to use the skill

| Mode | When to use it | Expected outcome |
| --- | --- | --- |
| **Create** | "Design a SaaS landing page." | Product direction, hierarchy, responsive system, and design rationale. |
| **Redesign** | "Modernize this interface without losing the brand." | Evidence-led improvements rather than a random visual reset. |
| **Audit** | "Review accessibility and UX on every device." | Prioritized findings, risks, and concrete remediation. |
| **Design system** | "Create tokens and reusable patterns." | Coherent color, type, spacing, component, and state conventions. |
| **Implement** | "Build this in Next.js and TypeScript." | Semantic, responsive, maintainable code with appropriate functional states. |
| **Critique** | "Tell me what looks AI-generated." | A candid review of clichés, hierarchy, content, and visual decisions. |

## 🔍 Before and after: design decisions

**Example 1 — Marketing homepage**

**Before:** A purple gradient, three glowing orbs, five identical cards, a vague headline, and multiple competing calls to action.

**After:** A specific value proposition, a clear primary action, distinctive but restrained typography, evidence-led sections, and a mobile composition designed first.

**Example 2 — SaaS dashboard**

**Before:** Metrics presented as decorative cards, weak table contrast, controls hidden on tablets, and no empty or loading states.

**After:** Scannable metrics, purposeful data grouping, accessible tables, responsive filtering, and defined loading, error, and empty states.

**Example 3 — Registration form**

**Before:** Placeholder-only labels, vague errors, small touch targets, and a desktop-only two-column layout.

**After:** Persistent labels, inline recovery guidance, appropriately sized controls, logical tab order, and an accessible single-column mobile flow.

*These examples illustrate the decisions the skill encourages, not measured before/after results from a specific product.*

## 📦 Installation

The skill follows the [Agent Skills specification](https://agentskills.io/specification). **Install the entire repository**, not only `SKILL.md`: the root instructions refer to `references/`, `assets/`, and optional `scripts/` that should remain alongside them.

### OpenAI Codex — project-local

From the project root:

```bash
mkdir -p .agents/skills
git clone https://github.com/Enevinel/design-excellence-skill-ai.git \
  .agents/skills/design-excellence
```

### Claude Code — project-local

```bash
mkdir -p .claude/skills
git clone https://github.com/Enevinel/design-excellence-skill-ai.git \
  .claude/skills/design-excellence
```

### Other compatible agents

Clone or copy the repository into a skill folder named **`design-excellence`** in your agent's configured skill location. Keep `SKILL.md` at that folder's root, alongside `references/`, `assets/`, and `scripts/`. Skill discovery and activation depend on your agent and environment.

**Requirements:** No runtime package dependencies are needed to read the skill. The optional contrast checker needs **Python 3** and uses the standard library. If you already installed the folder, update the existing Git checkout instead of cloning into the same location again.

## 🚀 Usage examples

Use natural-language instructions after installing the skill:

**Build an original homepage**

```text
Use design-excellence to design a premium SaaS homepage.
Start with mobile, then adapt for tablet and desktop.
Avoid generic AI aesthetics and explain the art direction.
```

**Audit an existing product**

```text
Audit this interface for WCAG 2.2 AA issues, real contrast,
semantic HTML, keyboard navigation, user flows, and
mobile/tablet/desktop responsiveness. Prioritize blockers.
```

**Build a design system**

```text
Create a distinctive design system with a 4-point grid,
semantic tokens, accessible light/dark themes, typography,
component states, and implementation guidance.
```

**Implement in React / Next.js**

```text
Implement this design in Next.js and TypeScript.
Reuse existing components, write semantic HTML, handle all
important UI states, and add schema.org JSON-LD only if relevant.
```

**Remove AI-looking visual patterns**

```text
Review this design critically. Identify excessive borders,
oversized cards, unnecessary glow, weak hierarchy, and other
AI-looking patterns. Propose a more mature art direction.
```

## ⚙️ How it works

The agent follows a practical sequence:

1. **Understand:** audience, business goals, critical tasks, existing brand, and constraints.
2. **Structure:** information hierarchy, navigation, content, and user journeys.
3. **Direct:** choose an original art direction backed by product reasoning.
4. **Systematize:** build tokens, typographic hierarchy, and 4-point spacing.
5. **Adapt:** design mobile first, then tablet and desktop behaviors.
6. **Implement:** accessible interactions, semantic code, and relevant data validation or structured data.
7. **Validate:** test what can actually be tested and state remaining gaps.
8. **Refine:** remove unnecessary visual noise and fix release-blocking issues.

Reference files are intended to be **loaded selectively** for the task, rather than all at once.

## 📚 Reference guides

The repository includes ten focused guides:

| Guide | Focus |
| --- | --- |
| [01 — Trends & art direction](references/01-trends-and-direction.md) | Brand expression and selective use of trends |
| [02 — Visual system](references/02-visual-system.md) | Typography, color, spacing, tokens, hierarchy |
| [03 — Responsive design](references/03-responsive-mobile-first.md) | Mobile, tablet, desktop, orientation, zoom |
| [04 — Accessibility](references/04-accessibility.md) | WCAG, contrast, focus, assistive technologies |
| [05 — Semantics, SEO & schema](references/05-semantics-seo-schema.md) | HTML, React/Next.js, JSON-LD, validation |
| [06 — Interactions & content](references/06-interaction-content.md) | Motion, states, forms, microcopy |
| [07 — Performance & validation](references/07-performance-validation.md) | Core Web Vitals, tests, production checks |
| [08 — Product patterns](references/08-product-patterns.md) | SaaS, dashboards, marketing, commerce |
| [09 — Quality gates](references/09-quality-gates.md) | Release blockers and internal review score |
| [10 — Implementation examples](references/10-implementation-examples.md) | Practical UI and code patterns |

## 🧪 Contrast checker

Use the included tool to calculate contrast for **opaque hexadecimal foreground/background color pairs**:

```bash
python3 scripts/check_contrast.py --fg '#171717' --bg '#ffffff'
python3 scripts/check_contrast.py --fg '#6b7280' --bg '#ffffff' --large
python3 scripts/check_contrast.py --fg '#8b8b8b' --bg '#ffffff' --ui --json
python3 scripts/test_contrast.py
```

It does **not** automatically assess transparency, image backgrounds, gradients, keyboard behavior, or end-to-end accessibility. Design review and assistive-technology testing are still needed.

## 📁 Repository structure

```text
design-excellence-skill-ai/
├── README.md               # English documentation (default)
├── README.pt-BR.md         # Portuguese documentation
├── SKILL.md                # English agent instructions (default)
├── SKILL.pt-BR.md          # Portuguese instructions (alternative)
├── references/             # 10 detailed English guides
├── assets/                 # Briefs, review template, CSS tokens
└── scripts/
    ├── check_contrast.py   # Contrast calculator
    └── test_contrast.py    # Unit tests
```

The agent should load **`SKILL.md` by default**. `SKILL.pt-BR.md` is an optional human-readable translation; instructions in English do **not** force the agent to answer in English. It should follow the user's language. The published repository does not require a `locales/` folder.

## 📖 Standards and inspiration

The skill draws on publicly available references, including [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/), [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/), [Google Material Design](https://m3.material.io/), [Microsoft Fluent 2](https://fluent2.microsoft.design/), [Vercel Geist](https://vercel.com/geist/introduction), [Google Search structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data), and [Design Trends 2026 on Behance](https://www.behance.net/gallery/239027109/Design-Trends-2026).

These are **references, not affiliations, endorsements, or claims of approval** from the organizations named.

## ⚠️ Limitations

Design Excellence is an **instruction set for AI agents**, not a standalone visual editor, browser-testing engine, design certification, or guarantee of error-free implementation. Actual results depend on the model, available tools, product context, and validation performed.

The internal [quality-gates scorecard](references/09-quality-gates.md) is a review heuristic—not an accessibility certificate or third-party approval. A visually impressive result can still fail usability or accessibility checks and must be corrected.

## 🤝 Contributing

Contributions are welcome. Open an [issue](https://github.com/Enevinel/design-excellence-skill-ai/issues) to report an unclear requirement, propose a better guideline, or document a reproducible failure. Submit a [pull request](https://github.com/Enevinel/design-excellence-skill-ai/pulls) with focused changes, rationale, and examples when possible.

Prioritize **clarity, accessibility, responsive behavior, technical correctness, and originality** over adding more rules or visual effects.

## 👤 Author

**Lenivene Bezerra** — **[Enevinel](https://github.com/Enevinel)**

**Repository:** https://github.com/Enevinel/design-excellence-skill-ai

---

<div align="center">

**Good design makes an impression. Excellent design earns trust through every interaction.**

If this project helps you build better digital experiences, consider leaving a ⭐ on GitHub.

</div>
