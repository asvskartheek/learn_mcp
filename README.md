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
-------------------
<details>
<summary>What is transport type? What difference does STDIO and SSE make?</summary>
???
</details>

<details>
<summary>What does the command and arguments mean on the Inspector?</summary>
I ran with default settings

```
uv run --with mcp mcp run server.py
```
<p style="color: red; font-weight: bold;">Maybe <a href="https://modelcontextprotocol.io/docs/concepts/transports">MCP Transports</a> in resources will have the answer to this</p>

???
</details>

<details>
<summary>What does ping do? What are sampling and roots?</summary>

???
</details>

## Resources
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#quickstart)
- [MCP Transports](https://modelcontextprotocol.io/docs/concepts/transports)