#!/usr/bin/env python3
"""WCAG 2.x contrast calculator for opaque hexadecimal color pairs.

Usage:
    python3 scripts/check_contrast.py --fg '#171717' --bg '#ffffff'
    python3 scripts/check_contrast.py --fg '#6b7280' --bg '#ffffff' --large
    python3 scripts/check_contrast.py --fg '#888' --bg '#fff' --ui --json

Limits: opaque solid colors only. Rendering, transparency, gradients,
background images, platform metrics, all other WCAG criteria not covered.
"""

from __future__ import annotations

import argparse
import json
import re
from typing import Tuple

Color = Tuple[int, int, int]


def parse_hex(value: str) -> Color:
    """Accept #RGB and #RRGGBB; reject alpha and non-hex colors."""
    value = value.strip()
    if not re.fullmatch(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})", value):
        raise ValueError(
            f"Cor inválida: {value!r}. Use #RGB ou #RRGGBB, sem transparência."
        )
    h = value[1:]
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def srgb_to_linear(channel: int) -> float:
    c = channel / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(color: Color) -> float:
    r, g, b = (srgb_to_linear(c) for c in color)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(foreground: Color, background: Color) -> float:
    a, b = relative_luminance(foreground), relative_luminance(background)
    light, dark = sorted((a, b), reverse=True)
    return (light + 0.05) / (dark + 0.05)


def assess(fg: str, bg: str, minimum: float) -> dict:
    if minimum <= 1 or minimum > 21:
        raise ValueError("O contraste mínimo precisa estar acima de 1 e até 21.")
    ratio = contrast_ratio(parse_hex(fg), parse_hex(bg))
    return {
        "foreground": fg,
        "background": bg,
        "contrast_ratio": round(ratio, 4),
        "minimum_ratio": minimum,
        "passes": ratio >= minimum,
        "scope": "WCAG 2.x — apenas contraste de cores sólidas opacas",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fg", required=True, help="Cor de primeiro plano #RGB/#RRGGBB")
    parser.add_argument("--bg", required=True, help="Cor de fundo #RGB/#RRGGBB")
    kind = parser.add_mutually_exclusive_group()
    kind.add_argument("--large", action="store_true", help="Texto grande (mínimo 3:1)")
    kind.add_argument("--ui", action="store_true", help="Componente/ícone essencial (3:1)")
    parser.add_argument("--min-ratio", type=float, help="Mínimo customizado (sobrescreve padrão)")
    parser.add_argument("--json", action="store_true", help="Emitir saída JSON")
    args = parser.parse_args()
    minimum = args.min_ratio if args.min_ratio is not None else (3.0 if args.large or args.ui else 4.5)
    try:
        result = assess(args.fg, args.bg, minimum)
    except ValueError as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        verdict = "PASSOU" if result["passes"] else "REPROVOU"
        print(
            f"{args.fg} sobre {args.bg}: {result['contrast_ratio']:.2f}:1 "
            f"(mín. {minimum:g}:1) — {verdict}"
        )
    return 0 if result["passes"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
