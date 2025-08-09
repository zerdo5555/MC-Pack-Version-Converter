import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import zipfile
import shutil
import os
from pathlib import Path
import tempfile
import re

class MinecraftPackUpdater:
    def __init__(self, root):
        self.root = root
        self.root.title("MC-Pack Version Converter")
        self.root.geometry("600x650")  # さらに高さを増やした
        self.root.configure(bg="#F5F5F5")
        self.root.resizable(False, False)
        
        # パック形式の対応表（バージョン -> pack_format）
        self.pack_formats = {
            "1.16": 6, "1.16.2": 6, "1.16.5": 6,
            "1.17": 7, "1.17.1": 7,
            "1.18": 8, "1.18.1": 8, "1.18.2": 9,
            "1.19": 9, "1.19.1": 9, "1.19.2": 9, "1.19.3": 12, "1.19.4": 13,
            "1.20": 15, "1.20.1": 15, "1.20.2": 18, "1.20.3": 22, "1.20.4": 22,
            "1.20.5": 32, "1.20.6": 32,
            "1.21": 34, "1.21.1": 34, "1.21.2": 42, "1.21.3": 42, "1.21.4": 46,
            "1.21.5": 55, "1.21.6": 63, "1.21.7": 64, "1.21.8": 64
        }
        
        self.selected_file = None
        self.pack_type = tk.StringVar(value="Mod")
        self.pack_version = tk.StringVar(value="1.18.2")
        self.mc_version = tk.StringVar(value="1.21.8")
        self.pack_file_path = tk.StringVar(value="")
        
        self.setup_ui()
    
    def setup_ui(self):
        # メインフレーム
        main_frame = tk.Frame(self.root, bg="#F5F5F5")
        main_frame.pack(expand=True, fill="both", padx=40, pady=20)  # paddingを少し減らした
        
        # タイトル
        title_label = tk.Label(main_frame, text="MC-Pack Version Converter", 
                              font=("Arial", 24, "normal"), fg="#333333", bg="#F5F5F5")
        title_label.pack(pady=(0, 30))  # タイトル下のスペースを少し減らした
        
        # Pack Type
        self.create_input_row(main_frame, "Pack Type", self.pack_type, 
                             ["Mod", "Resource Pack", "Data Pack"], 0)
        
        # Pack Version
        self.create_input_row(main_frame, "Pack Version", self.pack_version,
                             list(self.pack_formats.keys()), 1)
        
        # MC Version
        self.create_input_row(main_frame, "MC Version", self.mc_version,
                             list(self.pack_formats.keys()), 2)
        
        # Pack File
        self.create_file_row(main_frame, "Pack File", self.pack_file_path, 3)
        
        # Convert Button - 元のコードのボタンを修正
        self.convert_button = tk.Button(main_frame, text="Convert",
                                       command=self.convert_pack, 
                                       font=("Arial", 18, "normal"),
                                       bg="#90EE90", fg="#333333", 
                                       relief="flat", cursor="hand2",
                                       width=15, height=2,
                                       activebackground="#7FDD7F")
        self.convert_button.pack(pady=(30, 10))
        
        # Status Label
        self.status_label = tk.Label(main_frame, text="", 
                                    font=("Arial", 10), fg="#666666", bg="#F5F5F5")
        self.status_label.pack(pady=(10, 0))
    
    def create_input_row(self, parent, label_text, variable, values, row):
        """入力行を作成"""
        row_frame = tk.Frame(parent, bg="#F5F5F5")
        row_frame.pack(fill="x", pady=(0, 20))
        
        # Label
        label = tk.Label(row_frame, text=label_text, 
                        font=("Arial", 14, "normal"), fg="#333333", bg="#D3D3D3",
                        width=12, height=2, relief="flat")
        label.pack(side="left")
        
        # Combobox
        combo_style = ttk.Style()
        combo_style.configure("Custom.TCombobox",
                             fieldbackground="#D3D3D3",
                             background="#D3D3D3",
                             borderwidth=1,
                             relief="flat")
        
        combo = ttk.Combobox(row_frame, textvariable=variable, values=values,
                            state="readonly", font=("Arial", 12),
                            style="Custom.TCombobox", width=25)
        combo.pack(side="right", fill="x", expand=True, padx=(10, 0))
        
        return combo
    
    def create_file_row(self, parent, label_text, variable, row):
        """ファイル選択行を作成"""
        row_frame = tk.Frame(parent, bg="#F5F5F5")
        row_frame.pack(fill="x", pady=(0, 20))
        
        # Label
        label = tk.Label(row_frame, text=label_text, 
                        font=("Arial", 14, "normal"), fg="#333333", bg="#D3D3D3",
                        width=12, height=2, relief="flat")
        label.pack(side="left")
        
        # File path display + browse button frame
        file_frame = tk.Frame(row_frame, bg="#F5F5F5")
        file_frame.pack(side="right", fill="x", expand=True, padx=(10, 0))
        
        # File path entry
        self.file_entry = tk.Entry(file_frame, textvariable=variable,
                                  font=("Arial", 10), bg="#D3D3D3", fg="#333333",
                                  relief="flat", bd=1)
        self.file_entry.pack(side="left", fill="x", expand=True)
        
        # Browse button
        browse_btn = tk.Button(file_frame, text="...", 
                              command=self.browse_file,
                              font=("Arial", 12, "bold"), bg="#D3D3D3", fg="#333333",
                              relief="flat", width=3, cursor="hand2",
                              activebackground="#C0C0C0")
        browse_btn.pack(side="right", padx=(5, 0))
    
    def browse_file(self):
        """ファイル参照ダイアログ"""
        if self.pack_type.get() == "Mod":
            filetypes = [("JAR files", "*.jar"), ("All files", "*.*")]
        else:
            filetypes = [("ZIP files", "*.zip"), ("All files", "*.*")]
        
        file_path = filedialog.askopenfilename(
            title="Select Pack File",
            filetypes=filetypes
        )
        
        if file_path:
            self.selected_file = file_path
            self.pack_file_path.set(file_path)
            self.update_status("File selected", "#28a745")
    
    def update_status(self, message, color="#666666"):
        """ステータス更新"""
        self.status_label.config(text=message, fg=color)
        self.root.update()
    
    def convert_pack(self):
        """パック変換メイン処理"""
        if not self.selected_file:
            messagebox.showerror("Error", "Please select a pack file")
            return
        
        if self.pack_version.get() == self.mc_version.get():
            messagebox.showwarning("Warning", "Source and target versions are the same")
            return
        
        try:
            self.convert_button.config(state="disabled", text="Converting...")
            self.update_status("Converting pack...", "#007bff")
            
            # 出力ファイル名生成
            input_path = Path(self.selected_file)
            output_filename = f"{input_path.stem}_v{self.mc_version.get()}{input_path.suffix}"
            output_path = input_path.parent / output_filename
            
            if self.pack_type.get() == "Resource Pack":
                self.convert_resource_pack(output_path)
            elif self.pack_type.get() == "Data Pack":
                self.convert_data_pack(output_path)
            else:
                self.convert_mod(output_path)
            
            self.update_status("Conversion completed successfully!", "#28a745")
            messagebox.showinfo("Success", f"Pack converted successfully!\nOutput: {output_path.name}")
            
        except Exception as e:
            self.update_status("Conversion failed", "#dc3545")
            messagebox.showerror("Error", f"Conversion failed:\n{str(e)}")
        
        finally:
            self.convert_button.config(state="normal", text="Convert")
    
    def convert_resource_pack(self, output_path):
        """リソースパック変換"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # ZIPを展開
            with zipfile.ZipFile(self.selected_file, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
            
            # pack.mcmeta更新
            self.update_pack_mcmeta(temp_dir)
            
            # 新しいZIPファイル作成
            self.create_zip_archive(temp_dir, output_path)
    
    def convert_data_pack(self, output_path):
        """データパック変換"""
        with tempfile.TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(self.selected_file, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
            
            # pack.mcmeta更新（データパック用）
            self.update_pack_mcmeta(temp_dir, is_datapack=True)
            
            self.create_zip_archive(temp_dir, output_path)
    
    def convert_mod(self, output_path):
        """MOD変換"""
        with tempfile.TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(self.selected_file, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
            
            # Forge MOD処理
            if os.path.exists(os.path.join(temp_dir, "META-INF", "mods.toml")):
                self.update_forge_mod(temp_dir)
            
            # Fabric MOD処理
            if os.path.exists(os.path.join(temp_dir, "fabric.mod.json")):
                self.update_fabric_mod(temp_dir)
            
            # Quilt MOD処理
            if os.path.exists(os.path.join(temp_dir, "quilt.mod.json")):
                self.update_quilt_mod(temp_dir)
            
            self.create_zip_archive(temp_dir, output_path)
    
    def update_pack_mcmeta(self, temp_dir, is_datapack=False):
        """pack.mcmeta更新"""
        mcmeta_path = os.path.join(temp_dir, "pack.mcmeta")
        if not os.path.exists(mcmeta_path):
            # pack.mcmetaが存在しない場合は作成
            mcmeta_data = {
                "pack": {
                    "pack_format": self.pack_formats[self.mc_version.get()],
                    "description": f"Converted to {self.mc_version.get()}"
                }
            }
            with open(mcmeta_path, 'w', encoding='utf-8') as f:
                json.dump(mcmeta_data, f, indent=2, ensure_ascii=False)
            return
        
        with open(mcmeta_path, 'r', encoding='utf-8') as f:
            mcmeta = json.load(f)
        
        # pack_format更新
        new_format = self.pack_formats[self.mc_version.get()]
        mcmeta["pack"]["pack_format"] = new_format
        
        # 説明文更新
        if "description" not in mcmeta["pack"]:
            mcmeta["pack"]["description"] = ""
        
        description = mcmeta["pack"]["description"]
        if isinstance(description, list):
            # リスト形式の場合、新しい行を追加
            description.append(f"Converted to {self.mc_version.get()}")
        else:
            # 文字列形式の場合、追記
            if description and not description.endswith(" "):
                description += " "
            mcmeta["pack"]["description"] = f"{description}(Converted to {self.mc_version.get()})"
        
        with open(mcmeta_path, 'w', encoding='utf-8') as f:
            json.dump(mcmeta, f, indent=2, ensure_ascii=False)
    
    def update_forge_mod(self, temp_dir):
        """Forge MOD更新"""
        toml_path = os.path.join(temp_dir, "META-INF", "mods.toml")
        
        try:
            with open(toml_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Minecraftバージョンの更新
            old_version = self.pack_version.get()
            new_version = self.mc_version.get()
            
            # 様々なパターンでバージョンを置換
            patterns = [
                (f'"{old_version}"', f'"{new_version}"'),
                (f"'{old_version}'", f"'{new_version}'"),
                (f'[{old_version}]', f'[{new_version}]'),
                (f'{old_version}', f'{new_version}')
            ]
            
            for old_pattern, new_pattern in patterns:
                content = content.replace(old_pattern, new_pattern)
            
            with open(toml_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
        except Exception as e:
            self.update_status(f"Warning: Could not update Forge mod file: {str(e)}", "#ffc107")
    
    def update_fabric_mod(self, temp_dir):
        """Fabric MOD更新"""
        json_path = os.path.join(temp_dir, "fabric.mod.json")
        
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                fabric_data = json.load(f)
            
            # Minecraft依存関係の更新
            if "depends" in fabric_data:
                if "minecraft" in fabric_data["depends"]:
                    fabric_data["depends"]["minecraft"] = f">={self.mc_version.get()}"
            
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(fabric_data, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.update_status(f"Warning: Could not update Fabric mod file: {str(e)}", "#ffc107")
    
    def update_quilt_mod(self, temp_dir):
        """Quilt MOD更新"""
        json_path = os.path.join(temp_dir, "quilt.mod.json")
        
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                quilt_data = json.load(f)
            
            # Quilt特有の更新処理
            if "depends" in quilt_data:
                if "minecraft" in quilt_data["depends"]:
                    quilt_data["depends"]["minecraft"] = f">={self.mc_version.get()}"
            
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(quilt_data, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.update_status(f"Warning: Could not update Quilt mod file: {str(e)}", "#ffc107")
    
    def create_zip_archive(self, temp_dir, output_path):
        """ZIPアーカイブ作成"""
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zip_ref:
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arc_name = os.path.relpath(file_path, temp_dir)
                    zip_ref.write(file_path, arc_name)

def main():
    root = tk.Tk()
    app = MinecraftPackUpdater(root)
    root.mainloop()

if __name__ == "__main__":
    main()
