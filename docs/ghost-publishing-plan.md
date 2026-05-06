# Ghost Publishing Plan

These packs are derived from Ghost-oriented content series but are not blog posts. If published later, treat them as a separate skills library:

1. Keep the current private repository as the source of truth.
2. Select packs with proven usefulness through real operator usage.
3. Convert each selected pack into a publishable article, downloadable resource, or OpenClaw skill package.
4. Preserve the related Ghost tag in `pack.yaml` for cross-linking.
5. Review every public artifact for confidentiality and remove internal paths before publication.


## Backlink fields

Each `pack.yaml` and manifest entry carries:
- `ghost_tag`: the existing Ghost tag used by the source posts.
- `ghost_series_status`: currently `draft_or_individual_posts` until a stable public series index exists.

When a pack receives a stable Ghost index URL, replace `ghost_series_status` with `ghost_series_url` in `pack.yaml` and `manifest.json`, then update the pack README Ghost backlinks section and re-run `python3 scripts/validate.py`.
