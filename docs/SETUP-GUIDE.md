# Roocode Memory Bank Setup Guide with Context7 Integration

## 📋 Overview

This guide will help you set up a comprehensive Memory Bank system for Roocode with integrated Context7 MCP support for up-to-date documentation. The system includes four specialized modes:

- **🏗️ Architect Mode**: System design, architecture, and Memory Bank management
- **💻 Code Mode**: Feature implementation and code development
- **❓ Ask Mode**: Questions, explanations, and information retrieval
- **🐛 Debug Mode**: Error investigation and troubleshooting

## 🎯 What You Get

### Memory Bank System
- **Persistent Context**: Maintains project knowledge across sessions
- **Structured Documentation**: Organized tracking of decisions, progress, and patterns
- **Mode Collaboration**: Seamless handoffs between different modes
- **Automatic Updates**: Memory Bank stays synchronized with your work

### Context7 Integration
- **Up-to-Date Docs**: Always get the latest library documentation
- **Version-Specific**: Accurate information for the exact version you're using
- **No Hallucinations**: Eliminates outdated API suggestions
- **Fast Access**: Documentation injected directly into your prompts

### Your Custom Coding Standards
- **PySpark Standards**: Integrated into the Memory Bank
- **Enforced Patterns**: All modes follow your established conventions
- **Quality Assurance**: Code generation adheres to your standards
- **Team Alignment**: Consistent approach across all development

## 📦 Prerequisites

1. **Roocode VS Code Extension**: Installed and configured
2. **Node.js**: v18.0.0 or higher (for Context7 MCP)
3. **Context7 API Key** (optional but recommended): Get from [Context7 website](https://context7.com)

## 🚀 Installation Steps

### Step 1: Set Up Context7 MCP

#### Option A: With API Key (Recommended)
1. Open Roocode settings in VS Code
2. Navigate to MCP Configuration
3. Add Context7 server:

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

#### Option B: Without API Key
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

#### For Streamable HTTP (Alternative)
```json
{
  "mcpServers": {
    "context7": {
      "type": "streamable-http",
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

### Step 2: Configure Roocode Modes

#### 2.1: Open Roocode Mode Settings
1. Open VS Code Settings (Cmd/Ctrl + ,)
2. Search for "Roo Code Prompts"
3. You'll see sections for each mode (Architect, Code, Ask, Debug)

#### 2.2: Configure Each Mode

**For Architect Mode:**
1. Click on "Architect" mode settings
2. Paste the contents of `roocode-architect-instructions.yml`
3. Save settings

**For Code Mode:**
1. Click on "Code" mode settings
2. Paste the contents of `roocode-code-instructions.yml`
3. Save settings

**For Ask Mode:**
1. Click on "Ask" mode settings
2. Paste the contents of `roocode-ask-instructions.yml`
3. Save settings

**For Debug Mode:**
1. Click on "Debug" mode settings
2. Paste the contents of `roocode-debug-instructions.yml`
3. Save settings

### Step 3: Set Up Your Project

#### 3.1: Create Project Brief (Optional but Recommended)
In your project root, create `projectBrief.md`:

```markdown
# [Project Name]

## Project Overview
[Describe your project]

## Goals
- [Goal 1]
- [Goal 2]

## Tech Stack
- **Data Platform**: [e.g., AWS, Azure, Databricks]
- **Data Processing**: [e.g., PySpark, Pandas]
- **Data Warehouse**: [e.g., Redshift, Snowflake]
- **Orchestration**: [e.g., Airflow, Step Functions]
- **Languages**: [e.g., Python 3.x, SQL]

## Key Stakeholders
- [Name/Role]

## Success Criteria
- [Criteria 1]
- [Criteria 2]
```

#### 3.2: Include Your Coding Standards Document
Place your `pyspark-coding-standards-memory.md` in your project root or docs folder. The Memory Bank will reference this.

## 🎬 Getting Started

### First Session: Initialize Memory Bank

1. **Open your project in VS Code**
2. **Start a new Roocode chat**
3. **Switch to Architect mode**
4. **Type**: "Initialize the Memory Bank"

Architect mode will:
- Detect if Memory Bank exists
- Offer to create it if not present
- Read your `projectBrief.md` if available
- Create the Memory Bank structure:
  ```
  project-root/
  ├── memory-bank/
  │   ├── productContext.md
  │   ├── activeContext.md
  │   ├── progress.md
  │   ├── decisionLog.md
  │   └── systemPatterns.md (with your PySpark standards)
  └── projectBrief.md
  ```

### Using the Modes

#### 🏗️ Architect Mode - Use When:
- Starting a new project
- Making architectural decisions
- Defining system design
- Establishing coding patterns
- Coordinating between modes

**Example Prompts:**
```
"Design the data pipeline architecture for customer analytics"
"What's the best way to structure our ETL jobs? use context7"
"Establish patterns for our Redshift data warehouse"
"Initialize the Memory Bank"
```

#### 💻 Code Mode - Use When:
- Implementing features
- Writing new code
- Refactoring existing code
- Fixing bugs (after Debug mode identifies the issue)

**Example Prompts:**
```
"Implement the customer data transformation pipeline"
"Create a PySpark function to clean address data"
"Refactor the order processing code to use better patterns"
"Implement Supabase authentication. use context7 for /supabase/supabase"
```

#### ❓ Ask Mode - Use When:
- Asking questions about code
- Learning how something works
- Getting explanations
- Looking up documentation

**Example Prompts:**
```
"How does this transformation function work?"
"What's the best way to handle null values in PySpark?"
"Explain the current data pipeline architecture"
"How do I use React Query? use context7"
```

#### 🐛 Debug Mode - Use When:
- Encountering errors
- Investigating bugs
- Troubleshooting issues
- Understanding why something isn't working

**Example Prompts:**
```
"I'm getting an AnalysisException: Column not found"
"This Lambda function is timing out, help me debug"
"The data quality checks are failing"
"Debug this Next.js error. use context7 for /vercel/next.js"
```

## 💡 Using Context7 Effectively

### Automatic Usage
Context7 will automatically activate when you mention libraries or frameworks:

```
"Implement OAuth with Supabase"
→ Automatically uses Context7 for /supabase/supabase

"How does Next.js routing work?"
→ Automatically uses Context7 for /vercel/next.js
```

### Explicit Usage
You can explicitly request Context7:

```
"use context7 for /tanstack/react-query"
"Get latest docs for /vercel/next.js"
"Check documentation for /python-poetry/poetry"
```

### Version-Specific
Request specific versions:

```
"use context7 for /supabase/supabase/2.0.0"
"Get docs for React 18"
```

### Supported Libraries
Context7 supports thousands of libraries. Common ones:
- `/vercel/next.js` - Next.js
- `/supabase/supabase` - Supabase
- `/tanstack/react-query` - React Query
- `/tailwindlabs/tailwindcss` - Tailwind CSS
- `/python-poetry/poetry` - Poetry
- `/psf/requests` - Python Requests
- Many more...

## 🔄 Memory Bank Workflow

### During Development

**Automatic Updates:**
- Code mode updates Memory Bank after implementations
- Architect mode records decisions
- Debug mode references context for troubleshooting
- Ask mode reads Memory Bank for informed answers

**Manual Sync:**
Use the "UMB" (Update Memory Bank) command:
```
"Update Memory Bank"
or
"UMB"
```

This triggers a comprehensive review and update of all Memory Bank files.

### Mode Handoffs

Modes will automatically recommend switching when appropriate:

```
[Architect Mode]
"I've designed the architecture. Switch to Code mode to implement."

[Code Mode]
"Implementation complete. Switch to Test mode to verify."

[Debug Mode]
"Root cause identified. Switch to Code mode to implement the fix."
```

## 📁 Memory Bank File Purposes

### productContext.md
- High-level project overview
- Tech stack and architecture
- Key features and goals
- Integration points

**Updated by:** Architect mode
**Read by:** All modes

### activeContext.md
- Current work focus
- Recent changes
- Open questions/issues
- Next session goals

**Updated by:** All active modes
**Read by:** All modes

### progress.md
- Task tracking
- Completed work
- Current tasks
- Next steps
- Blockers

**Updated by:** Code, Architect modes
**Read by:** All modes

### decisionLog.md
- Architectural decisions
- Rationale and context
- Implementation details
- Impact assessment

**Updated by:** Architect, Code modes (significant decisions)
**Read by:** All modes

### systemPatterns.md
- Coding standards (includes your PySpark standards)
- Architectural patterns
- Best practices
- Testing patterns

**Updated by:** Architect mode
**Read by:** All modes (especially Code mode)

## 🎨 Customization

### Adjusting Standards
Edit `memory-bank/systemPatterns.md` to:
- Add new coding patterns
- Update standards
- Include team conventions
- Document anti-patterns to avoid

### Project-Specific Rules
Edit `productContext.md` to add:
- Specific architectural decisions
- Team preferences
- Client requirements
- Technical constraints

## 🔧 Troubleshooting

### Context7 Not Working
1. Verify Node.js installation: `node --version`
2. Check MCP configuration in Roocode settings
3. Restart VS Code
4. Try without API key first

### Memory Bank Not Initializing
1. Ensure in Architect mode
2. Check file permissions in project directory
3. Try manual creation:
   ```
   mkdir memory-bank
   cd memory-bank
   touch productContext.md activeContext.md progress.md decisionLog.md systemPatterns.md
   ```

### Modes Not Following Standards
1. Verify systemPatterns.md exists and has your standards
2. Ensure mode configuration includes the full YAML content
3. Restart Roocode chat
4. Explicitly reference: "Following systemPatterns.md, implement..."

### Memory Bank Updates Not Happening
1. Use "UMB" command to force update
2. Check that mode is not in read-only status
3. Verify Memory Bank files are not read-only

## 📚 Advanced Features

### Multiple Projects
Roocode can handle multiple Memory Banks:
1. Each project gets its own `memory-bank/` directory
2. Roocode prompts to select which project when starting a chat
3. Context remains separate per project

### Custom Patterns
Add project-specific patterns to `systemPatterns.md`:

```markdown
## Project-Specific Patterns

### Data Lake Naming Convention
- Bronze layer: `raw_[source]_[entity]`
- Silver layer: `clean_[domain]_[entity]`
- Gold layer: `[domain]_[entity]_agg`

### Error Handling Pattern
Always use try-except with specific exceptions:
```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    raise
```
\`\`\`
```

### Context7 Custom Prompts
Create custom instructions for Context7:

```
"When implementing with [library], always use context7 and follow these patterns: [your patterns]"
```

## 🤝 Team Collaboration

### Sharing Standards
1. Commit `memory-bank/systemPatterns.md` to version control
2. Team members clone and get same standards
3. Update collectively as patterns evolve

### Session Handoffs
Use "UMB" before ending your session:
```
"UMB"
```
This ensures the next person has complete context.

### Code Reviews
Reference Memory Bank in reviews:
- "Does this follow our systemPatterns.md?"
- "Was this decision logged in decisionLog.md?"
- "Is progress.md updated?"

## 📊 Best Practices

### Daily Workflow
1. **Start of day**: Check `activeContext.md` and `progress.md`
2. **During work**: Let modes update Memory Bank automatically
3. **End of day**: Run "UMB" to sync everything
4. **Before breaks**: Run "UMB" for context preservation

### Code Quality
1. **Before coding**: Read `systemPatterns.md`
2. **During coding**: Reference patterns continuously
3. **After coding**: Verify against standards
4. **Use Context7**: For any library implementations

### Decision Making
1. **Architect mode**: Make design decisions
2. **Log immediately**: In `decisionLog.md`
3. **Reference later**: Other modes will follow
4. **Use Context7**: For technology evaluations

## 🎓 Learning Resources

### Context7 Documentation
- [Official Docs](https://github.com/upstash/context7)
- [Supported Libraries](https://context7.com/libraries)
- [API Reference](https://docs.context7.com)

### Roocode Memory Bank
- [Original Repo](https://github.com/GreatScottyMac/roo-code-memory-bank)
- [RooFlow](https://github.com/GreatScottyMac/RooFlow)

### PySpark Resources
- Your `pyspark-coding-standards-memory.md`
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)
- Use Context7: `use context7 for /apache/spark`

## 🆘 Getting Help

### Issues with Setup
1. Check this guide's Troubleshooting section
2. Verify all prerequisites
3. Review error messages carefully
4. Try fresh installation

### Issues with Modes
1. Use Ask mode: "Why isn't [mode] working as expected?"
2. Check Memory Bank status at start of response
3. Verify systemPatterns.md is properly configured
4. Try "UMB" to resync

### Issues with Context7
1. Test with simple query: "use context7 for /vercel/next.js"
2. Check MCP configuration
3. Verify Node.js version
4. Try without API key

## 🚀 Next Steps

1. **Install Context7 MCP**
2. **Configure Roocode modes** with provided YAML files
3. **Create projectBrief.md** for your project
4. **Initialize Memory Bank** in Architect mode
5. **Start coding** with confidence!

---

## 📝 Quick Reference Card

### Mode Selection
- Architecture/Design → **🏗️ Architect**
- Writing Code → **💻 Code**
- Questions → **❓ Ask**
- Debugging → **🐛 Debug**

### Context7 Usage
- Library implementation → `use context7 for /library/path`
- API questions → `use context7`
- Version-specific → `use context7 for /library/path/version`

### Memory Bank Commands
- Force update → `UMB` or `Update Memory Bank`
- Initialize → "Initialize the Memory Bank" (Architect mode)

### Memory Bank Files
- `productContext.md` → Project overview
- `activeContext.md` → Current status
- `progress.md` → Task tracking
- `decisionLog.md` → Decisions made
- `systemPatterns.md` → Your standards (PySpark, etc.)

---

**Happy Coding! 🎉**

Your Roocode setup now has:
✅ Persistent project context
✅ Up-to-date library documentation
✅ Enforced coding standards
✅ Collaborative mode system
✅ Automatic knowledge management