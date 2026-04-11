---
name: image-generator
description: Generate images from text prompts using Google Imagen 3 API. Use this skill when the user asks to create, generate, draw, or render an image or picture, or specifically mentions using Imagen or AI image generation.
---

# Image Generator Skill

This skill allows Gemini CLI to generate images based on text prompts using Google's Imagen 3 API via the `@google/genai` SDK.

## Requirements

The user must have the `GEMINI_API_KEY` environment variable set. The script will automatically pick it up. If it's missing, the script will fail and prompt the user to set it.

## How to use this skill

When the user asks to generate an image:

1. Formulate a descriptive text prompt based on the user's request.
2. Determine a suitable filename for the output image (e.g., `cute_cat.jpg`).
3. Run the generation script using the `run_shell_command` tool:

```bash
node .gemini/skills/image-generator/scripts/generate.js "YOUR DETAILED PROMPT HERE" "output_filename.jpg"
```

*Note: The script uses the current working directory, so the image will be saved directly to the folder you are currently in, unless an absolute path is provided.*

## Handling Output

- After the command completes successfully, notify the user that the image has been generated and saved.
- If the script fails due to a missing API key, instruct the user to set it (`export GEMINI_API_IMG="your_api_key_here"`).
- If the script fails due to other API errors (e.g., safety violations, network issues), relay the error message to the user.
