JARVIS started as a simple command-line AI assistant. In V1, it could receive a user's question and send it to an LLM to generate a response.
V2 continued developing the same assistant foundation while improving its structure and organization, helping me understand how an LLM-powered application is built beyond simply writing a prompt.

JARVIS V3 introduces its first practical tool: a calculator. Instead of relying entirely on the LLM to perform arithmetic, JARVIS can use a Python calculation function for operations such as addition, subtraction, multiplication, and division. This introduces the idea of **tool calling**, where the AI can decide when an external function should be used to accomplish a task.
