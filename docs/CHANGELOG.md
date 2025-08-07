# Changelog

All notable changes to the MC-Pack Version Converter project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned Features
- [ ] Batch processing for multiple files
- [ ] Preview mode to see changes before conversion
- [ ] Custom conversion rules
- [ ] Multi-language support (Japanese, Chinese)
- [ ] Drag and drop file selection

## [1.0.0] - 2025-01-XX

### Added
- ✨ Initial release of MC-Pack Version Converter
- 🎯 GUI application with clean, intuitive interface
- 📦 Support for Resource Packs (.zip files)
- 🛠️ Support for Data Packs (.zip files)  
- ⚙️ Support for Mods (.jar files)
  - Forge mods (mods.toml updates)
  - Fabric mods (fabric.mod.json updates)
  - Quilt mods (quilt.mod.json updates)
- 🔄 Version support for Minecraft 1.16 through 1.21.8
- 📋 Automatic pack_format updates for all pack types
- 🖥️ Cross-platform compatibility (Windows, macOS, Linux)
- 📁 File structure preservation during conversion
- ⚡ Fast, lightweight processing
- 🔒 Safe conversion with original file preservation
- 📊 Status updates during conversion process
- ❌ Error handling with user-friendly messages

### Technical Details
- Built with Python 3.8+ and tkinter
- Supports all pack_format values from 6 to 64
- Handles complex file structures including OptiFine content
- RegEx-based version string updates for mod files
- ZIP compression with optimal settings
- Memory-efficient temporary file processing

### Supported Pack Formats
- Pack Format 6: Minecraft 1.16-1.16.5
- Pack Format 7: Minecraft 1.17-1.17.1
- Pack Format 8: Minecraft 1.18-1.18.1
- Pack Format 9: Minecraft 1.18.2, 1.19-1.19.2
- Pack Format 12: Minecraft 1.19.3
- Pack Format 13: Minecraft 1.19.4
- Pack Format 15: Minecraft 1.20-1.20.1
- Pack Format 18: Minecraft 1.20.2
- Pack Format 22: Minecraft 1.20.3-1.20.4
- Pack Format 32: Minecraft 1.20.5-1.20.6
- Pack Format 34: Minecraft 1.21-1.21.1
- Pack Format 42: Minecraft 1.21.2-1.21.3
- Pack Format 46: Minecraft 1.21.4
- Pack Format 55: Minecraft 1.21.5
- Pack Format 63: Minecraft 1.21.6
- Pack Format 64: Minecraft 1.21.7-1.21.8

### Distribution
- Standalone executable for Windows (.exe)
- Python source code for all platforms
- PyPI package (planned for future release)

---

## Version History Template

### [X.Y.Z] - YYYY-MM-DD

#### Added
- New features

#### Changed
- Changes in existing functionality

#### Deprecated
- Soon-to-be removed features

#### Removed
- Removed features

#### Fixed
- Bug fixes

#### Security
- Security improvements
