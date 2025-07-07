# NestJS Prompt Generator

A Python web app using **Streamlit** to generate structured prompts for building NestJS modules using AI. Prompts include module info, entity schemas, DTOs, endpoints, and a task execution pipeline.

## Features
- Module definition form
- Entity editor
- DTO section
- Endpoint section
- Swagger toggle
- YAML prompt generator
- Natural language prompt generator
- Atomic task pipeline
- Export options (clipboard, YAML as .txt)

## Tech Stack
- Python 3.11+
- Streamlit
- pyyaml
- pyperclip (optional)

## File Structure
```
promptGenerator/
├── app.py
├── modules/
│   ├── form.py
│   ├── dto.py
│   ├── pipeline.py
│   ├── prompt_builder.py
├── styles/
│   └── layout.css (optional)
├── README.md
└── requirements.txt
```

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   streamlit run app.py
   ```
# nestjs-prompt-generator
