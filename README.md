# TokyoAECIndustryDevGroup-Revit
Revit Dev Contents

## 0. はじめに
 - Autodesk Revitのエクステンションのコードサンプルとなります。
 - Revit2020でのみ動作テストをしています。
 - なお、本エクステンションはRUG Japanが提供しているsample architectureモデルでのみ動作をテストしています。
 - 独自のファイルで使用する場合にはコードのアップデートが必要となります。

## 1. 参考
- [Revit API Docs](https://www.revitapidocs.com/2020/)
- [pyRevit](https://www.notion.so/pyrevitlabs/pyRevit-bd907d6292ed4ce997c46e84b6ef67a0)
- [Revit Python Wrapper](https://revitpythonwrapper.readthedocs.io/en/latest/)
- [IronPython Stubs](https://github.com/gtalarico/ironpython-stubs)

## 2. 設定
### 2.1 pyRevit
[インストーラ (4.7.6)](https://github.com/eirannejad/pyRevit/releases/download/v4.7.6/pyRevit_4.7.6_signed.exe)
 - ガイドにしたがってインストールしてください。
 - インストールに失敗した場合にはアンインストール後に再度インストールしてみてください。
 - 上記を試しても正常にインストールされない場合には、PCのアカウントを変更するとインストールされる可能性があります。
### 2.2 RevitPythonShell
[インストーラ (2020)](https://github.com/architecture-building-systems/revitpythonshell/releases/download/2019.01.27/2020.01.19_Setup_RevitPythonShell_2020.exe)
 - ガイドにしたがってインストールしてください。
 - インストールに失敗した場合にはアンインストール後に再度インストールしてみてください。
 - 上記を試しても正常にインストールされない場合には、PCのアカウントを変更するとインストールされる可能性があります。
#### 2.2.1 Revit Python Wrapper
 * Githubより[Revit Python Wrapper](https://github.com/gtalarico/revitpythonwrapper)をクローンしてください
 * Revit Python ShellのSearch Pathタブにリポジトリのディレクトリを追加してください。[参考](https://revitpythonwrapper.readthedocs.io/en/latest/installation.html#revitpythonshell)
  - pyRevitには初期設定でインストールされているため、設定の変更は必要ありません。
### 2.3 RevitLookup
[インストーラ (2017 - 2020)](https://drive.google.com/file/d/1KyH5vg3sHsYQEkHK0JrOaPti-2c1-6A_/view)
 - ガイドにしたがってインストールしてください。
 - インストールに失敗した場合にはアンインストール後に再度インストールしてみてください。
 - 上記を試しても正常にインストールされない場合には、PCのアカウントを変更するとインストールされる可能性があります。
### 2.4 IronPython Stubs
 - 使用しているエディタによって設定が異なりますので、[こちら](https://github.com/gtalarico/ironpython-stubs/wiki)を参照して設定してください。
 - 設定していなくても問題はありません。

## 3. エクステンション作成
 [参考リンク](https://www.notion.so/Install-Extensions-0753ab78c0ce46149f962acc50892491)  
 設定するパスの例
 ```
 C:\Users\[UserName]\Documents\Github\TokyoAECIndustryDevGroup-Revit
 ```
