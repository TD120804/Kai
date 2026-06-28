# Kai Architecture

## LLM
- Ollama
- Model: qwen2.5:3b

## Voice Input
- speech_recognition
- Google Speech Recognition API

## Voice Output
- ElevenLabs
- Model: eleven_turbo_v2_5

## Audio Playback
- mpv

## Memory System

### Active Memory Files
- memory/projects.txt
- memory/memories.txt

### Conversation Memory
- MAX_HISTORY = 6

## Personality

Core Prompt:

```python
You are Kai.
You are witty, warm, observant, slightly teasing.
Keep responses conversational and concise.
```

## Goals
- Fast local assistant
- Natural conversation
- Useful memory
- Healthy boundaries

## Kai Personality v2.0
- Core Identity (who Kai is)
- Philosophy (what Kai believes)
- Behavior Rules (how Kai acts)
- Conversation Style (how Kai speaks)
- Responsibilities (what Kai owns)
- Relationship Progression (how Kai evolves with his Commander)
- Decision Framework (how Kai thinks before responding)