---
title: Providers
description: Choose and install a Kujo provider package, then move from a first request to native features.
template: docs
section: Ecosystem
nav_title: Providers
order: 15
audience: developer
difficulty: beginner
status: source-backed inventory
version: current
last_updated: 2026-08-27
previous: /learn/packages/
next: /tools/ai-sdk/
tags: [ecosystem, providers, ai, packages]
---

Kujo provider packages keep each provider's wire format visible while offering a normalized AI SDK driver when the package supports one. Choose a package here, install its immutable tag with Kennel, and use the provider's native API first when you need provider-specific fields.

## Choose a provider

The inventory below is checked against the official Kujo provider repositories on **2026-08-27**. `AI SDK` means the package exports a public provider factory and depends on AI SDK `v1.1.0`; `Native only` means no normalized driver is advertised in that package release.

| Provider | Kujo package | Release tag | Protocol | AI SDK | Authentication |
| --- | --- | --- | --- | --- | --- |
| [Ollama](#ollama) | `ollama` | `v0.1.11` | Ollama API; local HTTP and NDJSON streams | Yes | `OLLAMA_API_KEY` for ollama.com; none for local use |
| [Anthropic](#anthropic) | `anthropic` | `v0.1.3` | Messages API and SSE | Yes | `ANTHROPIC_API_KEY` |
| [Gemini](#gemini) | `gemini` | `v0.1.3` | Gemini Developer API | Yes | `GEMINI_API_KEY` |
| [OpenAI](#openai) | `openai` | `v0.1.2` | Responses API | Yes | `OPENAI_API_KEY` |
| [OpenRouter](#openrouter) | `openrouter` | `v0.1.2` | OpenAI-compatible routing API | Yes | `OPENROUTER_API_KEY` |
| [xAI](#xai) | `xai` | `v0.1.2` | OpenAI-compatible chat API | Yes | `XAI_API_KEY` |
| [Groq](#groq) | `groq` | `v0.1.1` | OpenAI-compatible chat API | Yes | `GROQ_API_KEY` |
| [Together AI](#together-ai) | `together` | `v0.1.1` | OpenAI-compatible chat API | Yes | `TOGETHER_API_KEY` |
| [Fireworks AI](#fireworks-ai) | `fireworks` | `v0.1.1` | OpenAI-compatible chat API | Yes | `FIREWORKS_API_KEY` |
| [Mistral](#mistral) | `mistral` | `v0.1.1` | Mistral chat API | Yes | `MISTRAL_API_KEY` |
| [Cerebras](#cerebras) | `cerebras` | `v0.1.1` | OpenAI-compatible chat API | Yes | `CEREBRAS_API_KEY` |
| [DeepInfra](#deepinfra) | `deepinfra` | `v0.1.1` | OpenAI-compatible chat API | Yes | `DEEPINFRA_API_KEY` |
| [DeepSeek](#deepseek) | `deepseek` | `v0.1.1` | OpenAI-compatible chat API | Yes | `DEEPSEEK_API_KEY` |
| [Cloudflare Workers AI](#cloudflare-workers-ai) | `cloudflare_ai` | `v0.1.1` | Workers AI chat API | Yes | `CLOUDFLARE_API_TOKEN` |
| [Hugging Face](#hugging-face) | `huggingface` | `v0.1.2` | Inference Providers router | Yes | `HF_TOKEN` |
| [Replicate](#replicate) | `replicate` | `v0.1.0` | Predictions API | Native only | `REPLICATE_API_TOKEN` |
| [Cohere](#cohere) | `cohere` | `v0.1.1` | Cohere chat, embed, and rerank APIs | Yes | `COHERE_API_KEY` |
| [Amazon Bedrock](#amazon-bedrock) | `bedrock` | `v0.1.1` | Bedrock Converse and InvokeModel | Native only | Caller-supplied SigV4 authorization |
| [Azure AI](#azure-ai) | `azure-ai` | `v0.1.1` | Azure OpenAI / Foundry deployments | Native only | `AZURE_OPENAI_API_KEY` or access token |
| [Vertex AI](#vertex-ai) | `vertex-ai` | `v0.1.1` | Vertex AI publisher models and predictions | Native only | Google ADC-derived access token |
| [NVIDIA NIM](#nvidia-nim) | `nvidia-nim` | `v0.1.1` | OpenAI-compatible NIM API | Yes | `NVIDIA_API_KEY` |
| [Perplexity](#perplexity) | `perplexity` | `v0.1.1` | Search-grounded chat API | Yes | `PERPLEXITY_API_KEY` |
| [Z.ai / GLM](#z-ai-glm) | `zai` | `v0.1.1` | OpenAI-compatible chat API | Yes | `ZAI_API_KEY` |
| [fal.ai](#fal-ai) | `fal` | `v0.1.1` | Queue and media inference API | Native only | `FAL_KEY` |
| [Baseten](#baseten) | `baseten` | `v0.1.1` | OpenAI-compatible deployment API | Yes | `BASETEN_API_KEY` |

All package versions above are immutable Git tags. The public package registry is not yet operated, so install from GitHub tags rather than using an unqualified package name.

## Install a provider

Install the package into the project's Kennel lockfile. Replace `PACKAGE` and `TAG` with a row from the table:

```bash
kujo kennel add github:kujolang/PACKAGE@TAG
kujo kennel install
```

Then export the provider's credential in your shell or secret manager. Never put a real key in a `.kujo` file, a lockfile, or a committed example. The package repositories and [Packages with Kennel](/learn/packages/) explain the local lockfile and trust boundary.

## Provider sections

Each section gives the package, immutable release, official documentation, native surface, AI SDK status, authentication variable, and a small starting point. Model IDs are copied from the provider repository examples; verify availability with the provider before using them in production.

### Ollama

Package: `ollama` `v0.1.11` · [Kujo repository](https://github.com/kujolang/ollama) · [Ollama API docs](https://docs.ollama.com/api)

Native API: local or cloud chat, generation, embeddings, model lifecycle, tools, structured output, thinking, and NDJSON streaming. AI SDK: `ollama_provider` for normalized chat and embeddings. Local Ollama needs no key; ollama.com uses `OLLAMA_API_KEY`.

```kujo
from ollama import chat

response := chat({"model": "some-installed-model", "messages": [{"role": "user", "content": "Hello!"}]})
print(response["data"]["message"]["content"])
```

### Anthropic

Package: `anthropic` `v0.1.3` · [Kujo repository](https://github.com/kujolang/anthropic) · [Messages API docs](https://docs.anthropic.com/en/api/messages)

Native API: Messages, content blocks, tools, thinking, multimodal input, token counting, and SSE. AI SDK: `anthropic_provider` for normalized chat and streaming; embeddings are not advertised. Set `ANTHROPIC_API_KEY` and `ANTHROPIC_MODEL`.

```kujo
from anthropic import messages

response := messages({"model": env("ANTHROPIC_MODEL"), "max_tokens": 256, "messages": [{"role": "user", "content": "Hello from Kujo!"}]})
print(response["data"]["content"][0]["text"])
```

### Gemini

Package: `gemini` `v0.1.3` · [Kujo repository](https://github.com/kujolang/gemini) · [Gemini API docs](https://ai.google.dev/gemini-api/docs)

Native API: contents and parts, streaming, tools, structured output, multimodal input, safety metadata, and usage. AI SDK: `gemini_provider` where the selected model supports the normalized capability. Set `GEMINI_API_KEY`.

```kujo
from gemini import create_client, client_generate_content

client := create_client({})
result := client_generate_content(client, "gemini-2.5-flash", [{"role": "user", "parts": [{"text": "Hello from Kujo!"}]}], {})
print(result["data"]["candidates"][0]["content"]["parts"][0]["text"])
```

### OpenAI

Package: `openai` `v0.1.2` · [Kujo repository](https://github.com/kujolang/openai) · [Responses API docs](https://platform.openai.com/docs/api-reference/responses)

Native API: Responses output items, built-in tools, reasoning, structured output, streaming, embeddings, and usage. AI SDK: `openai_provider` for normalized chat and streaming. Set `OPENAI_API_KEY`.

```kujo
from openai import create_client, client_responses

result := client_responses(create_client({}), {"model": "gpt-5.5", "input": "Hello from Kujo!"})
print(result["data"]["output"][0]["content"][0]["text"])
```

### OpenRouter

Package: `openrouter` `v0.1.2` · [Kujo repository](https://github.com/kujolang/openrouter) · [OpenRouter API docs](https://openrouter.ai/docs/api-reference/overview)

Native API: model discovery, provider routing and preferences, fallbacks, privacy controls, and usage metadata. AI SDK: `openrouter_provider` for normalized chat and streaming. Set `OPENROUTER_API_KEY`.

```kujo
from openrouter import create_client, client_chat

result := client_chat(create_client({}), {"model": "openai/gpt-5.5", "messages": [{"role": "user", "content": "Hello!"}]})
print(result["data"]["choices"][0]["message"]["content"])
```

### xAI

Package: `xai` `v0.1.2` · [Kujo repository](https://github.com/kujolang/xai) · [xAI API docs](https://docs.x.ai/docs/api-reference)

Native API: xAI chat responses, reasoning controls, tools, multimodal inputs, and usage. AI SDK: `xai_provider` through the compatible driver. Set `XAI_API_KEY`; the repository example uses `grok-4.6`.

```kujo
from xai import create_client, client_chat

result := client_chat(create_client({}), {"model": "grok-4.6", "messages": [{"role": "user", "content": "Hello!"}]})
print(result["data"]["choices"][0]["message"]["content"])
```

### Groq

Package: `groq` `v0.1.1` · [Kujo repository](https://github.com/kujolang/groq) · [Groq API docs](https://console.groq.com/docs/api-reference)

Native API: compatible chat, reasoning controls, tools, supported vision, Compound behavior, citations, and usage. AI SDK: `groq_provider`. Set `GROQ_API_KEY`; the repository example uses `llama-3.3-70b-versatile`.

```kujo
from groq import create_client, client_chat

result := client_chat(create_client({}), {"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": "Hello!"}]})
print(result["data"]["choices"][0]["message"]["content"])
```

### Together AI

Package: `together` `v0.1.1` · [Kujo repository](https://github.com/kujolang/together) · [Together API docs](https://docs.together.ai/reference/chat-completions)

Native API: chat, tools, reasoning, vision, model metadata, and embeddings. AI SDK: `together_provider`; media, fine-tuning, files, and batch workflows remain provider-native. Set `TOGETHER_API_KEY`.

```kujo
from together import create_client, client_chat

result := client_chat(create_client({}), {"model": "meta-llama/Llama-3.3-70B-Instruct-Turbo", "messages": [{"role": "user", "content": "Hello!"}]})
print(result["data"]["choices"][0]["message"]["content"])
```

### Fireworks AI

Package: `fireworks` `v0.1.1` · [Kujo repository](https://github.com/kujolang/fireworks) · [Fireworks API docs](https://docs.fireworks.ai/api-reference/post-chatcompletions)

Native API: Fireworks chat, streaming, tools, reasoning, vision, and hosted-model controls. AI SDK: `fireworks_provider`. Set `FIREWORKS_API_KEY` and choose a currently available Fireworks model.

```kujo
from fireworks import create_client, client_chat

result := client_chat(create_client({}), {"model": "accounts/fireworks/models/kimi-k2-instruct-0905", "messages": [{"role": "user", "content": "Hello!"}]})
print(result["data"]["choices"][0]["message"]["content"])
```

### Mistral

Package: `mistral` `v0.1.1` · [Kujo repository](https://github.com/kujolang/mistral) · [Mistral API docs](https://docs.mistral.ai/api/)

Native API: Mistral chat and its provider-specific request and response fields. AI SDK: `mistral_provider` for normalized chat and streaming. Set `MISTRAL_API_KEY`.

```kujo
from mistral import create_client, client_chat

result := client_chat(create_client({}), {"model": "mistral-small-latest", "messages": [{"role": "user", "content": "Hello!"}]})
print(result["data"]["choices"][0]["message"]["content"])
```

### Cerebras

Package: `cerebras` `v0.1.1` · [Kujo repository](https://github.com/kujolang/cerebras) · [Cerebras API docs](https://inference-docs.cerebras.ai/api-reference/chat-completions)

Native API: compatible chat, streaming, tools, reasoning, vision, and usage. AI SDK: `cerebras_provider`. Set `CEREBRAS_API_KEY`.

```kujo
from cerebras import create_client, client_chat

result := client_chat(create_client({}), {"model": "llama-3.3-70b", "messages": [{"role": "user", "content": "Hello!"}]})
print(result["data"]["choices"][0]["message"]["content"])
```

### DeepInfra

Package: `deepinfra` `v0.1.1` · [Kujo repository](https://github.com/kujolang/deepinfra) · [DeepInfra API docs](https://deepinfra.com/docs/openai_api)

Native API: compatible chat, streaming, tools, reasoning, vision, and usage. AI SDK: `deepinfra_provider`. Set `DEEPINFRA_API_KEY` and use a model ID available from DeepInfra.

```kujo
from deepinfra import create_client, client_chat

result := client_chat(create_client({}), {"model": "meta-llama/Meta-Llama-3.1-8B-Instruct", "messages": [{"role": "user", "content": "Hello!"}]})
print(result["data"]["choices"][0]["message"]["content"])
```

### DeepSeek

Package: `deepseek` `v0.1.1` · [Kujo repository](https://github.com/kujolang/deepseek) · [DeepSeek API docs](https://api-docs.deepseek.com)

Native API: compatible chat, reasoning, tools, streaming, and usage. AI SDK: `deepseek_provider`. Set `DEEPSEEK_API_KEY` and verify the current DeepSeek model ID before use.

```kujo
from deepseek import create_client, client_chat

result := client_chat(create_client({}), {"model": "deepseek-chat", "messages": [{"role": "user", "content": "Hello!"}]})
print(result["data"]["choices"][0]["message"]["content"])
```

### Cloudflare Workers AI

Package: `cloudflare_ai` `v0.1.1` · [Kujo repository](https://github.com/kujolang/cloudflare-ai) · [Workers AI docs](https://developers.cloudflare.com/workers-ai/)

Native API: Workers AI chat and provider-specific account/model routing. AI SDK: `cloudflare_ai_provider`. Set the Cloudflare token and account configuration required by the package; do not confuse this package with Cloudflare's unrelated OpenAI-compatible gateway.

```kujo
from cloudflare_ai import create_client, client_chat

result := client_chat(create_client({}), {"model": "@cf/meta/llama-3.1-8b-instruct", "messages": [{"role": "user", "content": "Hello!"}]})
print(result["data"])
```

### Hugging Face

Package: `huggingface` `v0.1.2` · [Kujo repository](https://github.com/kujolang/huggingface) · [Inference Providers docs](https://huggingface.co/docs/inference-providers)

Native API: routed chat plus native task operations through the Inference Providers router. AI SDK: `huggingface_provider` for normalized chat. Set `HF_TOKEN`; model and routed provider availability are dynamic.

```kujo
from huggingface import create_client, chat

result := chat(create_client({}), {"model": "meta-llama/Llama-3.1-8B-Instruct", "messages": [{"role": "user", "content": "Hello!"}]})
print(result["data"])
```

### Replicate

Package: `replicate` `v0.1.0` · [Kujo repository](https://github.com/kujolang/replicate) · [Replicate HTTP API docs](https://replicate.com/docs/reference/http)

Native API: create, inspect, poll, cancel, and retrieve predictions. AI SDK: none in this release because prediction and media jobs do not have a stable one-to-one normalized chat semantic. Set `REPLICATE_API_TOKEN`.

```kujo
from replicate import create_client, create_prediction

prediction := create_prediction(create_client({}), {"version": "VERSION_OR_MODEL", "input": {"prompt": "Hello!"}})
print(prediction["data"]["id"])
```

### Cohere

Package: `cohere` `v0.1.1` · [Kujo repository](https://github.com/kujolang/cohere) · [Cohere API docs](https://docs.cohere.com/reference/chat)

Native API: chat, embeddings, and reranking. AI SDK: `cohere_provider` for chat and embeddings; reranking remains native-only. Set `COHERE_API_KEY`.

```kujo
from cohere import create_client, chat

result := chat(create_client({"model": "command-a-03-2025"}), {"messages": [{"role": "user", "content": "Explain Kujo in one sentence."}]})
print(result["output_text"])
```

### Amazon Bedrock

Package: `bedrock` `v0.1.1` · [Kujo repository](https://github.com/kujolang/bedrock) · [Bedrock API reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)

Native API: regional Converse and InvokeModel calls with model IDs, content blocks, guardrails, and native responses. AI SDK: none advertised; caller-supplied SigV4 authorization remains explicit. Set short-lived authorization and date values through your deployment's secret boundary.

```kujo
from bedrock import create_client, converse

result := converse(create_client({"region": "us-east-1", "authorization": env("AWS_BEDROCK_AUTHORIZATION")}), {"model_id": "amazon.nova-lite-v1:0", "messages": [{"role": "user", "content": [{"text": "Say hello."}]}]})
print(result["data"])
```

### Azure AI

Package: `azure-ai` `v0.1.1` · [Kujo repository](https://github.com/kujolang/azure-ai) · [Azure OpenAI REST reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)

Native API: deployment-scoped Azure OpenAI and Microsoft Foundry requests, API versions, and native response data. AI SDK: none advertised until deployment-scoped auth and API-version behavior have a governed adapter. Set `AZURE_OPENAI_API_KEY` or `AZURE_OPENAI_ACCESS_TOKEN`.

```kujo
from azure_ai import create_client, chat

result := chat(create_client({"endpoint": env("AZURE_OPENAI_ENDPOINT"), "api_key": env("AZURE_OPENAI_API_KEY"), "deployment": "my-model"}), {"messages": [{"role": "user", "content": "Say hello."}]})
print(result["data"])
```

### Vertex AI

Package: `vertex-ai` `v0.1.1` · [Kujo repository](https://github.com/kujolang/vertex-ai) · [Vertex AI model reference](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference)

Native API: project and location-scoped publisher models, content parts, and prediction endpoints. AI SDK: none advertised; Google Cloud authentication remains an explicit integration boundary. Supply a short-lived ADC-derived token through `GOOGLE_ACCESS_TOKEN`.

```kujo
from vertex_ai import create_client, generate_content

result := generate_content(create_client({"project": env("GOOGLE_CLOUD_PROJECT"), "location": "us-central1", "access_token": env("GOOGLE_ACCESS_TOKEN")}), {"model": "gemini-2.5-flash", "contents": [{"role": "user", "parts": [{"text": "Say hello."}]}]})
print(result["data"])
```

### NVIDIA NIM

Package: `nvidia-nim` `v0.1.1` · [Kujo repository](https://github.com/kujolang/nvidia-nim) · [NVIDIA NIM docs](https://docs.nvidia.com/nim/)

Native API: hosted or self-managed OpenAI-compatible chat with explicit host and model configuration. AI SDK: `nvidia_nim_provider`. Set `NVIDIA_API_KEY` for the hosted endpoint.

```kujo
from nvidia_nim import create_client, chat

result := chat(create_client({"api_key": env("NVIDIA_API_KEY"), "model": "meta/llama-3.1-8b-instruct"}), {"messages": [{"role": "user", "content": "Say hello."}]})
print(result["data"])
```

### Perplexity

Package: `perplexity` `v0.1.1` · [Kujo repository](https://github.com/kujolang/perplexity) · [Perplexity API docs](https://docs.perplexity.ai/docs/getting-started/overview)

Native API: the Kujo package's search-grounded chat, citations, search filters, usage, and native metadata. AI SDK: `perplexity_provider` for normalized chat; citations remain native provider data. Perplexity's current documentation also describes a separate Router API in private preview, so do not assume Router features are available through this package. Set `PERPLEXITY_API_KEY`.

```kujo
from perplexity import create_client, chat

result := chat(create_client({"api_key": env("PERPLEXITY_API_KEY"), "model": "sonar-pro"}), {"messages": [{"role": "user", "content": "What is Kujo?"}]})
print(result["data"])
```

### Z.ai / GLM

Package: `zai` `v0.1.1` · [Kujo repository](https://github.com/kujolang/zai) · [Z.ai API reference](https://docs.z.ai/api-reference)

Native API: GLM chat with reasoning, tools, and multimodal fields. AI SDK: `zai_provider` through the compatible driver; GLM-specific fields remain native. Set `ZAI_API_KEY`.

```kujo
from zai import create_client, chat

result := chat(create_client({"api_key": env("ZAI_API_KEY"), "model": "glm-4.5"}), {"messages": [{"role": "user", "content": "Say hello."}]})
print(result["data"])
```

### fal.ai

Package: `fal` `v0.1.1` · [Kujo repository](https://github.com/kujolang/fal) · [fal.ai model APIs](https://docs.fal.ai/model-apis)

Native API: queued image, video, audio, and other model inference with submit, status, result, and cancel operations. AI SDK: none in this release because queued media has no stable normalized chat semantic. Set `FAL_KEY`.

```kujo
from fal import create_client, submit

request := submit(create_client({"key": env("FAL_KEY"), "model": "fal-ai/flux/schnell"}), {"input": {"prompt": "A monochrome Kujo mascot"}})
print(request["data"]["request_id"])
```

### Baseten

Package: `baseten` `v0.1.1` · [Kujo repository](https://github.com/kujolang/baseten) · [Baseten API reference](https://docs.baseten.co/api-reference/openai)

Native API: deployment-scoped OpenAI-compatible chat, streaming-ready fields, and provider metadata. AI SDK: `baseten_provider`; keep the deployment and base URL explicit. Set `BASETEN_API_KEY`.

```kujo
from baseten import create_client, chat

result := chat(create_client({"api_key": env("BASETEN_API_KEY"), "model": "my-deployment"}), {"messages": [{"role": "user", "content": "Say hello."}]})
print(result["data"])
```

## Contracts and related guides

The current baseline is Kujo `v1.0.1`, Kennel `v1.0.0`, AI SDK `v1.1.0`, AI SDK normalized response contract `1.0.0`, AI SDK provider-driver contract `1.0.0`, and Kujo Provider Package Contract `1.0.1`. Provider package versions are independent of these contracts.

- [AI SDK](/tools/ai-sdk/) — normalized chat and embedding behavior, retries, fixtures, and redaction.
- [AI runtime basics](/learn/ai-runtime/) — credentials, budgets, replay, and egress boundaries.
- [Packages with Kennel](/learn/packages/) — manifests, lockfiles, and frozen installs.
- [AI and agents](/build/ai-and-agents/) — the path from a provider call to agents and workflows.
- [Release boundaries](/release-boundaries/) — how to interpret repository maturity and evidence.

Evidence date: 2026-08-27. Recheck the linked Kujo repository and official provider documentation before pinning a new release or model in a production system.
