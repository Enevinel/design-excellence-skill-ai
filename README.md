# Design Excellence

**A production-minded Design Director + Product Design + UX + Accessibility + Front-end Engineering agent skill.** Build, audit, and refine high-quality websites, SaaS platforms, dashboards, e-commerce, and mobile experiences.

> Memorable design remains clear, accessible, and useful after the novelty wears off.

[Leia em Português (Brasil)](locales/pt-BR/README.md) · [Instruções da skill em Português](locales/pt-BR/SKILL.md)

## Why this skill exists

Generative AI often produces repetitive interfaces: purple gradients, floating glow, oversized rounded cards, arbitrary bento layouts, desktop-only compositions, and weak hierarchy. This skill requires a **distinct point of view, structured execution, and verifiable quality** rather than AI-looking decoration.

The baseline includes **mobile first → tablet → desktop**, WCAG 2.2 AA as an applicable web target, measurable contrast, **4-point spacing**, semantic HTML and heading structure, meaningful UX states, contextual schema.org/JSON-LD, and performance discipline. Trends inform decisions; they do not dictate them.

## Author and project

- **Author:** Lenivene Bezerra
- **Organization:** Enevinel
- **Version:** 1.1.0
- **Default language:** English (`en`)
- **Translation:** Brazilian Portuguese (`pt-BR`)
- **Skill name:** `design-excellence`

`author` is intentionally stored in `metadata.author` in the YAML frontmatter, in line with the Agent Skills format; it is not an unsupported top-level field.

## Language strategy

The **root `SKILL.md`, `README.md`, `references/`, and `assets/` are in English by default**, reducing multilingual instruction overhead and preserving a consistent source of truth. A complete Portuguese documentation/instruction/reference counterpart lives in `locales/pt-BR/`.

**Instruction language does not determine response language.** The skill should always use the user's preferred language for explanations, interfaces, and code-related copy unless explicitly instructed otherwise.

To change the default instruction language in a personal copy, swap the root `SKILL.md` with `locales/pt-BR/SKILL.md` and use its matching `references/` and `assets/`; the Python script remains in the root `scripts/` directory. The installed folder name must remain `design-excellence`.

## Installation

Copy the entire `design-excellence/` folder to your agent's skills directory. The exact path depends on the product. Keep `SKILL.md` at the root; reference files are loaded on demand, not all at once. Reading the skill requires no extra libraries.

```text
skills/
└── design-excellence/
    ├── SKILL.md                       # English default
    ├── README.md                      # English default
    ├── references/                    # 10 English deep dives
    ├── assets/                        # English briefs and CSS tokens
    ├── scripts/
    │   ├── check_contrast.py
    │   └── test_contrast.py
    └── locales/
        └── pt-BR/
            ├── SKILL.md
            ├── README.md
            ├── references/             # 10 Portuguese deep dives
            └── assets/                 # Portuguese templates
```

## Example prompts

- “Use design-excellence to redesign this homepage without generic AI aesthetics. Start with mobile and respect my brand.”
- “Audit this dashboard against WCAG 2.2 AA, contrast, semantics, task flows, and phone/tablet/desktop behavior.”
- “Implement this design in Next.js and TypeScript, using my existing components, complete UI states, and relevant structured data.”
- “Build an original design system with a 4-point grid, semantic tokens, readable type, light/dark themes, and accessible components.”

## Contrast tool

Python 3, standard library only:

```bash
python3 scripts/check_contrast.py --fg '#171717' --bg '#ffffff'
python3 scripts/check_contrast.py --fg '#6b7280' --bg '#ffffff' --large
python3 scripts/check_contrast.py --fg '#8b8b8b' --bg '#ffffff' --ui --json
python3 scripts/test_contrast.py
```

This script calculates WCAG contrast ratios for **opaque hexadecimal color pairs only**. It does not test real gradients, images, transparency, focus behavior, assistive technologies, or overall WCAG conformance.

## Sources and inspiration

Built around publicly available WCAG 2.2, WAI-ARIA APG, Apple Human Interface Guidelines, Google Material, Microsoft Fluent 2, Vercel Geist, Google Search structured-data documentation, and the Behance **Design Trends 2026** project. Direct URLs and criteria appear in each reference guide.

No company affiliation, endorsement, design approval, or formal accessibility certification is claimed.

## Release criteria

[Quality gates](references/09-quality-gates.md) define blockers (broken critical tasks, contrast failures, misleading content, unusable mobile UI, etc.) and an internal 0–100 heuristic score. This score is not a WCAG certificate or third-party approval.

## Credits

Created by **Lenivene Bezerra · Enevinel**. Original practical guidance synthesizing public design research, platform standards, and production engineering practices.
