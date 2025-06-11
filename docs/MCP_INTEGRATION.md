# Model Context Protocol Integration

Aider can read a simple MCP configuration file to preload project
documents. The configuration file defaults to `mcp.yml` and accepts a
list of documents to add into the model context.

Example `mcp.yml`:

```yaml
meta:
  version: 1

docs:
  - docs/PRD.md
```

The documents are loaded at startup and can be accessed through
`args.mcp` in the codebase.
