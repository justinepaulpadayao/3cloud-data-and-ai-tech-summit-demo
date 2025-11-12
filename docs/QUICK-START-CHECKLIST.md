# 🚀 Roocode Memory Bank + Context7 - Quick Start Checklist

## ✅ Pre-Setup Checklist

- [ ] VS Code installed
- [ ] Roocode extension installed in VS Code
- [ ] Node.js v18+ installed (`node --version` to check)
- [ ] Project folder ready
- [ ] (Optional) Context7 API key obtained from https://context7.com

---

## 📋 Setup Steps

### Part 1: Context7 MCP Setup (5 minutes)

- [ ] Open VS Code Settings (Cmd/Ctrl + ,)
- [ ] Search for "Roo Code MCP"
- [ ] Click "Edit in settings.json"
- [ ] Add Context7 configuration:

**Copy this if you have an API key:**
```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp", "--api-key", "YOUR_API_KEY_HERE"]
    }
  }
}
```

**Or this if no API key:**
```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    }
  }
}
```

- [ ] Save settings.json
- [ ] Restart VS Code

### Part 2: Configure Roocode Modes (10 minutes)

#### Architect Mode
- [ ] Open VS Code Settings
- [ ] Search "Roo Code Prompts"
- [ ] Click "Architect" section
- [ ] Find "Custom Instructions" text box
- [ ] Open `roocode-architect-instructions.yml`
- [ ] Copy entire contents
- [ ] Paste into Architect Custom Instructions
- [ ] Save

#### Code Mode
- [ ] Still in Roo Code Prompts settings
- [ ] Click "Code" section
- [ ] Open `roocode-code-instructions.yml`
- [ ] Copy entire contents
- [ ] Paste into Code Custom Instructions
- [ ] Save

#### Ask Mode
- [ ] Still in Roo Code Prompts settings
- [ ] Click "Ask" section
- [ ] Open `roocode-ask-instructions.yml`
- [ ] Copy entire contents
- [ ] Paste into Ask Custom Instructions
- [ ] Save

#### Debug Mode
- [ ] Still in Roo Code Prompts settings
- [ ] Click "Debug" section  
- [ ] Open `roocode-debug-instructions.yml`
- [ ] Copy entire contents
- [ ] Paste into Debug Custom Instructions
- [ ] Save

### Part 3: Prepare Your Project (5 minutes)

- [ ] Open your project in VS Code
- [ ] (Optional but recommended) Create `projectBrief.md` in project root:

```markdown
# [Your Project Name]

## Project Overview
[Brief description of what this project does]

## Goals
- [Goal 1]
- [Goal 2]

## Tech Stack
- **Platform**: [e.g., AWS, Azure, Databricks]
- **Data Processing**: PySpark
- **Data Warehouse**: [e.g., Redshift, Snowflake]
- **Languages**: Python 3.x, SQL

## Success Criteria
- [What defines success for this project]
```

- [ ] Copy your `pyspark-coding-standards-memory.md` to project docs folder (optional reference)

### Part 4: Initialize Memory Bank (2 minutes)

- [ ] Open Roocode chat in VS Code
- [ ] Switch to **Architect mode** (select from dropdown)
- [ ] Type: `Initialize the Memory Bank`
- [ ] Press Enter
- [ ] Confirm when asked
- [ ] Wait for Memory Bank creation
- [ ] Verify `memory-bank/` folder created with 5 files:
  - [ ] productContext.md
  - [ ] activeContext.md
  - [ ] progress.md
  - [ ] decisionLog.md
  - [ ] systemPatterns.md

---

## 🎯 Verification Tests

### Test Context7
- [ ] Open Roocode chat
- [ ] Type: `How do I use Next.js routing? use context7 for /vercel/next.js`
- [ ] Verify you get up-to-date Next.js documentation

### Test Memory Bank
- [ ] Type: `What's in our productContext?`
- [ ] Verify Roocode responds with content from productContext.md
- [ ] Response should start with `[MEMORY BANK: ACTIVE]`

### Test Modes

**Test Architect Mode:**
- [ ] Switch to Architect mode
- [ ] Type: `Design a simple data transformation pipeline`
- [ ] Verify response references systemPatterns.md

**Test Code Mode:**
- [ ] Switch to Code mode  
- [ ] Type: `Create a PySpark function to filter active users`
- [ ] Verify code follows PySpark standards (F, T, W imports, naming conventions)
- [ ] Verify Memory Bank updated

**Test Ask Mode:**
- [ ] Switch to Ask mode
- [ ] Type: `Explain what systemPatterns.md contains`
- [ ] Verify response summarizes your coding standards

**Test Debug Mode:**
- [ ] Switch to Debug mode
- [ ] Type: `I'm getting this error: AnalysisException: cannot resolve column`
- [ ] Verify debugging guidance provided

---

## 📖 Quick Usage Guide

### Daily Workflow

**Morning:**
1. Open Roocode chat
2. Check Memory Bank status
3. Type: `What's the current focus?` (Ask mode)
4. Review progress.md and activeContext.md

**During Development:**
1. Use appropriate mode:
   - Design → **Architect** mode
   - Code → **Code** mode
   - Questions → **Ask** mode
   - Errors → **Debug** mode
2. Let modes automatically update Memory Bank
3. Use Context7 for library implementations

**End of Day:**
1. Type: `UMB` (Update Memory Bank)
2. Verify all work is captured
3. Session complete!

### Context7 Usage Patterns

**Automatic (just mention the library):**
```
"Implement Supabase authentication"
→ Automatically uses Context7

"How does React Query work?"
→ Automatically uses Context7
```

**Explicit:**
```
"use context7 for /tanstack/react-query"
"Get latest docs for /supabase/supabase"
```

**Version-specific:**
```
"use context7 for /vercel/next.js/14.0.0"
```

### Memory Bank Commands

**Force update:**
```
UMB
```
or
```
Update Memory Bank
```

**Check status:**
```
What's the current focus?
What tasks are in progress?
What decisions have been made?
```

---

## 🎓 Learning Curve

### Day 1: Getting Comfortable
- [ ] Initialize Memory Bank
- [ ] Try each mode
- [ ] Make a simple change
- [ ] Check Memory Bank updates

### Week 1: Building Habits
- [ ] Start each session by checking activeContext.md
- [ ] Use appropriate modes for tasks
- [ ] Let Memory Bank auto-update
- [ ] Run "UMB" before breaks

### Month 1: Full Adoption
- [ ] Memory Bank is your project brain
- [ ] Context7 is second nature
- [ ] Modes feel natural
- [ ] Team collaboration smooth

---

## 🆘 Troubleshooting Quick Fixes

| Problem | Quick Fix |
|---------|-----------|
| Context7 not working | Restart VS Code, check Node.js version |
| Memory Bank says INACTIVE | Switch to Architect, type "Initialize the Memory Bank" |
| Modes not following standards | Run "UMB", check systemPatterns.md exists |
| Can't find MCP settings | Search "Roo Code MCP" in settings, look for JSON config |
| Memory Bank not updating | Use "UMB" command, verify you're in Code/Architect mode |

---

## ✨ Pro Tips

1. **Always start sessions in Ask mode** to check context
2. **Use "UMB" before ending sessions** for clean handoffs
3. **Reference Memory Bank explicitly**: "Following systemPatterns.md, implement..."
4. **Use Context7 for all library work** to avoid outdated APIs
5. **Keep projectBrief.md updated** as project evolves

---

## 📞 Support Resources

- **Setup Guide**: `SETUP-GUIDE.md` (detailed instructions)
- **PySpark Standards**: `pyspark-coding-standards-memory.md`
- **Context7 Docs**: https://github.com/upstash/context7
- **Roocode Memory Bank**: https://github.com/GreatScottyMac/roo-code-memory-bank

---

## ✅ Final Checklist

Before you start developing:

- [ ] ✅ Context7 MCP configured
- [ ] ✅ All 4 modes configured (Architect, Code, Ask, Debug)
- [ ] ✅ Memory Bank initialized
- [ ] ✅ Verification tests passed
- [ ] ✅ projectBrief.md created (optional)
- [ ] ✅ Understand mode purposes
- [ ] ✅ Know how to use Context7
- [ ] ✅ Ready to code! 🚀

---

**🎉 You're All Set!**

Your Roocode is now supercharged with:
- 🧠 Persistent Memory Bank
- 📚 Up-to-date documentation via Context7
- 🎯 Your PySpark coding standards enforced
- 🤝 Collaborative mode system

**Happy coding!**