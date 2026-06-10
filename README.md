<div align="center">

![YUNG CLONE Banner](./assets/banner.png)

# 🦇 YUNG CLONE

### ⚡ High-Performance Discord Server Cloner

> A modern, powerful, and interactive Discord server cloning utility built with Python and discord.py

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![Discord.py](https://img.shields.io/badge/discord.py-v2+-000000?style=for-the-badge&logo=discord)](https://discordpy.readthedocs.io/)
[![Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)](https://github.com/yvngxsanty/Yung-Cloner)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

**Fast • Clean • Precise • Bilingual**

</div>

---

## 📺 Demo & Tutorial

**[Watch Full Tutorial on YouTube](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)** ← Replace with your YouTube link

---

## 📋 Overview

YUNG CLONE is a sophisticated Discord server cloning tool designed for users who need to duplicate server structures. It features a sleek terminal UI, bilingual support (English/Spanish), and robust capabilities for cloning roles, channels, categories, and permissions.

> ⚠️ **Important**: This tool is for educational purposes and controlled environments only. Self-bots violate Discord's Terms of Service.

---

## ✨ Features

- 🔄 **Complete Server Cloning**
  - Clone all roles with exact permissions
  - Clone text channels with settings
  - Clone voice channels with bitrate settings
  - Clone categories and channel organization
  - Preserve channel permissions and overwrites

- 🎨 **Modern Terminal Interface**
  - Beautiful ASCII art banner
  - Color-coded output with ANSI colors
  - Interactive menu system
  - Real-time operation logging
  - Success summaries with statistics

- 🌍 **Bilingual Support**
  - Full English interface
  - Complete Spanish (Español) interface
  - Easy language switching
  - Translated messages and menus

- ⚙️ **Smart Features**
  - Permission validation before cloning
  - Rate-limit handling with delays
  - Role hierarchy preservation
  - Detailed error logging
  - Operation timing statistics

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- discord.py 2.3.2 or higher
- A Discord account with server permissions

### Installation

```bash
# Clone the repository
git clone https://github.com/yvngxsanty/Yung-Cloner.git
cd Yung-Cloner

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
# Run the application
python main.py
```

**Step-by-Step Guide:**

1. Select your preferred language (English/Spanish)
2. Enter your Discord account token
3. Choose source and destination servers
4. Review the clone summary
5. Type `CLONE` or `CLONAR` to confirm
6. Watch the real-time cloning process
7. View the completion summary with statistics

---

## 📁 Project Structure

```
Yung-Cloner/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── README.md              # Documentation
├── LICENSE                # MIT License
├── CONTRIBUTING.md        # Contribution guidelines
├── CHANGELOG.md           # Version history
├── CODE_OF_CONDUCT.md     # Community guidelines
├── FAQ.md                 # Frequently asked questions
├── assets/                # Images and banners
│   └── banner.png
├── config/                # Configuration files
│   └── .gitkeep
└── src/                   # Source code
    ├── __init__.py
    ├── ui/                # Terminal UI components
    │   ├── __init__.py
    │   ├── ui_manager.py  # Main UI class
    │   ├── colors.py      # ANSI color definitions
    │   └── translations.py # Language translations
    └── core/              # Core cloning logic
        ├── __init__.py
        ├── clone_bot.py   # Discord bot client
        └── clone_operations.py # Cloning operations
```

---

## 🔧 Configuration

The application supports both English and Spanish languages. Select your preferred language when prompted:

- **English** (Option 2)
- **Español** (Option 1 - Default)

Configuration can be customized in:
- `src/ui/translations.py` - Language strings
- `src/ui/colors.py` - Terminal colors
- `main.py` - Application settings

---

## 📚 API Documentation

### Main Modules

#### `src/ui/ui_manager.py` - Terminal UI Management
```python
UI.t(key)              # Get translated text
UI.menu()              # Display interactive menus
UI.log()               # Log operations with colors
UI.banner()            # Display ASCII banner
UI.input_prompt()      # Get user input
UI.success_box()       # Show success message
```

#### `src/core/clone_bot.py` - Discord Client
```python
CloneBot.main_menu()           # Main interaction menu
CloneBot.show_servers()        # List available servers
CloneBot.clone_server_menu()   # Cloning interface
CloneBot.clone_guild()         # Execute cloning
```

#### `src/core/clone_operations.py` - Cloning Operations
```python
clone_roles()          # Copy roles with permissions
clone_channels()       # Copy channels and categories
delete_roles()         # Clean destination roles
delete_channels()      # Clean destination channels
update_server_info()   # Update server name and icon
```

---

## 🎯 Usage Examples

### List Your Servers
```
1. Start the application: python main.py
2. Select "List Servers" from main menu
3. View all servers with admin status and member count
```

### Clone a Server
```
1. Select "Clone Server" from main menu
2. Choose source server (by number or ID)
3. Choose destination server (by number or ID)
4. Review the summary
5. Type 'CLONE' or 'CLONAR' to confirm
6. Wait for completion
```

---

## ⚙️ Requirements

```
discord.py>=2.3.2
```

### Permissions Required

The bot needs the following permissions in the destination server:

- `Manage Roles` - To create and modify roles
- `Manage Channels` - To create text/voice channels
- `Manage Server` - To update server settings

---

## 🐛 Troubleshooting

### "Invalid token" error
- Verify your Discord token is correct
- Ensure your account has proper permissions
- Check for special characters in token
- Tokens are case-sensitive

### "Missing permissions in destination server"
- Ensure your account has admin rights in destination
- Check role hierarchy doesn't conflict
- Verify bot permissions are properly set

### Channels not cloning
- Verify destination has available space
- Check account role is below channels being created
- Ensure rate-limit delays are sufficient
- Review error logs for specific issues

### Slow cloning process
- This is normal due to Discord's rate-limiting
- Rate limits prevent API abuse
- Typical clone takes 5-30 minutes depending on server size
- Do not attempt to speed up the process

---

## 📝 Operation Logs

Operation logs are displayed in real-time with timestamps and status icons:

| Icon | Status | Color |
|------|--------|-------|
| ✓ | Success | Green |
| ✗ | Error | Red |
| ⚠ | Warning | Yellow |
| ℹ | Info | Cyan |
| ⟳ | Process | Blue |

Each log entry includes:
- Timestamp (HH:MM:SS)
- Status icon
- Operation message

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit with clear messages: `git commit -m "feat: your feature"`
4. Push to your fork: `git push origin feature/your-feature`
5. Open a Pull Request

For detailed guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚖️ Legal Disclaimer

> **Self-bots violate Discord's Terms of Service.** This tool is provided for educational purposes in controlled environments only. The author assumes no responsibility for misuse of this software. Use at your own risk and in compliance with Discord's Terms of Service.

---

## 🔗 Resources

- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/applications)
- [Discord Terms of Service](https://discord.com/terms)
- [GitHub Repository](https://github.com/yvngxsanty/Yung-Cloner)

---

## 📊 Project Stats

- **Language**: Python 100%
- **Version**: 1.0.0
- **Status**: Active Development
- **License**: MIT

---

<div align="center">

### 「 夜明けのコード 」

**Created with ❤️ by YvngxSanty**

[GitHub](https://github.com/yvngxsanty) • [YouTube](#) • [Discord](#)

</div>
