# 🧠 Roocode Memory Bank with Context7 Integration

> A comprehensive memory bank system for Roocode with integrated Context7 MCP support for up-to-date documentation and enforced PySpark coding standards.

## 📦 What's Included

This package provides everything you need to set up a professional-grade development environment in Roocode:

### 🎯 Core Components

1. **Four Specialized Modes**
   - 🏗️ **Architect Mode**: System design and Memory Bank management
   - 💻 **Code Mode**: Feature implementation with enforced standards
   - ❓ **Ask Mode**: Questions and documentation lookup
   - 🐛 **Debug Mode**: Error investigation and troubleshooting

2. **Memory Bank System**
   - Persistent project context across sessions
   - Automatic tracking of decisions, progress, and patterns
   - Structured documentation that modes maintain
   - Your PySpark coding standards integrated

3. **Context7 Integration**
   - Up-to-date library documentation
   - Version-specific API information
   - No more outdated code suggestions
   - Direct integration with all modes

## 📁 Files in This Package

### Mode Configuration Files
| File | Purpose | Use With |
|------|---------|----------|
| `roocode-architect-instructions.yml` | Architect mode configuration | Roocode Architect mode settings |
| `roocode-code-instructions.yml` | Code mode configuration | Roocode Code mode settings |
| `roocode-ask-instructions.yml` | Ask mode configuration | Roocode Ask mode settings |
| `roocode-debug-instructions.yml` | Debug mode configuration | Roocode Debug mode settings |

### Documentation Files
| File | Purpose |
|------|---------|
| `SETUP-GUIDE.md` | Complete setup instructions and usage guide |
| `QUICK-START-CHECKLIST.md` | Step-by-step checklist for quick setup |
| `pyspark-coding-standards-memory.md` | Your PySpark coding standards (AI-optimized) |
| `README.md` | This file - overview and navigation |

## 🚀 Quick Start

### Option 1: Follow the Checklist (Recommended for First-Time Setup)
Open `QUICK-START-CHECKLIST.md` and follow the step-by-step checklist. It takes ~20 minutes.

### Option 2: Follow the Detailed Guide
Open `SETUP-GUIDE.md` for comprehensive instructions with explanations.

### Option 3: Fast Setup (If You Know What You're Doing)
1. Configure Context7 MCP in Roocode settings
2. Copy each `.yml` file to its corresponding Roocode mode
3. Create `projectBrief.md` in your project
4. Run Architect mode: "Initialize the Memory Bank"

## 🎯 System Capabilities

### What You Can Do

**With Memory Bank:**
- ✅ Maintain project context across all sessions
- ✅ Track architectural decisions automatically
- ✅ Monitor progress and tasks
- ✅ Enforce coding standards consistently
- ✅ Seamless handoffs between modes
- ✅ Never lose context when closing VS Code

**With Context7:**
- ✅ Get latest library documentation on-demand
- ✅ Avoid outdated API suggestions
- ✅ Work with correct, version-specific code
- ✅ Reduce debugging time
- ✅ Stay current with evolving libraries

**With Modes:**
- ✅ Clear separation of concerns
- ✅ Specialized expertise for each task
- ✅ Automatic context sharing
- ✅ Guided workflows
- ✅ Best practices enforced

## 📊 Memory Bank Structure

Once initialized, your project will have:

```
project-root/
├── memory-bank/
│   ├── productContext.md      # Project overview and architecture
│   ├── activeContext.md        # Current focus and recent changes
│   ├── progress.md             # Task tracking and completion
│   ├── decisionLog.md          # Architectural decisions and rationale
│   └── systemPatterns.md       # Coding standards (includes PySpark)
├── projectBrief.md             # Optional: Initial project description
└── [your code and files]
```

### File Purposes

**productContext.md** - The Big Picture
- What the project is
- Tech stack and architecture
- Key features and goals
- Updated by: Architect mode

**activeContext.md** - Right Now
- What you're working on
- Recent changes
- Open questions
- Updated by: All modes

**progress.md** - Task Tracking
- Completed tasks ✅
- Current tasks 🔄
- Next steps 📋
- Updated by: Code, Architect modes

**decisionLog.md** - Why We Did It
- Architectural decisions
- Rationale and alternatives
- Implementation approach
- Updated by: Architect, Code modes

**systemPatterns.md** - How We Code
- PySpark coding standards
- Project patterns
- Best practices
- Updated by: Architect mode

## 🎨 Mode Details

### 🏗️ Architect Mode
**Use for:** System design, architecture, planning

**Capabilities:**
- Initialize and manage Memory Bank
- Make architectural decisions
- Establish coding patterns
- Design system structure
- Coordinate other modes

**Example prompts:**
```
"Design the data pipeline architecture"
"Initialize the Memory Bank"
"What's the best way to structure our ETL? use context7"
```

### 💻 Code Mode
**Use for:** Implementation, coding, development

**Capabilities:**
- Write new features
- Modify existing code
- Refactor code
- Implement bug fixes
- Update Memory Bank with progress

**Example prompts:**
```
"Implement customer data transformation"
"Create a PySpark function to validate emails"
"Implement Supabase auth. use context7 for /supabase/supabase"
```

**Always follows:** systemPatterns.md standards

### ❓ Ask Mode
**Use for:** Questions, explanations, documentation

**Capabilities:**
- Answer questions about code
- Explain concepts
- Look up documentation
- Guide to appropriate modes
- Read Memory Bank for context

**Example prompts:**
```
"How does this pipeline work?"
"What's in our productContext?"
"How do I use React Query? use context7"
```

### 🐛 Debug Mode
**Use for:** Troubleshooting, error investigation

**Capabilities:**
- Analyze errors
- Investigate root causes
- Propose solutions
- Check against standards
- Hand off to Code mode for fixes

**Example prompts:**
```
"I'm getting: AnalysisException column not found"
"Debug this Lambda timeout issue"
"This error appears in Next.js routing. use context7"
```

## 🔄 Typical Workflow

### Starting a New Feature

1. **Architect Mode**: Design the approach
   ```
   "Design the customer segmentation feature"
   ```

2. **Code Mode**: Implement the feature
   ```
   "Implement customer segmentation using PySpark"
   ```

3. **Code Mode** (automatically updates Memory Bank)
   - Updates progress.md
   - Updates activeContext.md

4. **(Optional) Test Mode**: Verify the implementation

### Debugging an Issue

1. **Debug Mode**: Investigate the error
   ```
   "Debug: AnalysisException in customer_segmentation.py"
   ```

2. **Debug Mode** (analyzes, proposes fix)
   ```
   Root cause: Column name case mismatch
   Solution: [provides fix]
   ```

3. **Code Mode**: Implement the fix
   ```
   "Implement the fix from Debug mode"
   ```

### Learning About Code

1. **Ask Mode**: Get explanations
   ```
   "Explain how the data pipeline works"
   "What standards are in systemPatterns.md?"
   ```

## 🎓 Best Practices

### Daily Workflow

**Morning:**
```
[Ask Mode] "What's the current focus?"
```

**During Work:**
- Use appropriate mode for each task
- Let Memory Bank auto-update
- Use Context7 for library work

**End of Day:**
```
UMB  (Update Memory Bank)
```

### Context7 Usage

**For any library work:**
```
"Implement feature using [library]. use context7"
```

**When debugging library issues:**
```
"Debug this [library] error. use context7"
```

### Memory Bank Maintenance

**Auto-Update:** Modes update automatically during work

**Manual Sync:** Use "UMB" command when:
- Ending a session
- Before long breaks
- After significant work
- When switching projects

## 🔧 Configuration Reference

### Context7 MCP Configuration

**Standard (with API key):**
```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp", "--api-key", "YOUR_API_KEY"]
    }
  }
}
```

**Without API key:**
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

### Mode Configuration Location

1. Open VS Code Settings (Cmd/Ctrl + ,)
2. Search "Roo Code Prompts"
3. Find your mode (Architect, Code, Ask, Debug)
4. Paste YAML content into "Custom Instructions"

## 📚 Key Concepts

### Memory Bank
A structured system of markdown files that maintains project context across sessions. Think of it as your project's external brain.

### Context7
An MCP (Model Context Protocol) server that fetches up-to-date, version-specific documentation for libraries and injects it into prompts.

### Modes
Specialized AI assistants with distinct roles that collaborate through the Memory Bank:
- Architect = Designer
- Code = Builder
- Ask = Teacher
- Debug = Detective

### UMB (Update Memory Bank)
A command that triggers a comprehensive review and sync of all Memory Bank files. Use it before ending sessions.

## 🆘 Getting Help

### Troubleshooting Steps

1. **Check Quick Start Checklist** - Verify all steps completed
2. **Check Setup Guide** - Detailed troubleshooting section
3. **Verify installations:**
   - Roocode extension installed
   - Node.js v18+ installed
   - Context7 configured
4. **Test each component:**
   - Context7: `use context7 for /vercel/next.js`
   - Memory Bank: Should show `[MEMORY BANK: ACTIVE]`
   - Modes: Switch between them

### Common Issues

| Issue | Solution |
|-------|----------|
| Context7 not working | Restart VS Code, verify Node.js |
| Memory Bank INACTIVE | Run Architect mode, initialize |
| Modes not following standards | Check systemPatterns.md exists |
| Can't find settings | Search "Roo Code Prompts" |

## 🔗 External Resources

- **Context7**: https://github.com/upstash/context7
- **Roocode Memory Bank**: https://github.com/GreatScottyMac/roo-code-memory-bank
- **PySpark Docs**: https://spark.apache.org/docs/latest/api/python/
- **Model Context Protocol**: https://modelcontextprotocol.io

## 📝 Next Steps

1. ✅ Read this README (you're here!)
2. 📋 Open `QUICK-START-CHECKLIST.md`
3. ⚙️ Complete setup steps
4. 🎯 Initialize Memory Bank
5. 🚀 Start developing with enhanced capabilities!

---

## 🎉 What You'll Experience

### Before This Setup
- ❌ Repeating project context every session
- ❌ Outdated library suggestions
- ❌ Inconsistent code patterns
- ❌ Context lost between sessions
- ❌ Manual tracking of decisions

### After This Setup
- ✅ Automatic context persistence
- ✅ Always up-to-date documentation
- ✅ Enforced coding standards
- ✅ Seamless mode collaboration
- ✅ Automatic decision tracking
- ✅ Professional development workflow

---

**Version**: 1.0  
**Created**: November 2025  
**Optimized for**: Roocode with Memory Bank + Context7 MCP  
**Includes**: PySpark coding standards integration

**Ready to get started?** Open `QUICK-START-CHECKLIST.md` and let's go! 🚀