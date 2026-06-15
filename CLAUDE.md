# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Development

```bash
# Start local dev server (includes drafts)
hugo server -D

# Production build (garbage collect + minify)
hugo --gc --minify

# Update the theme to latest version
hugo mod get -u github.com/CaiJimmy/hugo-theme-stack/v4
hugo mod tidy
```

Requires **Hugo Extended** edition (for SCSS/Sass support). There are no lint or test commands — this is a static site with no test framework.

## Architecture

This is a **Hugo static blog** deployed to GitHub Pages. The theme is [Hugo Theme Stack v4](https://github.com/CaiJimmy/hugo-theme-stack), loaded as a Hugo module (Go module system). The Go module is pinned at `v4.0.3` in `go.mod`.

### Configuration

All site config lives in `config/_default/` as TOML files:

| File | Purpose |
|------|---------|
| `config.toml` | Base URL, language, title, pagination |
| `module.toml` | Hugo module imports (the theme) |
| `params.toml` | Theme parameters — widgets, sidebar, comments, date format, color scheme |
| `languages.toml` | Bilingual setup: zh-cn (default) and en |
| `menu.toml` | Social links |
| `markup.toml` | Markdown renderer — LaTeX math delimiters, syntax highlighting with line numbers |
| `permalinks.toml` | URL structure: posts at `/p/:slug/`, pages at `/:slug/` |
| `related.toml` | Related content by tags and categories |

### Content Structure

```
content/
├── _index.md              # Homepage placeholder (not actually rendered — see layouts)
├── blog/
│   ├── _index.en.md       # Blog listing page (en)
│   └── _index.zh-cn.md    # Blog listing page (zh-cn)
├── categories/
│   └── 技术博客/_index.md  # Category with badge styling
├── page/
│   ├── about/             # About page (both languages, heavy custom CSS)
│   ├── archives/          # Archives page (uses theme's "archives" layout)
│   └── links/             # Links page
└── post/
    └── 机器学习/           # Blog posts organized by topic subdirectory
```

### Bilingual Setup

The site has two languages: **zh-cn** (default, weight 1) and **en** (weight 2). Each translatable page exists as `index.zh-cn.md` and `index.en.md` within its own directory. Blog posts are primarily Chinese with `languageCode = "zh-cn"` and `hasCJKLanguage = true`.

### Custom Layouts (overriding the theme)

Three custom templates in `layouts/` override the theme:

- **[layouts/index.html](layouts/index.html)** — Homepage renders the About page content instead of a post list
- **[layouts/blog/list.html](layouts/blog/list.html)** — Blog listing renders all posts from the `post` section
- **[layouts/_partials/article-list/compact.html](layouts/_partials/article-list/compact.html)** — Compact article card showing title + date only

### Custom Assets

- [assets/scss/custom.scss](assets/scss/custom.scss) — Style overrides (currently empty placeholder)
- [assets/img/](assets/img/) — Avatar, favicon, and other images
- [assets/icons/](assets/icons/) — Custom SVG icons

### Content Frontmatter

Posts use YAML frontmatter with these fields:

```yaml
title: "Post Title"
description: ""
slug: post-slug
date: 2026-03-07 00:00:00+0000
categories:
    - CategoryName
tags:
    - TagName
weight: 1  # optional, overrides default date-descending sort
```

## CI/CD

Two GitHub Actions workflows in `.github/workflows/`:

- **deploy.yml** — Triggered on push to master. Installs Go, Node.js, Dart Sass, and Hugo Extended, then builds (`hugo --gc --minify`) and deploys to GitHub Pages.
- **update-theme.yml** — Runs daily at 00:00 UTC. Runs `hugo mod get -u && hugo mod tidy` and commits any theme updates.

## Devcontainer

Preconfigured in `.devcontainer/` with Hugo Extended, Node.js 22, Go, and Dart Sass. The VS Code tasks in `.vscode/tasks.json` provide "Serve Drafts" (`hugo server -D`) and "Build" commands.
