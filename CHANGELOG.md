## Version History 🚀

### v0.1.2 🔧

- 🐞 **Bug fixed:** A small error originating from the `dev` development branch has been resolved. ✅ Now, if an MCP server is detected, **no error will be thrown because of this**.

### v0.1.1 ⚙️

- 🔐 **Full integration with the new OAuth system:** Enhanced security and compatibility.
- ⚙️ **Advanced customization:** You can now add **custom headers** directly from the configuration.
- 🏷️ **Improved flexibility:** Support for passing `app_name` from the configuration for better identification.

### v0.1.0 ✨

- 🌟 Full integration of prompts from MCP servers into the client workflow.
- ⚙️ Enhancement of prompt engineering within the repository.
- 🔗 Exclusive integration with `mcp.types.PromptMessage`.

---

### v0.0.8 🎯

- 🚀 The prompts for language models (LLMs) were optimized to deliver responses that are more closely aligned with the MCP context.
- 🔄 The service extraction step was merged with the argument creation step, enabling both services and arguments to be identified in a single stage.

---

### v0.0.7 🔐

- 🛡️ A simple authorization system based on user credential authentication (username and password) was integrated. For further reference, please see [mcp-oauth](https://github.com/rb58853/mcp-oauth).

---

### v0.0.6 📡

- 📥 The exposed services have been added to the context of all queries, including those that do not require the use of a specific service. This approach allows for general inquiries regarding the available services.

---

### v0.0.5 🧩

- 📑 The LLM system is structured in steps, with each step being returned to the client making the query. This approach allows for the identification of the current stage within the query process.
- 🌐 Efficient language detection has been implemented for queries, enabling responses to be provided based on the detected language.
- 💬 The `open_local_chat()` function has been added, making it easy to use a local chat.

---

### v0.0.4 📦

- 📥 Package dependencies are incorporated during its initial installation process.

---

### v0.0.1 🛠️

- 🚀 Initial implementation of `Chat` client
- 🔗 Complete integration of `httpstream` protocol ([fasmcp](https://github.com/modelcontextprotocol/python-sdk))
- 🌍 Connectivity with multiple servers
- 🔧 Simplified config.json file for connection management
- ⚡ Efficient processing of multiple simultaneous requests to tools and resources within a single query
- 🔓 Simple connection without authorization (compatible only with servers that do not require authentication)
