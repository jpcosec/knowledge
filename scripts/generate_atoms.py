import os

atoms = [
    {
        "id": "atom-what-is-adk-technical-overview",
        "title": "What is the ADK technical overview",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "layer:architecture", "artifact_role:definition"],
        "content": """The Agent Development Kit (ADK) architecture provides a robust environment for building, evaluating, and deploying AI-powered agents. \n\nAt its core, the ADK runtime acts as the execution engine for the framework. It manages the Event Loop, Session management, and orchestrates the flow of data between agents, LLMs, and external tools. The framework supports multiple run modes, including a Dev UI (`adk web`), a CLI runner (`adk run`), and an API Server for production deployments. It provides primitives like Runners (to handle execution flow), Sessions (to track conversation threads), State (for short-term scratchpad memory), and MemoryService (for long-term storage)."""
    },
    {
        "id": "atom-what-are-function-tools-in-adk",
        "title": "What are function tools in ADK",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:tools", "layer:implementation", "artifact_role:definition"],
        "content": """In the Agent Development Kit (ADK), Function Tools are custom, developer-defined functions tailored to an application's specific needs. \n\nThese are typically standard synchronous or asynchronous functions (e.g., a Python `def` or a class method) that interact with the world outside the agent. They can also represent long-running operations or even other specialized sub-agents acting as a tool (Agents-as-Tools). The LLM determines when to call a function tool by analyzing the system instructions, conversation history, and the provided function names and docstrings."""
    },
    {
        "id": "atom-what-are-mcp-tools-in-adk",
        "title": "What are MCP tools in ADK",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:tools", "system:mcp", "layer:architecture", "artifact_role:definition"],
        "content": """Model Context Protocol (MCP) Tools in the Agent Development Kit (ADK) provide a standardized way for Large Language Models (LLMs) to communicate with external applications and data sources.\n\nMCP follows an open standard client-server architecture, acting as a universal connection mechanism that simplifies how agents obtain context and execute actions. By using MCP tools, developers can seamlessly integrate their ADK agents with third-party systems that conform to the MCP protocol without building custom, one-off API integrations."""
    },
    {
        "id": "atom-what-are-openapi-tools-in-adk",
        "title": "What are OpenAPI tools in ADK",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:tools", "layer:implementation", "artifact_role:definition"],
        "content": """OpenAPI Tools in the Agent Development Kit (ADK) allow developers to automatically generate callable agent tools directly from an OpenAPI Specification (v3.x).\n\nBy using the `OpenAPIToolset` class, ADK parses the existing API documentation and creates a `RestApiTool` for each defined operation (like `GET /users` or `POST /data`). This eliminates the need to manually write individual Python or TypeScript function tools for each REST API endpoint, enabling agents to seamlessly interact with web services out-of-the-box."""
    },
    {
        "id": "atom-how-adk-handles-tool-authentication",
        "title": "How ADK handles tool authentication",
        "five_wh_one_plus": "how",
        "tags": ["system:adk", "topic:tools", "topic:security", "layer:architecture", "artifact_role:process"],
        "content": """The Agent Development Kit (ADK) manages tool authentication by carefully controlling how credentials and access keys are provided to functions accessing protected resources (e.g., user emails, databases).\n\nADK cautions developers against storing sensitive credentials (like access tokens or refresh tokens) directly in the session state due to security risks. Instead, authentication data should be managed through secure backend mechanisms or runtime configuration injections when executing tool calls. The framework supports handling multi-user environments where different users might have different access permissions, requiring careful scoping of access within the execution context."""
    },
    {
        "id": "atom-what-are-tool-limitations-in-adk",
        "title": "What are tool limitations in ADK",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:tools", "layer:concepts", "artifact_role:constraint"],
        "content": """In the Agent Development Kit (ADK), certain tools impose structural limitations on agent configurations. \n\nFor instance, historically (in ADK Python v1.15.0 and lower), using specific tools like Google Search or the Code Execution environment restricted the agent from using any other tools simultaneously (the "one tool per agent" limitation). While newer versions of the framework provide built-in workarounds or remove this limitation (e.g., in TypeScript requiring Gemini 2.0+), developers must be mindful of how some heavy-weight tools might monopolize the LLM's tool-calling capabilities."""
    },
    {
        "id": "atom-what-are-artifacts-in-adk",
        "title": "What are artifacts in ADK",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:artifacts", "layer:data", "artifact_role:definition"],
        "content": """Artifacts in the Agent Development Kit (ADK) are a crucial mechanism for managing named, versioned binary data associated with specific user sessions or persistent user profiles. \n\nThey allow agents and tools to handle complex data beyond simple text strings, enabling rich interactions with files, images, audio, and PDFs. Artifacts are consistently represented using the standard `google.genai.types.Part` object, storing the raw binary content and a `mime_type` indicating the format."""
    },
    {
        "id": "atom-what-are-skills-for-agents-in-adk",
        "title": "What are skills for agents in ADK",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:skills", "layer:concepts", "artifact_role:definition"],
        "content": """An Agent Skill in the Agent Development Kit (ADK) is an experimental, self-contained unit of functionality that an agent can load to perform a specific task. \n\nBased on the Agent Skill specification, a Skill encapsulates the necessary system instructions, resources, and tools required for the job. This modular structure allows the agent to load capabilities incrementally, minimizing the impact on the agent's operating context window while extending its functionality efficiently."""
    },
    {
        "id": "atom-what-are-callbacks-in-adk-app-management",
        "title": "What are callbacks in ADK app management",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:callbacks", "layer:architecture", "artifact_role:definition"],
        "content": """Callbacks in the Agent Development Kit (ADK) provide a powerful mechanism to hook into an agent's execution process to observe, customize, and control behavior without modifying core framework code.\n\nDevelopers can associate custom functions with an agent that automatically trigger at key stages. Important hooks include `Before Agent` / `After Agent` (wrapping the entire lifecycle of a user request), `Before Model` / `After Model` (for inspecting/modifying data sent to or received from the LLM), and `Before Tool` / `After Tool` (for controlling the execution of specific tools). They are vital for implementing safety guardrails and debugging."""
    },
    {
        "id": "atom-what-are-plugins-in-adk",
        "title": "What are plugins in ADK",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:plugins", "layer:architecture", "artifact_role:definition"],
        "content": """A Plugin in the Agent Development Kit (ADK) is a custom code module executed at various stages of an agent workflow lifecycle using callback hooks. \n\nPlugins package functionality applicable across the entire agent workflow. Common use cases include Logging and Tracing (recording agent, tool, and LLM activity for debugging), Policy Enforcement (implementing security guardrails to block unauthorized tool access), and Monitoring and Metrics (exporting token usage and latency to systems like Prometheus or Google Cloud Observability)."""
    },
    {
        "id": "atom-how-adk-supports-context-caching",
        "title": "How ADK supports context caching",
        "five_wh_one_plus": "how",
        "tags": ["system:adk", "topic:context", "layer:architecture", "artifact_role:process"],
        "content": """The Agent Development Kit (ADK) supports context caching to optimize performance and reduce costs when sending large sets of data or extended instructions repeatedly to a generative AI model (such as Gemini 1.5 Pro and higher). \n\nBy configuring context caching at the ADK `App` object level, the framework allows developers to cache static request data. Instead of resending the entire payload on every agent interaction, the agent reuses the cached context, significantly speeding up response latency and lowering the total number of processed tokens per request."""
    },
    {
        "id": "atom-how-adk-supports-context-compression",
        "title": "How ADK supports context compression",
        "five_wh_one_plus": "how",
        "tags": ["system:adk", "topic:context", "layer:architecture", "artifact_role:process"],
        "content": """The Agent Development Kit (ADK) supports context compression (or compaction) to prevent an agent's context window from growing indefinitely, which would otherwise increase latency and costs. \n\nUsing the `CompactionRequestProcessor` integrated into the execution flow, ADK summarizes older session history—including past instructions, inputs, and tool responses. Managed via `EventsCompactionConfig`, this strategy ensures the agent retains access to crucial recent interactions while trimming older events, optimizing model processing times without losing critical narrative context."""
    },
    {
        "id": "atom-what-is-a-session-in-adk",
        "title": "What is a session in ADK",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:sessions", "layer:concepts", "artifact_role:definition"],
        "content": """A `Session` in the Agent Development Kit (ADK) represents a single, ongoing conversation thread or interaction between a user and an agent. \n\nIt is the primary structure used to track conversational context. A session tracks the history of what has been said and done (`session.events`) to maintain continuity and avoid repetition during an active interaction, acting as the short-term memory block for the current conversation lifecycle."""
    },
    {
        "id": "atom-what-is-state-in-adk-sessions",
        "title": "What is state in ADK sessions",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:sessions", "layer:concepts", "artifact_role:definition"],
        "content": """Within an ADK `Session`, the `state` attribute acts as a dedicated scratchpad for the agent during a specific interaction. \n\nConceptually, `session.state` is a dictionary or map holding serializable key-value pairs. While the `events` array holds the full conversational history, `state` stores dynamic, accumulated details needed to track progress—such as user preferences, multi-turn booking steps, shopping cart items, or authentication flags."""
    },
    {
        "id": "atom-what-are-events-in-adk",
        "title": "What are events in ADK",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:events", "layer:concepts", "artifact_role:definition"],
        "content": """Events are the fundamental units of information flow in the Agent Development Kit (ADK). \n\nAn `Event` is an immutable record representing a specific point in the agent's execution lifecycle. It captures user messages, agent replies, tool function calls, tool results, state changes, and error signals. Events are the primary mechanism through which ADK components communicate, manage state, and direct the control flow of a multi-turn conversation."""
    },
    {
        "id": "atom-what-is-long-term-memory-in-adk",
        "title": "What is long-term memory in ADK",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:memory", "layer:concepts", "artifact_role:definition"],
        "content": """In the Agent Development Kit (ADK), Long-Term Memory refers to the agent's ability to recall information from past conversations, managed by the `MemoryService`.\n\nWhile `Session` and `State` represent short-term memory for an active chat, the `MemoryService` acts as a searchable archive. Developers can ingest entire completed sessions (`add_session_to_memory`), incrementally append event deltas, or write direct `MemoryEntry` items, enabling the agent to learn and recall cross-session facts about a user continuously."""
    },
    {
        "id": "atom-what-is-the-a2a-protocol-in-adk",
        "title": "What is the A2A protocol in ADK",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:a2a", "layer:architecture", "artifact_role:definition"],
        "content": """The Agent2Agent (A2A) Protocol in the Agent Development Kit (ADK) is a standardized open standard allowing independent agents running as separate remote services to communicate over a network. \n\nUnlike "Local Sub-Agents" that run within the same application process and share memory, A2A agents function as discrete modules communicating across distributed environments. It defines how payloads, goals, and tools are exchanged between a central router agent and remote specialist agents."""
    },
    {
        "id": "atom-how-to-expose-an-agent-via-a2a-protocol",
        "title": "How to expose an agent via A2A protocol",
        "five_wh_one_plus": "how",
        "tags": ["system:adk", "topic:a2a", "layer:implementation", "artifact_role:process"],
        "content": """To expose an agent via the A2A (Agent2Agent) protocol in ADK, developers configure their agent to run as a remote service accessible over the network. \n\nThis typically involves deploying the ADK agent using an API Server setup (such as FastAPI in Python or an equivalent web framework) and wrapping the agent's execution loop with an endpoint that implements the A2A standard schema. This endpoint accepts standard A2A request payloads, routes them into the agent's `RunConfig`, and streams back standard A2A response events."""
    },
    {
        "id": "atom-how-to-consume-an-agent-via-a2a-protocol",
        "title": "How to consume an agent via A2A protocol",
        "five_wh_one_plus": "how",
        "tags": ["system:adk", "topic:a2a", "layer:implementation", "artifact_role:process"],
        "content": """To consume an agent via the A2A protocol in ADK, a parent or router agent connects to the remote service acting as an A2A tool. \n\nThe developer configures the parent agent with network connectivity details (URL, API keys) corresponding to the remote agent. The parent agent's LLM can then invoke the remote agent exactly like a local tool. The ADK framework handles serializing the request into the A2A protocol format, transmitting it over the network, and parsing the remote agent's output back into the local event loop for continuous processing."""
    },
    {
        "id": "atom-what-is-the-a2a-extension-in-adk",
        "title": "What is the A2A extension in ADK",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:a2a", "layer:implementation", "artifact_role:definition"],
        "content": """The A2A Extension in the Agent Development Kit (ADK) refers to the supplementary libraries and configurations designed to smoothly plug the Agent2Agent Protocol into standard ADK applications. \n\nIt provides boilerplate implementations, middleware, and type bindings necessary to turn standard local workflows into remote distributed ones. Using the extension reduces the manual network handling required to either expose a local agent to an A2A-compliant network or to register an external A2A service as a callable tool in the local workflow."""
    },
    {
        "id": "atom-what-is-the-gemini-live-api-toolkit-dev-guide",
        "title": "What is the Gemini Live API Toolkit development guide series",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:streaming", "layer:data", "artifact_role:definition"],
        "content": """The Gemini Live API Toolkit development guide series is a comprehensive set of instructional articles provided by the ADK documentation to master real-time multimodal agent development. \n\nThe series covers five main parts: an introduction to streaming architectures, how to send messages upstream using `LiveRequestQueue`, how to handle downstream events with the `run_live()` loop, understanding `RunConfig` (including modes and quotas), and how to leverage complex Audio, Image, and Video inputs, effectively guiding developers from basic voice bots to advanced affective dialogue systems."""
    },
    {
        "id": "atom-what-are-streaming-tools-in-adk",
        "title": "What are streaming tools in ADK",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:tools", "topic:streaming", "layer:concepts", "artifact_role:definition"],
        "content": """Streaming Tools in the Agent Development Kit (ADK) are specialized functions that allow continuous or asynchronous operations to stream intermediate results back to the agent in real time. \n\nUnlike standard tools that return a single discrete output upon completion, streaming tools enable the agent to react to unfolding events. Examples include monitoring live stock price changes or continuous video feeds, where the tool constantly feeds partial updates to the agent, which in turn can decide to interrupt its flow and respond dynamically to the new context."""
    },
    {
        "id": "atom-how-to-configure-streaming-behavior-in-adk",
        "title": "How to configure streaming behavior in ADK",
        "five_wh_one_plus": "how",
        "tags": ["system:adk", "topic:streaming", "layer:implementation", "artifact_role:process"],
        "content": """Configuring streaming behavior in the Agent Development Kit (ADK) involves fine-tuning the `RunConfig` applied during the `run_live()` execution loop. \n\nDevelopers can customize various parameters such as response modalities (specifying if the agent should output only text, or voice and text simultaneously), streaming modes, session context parameters, and interruption tolerances. Proper configuration ensures the agent optimally processes live Audio/Video input and manages WebSocket limits, quota controls, and automatic transcription layers."""
    },
    {
        "id": "atom-how-adk-supports-google-search-grounding",
        "title": "How ADK supports Google search grounding",
        "five_wh_one_plus": "how",
        "tags": ["system:adk", "topic:grounding", "layer:implementation", "artifact_role:process"],
        "content": """The Agent Development Kit (ADK) integrates Google Search Grounding to enhance agent responses with up-to-date, factually accurate web information. \n\nBy configuring an agent with the built-in Search Tool, the LLM is explicitly allowed to query Google Search dynamically. When a user asks a question requiring current world knowledge, the agent delegates the query to the search tool, retrieves snippets of the live web data, and uses that external truth to ground its generation. This reduces hallucination rates and injects high-quality provenance into the response."""
    },
    {
        "id": "atom-what-is-grounding-with-search-in-adk",
        "title": "What is grounding with search in ADK",
        "five_wh_one_plus": "what",
        "tags": ["system:adk", "topic:grounding", "layer:concepts", "artifact_role:definition"],
        "content": """Grounding with search in the Agent Development Kit (ADK) refers to the capability of an agent to anchor its generative responses against factual, real-world data retrieved via search engines or retrieval systems. \n\nRather than relying purely on the static pre-trained weights of the underlying LLM, the agent performs an online query (like using Google Search), extracts relevant facts, and synthesizes its final answer based explicitly on the retrieved documents. This epistemic strategy ensures high accuracy for temporal or highly specific queries and provides traceable citations for user verification."""
    }
]

for atom in atoms:
    filepath = os.path.join("paper_IEEE", "desk", "atoms", f"{atom['id']}.md")
    with open(filepath, "w") as f:
        f.write(f"---\n")
        f.write(f"id: {atom['id']}\n")
        f.write(f"title: {atom['title']}\n")
        f.write(f"five_wh_one_plus: {atom['five_wh_one_plus']}\n")
        f.write(f"tags:\n")
        for tag in atom['tags']:
            f.write(f"- {tag}\n")
        f.write(f"---\n\n")
        f.write(f"# {atom['title']}\n\n")
        f.write(f"## Answer\n\n")
        f.write(f"_Answer the selected 5WH1+ question as one stable knowledge unit._\n\n")
        f.write(f"{atom['content']}\n")
    print(f"Created {filepath}")

