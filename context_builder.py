import json
import re


# -----------------------------
# LOAD JSON
# -----------------------------
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# -----------------------------
# RELEVANCE SCORING
# -----------------------------
def score_relevance(text, idea):
    idea_words = set(re.findall(r"\w+", idea.lower()))
    text_words = set(re.findall(r"\w+", str(text).lower()))
    return len(idea_words.intersection(text_words))


# -----------------------------
# CHARACTER ALIASES (IMPORTANT FIX)
# -----------------------------
CHARACTER_ALIASES = {
    "monkey_d_luffy": ["luffy", "monkey", "straw hat", "captain"],
    "roronoa_zoro": ["zoro", "swordsman"],
    "portgas_d_ace": ["ace", "fire"],
    "blackbeard": ["teach", "marshall", "darkness"],
    "shanks": ["red hair"],
}


# -----------------------------
# SELECT CHARACTERS (FIXED)
# -----------------------------
def select_characters(characters, idea, top_k=6):
    scored = []

    idea_lower = idea.lower()

    for name, data in characters.items():
        score = score_relevance(data, idea)

        # direct name match boost
        if name.replace("_", " ") in idea_lower:
            score += 10

        # alias boost (IMPORTANT FIX)
        for alias in CHARACTER_ALIASES.get(name, []):
            if alias in idea_lower:
                score += 5

        scored.append((score, name, data))

    scored.sort(reverse=True, key=lambda x: x[0])

    return {
        name: data
        for _, name, data in scored[:top_k]
    }


# -----------------------------
# SELECT LORE (UNCHANGED BUT CLEANED)
# -----------------------------
def select_lore(lore, idea):
    return {
        "world": lore.get("world", {}),
        "factions": lore.get("factions", {}),
        "power_system": lore.get("power_system", {}),
        "timeline_logic": lore.get("timeline_logic", {}),
        "arc_progression": lore.get("arc_progression", {})
    }


# -----------------------------
# COMPRESSION HELPERS (NEW FIX)
# -----------------------------
def compress_lore(lore):
    lines = []

    for section in lore.values():
        if isinstance(section, dict):
            for v in section.values():
                if isinstance(v, str):
                    lines.append(f"- {v}")
                elif isinstance(v, list):
                    for item in v:
                        lines.append(f"- {item}")

    return "\n".join(lines[:10])


def compress_characters(chars):
    lines = []

    for name, data in chars.items():
        role = data.get("role", "unknown")
        traits = ", ".join(data.get("traits", []))

        lines.append(f"- {name}: {role} | {traits}")

    return "\n".join(lines[:8])


# -----------------------------
# BUILD CONTEXT PROMPT
# -----------------------------
def build_context(idea):
    lore = load_json("knowledge/lore.json")
    characters = load_json("knowledge/characters.json")["characters"]
    engine = load_json("knowledge/what_if_engine.json")

    selected_lore = select_lore(lore, idea)
    selected_characters = select_characters(characters, idea)

    retention_rules = engine.get("retention_engine", {}).get("rules", [])
    timeline = engine.get("micro_timeline", {}).get("stages", [])

    prompt = f"""
You are an elite viral anime storytelling AI.

You generate HIGH-RETENTION 20–30 second One Piece "What If" TikTok scripts.

========================
IDEA:
{idea}

========================
WORLD RULES (compressed canon):
{compress_lore(selected_lore)}

========================
RELEVANT CHARACTERS ONLY:
{compress_characters(selected_characters)}

========================
TIMELINE STRUCTURE:
{timeline}

========================
RETENTION RULES:
{retention_rules}

========================

STRICT REQUIREMENTS:
- ONE divergence only
- Everything must be cause → effect
- No filler, no side arcs
- Must escalate every 3–5 seconds
- Must end with a twist or collapse
- Keep sentences extremely short
- MAX 6 SENTENCES TOTAL

OUTPUT FORMAT:

HOOK (0–2s):
DIVERGENCE:
CHAIN OF EVENTS:
WORLD IMPACT:
TWIST ENDING:
"""

    return prompt