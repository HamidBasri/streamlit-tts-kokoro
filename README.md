<div align="center">

# 🗣️ TTS-Kokoro

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg) ![Streamlit](https://img.shields.io/badge/Streamlit-1.50+-red.svg) ![Kokoro](https://img.shields.io/badge/Kokoro-0.9.4+-green.svg) ![License](https://img.shields.io/badge/License-MIT-yellow.svg)

### ✨ Transform text into natural-sounding speech with Kokoro TTS

*A beautiful, multilingual Text-to-Speech web application powered by state-of-the-art AI*

<br>

[🚀 **Quick Start**](#-quick-start) • [📖 **Features**](#-features) • [🎮 **Usage**](#-usage) • [🛠️ **Development**](#️-development)

<br>

</div>

## ✨ Features

<div align="center">

### 🌍 **Multilingual Support**
🇺🇸 **American English** (20+ voices) • 🇬🇧 **British English** (8 voices) • 🇪🇸 **Spanish** (3 voices) • 🇫🇷 **French** (1 voice) • 🇮🇳 **Hindi** (4 voices) • 🇮🇹 **Italian** (2 voices) • 🇯🇵 **Japanese** (5 voices) • 🇧🇷 **Brazilian Portuguese** (3 voices) • 🇨🇳 **Mandarin Chinese** (8 voices)

### 🎯 **Voice Quality**
🟢 **A-Grade Voices** (Premium) • 🟡 **B-Grade Voices** (High-quality) • 🟠 **C-Grade Voices** (Good) • 🔴 **D-Grade Voices** (Standard)

### 🚀 **Key Features**
🎵 **Real-time Audio** • 💾 **Download Support** • ⌨️ **Keyboard Shortcuts** • 🎨 **Modern UI** • 🔄 **Auto-replay** • 📱 **Mobile Friendly**

</div>

## 🚀 Quick Start

### 📋 Prerequisites
- **Python 3.11+** installed on your system
- **[uv](https://docs.astral.sh/uv/)** package manager (recommended)

### ⚡ Installation

<details>
<summary><b>📥 Step 1: Clone the repository</b></summary>

```bash
git clone https://github.com/yourusername/TTS-Kokoro.git
cd TTS-Kokoro
```
</details>

<details>
<summary><b>📦 Step 2: Install dependencies</b></summary>

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -r requirements.txt
```
</details>

<details>
<summary><b>▶️ Step 3: Run the application</b></summary>

```bash
# Using just (recommended)
just run

# Or directly with Python
python homepage.py

# Or with Streamlit
streamlit run homepage.py
```
</details>

<details>
<summary><b>🌐 Step 4: Open in browser</b></summary>

Navigate to **`http://localhost:8501`** and start creating speech! 🎵
</details>

## 🎮 Usage

### 🎯 Basic Workflow

<div align="center">

| Step | Action | Description |
|------|--------|-------------|
| **1** | 🌍 **Select Language** | Choose from 9 supported languages |
| **2** | 🎤 **Pick a Voice** | Browse voices with quality ratings |
| **3** | ✍️ **Enter Text** | Type or paste your text |
| **4** | 🎵 **Generate & Download** | Create speech and download WAV file |

</div>

### ⚡ Quick Tips

- **Keyboard Shortcut**: `Cmd+Enter` (Mac) or `Ctrl+Enter` (Windows/Linux) for instant generation
- **Voice Quality**: Look for A-grade voices for the best quality
- **Gender Selection**: Choose between male (♂) and female (♀) voices
- **Auto-play**: Generated audio plays automatically in your browser

### 🔧 Advanced Features

🎯 **Voice Quality Filtering** • ♂♀ **Gender Selection** • ⚡ **Speed Control** • 📝 **Text Splitting**

## 🛠️ Development

### 📁 Project Structure

```
TTS-Kokoro/
├── 📁 static/           # Static assets (CSS, fonts)
├── 📄 homepage.py       # Main Streamlit application
├── 📄 constants.py      # Language and voice configurations
├── 📄 utils.py          # Utility functions
├── 📄 pyproject.toml    # Project dependencies
├── 📄 justfile          # Development commands
└── 📄 README.md         # This file
```

### 🚀 Available Commands

<details>
<summary><b>🔧 Development Commands</b></summary>

```bash
just dev          # Run in development mode
just run          # Run the application
just install      # Install dependencies
```
</details>

<details>
<summary><b>🔍 Code Quality Commands</b></summary>

```bash
just format       # Format code with black
just lint         # Lint code with ruff
just lint-fix     # Fix linting issues
just check        # Run all checks
```
</details>

<details>
<summary><b>🧹 Maintenance Commands</b></summary>

```bash
just clean        # Clean build artifacts
just update-deps  # Update dependencies
```
</details>

### 📦 Key Dependencies

🎤 **kokoro** • 🌐 **streamlit** • 🔥 **torch** • 🤗 **transformers** • 🎵 **soundfile**

## 🎯 Supported Languages & Voices

<div align="center">

| Language | Code | Voices | Quality Range |
|----------|------|--------|---------------|
| 🇺🇸 **American English** | `a` | **20 voices** | A to F+ |
| 🇬🇧 **British English** | `b` | **8 voices** | B- to D+ |
| 🇪🇸 **Spanish** | `e` | **3 voices** | N/A |
| 🇫🇷 **French** | `f` | **1 voice** | B- |
| 🇮🇳 **Hindi** | `h` | **4 voices** | C |
| 🇮🇹 **Italian** | `i` | **2 voices** | C |
| 🇯🇵 **Japanese** | `j` | **5 voices** | C+ to C- |
| 🇧🇷 **Brazilian Portuguese** | `p` | **3 voices** | N/A |
| 🇨🇳 **Mandarin Chinese** | `z` | **8 voices** | D |

</div>

---

## 🤝 Contributing

<div align="center">

**We welcome contributions! Here's how you can help:**

</div>

### 🚀 Getting Started

1. **🍴 Fork the repository**
2. **🌿 Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **💾 Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **📤 Push to the branch** (`git push origin feature/amazing-feature`)
5. **🔄 Open a Pull Request**

### 📋 Development Guidelines

📋 **PEP 8 Style** • 🧪 **Add Tests** • 📚 **Update Docs** • 💬 **Meaningful Commits**

## 📝 License

<div align="center">

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

</div>

## 🙏 Acknowledgments

<div align="center">

🎤 **Kokoro Team** • 🌐 **Streamlit** • 🤗 **Hugging Face** • 👥 **Contributors**

</div>

## 📞 Support

<div align="center">

| Support Type | Link |
|--------------|------|
| 🐛 **Bug Reports** | [GitHub Issues](https://github.com/yourusername/TTS-Kokoro/issues) |
| 💡 **Feature Requests** | [GitHub Discussions](https://github.com/yourusername/TTS-Kokoro/discussions) |
| 📧 **Email** | dev.hamidbasri@gmail.com |

</div>

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

<br>

Made with ❤️ by [Hamid Basri](https://github.com/hamidbasri)

</div>