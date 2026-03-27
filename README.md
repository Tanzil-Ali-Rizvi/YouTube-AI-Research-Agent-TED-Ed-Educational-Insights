# YouTube AI Research Agent: TED-Ed Educational Insights

## 📌 Problem Statement
Extracting meaningful insights from long-form educational content is time-consuming. This project builds a **Durable AI Agent** capable of indexing high-volume YouTube playlists (specifically TED-Ed's "Are the Kids Alright?") and performing deep, multi-stage research to answer complex pedagogical and psychological questions.

## 🛠 Tech Stack
* **Orchestration:** [Temporal.io](https://temporal.io/) (Durable execution & retries)
* **Agent Framework:** [PydanticAI](https://ai.pydantic.dev/) (Type-safe LLM tool calling)
* **Database:** [Elasticsearch](https://www.elastic.co/) (Full-text search & indexing)
* **Language:** Python 3.12+
* **LLM:** OpenAI GPT-4o
* **Data Source:** YouTube Transcript API (via Residential Proxies)

## 💡 Key Insights
* **Durability over Scripts:** Using Temporal ensures that 100+ video extractions don't fail due to a single network timeout or proxy rotation.
* **Context Management:** By using a "Summarizer" agent pattern, we can process hour-long transcripts without hitting LLM token limits.
* **Hybrid Search:** Combining keyword-based Elasticsearch retrieval with LLM reasoning provides more accurate citations than standard RAG.
