# Tiến Lên Miền Nam Extended by iaminfinityiq

Tiến Lên Miền Nam Extended, but now you'll play against AI.

The AI model used is Google Gemini 3.1 Flash Lite.

# Installation

## 1. Get your Gemini API key

1. Go to https://aistudio.google.com/api-keys
2. Click **Create API key**.
3. Enter a name, choose a project, then click **Create key**.
4. Copy the generated API key.

## 2. Download and run

Open a terminal and run:

```bash
git clone https://github.com/anlqdev/tlmne-PVE
cd tlmne-PVE
python -m pip install -U -r requirements.txt
```

Rename `.env.example` to `.env`, then replace `Your_Token_Here` with the API key you copied.

Finally, run:

```bash
python main.py
```

# Rules

Please read the rules in the `RULE.md` file before playing.