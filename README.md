# Learn MCP
This repository contains my personal notes of learning MCPs.

## Notes
### Implement the server in Quickstart
You need to add to have the server running, without the server running you cannot run inspector
```
if __name__ == "__main__":
    server.run()
```
----------------
Command for running inspector
```
mcp dev server.py
```
-----------
- When URI has a parameter, it will be registered as a template resource
    ```
    resource://{param}
    ```
- All resources must have URI not name

### Smolagents Integration 🤖
- Use `ToolCollection.from_mcp()` to get MCP tools
- Initialize CodeAgent with tools and model

Example implementation can be found in [`mcp_smolagents.py`](./mcp_smolagents.py)

## Questions 🤔

### Transport Types (STDIO vs SSE) 🔄
*Note: Maybe [MCP Transports documentation](https://modelcontextprotocol.io/docs/concepts/transports) has answers for this*

*Rough understanding so far is STDIO is used for locally hosted MCP servers and SSE for hosted ones.*

- [ ] STDIO (Standard Input/Output)
    - How does it handle communication?
    - Use cases and limitations
- [ ] SSE (Server-Sent Events)
    - Benefits and drawbacks
    - Implementation differences
---

### Inspector Command Details 🔍
- [ ] Understanding the command:
    ```
    uv run --with mcp mcp run server.py
    ```
---

### MCP Protocol Features 📡
- [ ] Ping functionality
    - Purpose and implementation
- [ ] Sampling
    - What is it?
- [ ] Roots
    - What is it?

---
### MCP Integration with AI Agents 🤖
- [ ] Integration with Langgraph
    - Architecture considerations
    - Implementation steps
    - Performance impacts

## Resources
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#quickstart)
- [MCP Transports](https://modelcontextprotocol.io/docs/concepts/transports)
- [SmolagentsTools Integration Guide](https://huggingface.co/docs/smolagents/tutorials/tools#tool-collection-from-any-mcp-server)