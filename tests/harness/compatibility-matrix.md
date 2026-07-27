# Harness Compatibility Matrix

| Harness | Root discovery file(s) | Native command adapter | Static readiness | Live test status |
|---|---|---|---|---|
| Codex / AGENTS-compatible | `AGENTS.md` | Portable commands in `commands/` | Ready | Not run here |
| Claude Code | `CLAUDE.md` imports `AGENTS.md` | `.claude/commands/` | Ready | Not run here |
| OpenCode | `AGENTS.md` | `.opencode/commands/` | Ready | Not run here |
| Cursor | `.cursor/rules/democratic-law.mdc` and root files | Use portable command prompt | Ready | Not run here |
| Google Antigravity | `.agents/rules/democratic-law.md` | Use portable command prompt | Ready | Not run here |
| Gemini | `GEMINI.md` | Use portable command prompt | Ready | Not run here |
| GitHub Copilot | `.github/copilot-instructions.md` | Use portable command prompt | Ready | Not run here |
| Windsurf | `.windsurfrules` | Use portable command prompt | Ready | Not run here |

“Ready” means the repository contains the expected adapter files. It is not a claim that a specific installed version has passed live behavioural testing.
