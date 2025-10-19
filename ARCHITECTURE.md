# 🏗️ WATBOT Architecture

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Python API  │  │  CLI Command │  │  Interactive │          │
│  │              │  │              │  │   Launcher   │          │
│  │  from watbot │  │  watbot      │  │              │          │
│  │  import Bot  │  │  start       │  │  start.py    │          │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘          │
│         │                  │                  │                   │
│         └──────────────────┴──────────────────┘                  │
│                            │                                      │
└────────────────────────────┼──────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PYTHON LAYER (watbot/)                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                  WhatsAppBot Class                       │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐        │   │
│  │  │  Config    │  │  Process   │  │  Control   │        │   │
│  │  │  Manager   │  │  Manager   │  │  Methods   │        │   │
│  │  └────────────┘  └────────────┘  └────────────┘        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                            │                                      │
│                            │  Environment Variables              │
│                            │  ┌───────────────────────┐          │
│                            └─→│ MONITOR_CONTACTS      │          │
│                               │ DEBUG_MODE            │          │
│                               │ HEADLESS              │          │
│                               │ AI_PERSONALITY        │          │
│                               │ ...                   │          │
│                               └───────────┬───────────┘          │
└───────────────────────────────────────────┼──────────────────────┘
                                            │
                                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                  NODE.JS LAYER (JavaScript)                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │         smart_whatsapp_bot.js                            │  │
│  │                                                           │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │  │
│  │  │  WhatsApp    │  │   Message    │  │   Session    │  │  │
│  │  │  Web.js      │  │   Handler    │  │   Manager    │  │  │
│  │  │  Client      │  │              │  │              │  │  │
│  │  └──────┬───────┘  └──────┬───────┘  └──────────────┘  │  │
│  │         │                  │                             │  │
│  │         │  ┌───────────────▼──────────────┐             │  │
│  │         │  │  SmartWhatsAppBot Class      │             │  │
│  │         │  │  - Chat History              │             │  │
│  │         │  │  - Contact Profiles          │             │  │
│  │         │  │  - Analytics                 │             │  │
│  │         │  │  - AI Introduction Tracking  │             │  │
│  │         │  └───────────────┬──────────────┘             │  │
│  │         │                  │                             │  │
│  │         ▼                  ▼                             │  │
│  │    ┌─────────────────────────────────┐                  │  │
│  │    │   WhatsApp Web Browser          │                  │  │
│  │    │   (Puppeteer - Headless/Headed) │                  │  │
│  │    └─────────────┬───────────────────┘                  │  │
│  └──────────────────┼──────────────────────────────────────┘  │
│                     │                                           │
│                     │  When message received                   │
│                     ▼                                           │
└─────────────────────────────────────────────────────────────────┘
                      │
                      │  Spawn Python process
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│                    AI LAYER (Python)                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              gemini_bot.py                               │  │
│  │                                                           │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │  │
│  │  │   Gemini API │  │  OpenRouter  │  │  Context     │  │  │
│  │  │   (Primary)  │  │  API (Backup)│  │  Analyzer    │  │  │
│  │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  │  │
│  │         │                  │                  │           │  │
│  │         └──────────────────┴──────────────────┘           │  │
│  │                            │                               │  │
│  │                            ▼                               │  │
│  │                 ┌─────────────────────┐                   │  │
│  │                 │  Response Generator │                   │  │
│  │                 │  - Personality      │                   │  │
│  │                 │  - Context          │                   │  │
│  │                 │  - Relationship     │                   │  │
│  │                 └──────────┬──────────┘                   │  │
│  │                            │                               │  │
│  └────────────────────────────┼───────────────────────────────┘  │
│                               │                                   │
│                               │  Generated Response               │
└───────────────────────────────┼───────────────────────────────────┘
                                │
                                ▼
                        Back to Node.js
                                │
                                ▼
                    Send reply to WhatsApp contact
```

## Data Flow

### 1. Incoming Message Flow
```
WhatsApp Contact → WhatsApp Web → Node.js Bot → Chat History
                                       ↓
                        Check if should respond
                                       ↓
                              AI Needed?
                                 ↓     ↓
                           Yes ←─┴─→ No
                            ↓         ↓
                      gemini_bot.py  Simple Reply
                            ↓         ↓
                    AI Response  ←────┘
                            ↓
                   Send to Contact
                            ↓
                    Store in History
```

### 2. Configuration Flow
```
User Config → Python BotConfig → Environment Variables → Node.js
    ↓              ↓                    ↓                    ↓
JSON File    Python Dict         Subprocess env        Read env vars
or                                                           ↓
Parameters                                          Apply to bot
```

### 3. Debugging Flow
```
User sets debug=True
        ↓
Python logger level set to DEBUG
        ↓
Environment variable DEBUG_MODE=true
        ↓
Node.js reads DEBUG_MODE
        ↓
Console logs all operations
        ↓
Python streams output to user
        ↓
User sees detailed logs
```

## Component Interactions

### Python ↔ Node.js Communication
```python
# Python spawns Node.js process
process = subprocess.Popen(
    ["node", "smart_whatsapp_bot.js"],
    env=config.get_env_dict(),  # Pass config as env vars
    stdout=subprocess.PIPE
)

# Python streams Node.js output
for line in process.stdout:
    logger.info(line)
```

### Node.js ↔ Python AI Communication
```javascript
// Node.js spawns Python for AI response
const python = spawn('python', [
    'gemini_bot.py',
    message,
    contactName,
    JSON.stringify(chatHistory),
    personality  // From env var
]);

python.stdout.on('data', (response) => {
    // Send response to WhatsApp
    client.sendMessage(chatId, response);
});
```

## File Storage

```
Project Root/
│
├── whatsapp_session_default/      # WhatsApp auth data
│   ├── session-*                  # Session files
│   └── .session_uploaded          # Upload flag
│
├── chat_history.json              # Conversation history
│   {
│     "contactId": {
│       "messages": [...],
│       "lastInteraction": "..."
│     }
│   }
│
├── contact_profiles.json          # Contact analysis
│   {
│     "contactId": {
│       "relationshipLevel": "...",
│       "communicationStyle": {...}
│     }
│   }
│
├── ai_introduced.json             # AI intro tracking
│   {
│     "contactId": true
│   }
│
└── bot_analytics.json             # Usage statistics
    {
      "totalMessages": 123,
      "dailyStats": {...}
    }
```

## State Management

### Bot States
1. **Initializing** - Starting up, loading configs
2. **Authenticating** - Showing QR code, waiting for scan
3. **Ready** - Connected, monitoring messages
4. **Processing** - Handling incoming message
5. **Responding** - Generating and sending reply
6. **Idle** - Waiting for next message
7. **Stopping** - Graceful shutdown

### Session States
1. **New** - No session exists, need QR scan
2. **Existing** - Session found, auto-login
3. **Uploaded** - Session backed up to server
4. **Expired** - Session invalid, need re-auth

## Security Considerations

### API Keys
```
❌ Hardcoded in files
✅ Environment variables
✅ .env file (gitignored)
✅ User configuration
```

### Session Data
```
❌ Committed to git
✅ Local only
✅ Optional server backup
✅ Encrypted storage
```

### Contact Privacy
```
✅ Local storage only
✅ No external logging
✅ Optional analytics disable
```

## Scaling & Performance

### Single Bot
- Handles 100+ contacts
- Responses in 1-3 seconds
- Memory: ~200MB
- CPU: Low (except AI calls)

### Multiple Bots (Different Sessions)
```python
# Work account
bot1 = WhatsAppBot(session_id="work")
bot1.start(blocking=False)

# Personal account
bot2 = WhatsAppBot(session_id="personal")
bot2.start(blocking=False)
```

### Rate Limiting
- WhatsApp: No official limits, but be reasonable
- Gemini API: 60 requests/minute (free tier)
- OpenRouter: Varies by model

## Error Handling

```
Error Level    →  Action
─────────────────────────────
Critical      →  Stop bot, notify user
Error         →  Log, use fallback
Warning       →  Log, continue
Info          →  Log (debug mode)
Debug         →  Log (debug mode only)
```

## Extension Points

### Adding New Platforms
1. Create `platform_bot.py` in `watbot/`
2. Add `PlatformConfig` to `config.py`
3. Update Node.js script for platform API
4. Add to `__init__.py` exports

### Custom AI Providers
1. Modify `gemini_bot.py`
2. Add API key to `AIConfig`
3. Implement fallback chain

### Custom Triggers
1. Extend message handler in JS
2. Add trigger config to `config.py`
3. Implement trigger logic

---

**This architecture allows for:**
- ✅ Easy configuration
- ✅ Platform independence
- ✅ Multiple account support
- ✅ Extensibility
- ✅ Debugging capabilities
- ✅ Error recovery
- ✅ Clean separation of concerns
