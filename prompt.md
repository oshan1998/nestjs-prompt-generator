You're my AI coding assistant.

I want to build a Python web app using **Streamlit** called **NestJS Prompt Generator**.

This tool will help me generate structured prompts for building NestJS modules using AI (like Cursor itself). The prompts will include module information, entity schemas, DTOs, endpoints, and a task execution pipeline.

---

🧱 FEATURES TO IMPLEMENT:

1. **Module Definition Form**
   - Input: Module name (string)
   - Input: Module description (text area)

2. **Entity Editor**
   - Input: Entity name
   - Input: Field definitions (one per line: `name:type`)
   - Auto-parses field list into a structured dict

3. **DTO Section**
   - Create DTOs for `create` and `update`
   - Input: Fields for each DTO (text area, same format)
   - Should allow optional multiple DTOs

4. **Endpoint Section**
   - Add multiple endpoint definitions
   - Inputs:
     - Method (GET, POST, etc.)
     - Path (e.g., `/users/:id`)
     - Action (e.g., `create`, `findOne`)
     - Description

5. **Swagger Toggle**
   - Boolean switch to include Swagger support in prompt

6. **YAML Prompt Generator**
   - Output the entire structure as **YAML**
   - Use `pyyaml` for formatting
   - Display in a code block

7. **Natural Language Prompt Generator**
   - Convert YAML into an AI-readable English prompt
   - Example:
     > "Generate a NestJS module named User. It has an entity User with fields id (string), email (string)..."

8. **Atomic Task Pipeline**
   - User can define ordered steps (e.g., `generate entity`, `generate DTO`)
   - Each step is shown with a "Confirm and Continue" button
   - Once confirmed, the next step appears

9. **Export Options**
   - Button to copy prompt to clipboard
   - Option to export YAML as `.txt`

---

🧱 TECH STACK:

- **Python 3.9+**
- **Streamlit**
- `pyyaml` for YAML output
- `pyperclip` (optional) for clipboard copy

---

📁 FILE STRUCTURE:

promptGenerator/
├── app.py
├── modules/
│ ├── form.py
│ ├── dto.py
│ ├── pipeline.py
│ ├── prompt_builder.py
├── styles/
│ └── layout.css (optional)
├── README.md
└── requirements.txt


---

🔧 GOALS:

- Clean, modular code
- Reusable components
- Minimalistic UI (Streamlit default)
- Easy to run locally via `streamlit run app.py`

---

Start by scaffolding the full codebase with dummy data for testing, then replace with actual logic. Each module should be in its own file.

Please generate the full implementation now.
